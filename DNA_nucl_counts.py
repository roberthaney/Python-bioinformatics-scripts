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

def nucl_count(DNA):
	"""returns counts of nucleotides in DNA sequence as list"""
	if validate_sequence(DNA):
		return [("A", str(DNA.count("A"))), ("C", str(DNA.count("C"))), ("G", str(DNA.count("G"))), ("T", str(DNA.count("T")))]
	else:
		return False

def main():
	args = retrieve_args()
	counts = nucl_count(args.dna_seq)
	if counts != False:
		for item in counts:
			print(" = ".join(item))
	else:
		print("Sequence does not appear to be DNA")

if __name__=='__main__':
	main()



