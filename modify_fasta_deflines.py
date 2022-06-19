import re

def remove_extra_info(file, output):
	'''Keeps only first entry on fasta defline up until first whitespace as sequence ID'''
	with open (file) as fhand, open (output, "w") as fhand_out:
		counter = 0
		for line in fhand:
			if line.startswith(">"):
				name = re.findall(">(\S+)", line)[0]
				fhand_out.write(">" + name + "\n")
				counter += 1
			else:
				fhand_out.write(line)
		return counter

def add_suffix_to_name(file):
	pass
	#for line in file:
	#	if line.startswith(">"):
	#		name = re.findall(">(\S+)", line)[0]
	#		name = name + "_Cdar"
	#		fhand_out.write(">" + name + "\n")
	#		counter += 1
	#	else:
	#		fhand_out.write(line)


print "Processed", remove_extra_info("spider_12sp_Hsp90_COBALT.fa", "spider_12sp_Hsp90_COBALT_processed.fa"), "deflines"
