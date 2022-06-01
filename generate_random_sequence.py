from random import randint

def random_seq(num):
	bases = 'ACGT'
	seq = []
	for i in range(0, num):
		seq.append(bases[randint(0,3)])
	return "".join(seq)


print random_seq(10)
