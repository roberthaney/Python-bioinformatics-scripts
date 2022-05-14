from random import randint

def replace_random_base(DNA_seq):
	"""Return a DNA sequence with a randomly selected position replaced by a randomly chosen base"""
	position = randint(0, len(DNA_seq) - 1)
	# replace base in position with empty string to make sure same base not chosen
	bases = 'TCAG'.replace(DNA_seq[position], '')
	# show mutated base in lowercase
	return DNA_seq[0:position] + bases[randint(0,2)].lower() + DNA_seq[position + 1:]

# test
print replace_random_base('ATCGGCGATGCAGTACGATACTA')
print replace_random_base('ATCGGCTACCCGGGTTAATGACA')

