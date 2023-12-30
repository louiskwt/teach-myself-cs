PREDEFINED_SYMBOLS = {
            "SP": 0,
            "LCL": 1,
            "ARG": 2,
            "THIS": 3,
            "THAT": 4,
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "11": 11,
            "12": 12,
            "13": 13,
            "14": 14,
            "15": 15,
            "R0": 0,
            "R1": 1,
            "R2": 2,
            "R3": 3,
            "R4": 4,
            "R5": 5,
            "R6": 6,
            "R7": 7,
            "R8": 8,
            "R9": 9,
            "R10": 10,
            "R11": 11,
            "R12": 12,
            "R13": 13,
            "R14": 14,
            "R15": 15,
            "SCREEN": 16384,
            "KBD": 24576
}

class SymbolTable:
    def __init__(self):
        self.symbol_table = PREDEFINED_SYMBOLS 
        self.next_addr = 16
    
    def get_address(self, key):
        return "{0:016b}".format(self.symbol_table[key])

    def contains(self, key):
        return key in self.symbol_table
    
    def add_entry(self, key):
        self.symbol_table[key] = self.next_addr
        next = self.next_addr + 1
        if self.contains(next):
            n = next + 1
            while self.contains(n):
                n += 1
            self.next_addr = n
        else:
            self.next_addr += 1
    
    def add_numeric_entry(self, key):
        self.symbol_table[key] = key

