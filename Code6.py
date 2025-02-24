from Bio import SeqIO
import re
description_original = []
Sequence_original = []
non_signal_sequence = []
description_no_signal_sequence= []
linkerfile= open(r'C:\Users\yanxi\Desktop\Work\Study\Research\oligosequence_generator\Pf1_overall_summary.signalp5', 'r')
linkerline= linkerfile.readlines()
index = 2
for seq_record in SeqIO.parse(r'C:\Users\yanxi\Desktop\Work\Study\Research\oligosequence_generator\Pf1_overall_toremovesignalP.fasta', "fasta"):
    description_original.append(seq_record.description) # this list will be different from pre-original if there's sequence with no obvious G linker region, same for Sequence
    Sequence_original.append(seq_record.seq)
    if re.findall('\d+\-\d+',linkerline[index]):
        current_seq_signal_peptide_cleavage = str(re.findall('\d+\-\d+',linkerline[index]))
        seq_signal_peptide_cleavage = re.search('\d+',current_seq_signal_peptide_cleavage)
        non_signal_sequence.append(str(seq_record.seq)[int(seq_signal_peptide_cleavage.group()) :])
        description_no_signal_sequence.append(seq_record.description)
    index +=1
linkerfile.close()
removedsignal_file = open(r"C:\Users\yanxi\Desktop\Work\Study\Research\oligosequence_generator\Pf1_overallremovedsignal.txt", "w")
for i in range(len(non_signal_sequence)):
    removedsignal_file.write(">" + str(description_no_signal_sequence[i]) + "\n"  + str(non_signal_sequence[i]) + "\n")
removedsignal_file.close()
