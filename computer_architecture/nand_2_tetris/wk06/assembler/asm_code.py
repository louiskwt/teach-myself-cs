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

A_LIST = ['M', '!M', '-M', 'M+1', 'M-1', 'D+M', 'D-M', 'M-D', 'D&M', 'D|M']

class Code:
    def __init__(self):
        self.DEST_TABLE = DEST_TABLE
        self.JUMP_TABLE = JMP_TABLE
        self.A_LIST = A_LIST
        self.COMP_TABLE = COMP_TABLE

    def get_dest(self, key):
        return "{0:03b}".format(self.DEST_TABLE[key])

    def get_jmp(self, key):
        return "{0:03b}".format(self.JUMP_TABLE[key])

    def get_comp(self, key):
        return "{0:06b}".format(self.COMP_TABLE[key])

    def is_a_code(self, comp):
        return comp in self.A_LIST 


    