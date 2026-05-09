# define the mRNA sequence
seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
# define the start codon and the stop codons
start_codon = 'AUG'
stop_codons = {'UAA', 'UAG', 'UGA'}

# the all
valid_orfs = []

for i in range(len(seq) - 2):
    if seq[i:i+3] == start_codon:
        for j in range(i + 3,len(seq) - 2, 3):
            if seq[j:j+3] in stop_codons:
                orf_seq = seq[i:j+3]
                orf_len = len(orf_seq)
                valid_orfs.append((orf_len,orf_seq))
                break

# Filter and print the longest ORF (handle the case of no valid ORFs)
if valid_orfs:
    # Sort valid ORFs in DESCENDING order of length, take the first one (longest)
    valid_orfs_sorted = sorted(valid_orfs, key=lambda x: x[0], reverse=True)
    longest_orf_len, longest_orf_seq = valid_orfs_sorted[0]
    # Print the results as required (report sequence and nucleotide length)
    print(f"Longest identified ORF sequence: {longest_orf_seq}")
    print(f"Nucleotide length of the longest ORF: {longest_orf_len}")
else:
    # Prompt if no valid ORF exists (no start codon or no stop codon after start codon)
    print("No valid ORF found in the sequence (no start codon, or no stop codon in the same reading frame after the start codon).")