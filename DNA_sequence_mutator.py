from random import randint

def validate_sequence(sequence):
	"""Check that sequence is DNA before mutating"""
	seq = sequence.upper()
	return len(seq) == (seq.count("A") + seq.count("C") + seq.count("G") + seq.count("T"))

def replace_random_base(DNA_seq):
	"""Return a DNA sequence with a randomly selected position replaced by a randomly chosen base"""
	if validate_sequence(DNA_seq):
		position = randint(0, len(DNA_seq) - 1)
		# replace base in position with empty string to make sure same base not chosen
		bases = 'TCAG'.replace(DNA_seq[position], '')
		# show mutated base in lowercase
		return DNA_seq[0:position] + bases[randint(0,2)].lower() + DNA_seq[position + 1:]
	else:
		print "Sequence does not appear to be DNA"
# test
print replace_random_base('ATCGGCGATGCAGTACGATACTA')
print replace_random_base('ATCGGCTACCCGGGTTAATGACA')
print replace_random_base('ATCGGCTACCCGGXTTAATGACA')

