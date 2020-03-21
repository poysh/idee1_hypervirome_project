#!/bin/bash
 blastn -db genomic/Viruses/Betacoronavirus -query reference.gb -remote -out blast.xml -outfmt 5 -ungapped
 java -jar blastn2snp.jar blast.xml > test.out
 