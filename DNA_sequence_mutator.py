from random import randint

def validate_sequence(sequence):
	"""Check that sequence is DNA before mutating"""
	seq = sequence.upper()
	return len(seq) == (seq.count("A") + seq.count("C") + seq.count("G") + seq.count("T"))

def replace_random_bases(DNA_seq, num):
	"""Return a DNA sequence with a randomly selected position replaced by a randomly chosen base"""
	DNA = DNA_seq
	DNA_history = []
	if validate_sequence(DNA):
		for i in range(num):
			# choose position
			position = randint(0, len(DNA) - 1)
			# replace base in position with empty string to make sure same base not chosen
			bases = 'TCAG'.replace(DNA[position], '')
			# show mutated base in lowercase
			DNA = DNA[0:position] + bases[randint(0,2)].lower() + DNA[position + 1:]
			DNA_history.append(DNA)
		return DNA
	else:
		return "Sequence does not appear to be DNA"

# test
print(replace_random_bases('ATCGGCGATGCAGTACGATACTA', 10))
print(replace_random_bases('ATCGGCTACCCGGGTTAATGACA', 1))
print(replace_random_bases('ATCGGCTACCCGGXTTAATGACA', 1))

