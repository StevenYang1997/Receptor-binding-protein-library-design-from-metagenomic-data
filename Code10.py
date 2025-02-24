import os
import csv
from Bio import SeqIO
from csv import reader
from csv import writer
from pandas import *
Allgene = []
genelength = []
indexscore = []
directory = r'C:\Users\yanxi\Desktop\Work\Study\Research\500 gene\All Blast Results'
Allsequence = []
data = read_csv(r'C:\Users\yanxi\Desktop\Work\Study\Research\oligosequence_generator\Inovirusp.csv')
sequence = data['Seq'].tolist()
for filename in os.listdir(directory):
    csv_file = open(os.path.join(directory, filename))
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        gene_label = row[0]
        if gene_label in Allgene:
            index_in_Allgene = Allgene.index(gene_label)
            if float(row[2]) == 0:
                score = 1/1E-175
            else:
                score = 1/float(row[2])
                indexscore[index_in_Allgene] = indexscore[index_in_Allgene] + score
        else:
            Allgene.append(gene_label)
            genelength.append(row[1])
            Allsequence.append(sequence[int(row[0])-1])
            if float(row[2]) == 0:
                score = 1/1E-175
            else:
                score = 1/float(row[2])
            indexscore.append(score)

# writing the data into the file
with open(r'C:\Users\yanxi\Desktop\500gene_evalue_addup.txt', 'w', newline='') as csvoutput:
    write = csv.writer(csvoutput)
    for i in range(len(Allgene)):
        content = [Allgene[i], genelength[i], indexscore[i],Allsequence[i]]
        write.writerow(content)
