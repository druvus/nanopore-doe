# miniasm

## Command

    minimap -Sw5 -L100 -m0 -t8 reads.fq reads.fq | gzip -1 > reads.paf.gz
    miniasm -f reads.fq reads.paf.gz > reads.gfa


## Parameters
### minimap

```
Usage: minimap [options] <target.fa> [query.fa] [...]
Options:
  Indexing:
    -k INT     k-mer size [15]
    -w INT     minizer window size [{-k}*2/3]
    -I NUM     split index for every ~NUM input bases [4G]
    -d FILE    dump index to FILE []
    -l         the 1st argument is a index file (overriding -k, -w and -I)
  Mapping:
    -f FLOAT   filter out top FLOAT fraction of repetitive minimizers [0.001]
    -r INT     bandwidth [500]
    -m FLOAT   merge two chains if FLOAT fraction of minimizers are shared [0.50]
    -c INT     retain a mapping if it consists of >=INT minimizers [4]
    -L INT     min matching length [40]
    -g INT     split a mapping if there is a gap longer than INT [10000]
    -T INT     SDUST threshold; 0 to disable SDUST [0]
    -S         skip self and dual mappings
    -O         drop isolated hits before chaining (EXPERIMENTAL)
    -P         filtering potential repeats after mapping (EXPERIMENTAL)
    -x STR     preset (recommended to be applied before other options) []
               ava10k: -Sw5 -L100 -m0 (PacBio/ONT all-vs-all read mapping)
  Input/Output:
    -t INT     number of threads [3]
    -V         show version number
```

### miniasm

```
Usage: miniasm [options] <in.paf>
Options:
  Pre-selection:
    -R          prefilter clearly contained reads (2-pass required)
    -m INT      min match length [100]
    -i FLOAT    min identity [0.05]
    -s INT      min span [2000]
    -c INT      min coverage [3]
  Overlap:
    -o INT      min overlap [same as -s]
    -h INT      max over hang length [1000]
    -I FLOAT    min end-to-end match ratio [0.8]
  Layout:
    -g INT      max gap differences between reads for trans-reduction [1000]
    -d INT      max distance for bubble popping [50000]
    -e INT      small unitig threshold [4]
    -f FILE     read sequences []
    -n INT      rounds of short overlap removal [3]
    -r FLOAT[,FLOAT]
                max and min overlap drop ratio [0.7,0.5]
    -F FLOAT    aggressive overlap drop ratio in the end [0.8]
  Miscellaneous:
    -p STR      output information: bed, paf, sg or ug [ug]
    -b          both directions of an arc are present in input
    -1          skip 1-pass read selection
    -2          skip 2-pass read selection
    -V          print version number
```

## Optimization
The variables are selected for evaluation.

* 
* 
