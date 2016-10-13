# spectrassembler

## Command

    minimap -S oxford.fasta oxford.fasta > oxford.mini
    bwa index oxford_reference.fa
    bwa bwasw oxford_reference.fa oxford.fasta > oxford.sam
    get_position_from_sam.py oxford.sam oxford.fasta
    spectral_layout_from_minimap.py -f oxford.fasta -m oxford.mini -w -vv --ref_pos_csvf reads_position.csv


## Parameters

```
python spectral_layout_from_minimap.py -f reads.fasta -m overlaps.mini
[-h (--help)]
[-f : file containing reads in FASTA format]
[-m : overlap file from minimap in PAF format]
[-r (--root) : root directory where to write layout files (default "./")]
[-w (--write_poa_files) : Whether to write POA input files for consensus generation or not.]
[--w_len <int(2500)> : length of consensus windows for POA]
[--w_ovl_len <int(1250)> : overlap length between two successive consensus windows]
[--sim_thr <int(850)> : threshold on overlap score (similarity matrix preprocessing). This is a
crucial parameter that should be increased for repetitive genomes (e.g., eukaryotic) or if
the results are unsatisfactory. Conversely, if the assembly is too fragmented (too many contigs),
it can be decreased. It should also be modified according to the overlapper used
(this value was chosen when using minimap).]
[--len_thr <int(3500)> : threshold on the length of the overlap (similarity matrix preprocessing)]
[--ref_pos_csvf : csv file (generated with get_position_from_sam.py)
with position of reads (in same order as in the fasta file)
obtained from BWA, in order to plot reads position found vs reference.)]
[-v verbosity level (-v, -vv or none), default none]
```

```
python gen_cons_from_poa.py -cc 3 --poa_mat_path /path/to/poa-score.mat -vv
[-h (--help)]
[-cc (--contig) : index of contig you wish to compute consensus for]
[--poa_mat_path : path to score matrix file for alignment]
[--poa_path : path to poa executable if it is not on your path
(do not specify this option if poa is on your path)]
[-r (--root) : root directory where to write layout files (default "./")]
[--w_len <int(2500)> : length of consensus windows for POA.
! MUST BE THE SAME VALUE AS IN spectral_layout_from_minimap.py !]
[--w_ovl_len <int(1250)> : overlap length between two successive consensus windows
! MUST BE THE SAME VALUE AS IN spectral_layout_from_minimap.py !]
[-v verbosity level (-v, -vv or none), default none]
```


## Optimization
The variables are selected for evaluation.

* 
* 
