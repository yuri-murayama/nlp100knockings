f1 = open("col1.txt")
f2 = open("col2.txt")

lines1 = f1.readlines()
lines2 = f2.readlines()

text = open("merge.txt", "w")
for col1, col2 in zip(lines1, lines2):
    text.write("\t".join([col1.rstrip(), col2]))
