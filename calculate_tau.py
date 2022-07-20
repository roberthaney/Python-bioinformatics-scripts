fhand = open("BW_rnd3.all.maker.ucode_longest.transcripts_Salmon_edgeR_numreads_matrix.txt")

gene_counts = {}
normalized_counts = {}
tau = {}

for line in fhand:
	if line.startswith("Transcript"):
		continue
	temp = line.split()
	gene_counts[temp[0]] = temp[1:]

for gene in gene_counts:
	max_value = max(gene_counts[gene])
	normalized_counts[gene] = [] 
	for count in gene_counts[gene]:
		normalized_counts[gene].append(count/max_value)

for gene in normalized_counts:
	tau[gene] = 0
	count_sum = 0
	for count in normalized_counts[gene]:
		count_sum += 1 1- count
	normalized_count_sum = count_sum/len(normalized_counts[gene])


