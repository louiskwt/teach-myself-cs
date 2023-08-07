from urllib.request import urlopen # a function to open url

shakespeare = urlopen('http://composingprograms.com/shakespeare.txt') # URL Error
shakespeare = urlopen('http://composingprograms.com/shakespeare.txt')

words = set(shakespeare.read().decode().split())

print(words)
