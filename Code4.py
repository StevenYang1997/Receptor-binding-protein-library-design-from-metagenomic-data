from Bio import SeqIO
description = []
Sequence = []
remove = []
for seq_record in SeqIO.parse(r'C:\Users\yanxi\Desktop\Work\Study\Research\oligosequence_generator\signalp-5.0b\test\Pf1.txt', "fasta"):
    description.append(seq_record.description)
    Sequence.append(seq_record.seq)
number_of_gene = len(description)
i = 1
while i < number_of_gene:
    current_seq = Sequence[i]
    for k in range(i):
        if current_seq == Sequence[k]:
            remove.append(i)
            break
    i = i+1
for index in sorted(remove, reverse=True):
    del description[index]
    del Sequence[index]

non_redundent_sequence_file = open(r"C:\Users\yanxi\Desktop\Work\Study\Research\oligosequence_generator\50gene\non_redundent_sequence.txt", "w")
for i in range(len(description)):
    non_redundent_sequence_file.write(">" + str(description[i]) + "\n" + str(Sequence[i]) + "\n")
non_redundent_sequence_file.close()
print('There were ' + str(number_of_gene) + ' genes before originally, ''There are ' + str(len(description)) + ' genes in total now')
