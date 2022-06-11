sequences = {}

def read_fasta_strings(filename):
	with open(filename) as fhand:
		return fhand.read().split('>')[1:]

def read_fasta_entries(filename):
	return [seq.partition('\n') for seq in read_fasta_strings(filename)]	

def read_fasta_sequences(filename):
	return [[seq[0], seq[2].replace('\n', '')] for seq in read_fasta_entries(filename)]

sequence_list = read_fasta_sequences('spider_12sp_Hsp75.fa')

for seq in sequence_list:
	sequences[seq[0]] = seq[1]

# test
#for seq in sequences:
#	print seq 
#	print sequences[seq]