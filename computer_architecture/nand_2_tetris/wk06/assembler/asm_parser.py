from asm_code import Code
from asm_symbol_table import SymbolTable


class ASM_Parser:
    def __init__(self) -> None:
        self.command = None
        self.symbols = SymbolTable()
        self.code_lines = []
        self.output = []

    def is_a_command(self, code):
        return "@" in code
    
    def is_l_command(self, code):
        return "(" in code and ")" in code

    def get_symbol_key(self, command):
        return command.split("@")[1]

    def get_label_key(self, code):
        return code[code.find("(")+1:code.find(")")].strip()
    
    def load_code_lines(self, code_lines):
        self.code_lines = code_lines
    
    def first_parse(self):
        '''
            focus on building the symbol in the first pass
            only work on A command or adding reference
            no code is generated in this pass
        '''
        for code in self.code_lines:
            self.command_type(code)
            if self.is_l_command(code):
                label = self.get_label_key(code)
                self.symbols.add_label_entry(label, self.symbols.line_num)
            else:
                self.symbols.march()

    def second_parse(self):
        code_generator = Code()
        for code in self.code_lines:
            if "(" in code and ")" in code:
                continue
            if self.is_a_command(code):
                key = self.get_symbol_key(code)
                if not self.symbols.contains(key):
                    if key.isnumeric():
                        self.symbols.add_numeric_entry(key, int(key))
                        code = self.symbols.get_address(key)
                    else: 
                        print(f'val: {self.symbols.next_addr}')
                        self.symbols.add_entry(key, self.symbols.next_addr)
                        code = self.symbols.get_address(key)
                else:
                    code = self.symbols.get_address(key)
                
                self.output.append(code)
            else:
                op_code = "{0:03b}".format(7)
                a_code = "0"
                dest = code_generator.get_dest('null')
                comp = code_generator.get_comp('0')
                jmp = code_generator.get_jmp('null')
                if "=" in code:
                    code_parts = code.split("=")
                    dest, right_hand_side = code_generator.get_dest(code_parts[0]), code_parts[1]
                    jmp = code_generator.get_jmp('null')
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
                self.output.append(out)

        return self.output