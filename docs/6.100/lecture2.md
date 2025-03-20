# Lecture 2

## Reading notes

Method or operator overloaded: it has different meanings depending upon the type of objects to which it is applied

- when * is applied to an int and a str, it becomes a repetition operator
- n*s = repeat str s n times

String in python is a non-secular object

- can be accessed using index
- slicing s[start: end]
    1. by default the start is set to 0; and the end is set to len(s)

- input will give you back a str

python map

- map(f1, list) apply f1 to every item in the list

---

## Lecture notes

### Recap

Objects have type and the types tell what operations you can do with the objects

### strings

Think of it as a sequence

negative indexing

- -1 will give you the last character of the str

slice to get substring

- s[start:end:step] step by default is 1
- for the ending, we go up to but not including the end index

Examples

s = "abcdefgh"

s[3:6] -> "def"
s[3:6:2] -> "df"
s[:] -> "abcedfgh" (make a copy)
s[::-1] -> "hgfdecba" (reverse the string)
s[4:1:-2] -> "ec"

Immutable string

strings are immutable

you can create new objects that are versions of the original one

### input

comma (,) in print automatically insert a space

### f-string

become available in python 3.6

var = "I'm"
f"{var} here"

place variables and expressions inside f string and no need to think about concatination

### condition and branching

two notions of equal

1. assignment (=) -> variable = 23

2. == -> test for equality
    - some expression == expression (evaluate to True or False)
    - similar for other comparisons 2 < 3 (gets evaluated to True)



