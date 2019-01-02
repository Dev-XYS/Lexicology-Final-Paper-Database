def lcp(en, fr):
	for i, c in enumerate(zip(en, fr)):
		if c[0] != c[1]:
			return i
	return min(len(en), len(fr))

def lcs(en, fr):
	for i, c in enumerate(zip(en[::-1], fr[::-1])):
		if c[0] != c[1]:
			return i
	return min(len(en), len(fr))

D = { }

with open("Raw-Word-List.txt") as f:
	for line in f:
		en, fr = line.split()
		pl, sl = lcp(en, fr), lcs(en, fr)
		a = en[pl:len(en)-sl]
		b = fr[pl:len(fr)-sl]
		if (a, b) not in D:
			D[(a, b)] = 0
		D[(a, b)] += 1
		print(en + "\t" + fr + "\t" + "'" + fr[pl:len(fr)-sl] + "' -> '" + en[pl:len(en)-sl] + "'")
