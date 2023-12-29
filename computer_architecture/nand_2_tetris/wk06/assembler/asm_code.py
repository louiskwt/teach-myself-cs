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

COMP_TABLE = {
    '0': 42,
    '1': 63,
    '-1': 58,
    'D': 12,
    'A': 48,
    'M': 48,
    '!D': 13,
    '!A': 49,
    '!M': 49,
    '-D': 15,
    '-A': 51,
    '-M': 51,
    'D+1': 31,
    'A+1': 55,
    'M+1': 55,
    'D-1': 14,
    'A-1': 50,
    'M-1': 50,
    'D+A': 2,
    'D+M': 2,
    'D-A': 19,
    'D-M': 19,
    'A-D': 7,
    'M-D': 7,
    'D&A': 0,
    'D&M': 0,
    'D|A': 21,
    'D|M': 21,
}

def get_dest(key):
    return "{0:03b}".format(DEST_TABLE[key])

def get_jmp(key):
    return "{0:03b}".format(JMP_TABLE[key])

def get_comp(key):
    return "{0:06b}".format(COMP_TABLE[key])