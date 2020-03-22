#!/bin/bash
#Get the candidates
blastn -db genomic/Viruses/Betacoronavirus -query sequence.fasta -remote -out blast.out -outfmt "6 sseqid sgi sacc  pident length mismatch gapopen qstart qend sstart send evalue bitscore" -ungapped
#Select candidates
awk -F " " 'NR <= 15{ if($4 != 100.00) printf $3" "}' blast.out > candidates.ids
#Download them
ncbi-acc-download -m nucleotide -F fasta --out candidates.fa $(cat candidates.ids)
#Sequence alignment
virulign sequence.fasta candidates.fa --exportKind GlobalAlignment  > alignment.mfa
virulign sequence.fasta candidates.fa --exportKind MutationTable  > alignment_mutations.tab
virulign sequence.fasta candidates.fa --exportKind PositionTable  > alignment_positions.tab

#Phylogenetic tree
Rscript phylo_tree.R