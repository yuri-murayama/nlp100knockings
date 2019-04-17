s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

s = s.strip(',.').split()
pi = [len(w) for w in s]

print(pi)