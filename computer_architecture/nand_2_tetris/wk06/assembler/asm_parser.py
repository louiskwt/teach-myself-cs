import re

from asm_symbol_table import SymbolTable

A_COMMAND = 'A_COMMAND'
C_COMMAND = 'C_COMMAND'
L_COMMAND = 'L_COMMAND'

def remove_comments_and_whitespace(code):
    if "//" in code:
        return code.split("//")[0].strip()
    else:      
        return code.strip()

def remove_linebreak(line):
    return re.sub("\n", "", line)

def clean_line(line):
    l = remove_linebreak(line)
    return remove_comments_and_whitespace(l)

def extract_code_from_file(path):
    try:
        with open(path) as file:
            lines = [clean_line(line) for line in file.readlines()]
            code = [line for line in lines if line]
            return code  
    except:
        print('Cannot open file. Check the file path')

def command_type(code):
    if "@" in code:
        return A_COMMAND
    elif "=" in code:
        return C_COMMAND
    else:
        return L_COMMAND

def get_symbol_key(command):
    return command.split("@")[1]

def parse(code_lines):
    commands = []
    symbols = SymbolTable()
    for code in code_lines:
        command = command_type(code)
        if command == A_COMMAND or command == L_COMMAND:
            key = get_symbol_key(code)
            if symbols.contains(key):
                code = symbols.get_address(key)
            commands.append(code)
        else:
            commands.append(code)
    return commands