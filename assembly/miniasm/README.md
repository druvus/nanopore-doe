# miniasm

## Command

    minimap -Sw5 -L100 -m0 -t8 reads.fq reads.fq | gzip -1 > reads.paf.gz
    miniasm -f reads.fq reads.paf.gz > reads.gfa


## Parameters
### minimap

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

