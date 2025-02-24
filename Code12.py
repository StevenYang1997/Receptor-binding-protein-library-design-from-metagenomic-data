from Bio import SeqIO
description = []
Sequence = []
newlist = []
for seq_record in SeqIO.parse(r'C:\Users\yanxi\Desktop\Work\Study\Research\500 gene\Processing\trimmed229.txt', "fasta"):
    description.append(seq_record.description)
    Sequence.append(seq_record.seq)
number_of_gene = len(description)
i = 0
a = 1
while i < number_of_gene:
    current_seq = Sequence[i]
    if 'GGG' in current_seq:
        a = a+1
    else:
        newlist.append(i)
    i = i+1

for index in sorted(newlist, reverse=True):
    del description[index]
    del Sequence[index]

rightlength_sequence_file500 = open(r"C:\Users\yanxi\Desktop\229withggg.txt", "w")
for i in range(len(description)):
    print(len(Sequence[i]))
    rightlength_sequence_file500.write(">" + str(description[i]) + "\n" + str(Sequence[i]) + "\n")
rightlength_sequence_file500.close()
print('There were ' + str(number_of_gene) + ' genes before originally, ''There are ' + str(len(description)) + ' genes in total now')
