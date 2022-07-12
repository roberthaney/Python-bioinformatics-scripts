
def nucl_count(DNA):
	"""returns counts of nucleotides in DNA sequence as list"""
	return [DNA.count("A"), DNA.count("C"), DNA.count("G"), DNA.count("T")]

def main():
	print(nucl_count("ATCGATCGATCG"))

if __name__=='__main__':
	main()



