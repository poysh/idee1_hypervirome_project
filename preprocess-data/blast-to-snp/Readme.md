# SNP data based on sequence alignments
Diese Readme-ToDo-Liste gerne bearbeiten, ergänzen, erledigte Sachen markieren.
Die Daten (Häufigkeiten) dieser Listen können zum Training in den folgenden ML-Ansätzen (oder HMMs etc.) benutzt werden.

## TODO
- Interessante Domänen finden? An die Biologen: Wo macht es Sinn zu suchen, welche Bereiche sind konserviert, gibt es Datenbanken?
- Blast zu ähnlichen Viren um die konserviereten Bereiche zu finden
- BLAST als Webanfrage oder mit lokaler Datenbank implementieren
- Welche Referenzsequenz soll verwendet werden?

## Beispiel Workflow 
### Blast results 
In diesem Fall habe ich die Ergbenisse fix über den NCBI-Webblast abgrufen. Das sollte a) noch richtig implementiert werden und b) die Referenzdatenbank korrekt gewählt werden. Hier ging es nur um den Workflow. 
Das Ergebnis kann man unter [https://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Get&RID=7ARW805W014](https://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Get&RID=7ARW805W014) abrufen. 

### Blast to SNPs
Um die SNPs aus dem Ergebnis zu extrahieren habe ich [BlastNtoSnp](http://lindenb.github.io/jvarkit/BlastNToSnp.html) verwendet.
Ich habe das Tool fix bei der Recherche gefunden - falls jemand Implikationen sieht, warum wir das nicht benutzen sollten, bitte kommentieren.

#### Komplieren

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

```
java -jar blastn2snp.jar < 7ARW805W014-Alignment.xml > snps.tab
```
### R-Schnipsel 
Ich habe die Daten noch kurz in R eingelesen, nur SNPs extrahiert die keine In-Dels waren und ein kurzes Histogram geplottet. 

```R
#Read file
snps<-read.table(file = "snps.tab", sep = "\t")
#Select only SNPs without In-Dels
snps_mut<-snps[nchar(as.character(snps[,8]))==1 & nchar(as.character(snps[,9]))==1,]
#Order according to position in query genome
snps_mut_order<-snps_mut[order(snps_mut[,5]),]
#Plot a histogram for the first 100 nucleotides
hist(snps_mut_order[1:100,5], breaks=100)
```

# Kommentare
## Tabellenstruktur
Die resultierende Tabelle für die Weiterverarbeitung sollte zumindest wahrscheinlich folgendes enthalten:

- Position im Referenzgenom
- Nukleotid im Referenzgenom
- Nukleotid im Hit 

die Tabelle kann denn vermutlich zum Training verwendet werden. 
Falls hier was fehlt, bitte melden! 

## Datensätze zum Blasten und Lernen
Wir müssen noch die entsprechenden Datensätze finden. 

## Nextstrain-Daten
Ich vermute wir müssen die Tabelle für die Nextstrain-Daten ebenfalls in diesem Format anbieten damit die ML-Leute damit arbeiten können.

