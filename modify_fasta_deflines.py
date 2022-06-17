import re

fhand_in = open("trinity2.6.6_str_Cdar_MaFl_paired.longest_transcripts.cdhit98.fa")
fhand_out = open("trinity2.6.6_str_Cdar_MaFl_paired.longest_transcripts.cdhit98.spname.fa", "w")

counter = 0
for line in fhand_in:
	if line.startswith(">"):
		name = re.findall(">(\S+)", line)[0]
		name = name + "_Cdar"
		fhand_out.write(">" + name + "\n")
		counter += 1
	else:
		fhand_out.write(line)

print "Processed", counter, "deflines"
