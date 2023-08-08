from urllib.request import urlopen # a function to open url

# shakespeare = urlopen('http://composingprograms.com/shakespeare.txt') # URL Error
shakespeare = urlopen('https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt')

words = set(shakespeare.read().decode().split())

print(len(words))

# a compound expression that evaluates to the set of all Shakespearian words that are simultaneously a word spelled in reverse
results = { w for w in words if len(w) == 6 and w[::-1] in words and "*" not in w }

print(results)
