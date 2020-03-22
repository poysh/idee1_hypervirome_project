# Preprocess data

### Scripts
To be able to process all data, here are some scripts that process data to bring it in a more suited format. A short overview:

  * parse-nextstrain-json-to-csv: parses `ncov.json` to `.csv`

#### generate-csv-from-json
A little script that parses the nexstrain.org `ncov.json` file and creates a table in `.csv` format. It extracts the following informations (if available).

  * name
  * mutations
  * clade
  * divisioncountry
  * nuc
  * sampling_date
  * originating_lab
  * submitting_lab
  * GISAID_EPI_ISL
  * GenBank_accession