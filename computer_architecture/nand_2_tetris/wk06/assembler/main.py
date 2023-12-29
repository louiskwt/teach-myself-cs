import sys

from asm_parser import extract_code_from_file, parse


def main():
    file_path = sys.argv[1]
    code = extract_code_from_file(file_path)
    machine_code = parse(code)
    file_name = file_path.split('.')[0]
    with open(f'{file_name}.hack', 'w') as file:
        for code_line in machine_code:
            file.write(code_line + '\n')

main()
