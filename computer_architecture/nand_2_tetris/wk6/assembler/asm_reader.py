import re


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

