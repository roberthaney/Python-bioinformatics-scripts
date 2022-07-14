import argparse

def retrieve_args():
	"""retrieve and parse command line arguments"""
	arg_parser = argparse.ArgumentParser()
	arg_parser.add_argument('dna_seq', metavar='DNA', help='Input DNA sequence')
	return arg_parser.parse_args()

def nucl_count(DNA):
	"""returns counts of nucleotides in DNA sequence as list"""
	return [DNA.count("A"), DNA.count("C"), DNA.count("G"), DNA.count("T")]

def main():
	args = retrieve_args()
	print(nucl_count(args.dna_seq))

if __name__=='__main__':
	main()



