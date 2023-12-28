import re


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

def read_and_process_file(path):
    try:
        with open(path) as file:
            lines = [clean_line(line) for line in file.readlines()]
            code = [line for line in lines if line]
            print(code)    
    except:
        print('Cannot open file. Check the file path')
