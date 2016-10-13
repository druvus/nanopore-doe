# abruijn

## Command

    abruijn.py MAP006-PCR-1_2D_pass.fasta out_abruijn 60 --platform nano --threads 4


## Parameters
### abruijn

```
    usage: abruijn.py [-h] [--debug] [--resume] [-t THREADS] [-i NUM_ITERS]
                      [-p {pacbio,nano,pacbio_hi_err}] [-k KMER_SIZE]
                      [-o MIN_OVERLAP] [-m MIN_KMER_COUNT] [-x MAX_KMER_COUNT]
                      [--version]
                      reads out_dir coverage
    
    ABruijn: assembly of long and error-prone reads
    
    positional arguments:
      reads                 path to a file with reads in FASTA format
      out_dir               output directory
      coverage              estimated assembly coverage
    
    optional arguments:
      -h, --help            show this help message and exit
      --debug               enable debug output
      --resume              try to resume previous assembly
      -t THREADS, --threads THREADS
                            number of parallel threads (default: 1)
      -i NUM_ITERS, --iterations NUM_ITERS
                            number of polishing iterations (default: 2)
      -p {pacbio,nano,pacbio_hi_err}, --platform {pacbio,nano,pacbio_hi_err}
                            sequencing platform (default: pacbio)
      -k KMER_SIZE, --kmer-size KMER_SIZE
                            kmer size (default: 15)
      -o MIN_OVERLAP, --min-overlap MIN_OVERLAP
                            minimum overlap between reads (default: 5000)
      -m MIN_KMER_COUNT, --min-coverage MIN_KMER_COUNT
                            minimum kmer coverage (default: auto)
      -x MAX_KMER_COUNT, --max-coverage MAX_KMER_COUNT
                            maximum kmer coverage (default: auto)
      --version             show program's version number and exit

```


## Optimization
The variables are selected for evaluation.

*KMER_SIZE
*MIN_OVERLAP
*
