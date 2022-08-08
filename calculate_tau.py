import numpy as np

fhand = open("BW_rnd3.all.maker.ucode_longest.transcripts_Salmon_numreads_matrix.txt")
fhand_out = open("BW_rnd3.all.maker.ucode_longest.transcripts_Salmon_numreads_tau.txt", "w")

gene_averaged_counts = {}
normalized_counts = {}
tau = {}

for line in fhand:
	if line.startswith("Transcript"):
		continue
	temp = line.split()
	gene_averaged_counts[temp[0]] = {}
	gene_averaged_counts[temp[0]]["Agg"] = np.mean([float(x) for x in temp[1:3]])
	gene_averaged_counts[temp[0]]["Ceph"] = np.mean([float(x) for x in temp[3:5]])
	gene_averaged_counts[temp[0]]["Flag"] = np.mean([float(x) for x in temp[5:7]])
	gene_averaged_counts[temp[0]]["Major"] = np.mean([float(x) for x in temp[7:9]])
	gene_averaged_counts[temp[0]]["Minor"] = np.mean([float(x) for x in temp[9:11]])
	gene_averaged_counts[temp[0]]["Ovary"] = np.mean([float(x) for x in temp[11:13]])
	gene_averaged_counts[temp[0]]["Tub"] = np.mean([float(x) for x in temp[13:15]])
	gene_averaged_counts[temp[0]]["Venom"] = np.mean([float(x) for x in temp[15:18]])
	gene_averaged_counts[temp[0]]["Pyr"] = np.mean([float(x) for x in temp[18:19]])
	gene_averaged_counts[temp[0]]["Aci"] = np.mean([float(x) for x in temp[19:20]])

print(gene_averaged_counts["Lhe_031888-RA"]["Agg"])
print(gene_averaged_counts["Lhe_031888-RA"]["Ceph"])
print(gene_averaged_counts["Lhe_031888-RA"]["Flag"])
print(gene_averaged_counts["Lhe_031888-RA"]["Major"])
print(gene_averaged_counts["Lhe_031888-RA"]["Minor"])
print(gene_averaged_counts["Lhe_031888-RA"]["Ovary"])
print(gene_averaged_counts["Lhe_031888-RA"]["Tub"])
print(gene_averaged_counts["Lhe_031888-RA"]["Venom"])
print(gene_averaged_counts["Lhe_031888-RA"]["Pyr"])
print(gene_averaged_counts["Lhe_031888-RA"]["Aci"])


for gene in gene_averaged_counts:
	exp_matrix = []
	for tissue in gene_averaged_counts[gene]:
		exp_matrix.append(gene_averaged_counts[gene][tissue]) 
	max_value = max(exp_matrix)
	# conditional to avoid division by zero
	if max_value != 0:
		normalized_counts[gene] = [] 
		for count in exp_matrix:
			normalized_counts[gene].append(count/max_value)

print(normalized_counts["Lhe_031888-RA"])

tau_check = []
for gene in normalized_counts:
	#tau[gene] = 0
	count_sum = 0
	for count in normalized_counts[gene]:
		count_sum += 1- count
	# ignore undefined values
	if not np.isnan(count_sum/(len(normalized_counts[gene]) - 1)):
		tau[gene] = count_sum/(len(normalized_counts[gene]) - 1)
		tau_check.append(tau[gene])
		#print(gene, tau[gene])

print("maximum tau value:", max(tau_check))
print("minimum tau value:", min(tau_check))

# print output file
for gene in tau:
	fhand_out.write(gene + "\t" + str(tau[gene]) + "\n")
