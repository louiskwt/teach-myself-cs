import sys

from asm_parser import ASM_Parser, ASM_Reader


def main():
    file_path = sys.argv[1]
    reader = ASM_Reader(file_path)
    reader.extract_code_from_file()
    code = reader.code

    parser = ASM_Parser()
    parser.load_code_lines(code)
    parser.first_parse()
    machine_code = parser.second_parse()
    
    file_name = file_path.split('.')[0]
    with open(f'{file_name}.hack', 'w') as file:
        for code_line in machine_code:
            file.write(code_line + '\n')

main()