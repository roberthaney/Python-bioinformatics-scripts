from random import randint


def base_comp(seq, RNAflag=False):
	if RNAflag:
		return (seq.count("A") + seq.count("U"))/float(len(seq))
	else:
		return (seq.count("A") + seq.count("T"))/float(len(seq))

def random_seq(num, RNAflag=False):
	''' Generates a random RNA or DNA sequence (deafult DNA) of a length determined by num parameter'''
	bases = 'ACGU' if RNAflag else 'ACGT' 
	seq = []
	for i in range(0, num):
		seq.append(bases[randint(0,3)])
	return "".join(seq), base_comp("".join(seq), RNAflag)


print random_seq(10)
print random_seq(10, True)
print random_seq(10, False)

#for testing base_comp function
#print base_comp("ATGCATGCATGC")
#print base_comp("ATATATATATATA")
#print base_comp("GCGCGCGCGCGCG")