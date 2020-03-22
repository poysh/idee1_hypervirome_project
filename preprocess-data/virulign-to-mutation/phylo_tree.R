library(seqinr)
library(ape)

myalg<-read.alignment("alignment.mfa", format = "fasta")
distances<- dist.alignment(myalg)
myTree <- nj(distances)

png("tree.png")
plot(myTree, main="Phylogenetic Tree")
dev.off()
