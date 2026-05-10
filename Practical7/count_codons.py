import matplotlib.pyplot as plt
import re

start_codons = 'ATG'
stop_codons = ['TAA', 'TAG', 'TGA']

#ask the user to enter a stop codon
user_stop_codon = input('Enter a stop codon (TAA, TAG, or TGA): ').upper()
user_stop_codon = user_stop_codon.strip().upper() #Remove any leading/trailing whitespace

#keep asking until the user enters a valid stop codon
while user_stop_codon not in stop_codons:
    print('Invalid stop codon. Please enter TAA, TAG, or TGA.')
    user_stop_codon = input('Enter a stop codon (TAA, TAG, or TGA): ').upper()
    user_stop_codon = user_stop_codon.strip().upper() #Remove any leading/trailing whitespace

#open the FASTA file for reading
infile = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')

#variables to store the current header and sequence while reading the file
header = ''
sequence = ''

codon_counts = {} #across all genes that contain a valid longest ORF ending with the user-specified stop codon
total_genes = 0 #counter to track how many genes we have read in total, including those without stop codons
used_genes = 0 #counter to track how many genes we have found that contain the user-specified stop codon    
total_codons_counted = 0 #counter to track how many codons we have counted in total across all genes, including those without the user-specified stop codon 

#read the input file line by line
for line in infile:
    line = line.rstrip() #remove newline characters at the end of the line

    if line.startswith('>'): #check if the line is a FASTA header
        if header != '': #if we have a previous gene stored, process it
            total_genes += 1 #increment total genes counter
            gene_name = re.findall(r'gene:(\S+)', header) #extract gene name from header using regex
            if gene_name:
                gene_name = gene_name[0] #if regex found a match, use it; otherwise fallback to full header
            else:
                gene_name = header[1:] #remove '>' from header
            longest_orf = '' #variable to store the longest ORF found in this gene
            #scan the sequence to find all ORFs
            for i in range(len(sequence) - 2):
                if sequence[i:i+3] == start_codons: #look for start codon ATG
                    for j in range(i+3, len(sequence) - 2, 3): #move in steps of 3 to stay in-frame
                        codon = sequence[j:j+3]
                        if codon in stop_codons: #check if this codon is a stop codon
                            if codon == user_stop_codon: #check if this codon is the user-specified stop codon
                                current_orf = sequence[i:j+3] #extract the ORF from start codon to stop codon
                                if len(current_orf) > len(longest_orf): #if this ORF is longer than the longest found so far, update longest ORF
                                    longest_orf = current_orf

                            break #stop scanning this ORF after the first stop codon
            if longest_orf != '': #if we found at least one ORF with the user-specified stop codon
                used_genes += 1 #increment used genes counter
                upstream_length = longest_orf[:-3] #get the sequence upstream of the stop codon (excluding the stop codon itself)
                for k in range(0, len(upstream_length) - 2, 3): #count codons in the longest ORF
                    codon = upstream_length[k:k+3]
                    total_codons_counted += 1 #increment total codons counted
                    if codon in codon_counts:
                        codon_counts[codon] += 1
                    else:
                        codon_counts[codon] = 1
        header = line #update header to the new one
        sequence = '' #reset sequence for the new gene
    else:
        sequence += line.upper() #append line to current sequence

#After the loop ends, we need to process the last gene if it exists
if header != '':
    total_genes += 1
    gene_name = re.findall(r'gene:(\S+)', header) #extract gene name from header using regex
    if gene_name: #if regex found a match, use it; otherwise fallback to full header
        gene_name = gene_name[0]
    else:
        gene_name = header[1:]
    longest_orf = '' #variable to store the longest ORF found in this gene  
    for i in range(len(sequence) - 2):
        if sequence[i:i+3] == start_codons:
            for j in range(i+3, len(sequence) - 2, 3):
                codon = sequence[j:j+3]
                if codon in stop_codons:
                    if codon == user_stop_codon:
                        current_orf = sequence[i:j+3]
                        if len(current_orf) > len(longest_orf):
                            longest_orf = current_orf
                    break
   # If this gene has a valid ORF ending with the user-selected stop codon
    if longest_orf != '':
        used_genes += 1

        # Remove the final stop codon
        # The practical asks for codons upstream of the specified stop codon
        upstream_sequence = longest_orf[:-3]

        # Count codons in the upstream sequence
        for k in range(0, len(upstream_sequence) - 2, 3):
            codon = upstream_sequence[k:k+3]

            total_codons_counted += 1

            if codon in codon_counts:
                codon_counts[codon] += 1
            else:
                codon_counts[codon] = 1


# Close the input file
infile.close()


# Print summary information to check whether the program worked
print('Selected stop codon:', user_stop_codon)
print('Total genes read:', total_genes)
print('Genes used in analysis:', used_genes)
print('Total upstream codons counted:', total_codons_counted)
print('Codon counts:')

for codon in codon_counts:
    print(codon, codon_counts[codon])


# Write codon counts to a text file
count_file_name = 'codon_counts_' + user_stop_codon + '.txt'
count_file = open(count_file_name, 'w')

count_file.write('Selected stop codon: ' + user_stop_codon + '\n')
count_file.write('Total genes read: ' + str(total_genes) + '\n')
count_file.write('Genes used in analysis: ' + str(used_genes) + '\n')
count_file.write('Total upstream codons counted: ' + str(total_codons_counted) + '\n')
count_file.write('\nCodon counts:\n')

for codon in codon_counts:
    count_file.write(codon + '\t' + str(codon_counts[codon]) + '\n')

count_file.close()


# Make and save a pie chart
if len(codon_counts) > 0:

    # Codon names will be used as labels
    labels = list(codon_counts.keys())

    # Codon counts will be used as pie chart sizes
    sizes = list(codon_counts.values())

    # Create a new figure
    plt.figure(figsize=(10, 10))

    # Draw the pie chart
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')

    # Add a clear title
    plt.title('Codon usage upstream of ' + user_stop_codon)

    # Improve layout
    plt.tight_layout()

    # Save the pie chart to a file
    image_file_name = 'codon_usage_' + user_stop_codon + '.png'
    plt.savefig(image_file_name, dpi=300)

    # Close the figure
    plt.close()

    print('Codon count file saved as:', count_file_name)
    print('Pie chart saved as:', image_file_name)

else:
    print('No valid ORFs found for this stop codon.')
    print('No pie chart was created.')