from Bio import SeqIO
from dnachisel import *

ID= []
Sequence = []
optimized_sequence = []
for seq_record in SeqIO.parse(r'C:\Users\yanxi\Desktop\Work\Study\Research\oligosequence_generator\500reverse_translation.txt', "fasta"):
    ID.append(seq_record.description)
    Sequence.append(seq_record.seq)
number_of_gene = len(ID)
k=0
for i in Sequence:
    print(k)
    problem = DnaOptimizationProblem(
        sequence=str(i),
        constraints=[
            AvoidHairpins(),
            AvoidPattern("NcoI_site"),
            AvoidPattern("AgeI_site"),
            AvoidPattern('MlyI_site'),
            AvoidPattern('NotI_site'),
            EnforceGCContent(mini=0.3, maxi=0.7, window=80),
            EnforceTranslation(),
            AvoidPattern('2x9mer')
        ],
        objectives=[CodonOptimize(species='m_phage' )]
    )

    # SOLVE THE CONSTRAINTS, OPTIMIZE WITH RESPECT TO THE OBJECTIVE

    problem.resolve_constraints()
    problem.optimize()

    # PRINT SUMMARIES TO CHECK THAT CONSTRAINTS PASS
    #print(i)
    print(problem.constraints_text_summary())
    print(problem.objectives_text_summary())
    k=k+1
    # GET THE FINAL SEQUENCE (AS STRING OR ANNOTATED BIOPYTHON RECORDS)

    optimized_sequence.append(problem.sequence)  # string

optimized_file = open(r"C:\Users\yanxi\Desktop\Work\Study\Research\oligosequence_generator\500_codon_optimized.txt", "w")
for j in range(number_of_gene):
    optimized_file.write(">" + str(ID[j]) + "\n"  + str(optimized_sequence[j]) + "\n")
optimized_file.close()
