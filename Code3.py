from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from csv import reader
from csv import writer
remove = []
Sequence = []
all_input = []
with open(r'C:\Users\yanxi\Desktop\Work\Study\Research\oligosequence_generator\pf1_check1_NC001331.txt','r') as csvinput:


    data = reader(csvinput)

    for row in data:
        all_input.append(row)
        Sequence.append(row[6])
    lines= len(Sequence)
    all = list(range(0, lines))
    i = 1
    while i < lines:
        current_seq = Sequence[i]
        for k in range(i-10,i):
            #print(i,k)
            a = pairwise2.align.globalxx(current_seq, Sequence[k],score_only=True)
            #print(a)
            if a >=320:
                remove.append(i)
                break
        i=i+1
    stay = [x for x in all if x not in remove]
    with open(r'C:\Users\yanxi\Desktop\Work\Study\Research\oligosequence_generator\pf1_check2_NC001331.txt', 'w', newline='') as csvoutput:
        csv_writer = writer(csvoutput)
        for j in stay:
            csv_writer.writerow(all_input[int(j)])
        
