def generate_oligo(phagename, complete_sequence):
    import math
    oligonumber = math.ceil((len(complete_sequence)-30)/190)
    index = 1
    oligoname = []
    oligo = []
    oligo_with_primers = []
    fill_up = 'ATGCTACGAATTGGCCTTAACCGGAAATTTGGGCCCTTTAAACCCGGGTTTTCCCCAAAAGGGG'
    PCR_forward_primer = 'CGATTAGCAAGAGTCCTAGC'
    PCR_reverse_primer = 'CGTAGGACTCTACAATACTC'
    MlyI_forward_sequence_nummber= []
    MlyI_reverse_sequence_number = []
    for i in range(1, oligonumber):
        oligoname.append(phagename + '_' + str(index))
        oligo.append(complete_sequence[ 190 * (index - 1) : 190 * index + 30])
        oligo_with_primers.append( PCR_forward_primer + oligo[index - 1 ] + PCR_reverse_primer)
        MlyI_forward_sequence_nummber.append(oligo_with_primers[index-1].count('GAGTC'))
        MlyI_reverse_sequence_number.append(oligo_with_primers[index-1].count('GACTC'))
        index = index + 1
    oligoname.append(phagename + '_' + str(index))
    last_oligo_length = len(complete_sequence[ 190 * (index - 1) :] )
    if last_oligo_length <= 64:
        oligo.append(complete_sequence[ 190 * (index - 1) :] + fill_up[-(64-last_oligo_length):]  + "T" *156)
    else:
        oligo.append((complete_sequence[ 190 * (index - 1) :]  + "T" * (220 - last_oligo_length)))
    oligo_with_primers.append( PCR_forward_primer + oligo[index - 1 ] + PCR_reverse_primer)
    MlyI_forward_sequence_nummber.append(oligo_with_primers[index-1].count('GAGTC'))
    MlyI_reverse_sequence_number.append(oligo_with_primers[index-1].count('GACTC'))
    resultarray = [oligoname, oligo, oligo_with_primers, MlyI_forward_sequence_nummber, MlyI_reverse_sequence_number]
    return(resultarray)
