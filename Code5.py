from Bio import SeqIO
description = []
Sequence = []
remove = []
for seq_record in SeqIO.parse(r'C:\Users\yanxi\Desktop\rightlength_sequence_file500.txt', "fasta"):
    description.append(seq_record.description)
    Sequence.append(seq_record.seq)
number_of_gene = len(description)
i = 0
while i < number_of_gene:
    current_seq = Sequence[i]
    if Sequence[i][0] !='M':
        Sequence[i] = 'M' + Sequence[i]
    i = i+1


Withstartcodon_file500 = open(r"C:\Users\yanxi\Desktop\Withstartcodon_file500.txt", "w")
for i in range(len(description)):
    Withstartcodon_file500.write(">" + str(description[i]) + "\n" + str(Sequence[i]) + "\n")
Withstartcodon_file500.close()
