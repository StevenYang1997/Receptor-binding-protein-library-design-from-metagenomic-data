from Bio import SeqIO
description = []
Sequence = []
Trimmed_sequence = []
for seq_record in SeqIO.parse(r'C:\Users\yanxi\Desktop\500_overallremovedsignal.txt', "fasta"):
    description.append(seq_record.description)
    Sequence.append(seq_record.seq)
number_of_gene = len(description)
i = 0
while i < number_of_gene:
    current_seq = Sequence[i]
    if len(current_seq) <=229:
        Trimmed_sequence.append(current_seq)
    else:
        Trimmed_sequence.append(current_seq[0:229])
    i = i+1
print(len(description), len(Sequence), len(Trimmed_sequence))
trimmed500 = open(r"C:\Users\yanxi\Desktop\trimmed500.txt", "w")
for j in range(len(description)):
    trimmed500.write(">" + str(description[j]) + "\n" + str(Trimmed_sequence[j]) + "\n")
trimmed500.close()
