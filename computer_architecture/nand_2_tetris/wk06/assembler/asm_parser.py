import os
import re

from asm_code import Code
from asm_symbol_table import SymbolTable

A_COMMAND = 'A_COMMAND'
C_COMMAND = 'C_COMMAND'
L_COMMAND = 'L_COMMAND'



class ASM_Reader:
    def __init__(self, path):
        self.file = open(path)
        self.code = []

    def remove_comments_and_whitespace(self, code):
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
            lines = self.file.readlines()
            lines = [self.clean_line(line) for line in lines]
            code = [line for line in lines if line]
            self.code = code
        except:
            print('Cannot open file. Check the file path')


class ASM_Parser:
    def __init__(self) -> None:
        self.A_COMMAND = A_COMMAND
        self.C_COMMAND = C_COMMAND
        self.L_COMMAND = A_COMMAND
        self.code_lines = []
        self.output = []

    def command_type(self, code):
        if "@" in code:
            return self.A_COMMAND
        elif "=" in code or ";" in code:
            return self.C_COMMAND
        else:
            return self.L_COMMAND

    def get_symbol_key(self, command):
        # print(command)
        return command.split("@")[1]
    
    def load_code_lines(self, code_lines):
        self.code_lines = code_lines

    def parse(self):
        commands = []
        symbols = SymbolTable()
        code_generator = Code()
        for code in self.code_lines:
            command = self.command_type(code)
            if command == A_COMMAND or command == L_COMMAND:
                key = self.get_symbol_key(code)
                if symbols.contains(key):
                    code = symbols.get_address(key)
                else:
                    if key.isnumeric():
                        code = symbols.add_numeric_entry(key)
                    else:
                        symbols.add_entry(key)
                        code = symbols.get_address(key)
                commands.append(code)
            else:
                op_code = "{0:03b}".format(7)
                a_code = "0"
                if "=" in code:
                    code_parts = code.split("=")
                    dest, right_hand_side = code_generator.get_dest(code_parts[0]), code_parts[1]
                    jmp = code.get_jmp('null')
                    if ";" in right_hand_side:
                        splited_rhs = right_hand_side.split(';')
                        comp, jmp = code_generator.get_comp(splited_rhs[0]), code_generator.get_jmp(splited_rhs[1])
                        if code_generator.is_a_code(splited_rhs[0]):
                            a_code = "1"
                    
                    comp = code_generator.get_comp(right_hand_side)
                    if code_generator.is_a_code(right_hand_side):
                        a_code = "1"

                if ";" in code:
                    code_parts = code.split(';')
                    comp, jmp = code_generator.get_comp(code_parts[0]), code_generator.get_jmp(code_parts[1])
                    dest = code_generator.get_dest('null')
                    if code_generator.is_a_code(comp):
                        a_code = "1"

                out = op_code + a_code + comp + dest + jmp
                print(f'a_code: {a_code}, comp: {comp}')
                self.output.append(out)

        return self.output