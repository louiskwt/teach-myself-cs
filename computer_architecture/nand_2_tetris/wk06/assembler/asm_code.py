DEST_TABLE = {
    "null": 0,
    "M": 1,
    "D": 2,
    "MD": 3,
    "A": 4,
    "AM": 5,
    "AD": 6,
    "AMD": 7,
}

JMP_TABLE = {
    "null": 0,
    "JGT": 1,
    "JEQ": 2,
    "JGE": 3,
    "JLT": 4,
    "JNE": 5,
    "JLE": 6,
    "JMP": 7,
}

def get_dest(key):
    return "{0:03b}".format(DEST_TABLE[key])

def get_jmp(key):
    return "{0:03b}".format(JMP_TABLE[key])