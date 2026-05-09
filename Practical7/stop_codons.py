import re

infile = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
outfile = open('stop_genes.fa', 'w')

header = ''
sequence = ''

for line in infile:
    line = line.rstrip()

    if line.startswith('>'):
        if header != '':
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
                out_header = '>' + gene_name + ' ' + ' '.join(found_stops)
                outfile.write(out_header + '\n')
                outfile.write(sequence + '\n')

        header = line
        sequence = ''

    else:
        sequence = sequence + line

if header != '':
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
        out_header = '>' + gene_name + ' ' + ' '.join(found_stops)
        outfile.write(out_header + '\n')
        outfile.write(sequence + '\n')

infile.close()
outfile.close()