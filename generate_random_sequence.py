from random import randint

def random_seq(num, RNAflag=False):
	''' Generates a random RNA or DNA sequence (deafult DNA) of a length determined by num parameter'''
	bases = 'ACGU' if RNAflag else 'ACGT' 
	seq = []
	for i in range(0, num):
		seq.append(bases[randint(0,3)])
	return "".join(seq)


print random_seq(10)
print random_seq(10, True)
print random_seq(10, False)
