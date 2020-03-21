# idee1_hypervirome_project
#wirvsvirus

## Content

### Data
In the data folder are files that contain important informations about the sars-cov-2 virus from the following sources:

#### raw sources
  * http://data.nextstrain.org/ncov.json

#### processed
  * tree-data.csv: ncov.json as .csv

### preprocess-data
Includes scripts that are necessary to preprocess external data to work with. 
#### nextstrain
Converts the JSON from nextstrain.org to a csv.
#### blast-to-snp
Includes scripts and workflows to extract SNPs from similiar sequences.