fhand_out = open("A28_1_2_test.fastq", "w")

numlines = 200000

with open ("A28_1_2.fq") as file:
	for i in range(numlines):
		fhand_out.write(file.next())
