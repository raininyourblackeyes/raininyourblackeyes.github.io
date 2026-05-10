import re

# Open input FASTA file containing yeast cDNA sequences
infile = open(r'D:\IBI\IBI1_2025-26\Practical7\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')

# Open output FASTA file to write genes that have at least one in-frame stop codon
outfile = open(r'D:\IBI\IBI1_2025-26\Practical7\stop_genes.fa', 'w')

# Variables to store current header and sequence while reading the file
header = ''
sequence = ''

#record the genes read
total_genes = 0  #count how many genes we have read in total, including those without stop codons
written_genes = 0 #count how many genes we have written to the output file, which should only include those with at least one in-frame stop codon
example_count = 0 #counter to track how many example genes we have printed to the console, we will print details for the first 5 genes with stop codons we encounter

print('Starting to process the input FASTA file...')

# Read the input file line by line
for line in infile:
    # Remove newline characters at the end of the line
    line = line.rstrip()

    # Check if the line is a FASTA header (starts with '>')
    if line.startswith('>'):
        # If we already have a previous gene stored, process it
        if header != '':
            # Extract gene name from header using regex
            # Matches gene:XXX pattern
            gene_name = re.findall(r'gene:(\S+)', header)

            # If regex found a match, use it; otherwise fallback to full header
            if gene_name:
                gene_name = gene_name[0]
            else:
                gene_name = header[1:]  # remove '>' from header

            # List to store stop codon types found in this gene
            found_stops = []

            # Scan the sequence to find all ORFs
            for i in range(len(sequence) - 2):
                # Look for start codon ATG
                if sequence[i:i+3] == 'ATG':
                    # Move in steps of 3 to stay in-frame
                    for j in range(i+3, len(sequence) - 2, 3):
                        codon = sequence[j:j+3]

                        # Check if this codon is a stop codon
                        if codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
                            # Add stop codon type to list if not already recorded
                            if codon not in found_stops:
                                found_stops.append(codon)
                            # Stop scanning this ORF after the first stop codon
                            break

            # Only write genes that have at least one in-frame stop codon
            if len(found_stops) > 0:
                # Build new FASTA header with gene name and stop codons
                out_header = '>' + gene_name + ' ' + ' '.join(found_stops)
                outfile.write(out_header + '\n')
                # Write the full sequence (as-is, without line wrapping)
                outfile.write(sequence + '\n')

        # Start new gene record
        header = line
        sequence = ''

    else:
        # Concatenate sequence lines; note: original code does not convert to uppercase
        sequence = sequence + line

# Process the last gene after the loop ends
if header != '':
    total_genes += 1
    gene_name = re.findall(r'gene:(\S+)', header)
    if gene_name:
        gene_name = gene_name[0]
    else:
        gene_name = header[1:]

    found_stops = []
    for i in range(len(sequence) - 2):
        if sequence[i:i+3] == 'ATG':
            for j in range(i+3, len(sequence) - 2, 3):
                codon = sequence[j:j+3]
                if codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
                    if codon not in found_stops:
                        found_stops.append(codon)
                    break

    if len(found_stops) > 0:
        written_genes += 1

        if example_count < 5:
            print(f'Example gene: {gene_name}, found stop codons: {found_stops}', 'sequence length:', len(sequence))
            example_count += 1

        out_header = '>' + gene_name + ' ' + ' '.join(found_stops)
        outfile.write(out_header + '\n')
        outfile.write(sequence + '\n')

# Close files to ensure all data is written
infile.close()
outfile.close()