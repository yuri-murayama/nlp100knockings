import sys

def col(source_lines, colunm_number, filename):
    col_list = []
    for line in source_lines:
        col_list.append(line.split()[colunm_number] + "\n")
    writer = open(filename, "w")
    writer.writelines(col_list)


f = open(sys.argv[1])
lines = f.readlines()

col(lines, 0, "col1.txt")
col(lines, 1, "col2.txt")
