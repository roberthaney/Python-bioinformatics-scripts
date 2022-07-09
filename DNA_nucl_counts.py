
def nucl_count(DNA):
	return [DNA.count("A"), DNA.count("C"), DNA.count("G"), DNA.count("T")]


print(nucl_count("ATCGATCGATCG"))