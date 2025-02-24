def Gfind(sequence):
    import re
    sequence_length = len(sequence)
    num_iter= sequence_length - 31 + 1
    start_location = 15
    peak_iter = 0
    G_peak = 0
    end_location = start_location + num_iter - 1
    for median in range(num_iter):
        current_sequence =  sequence[start_location + median -15 : start_location + median + 15]
        G_count = current_sequence.count('G') + current_sequence.count('S')+ current_sequence.count('N')+ current_sequence.count('T') + current_sequence.count('D') + current_sequence.count('P') + current_sequence.count('E')
        if G_count >= G_peak:
            G_peak = G_count
            peak_iter = median
    if G_peak <=9:
        newsequence = 'no obvious G linker region'
    if G_peak > 9:
        current_median = start_location + peak_iter
        windowfiveupstream = current_median - 2
        windowfivedownstream = current_median+ 3
        seqof5 = sequence[windowfiveupstream : windowfivedownstream]
        skip1_median = current_median - 1
        skip1_windowfiveupstream = skip1_median - 2
        skip1_wondowfivedownstream = skip1_median + 3
        skip1_seqof5 = sequence[skip1_windowfiveupstream : skip1_wondowfivedownstream]
        skip2_median = current_median - 2
        skip2_windowfiveupstream = skip2_median - 2
        skip2_wondowfivedownstream = skip2_median + 3
        skip2_seqof5 = sequence[skip2_windowfiveupstream : skip2_wondowfivedownstream]
        skip3_median = current_median - 3
        skip3_windowfiveupstream = skip3_median - 2
        skip3_wondowfivedownstream = skip3_median + 3
        skip3_seqof5 = sequence[skip3_windowfiveupstream : skip3_wondowfivedownstream]
        skip4_median = current_median - 4
        skip4_windowfiveupstream = skip4_median - 2
        skip4_wondowfivedownstream = skip4_median + 3
        skip4_seqof5 = sequence[skip4_windowfiveupstream : skip4_wondowfivedownstream]
        skip5_median = current_median - 5
        skip5_windowfiveupstream = skip5_median - 2
        skip5_wondowfivedownstream = skip5_median + 3
        skip5_seqof5 = sequence[skip5_windowfiveupstream : skip5_wondowfivedownstream]
        while seqof5.count('G')  >= 3 or skip1_seqof5.count('G') >= 3 or skip2_seqof5.count('G') >= 3 or skip3_seqof5.count('G')>= 3 or skip4_seqof5.count('G')>= 3 or skip5_seqof5.count('G')>= 3:
            current_median = current_median - 1
            windowfiveupstream = current_median - 2
            windowfivedownstream = current_median+ 3
            seqof5 = sequence[windowfiveupstream : windowfivedownstream]
            skip1_median = current_median - 1
            skip1_windowfiveupstream = skip1_median - 2
            skip1_wondowfivedownstream = skip1_median + 3
            skip1_seqof5 = sequence[skip1_windowfiveupstream : skip1_wondowfivedownstream]
            skip2_median = current_median - 2
            skip2_windowfiveupstream = skip2_median - 2
            skip2_wondowfivedownstream = skip2_median + 3
            skip2_seqof5 = sequence[skip2_windowfiveupstream : skip2_wondowfivedownstream]
            skip3_median = current_median - 3
            skip3_windowfiveupstream = skip3_median - 2
            skip3_wondowfivedownstream = skip3_median + 3
            skip3_seqof5 = sequence[skip3_windowfiveupstream : skip3_wondowfivedownstream]
            skip4_median = current_median - 4
            skip4_windowfiveupstream = skip4_median - 2
            skip4_wondowfivedownstream = skip4_median + 3
            skip4_seqof5 = sequence[skip4_windowfiveupstream : skip4_wondowfivedownstream]
            skip5_median = current_median - 5
            skip5_windowfiveupstream = skip5_median - 2
            skip5_wondowfivedownstream = skip5_median + 3
            skip5_seqof5 = sequence[skip5_windowfiveupstream : skip5_wondowfivedownstream]
        cutoffpoint1 = current_median -2
        cutoffpoint2 = current_median -2
        try:
            while sequence[cutoffpoint1] != 'G' or sequence[cutoffpoint1 + 1] != 'G':
                cutoffpoint1 = cutoffpoint1 + 1
        except:
            cutoffpoint1 = 1000000 #just to be a number large enough
        try:
            while re.match('G[A-Z]G[A-Z]G[A-Z]',sequence[cutoffpoint2:cutoffpoint2 + 6]) is None:
                if cutoffpoint2 <= len(sequence)-5:
                    cutoffpoint2 = cutoffpoint2 + 1
                else:
                    break
        except:
            cutoffpoint2 = 1000000 #just to be a number large enough
        cutoffpoint = min(cutoffpoint1,cutoffpoint2)
        newsequence = sequence[: cutoffpoint]
        return(sequence,newsequence)
    
