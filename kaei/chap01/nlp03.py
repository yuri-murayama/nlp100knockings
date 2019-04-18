str = "Now I need a drink, alcoholic of course, after the heavy lectures incolcing quantum mechanics."

str = str.split()
count = []

for i in str:
    i = i.strip(',.')
    count.append(len(i))

print(count)
