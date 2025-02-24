
from Bio import SeqIO
description = []
Sequence = []
remove = []
for seq_record in SeqIO.parse(r'C:\Users\yanxi\Desktop\non_mutant_sequence500.txt', "fasta"):
    description.append(seq_record.description)
    Sequence.append(seq_record.seq)
number_of_gene = len(description)
i = 0
while i < number_of_gene:
    current_seq = Sequence[i]
    if len(current_seq) <=300 or len(current_seq) >=550:
            remove.append(i)
    i = i+1
for index in sorted(remove, reverse=True):
    del description[index]
    del Sequence[index]

rightlength_sequence_file500 = open(r"C:\Users\yanxi\Desktop\rightlength_sequence_file500.txt", "w")
for i in range(len(description)):
    print(len(Sequence[i]))
    rightlength_sequence_file500.write(">" + str(description[i]) + "\n" + str(Sequence[i]) + "\n")
rightlength_sequence_file500.close()
print('There were ' + str(number_of_gene) + ' genes before originally, ''There are ' + str(len(description)) + ' genes in total now')
