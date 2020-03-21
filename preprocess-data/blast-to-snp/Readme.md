# SNP data based on sequence alignments
Diese Readme-ToDo-Liste gerne bearbeiten, ergänzen, erledigte Sachen markieren.
Die Daten (Häufigkeiten) dieser Listen können zum Training in den folgenden ML-Ansätzen (oder HMMs etc.) benutzt werden. Weiterhin bietet dieser Ansatz eine einfache Vergleichmöglichkeit für bekannte SNP-Positionen und Vergleiche gegen andere Genome als im nextstrain-Baum vorhanden sind.

## Mögliche Anwendungen
- Interessante Domänen finden? An die Biologen: Wo macht es Sinn zu suchen, welche Bereiche sind konserviert, gibt es Datenbanken?
- Blast zu ähnlichen Viren um die konserviereten Bereiche zu finden
- BLAST als Webanfrage oder mit lokaler Datenbank implementieren

## Beispiel Workflow 
### Blast results 
In diesem Fall habe ich die Ergbenisse fix über den NCBI-Webblast abgrufen. Das sollte a) noch richtig implementiert werden und b) die Referenzdatenbank für konkrete Fragestellungen korrekt gewählt werden.
Die Anfrage verwendet derzeit genomic/Viruses/Betacoronavirus. 
Das Ergebnis liegt in blast.xml. Ich habe nur ungapped Alignments prozessiert.
### Blast to SNPs
Um die SNPs aus dem Ergebnis zu extrahieren habe ich [BlastNtoSnp](http://lindenb.github.io/jvarkit/BlastNToSnp.html) verwendet.
Ich habe das Tool fix bei der Recherche gefunden - falls jemand Implikationen sieht, warum wir das nicht benutzen sollten, bitte kommentieren.

#### Komplieren
Wäre schön wenn jemand hier ein Dockerfile anlegen könnte mit BAST und diesem jvarkit. 

```bash
git clone "https://github.com/lindenb/jvarkit.git"
cd jvarkit
./gradlew blast2snp
cp dist/blastn2snp.jar ../..
#oder wohin es soll
cd ../..
chmod +x blastn2snp.jar
```

#### Ergebnisse verarbeiten
Siehe auch blast-to-snp.sh. 

```
 java -jar blastn2snp.jar blast.xml > snps.txt
 
```

# Weitere ToDos
## Tabellenstruktur
Die Tabelle entspricht noch nicht der finalen Struktur. Diese sollte wie [https://github.com/poysh/idee1_hypervirome_project/blob/dev/data/processed/tree-data-nucleotide-mutations.csv]() aufgbaut sein.
Hier brauchen wir noch einen Parser, der Einträge erstellt. Folgendes ist zu beachten:

- position ist query-POS
- original_nucleotide ist REF(hit)
- mutation_nucleotide ist ALT(query)
- original_id ist 0
- mutation_id ist hit
- Manchmal ist mehr als eine Base in REF(hit) und ALT(query). Dann müsstet ihr das auseinandernehmen. Hinten in der Spalte blast.mid.var gibt es . und | : . bedeutet Mutation, | bedeutet Base ist gleich. Hier muss dann also ein Eintrag in mehrere aufgesplittet werden.

##Dockerfile
Sollte blast und java enthalten für jvarkit. 
Gut wäre es, wenn vielleicht die reference.gb ersetzt werden kann (mount etc.)
