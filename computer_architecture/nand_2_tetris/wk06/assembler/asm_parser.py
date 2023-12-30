import re

from asm_code import Code
from asm_symbol_table import SymbolTable

A_COMMAND = 'A_COMMAND'
C_COMMAND = 'C_COMMAND'
L_COMMAND = 'L_COMMAND'



class ASM_Reader:
    def __init__(self, path):
        self.path = path

    def remove_comments_and_whitespace(code):
        if "//" in code:
            return code.split("//")[0].strip()
        else:      
            return code.strip()

    def remove_linebreak(self, line):
        return re.sub("\n", "", line)

    def clean_line(self, line):
        l = self.remove_linebreak(line)
        return self.remove_comments_and_whitespace(l)

    def extract_code_from_file(self):
        try:
            with open(self.path) as file:
                lines = [self.clean_line(line) for line in file.readlines()]
                code = [line for line in lines if line]
                return code  
        except:
            print('Cannot open file. Check the file path')


class ASM_Parser:
    def __init__(self) -> None:
        self.A_COMMAND = A_COMMAND
        self.C_COMMAND = C_COMMAND
        self.L_COMMAND = A_COMMAND
        self.code_lines = []
        self.output = []

    def command_type(code):
        if "@" in code:
            return A_COMMAND
        elif "=" in code or ";" in code:
            return C_COMMAND
        else:
            return L_COMMAND

    def get_symbol_key(command):
        # print(command)
        return command.split("@")[1]
    
    def load_code_lines(self, code_lines):
        self.code_lines = code_lines





def parse(code_lines):
    commands = []
    symbols = SymbolTable()
    for code in code_lines:
        command = command_type(code)
        if command == A_COMMAND or command == L_COMMAND:
            key = get_symbol_key(code)
            if symbols.contains(key):
                code = symbols.get_address(key)
            else:
                symbols.add_entry(key)
                code = symbols.get_address(key)
            commands.append(code)
        else:
            op_code = "{0:03b}".format(7)
            a_code = "0"
            if "=" in code:
                code_parts = code.split("=")
                dest, right_hand_side = get_dest(code_parts[0]), code_parts[1]
                jmp = get_jmp('null')
                if ";" in right_hand_side:
                    splited_rhs = right_hand_side.split(';')
                    comp, jmp = get_comp(splited_rhs[0]), get_jmp(splited_rhs[1])
                    if is_a_code(splited_rhs[0]):
                        a_code = "1"
                
                comp = get_comp(right_hand_side)
                if is_a_code(right_hand_side):
                    a_code = "1"

            if ";" in code:
                code_parts = code.split(';')
                comp, jmp = get_comp(code_parts[0]), get_jmp(code_parts[1])
                dest = get_dest('null')
                if is_a_code(comp):
                    a_code = "1"

            out = op_code + a_code + comp + dest + jmp
            print(f'a_code: {a_code}, comp: {comp}')
            commands.append(out)
    return commands