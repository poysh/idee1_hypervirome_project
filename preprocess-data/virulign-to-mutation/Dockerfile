FROM ubuntu:18.04
RUN apt-get update
RUN apt-get -y install ncbi-blast+
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata
RUN apt-get -y --assume-yes install r-base
RUN apt-get -y install python3-pip
RUN apt-get -y install wget
RUN pip3 install ncbi-acc-download
RUN cd /tmp 
RUN wget https://github.com/rega-cev/virulign/releases/download/v1.0.1/virulign-linux-64bit.tgz
RUN gunzip virulign-linux-64bit.tgz 
RUN tar -xf virulign-linux-64bit.tar
RUN cp virulign /usr/local/bin/
RUN Rscript -e 'install.packages("BiocManager")'
RUN Rscript -e 'BiocManager::install(c("ape", "seqinr"))'
