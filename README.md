# idee1_hypervirome_project
#wirvsvirus

## Content

### Data
In the data folder are files that contain important informations about the sars-cov-2 virus from the following sources:

  * http://data.nextstrain.org/ncov.json

### Scripts
To be able to process all data, here are some scripts that process data to bring it in a more suited format. A short overview:

  * generate-csv-from-json: parses `ncov.json` to `.csv`

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