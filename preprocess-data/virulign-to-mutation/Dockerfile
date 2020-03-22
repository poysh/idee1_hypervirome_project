#docker build -t <imagename> .
#docker run --rm -d --hostname localhost --name <containername> -i <imagename> /bin/bash
#docker exec -it <containername> /bin/bash

FROM ubuntu:19.10

RUN apt-get update && \
  export DEBIAN_FRONTEND=noninteractive && \
  apt-get -y --assume-yes install ncbi-blast+ python3 python3-pip wget tzdata r-base && \
  pip3 install ncbi-acc-download && \
  cd /tmp && \
  wget https://github.com/rega-cev/virulign/releases/download/v1.0.1/virulign-linux-64bit.tgz && \
  gunzip virulign-linux-64bit.tgz && \
  tar -xf virulign-linux-64bit.tar && \
  cp virulign /usr/local/bin/ && \
  Rscript -e 'install.packages("BiocManager")' && \
  Rscript -e 'BiocManager::install(c("ape", "seqinr"))'

WORKDIR /root
COPY phylo_tree.R phylo_tree.R
COPY pipline.sh pipline.sh
COPY data data