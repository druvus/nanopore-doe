# links

## Command

    LINKS -f seq.fasta -s readfiles.fof


## Parameters

```
Usage: LINKS [-OPTIONS [-MORE_OPTIONS]] [--] [PROGRAM_ARG1 ...]

The following single-character options are accepted:
        With arguments: -f -s -d -k -e -l -a -v -b -t -p -o -r -x -m -z

Options may be merged together.  -- stops processing of options.
Space is not required between options and their arguments.
  [Now continuing due to backward compatibility and excessive paranoia.
   See 'perldoc Getopt::Std' about $Getopt::Std::STANDARD_HELP_VERSION.]
Usage: /mnt/powervault/bin/conda/bin/LINKS [v1.8.4]
-f  sequences to scaffold (Multi-FASTA format, required)
-s  file-of-filenames, full path to long sequence reads or MPET pairs [see below] (Multi-FASTA/fastq format, required)
-m  MPET reads (default -m 1 = yes, default = no, optional
        ! DO NOT SET IF NOT USING MPET. WHEN SET, LINKS WILL EXPECT A SPECIAL FORMAT UNDER -s
        ! Paired MPET reads in their original outward orientation <- -> must be separated by ":"
          >template_name
          ACGACACTATGCATAAGCAGACGAGCAGCGACGCAGCACG:ATATATAGCGCACGACGCAGCACAGCAGCAGACGAC
-d  distance between k-mer pairs (ie. target distances to re-scaffold on. default -d 4000, optional)
        Multiple distances are separated by comma. eg. -d 500,1000,2000,3000
-k  k-mer value (default -k 15, optional)
-t  step of sliding window when extracting k-mer pairs from long reads (default -t 2, optional)
        Multiple steps are separated by comma. eg. -t 10,5
-o  offset position for extracting k-mer pairs (default -o 0, optional)
-e  error (%) allowed on -d distance   e.g. -e 0.1  == distance +/- 10% (default -e 0.1, optional)
-l  minimum number of links (k-mer pairs) to compute scaffold (default -l 5, optional)
-a  maximum link ratio between two best contig pairs (default -a 0.3, optional)
         *higher values lead to least accurate scaffolding*
-z  minimum contig length to consider for scaffolding (default -z 500, optional)
-b  base name for your output files (optional)
-r  Bloom filter input file for sequences supplied in -s (optional, if none provided will output to .bloom)
         NOTE: BLOOM FILTER MUST BE DERIVED FROM THE SAME FILE SUPPLIED IN -f WITH SAME -k VALUE
         IF YOU DO NOT SUPPLY A BLOOM FILTER, ONE WILL BE CREATED (.bloom)
-p  Bloom filter false positive rate (default -p 0.001, optional; increase to prevent memory allocation errors)
-x  Turn off Bloom filter functionality (-x 1 = yes, default = no, optional)
-v  Runs in verbose mode (-v 1 = yes, default = no, optional)

```


## Optimization
The variables are selected for evaluation.

* -d  distance between k-mer pairs 
* -k  k-mer value
* -z  minimum contig length to consider for scaffolding
