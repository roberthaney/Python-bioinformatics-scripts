import re

fhand_gff = open("GCA_019974015.1_Npil_1.0_genomic.gff")
fhand_out  = open("GCA_019974015.1_Npil_1.0_protein_gene_map.txt", "w")

genes = {}
found_prots = []

for line in fhand_gff:
	if line.startswith("#"):
		continue
	temp = line.split()
	if temp[2] == "CDS":
		cdsprot = re.findall("ID=cds-(\S+);Parent", line)[0]
		if cdsprot not in found_prots:
			found_prots.append(cdsprot)
			#gene = re.findall("gene=(LOC\d+)", line)[0]
			gene = re.findall("locus_tag=(\S+);product", line)[0]
			if gene in genes:
				genes[gene].append(cdsprot)
			else:
				genes[gene] = []
				genes[gene].append(cdsprot)
			#genes[cdsprot] = gene

print "Number of genes:", len(genes)
prot_counter = 0
for gene in genes:
	prot_counter += len(genes[gene])

print "Proteins mapped to genes:", prot_counter

#for protein in genes:
#	fhand_out.write(protein + "\t" + genes[protein] + "\n")


