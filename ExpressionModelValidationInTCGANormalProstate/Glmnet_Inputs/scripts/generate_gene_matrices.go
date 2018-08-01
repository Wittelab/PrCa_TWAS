package main

// Go Style: github.com/golang/go/wiki/CodeReviewComments
// golang.org/ref/spec

// Explanation for Go declaration syntax "var asdf int = 10"
// https://blog.golang.org/gos-declaration-syntax

// Built in's:
// https://golang.org/pkg/builtin/

import (
  "bufio"
  "bytes"
  "fmt"
  "flag"
  "io/ioutil"
  "log"
  "math"
  "os"
  "os/exec"
  "regexp"
  "strings"
  "strconv"
  "sync"
)

var (

  txomeMap map[string]string
  dbGaP_Expression_File = flag.String("E", "NIL", "Local path to dbGaP repository file directory: 'RootStudyConsentSet_phs000985.ProstateCancer_RiskSNPs.v1.p1.c1.DS-PC-PUB-MDS/ExpressionFiles/phe000016.v1.NCI_ProstateCancer_RiskSNPs.expression-data-matrixfmt.RNAseq_probe_set_grc37.c1.DS-PC-PUB-MDS/normalizedcounts.txt'")

)

func main() {
  
  txomeMap = initTxomeMap()
  launchWorkers()

}

///////////////
// Functions //
///////////////

func initTxomeMap() map[string]string {

  flag.Parse()
  txomeMap := make(map[string]string)

  var dbGaP_Expression_FullPath bytes.Buffer
  dbGaP_Expression_FullPath.WriteString(*dbGaP_Expression_File)
  dbGaP_Expression_FullPath.WriteString("/RootStudyConsentSet_phs000985.ProstateCancer_RiskSNPs.v1.p1.c1.DS-PC-PUB-MDS/ExpressionFiles/phe000016.v1.NCI_ProstateCancer_RiskSNPs.expression-data-matrixfmt.RNAseq_probe_set_grc37.c1.DS-PC-PUB-MDS/normalizedcounts.txt")
  file, err := os.Open(dbGaP_Expression_FullPath.String())
  if err != nil {
      log.Fatal(err)
  }
  defer file.Close()

  scanner := bufio.NewScanner(file)
  // Custom split function: https://golang.org/src/bufio/example_test.go
  // scanner.Split(bufio.ScanWords) <-- have to call before scanner.Scan()
  for scanner.Scan() {
    line := scanner.Text()
    words := strings.Split(line, "\t")
    txomeMap[words[0]] = line

    if err := scanner.Err(); err != nil {
        log.Fatal(err)
    }
  }

  return txomeMap
}

func initJob(line string) *Job {
  words := strings.Split(line, "\t")
  var newJob Job

  start, err := strconv.Atoi(words[1])
  if err != nil {
    panic(err)
  }
  stop, err := strconv.Atoi(words[2])
  if err != nil {
    panic(err)
  }
  startFl, stopFl := float64(start), float64(stop)
  startFl, stopFl = math.Max(0, startFl - 5e5), stopFl + 5e5

  newJob.GENE = words[3]
  newJob.CHR = words[0]
  newJob.START = startFl
  newJob.STOP = stopFl
  return &newJob
}

func launchWorkers() {

    // In order to use our pool of workers we need to send
    // them work and collect their results. We make 2
    // channels for this.
    jobs := make(chan Job)
    rchch := make(chan chan string, 3)

    // This starts up 3 workers, initially blocked
    // because there are no jobs yet.
    for i := 0; i < 3; i++ {
        rch := make(chan string)
        go worker(i, jobs, rch)
        rchch <- rch
    }

    // Stackoverflow: "The problem is that ranging over a channel in a for loop will continue forever unless the channel is closed."
    // http://stackoverflow.com/questions/34108862/golang-program-hangs-without-finishing-execution
    close(rchch)

    file, err := os.Open("hg19_coords.bed")
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()

    var mergeCh = make(chan string)
    MergeGround(mergeCh)
    MergeRchs(rchch, mergeCh)

    jobScanner := bufio.NewScanner(file)
    for jobScanner.Scan() {
      line := jobScanner.Text()
      jobPtr := initJob(line)
      jobs <- *jobPtr
      fmt.Println(fmt.Sprintf("\tPushed: %s", line))
      if err := jobScanner.Err(); err != nil {
          log.Fatal(err)
      }
    }
}

func MergeGround(mergeCh <-chan string) {
  fmt.Println("Launched MergeGround")
  go func(){
    for result := range mergeCh {
      fmt.Printf("collected: %s", result)
    }
    fmt.Println("MergeGround GoRoutine Terminating")
  }()
  fmt.Println("Returned MergeGround")
}

func MergeRchs(cs <-chan chan string, out chan<- string) {
    var wg sync.WaitGroup
    // out := make(chan string)

    // Start an output goroutine for each input channel in cs.  output
    // copies values from c to out until c is closed, then calls wg.Done.
    output := func(c <-chan string) {
        fmt.Println("Running Output")
        for n := range c {
          fmt.Println(fmt.Sprintf("Merging %s into output channel", n))
          out <- n
          fmt.Println(fmt.Sprintf("\tMerged %s into output channel", n))
        }
        fmt.Println("** Decrementing waitgroup")
        wg.Done()
    }
    wg.Add(len(cs))
    for c := range cs {
        go output(c)
        // fmt.Println("Launched Merge")
    }

    fmt.Println("Launched mergeRchs goroutines")

    // Start a goroutine to close out once all the output goroutines are
    // done.  This must start after the wg.Add call.
    go func() {
        wg.Wait()
        close(out)
    }()

    fmt.Println("Returned rchch")
    // return out
}

func receiveWorkerResults(results <-chan int) {
  for result := range results{
    _ = result
  }
}

type Job struct {
  GENE, CHR string
  START, STOP float64
}

func worker(id int, jobs <-chan Job, rch chan<- string) chan<- string {
  checkNo := 1
  go func(){
    for job := range jobs {

      fmt.Println(fmt.Sprintf("Worker %s", strconv.Itoa(id)))
      fmt.Println(fmt.Sprintf("\tJobChan Length %s", strconv.Itoa(len(jobs))))
      fmt.Println(fmt.Sprintf("Worker %s (%s)", strconv.Itoa(id), strconv.Itoa(checkNo)))
      checkNo++

      gene, chr, start, stop := job.GENE, job.CHR, job.START, job.STOP
      re := regexp.MustCompile("/")
      gene = re.ReplaceAllString(gene, "-")
      if chr == "chrY" {
        continue
      }

      mfn := fmt.Sprintf("../intermediates/%s.txt", gene)

      file, err := os.Open("header.txt")
      if err != nil {
          log.Fatal(err)
      }

      scanner := bufio.NewScanner(file)
      var header string
      for scanner.Scan() {
        header = scanner.Text() + "\n"
        break
      }
      file.Close()

      headByt := []byte(header)
      err = ioutil.WriteFile(mfn, headByt, 0644)
      if err != nil {
        log.Fatal(err)
      }

      startStr := strconv.Itoa(int(start))
      stopStr := strconv.Itoa(int(stop))
      chr = chr[3:]
      bedStr := fmt.Sprintf("%s\t%s\t%s\n", chr, startStr, stopStr)
      bfn := fmt.Sprintf("../intermediates/%s.bed", gene)
      bedByt := []byte(bedStr)
      err = ioutil.WriteFile(bfn, bedByt, 0644)
      if err != nil {
        log.Fatal(err)
      }

      tbf := fmt.Sprintf("../../Genotypes/chr%s.dbGaP.r2gt0.8.vcf.gz", chr)
      cmd := exec.Command("tabix", "-R", bfn, tbf)
      // cmd := exec.Command("ls")
      fmt.Printf("%s %s %s %s\n", "tabix", "-R", bfn, tbf)
      stdout, err := cmd.StdoutPipe()

      if err != nil {
        panic(err)
      }
      if err := cmd.Start(); err != nil {
        log.Fatal(err)
      }
      fmt.Printf("Process started (%s)\n", gene)

      mfh, err := os.OpenFile(mfn, os.O_APPEND|os.O_WRONLY, 0600)
      if err != nil {
          panic(err)
      }

      scanner = bufio.NewScanner(stdout)
      for scanner.Scan() {
        tabStr := scanner.Text()
        if _, err = mfh.WriteString(tabStr+"\n"); err != nil {
            panic(err)
        }
      }

      if err := cmd.Wait(); err != nil {
        fmt.Printf("* Process error: %s, %s *\n", gene, chr)
        log.Fatal(err)
      }
      fmt.Printf("Process ended (%s).\n", gene)

      rpkmStr := txomeMap[job.GENE]
      if _, err = mfh.WriteString(rpkmStr+"\n"); err != nil {
          panic(err)
      }
      mfh.Close()

      tmatfn := fmt.Sprintf("../%s.matrix", gene)
      awkTranspose := fmt.Sprintf(`awk -v TNR=$(wc -l %s | awk '{print $1}') 'BEGIN{FS=OFS="\t"}{if(NR == 1 || NR == TNR){ print $0 } else { printf "chr"$1"-"$2"-"$4"-"$5; split($9, gt_array, ":"); ds_index=0; for(gt_var in gt_array){ if( gt_array[ds_index] == "DS" ){ break }; ds_index = ds_index + 1 }; for( i=10; i<=NF; i++ ){ split($i, ds_array, ":"); printf "\t"ds_array[ds_index]}; printf "\n" }}' %s | transpose -t --limit 100000x100000 --fieldmax 10000 > %s`, mfn, mfn, tmatfn)
      cmd = exec.Command("bash", "-c", awkTranspose)

      // stdout, err = cmd.StdoutPipe()

      // if err != nil {
      //   panic(err)
      // }
      if err := cmd.Start(); err != nil {
        log.Fatal(err)
      }
      fmt.Printf("Transposition started (%s)\n", gene)

      if err := cmd.Wait(); err != nil {
        fmt.Printf("* Transposition error: %s, %s *\n", gene, chr)
        log.Fatal(err)
      }

      fmt.Printf("Transposition ended (%s).\n", gene)

      // fmt.Println(fmt.Sprintf("\tDone: Worker %s (%s)", strconv.Itoa(id), strconv.Itoa(checkNo)))
      rch <- gene
      // fmt.Println(fmt.Sprintf("\tPushed to rch: Worker %s (%s)", strconv.Itoa(id), strconv.Itoa(checkNo)))

    }
    close(rch)
  }()
  return rch
}
