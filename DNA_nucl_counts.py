import argparse
from typing import NamedTuple

class Args(NamedTuple):
	"""structure to store command line arguments"""
	dna_seq: str

def retrieve_args() -> Args:
	"""retrieve and parse command line arguments"""
	arg_parser = argparse.ArgumentParser()
	arg_parser.add_argument('dna_seq', metavar='DNA', help='Input DNA sequence')
	args = arg_parser.parse_args()
	return Args(args.dna_seq)

def validate_sequence(sequence):
	"""Check that sequence is DNA before mutating"""
	seq = sequence.upper()
	return len(seq) == (seq.count("A") + seq.count("C") + seq.count("G") + seq.count("T"))

def nucl_count(dna):
	"""returns counts of nucleotides in DNA sequence as list"""
	if validate_sequence(dna):
		return [("A", str(dna.upper().count("A"))), ("C", str(dna.upper().count("C"))), ("G", str(dna.upper().count("G"))), ("T", str(dna.upper().count("T")))]
	else:
		return False

def test_counts():
	assert nucl_count('') == [("A", 0), ("C", 0), ("G", 0), ("T", 0)]

def main():
	args = retrieve_args()
	counts = nucl_count(args.dna_seq)
	if counts != False:
		for item in counts:
			print(" = ".join(item))
	else:
		print("Sequence does not appear to be DNA")
	print("Total length of sequence:", len(args.dna_seq))

if __name__=='__main__':
	main()
	test_counts()


