import re
import os

def identify(text):
    global indent

    if_re = re.compile(r'^IF\s(.+)\sTHEN$')
    endif_re = re.compile(r'^ENDIF$')
    else_re = re.compile(r'^ELSE$')
    elif_re = re.compile(r'^ELSE\sIF\s(.+)\sTHEN$')
    
    output_re = re.compile(r'^OUTPUT\s(.+)')
    input_re = re.compile(r'^INPUT\s(.+)')
    
    while_re = re.compile(r'^WHILE\s(.+)\sDO$')
    endwhile_re = re.compile(r'^ENDWHILE$')

    for_re = re.compile(r'^FOR\s(.+)\s<-\s(.+)\sTO\s(.+)')
    next_re = re.compile(r'^NEXT$')

    repeat_re = re.compile(r'^REPEAT$')
    until_re = re.compile(r'^UNTIL\s(.+)')

    if re.search(if_re, text):
        statement = re.search(if_re, text).group(1)
        statement = indent * "  " + "if(" + statement + "):"
        indent += 1
        return statement

    elif re.search(endif_re, text):
        indent -= 1
        return None

    elif re.search(else_re, text):
        statement = re.search(else_re, text).group()
        statement = (indent - 1) * "  " + "else:"
        return statement

    elif re.search(output_re, text):
        statement = re.search(output_re, text).group(1)
        statement = indent * "  " + "print(" + statement + ")"
        return statement

    elif re.search(while_re, text):
        statement = re.search(while_re, text).group(1)
        statement = indent * "  " + "while(" + statement + "):"
        indent += 1
        return statement

    elif re.search(endwhile_re, text):
        indent -= 1
        return None

    elif re.search(input_re, text):
        statement = re.search(input_re, text).group(1)
        statement = indent * "  " + statement + " = check(input())"
        return statement

    elif re.search(next_re, text):
        indent -= 1
        return None

    elif re.search(for_re, text):
        var = re.search(for_re, text).group(1)
        low = re.search(for_re, text).group(2)
        high = re.search(for_re, text).group(3)
        statement = indent * "  " + "for " + var + " in range(" + low + "," + high + "):"
        indent += 1
        return statement

    elif re.search(elif_re, text):
        statement = re.search(elif_re, text).group(1)
        statement = (indent - 1) * "  " + "elif (" + statement + "):"
        return statement

    elif re.search(repeat_re, text):
        statement = re.search(repeat_re, text).group()
        statement = indent * "  " + "while True:"
        indent += 1
        return statement

    elif re.search(until_re, text):
        statement = re.search(until_re, text).group(1)
        statement = indent * "  " + "if (" + statement + "):\n" + (indent + 1) * "  " + "break"
        indent -= 1
        return statement

    else:
        statement = (indent * "  " + text)
        return statement

def read(count):
    compiler = os.path.realpath(__file__)
    
    self_path = re.compile(r'(.+)Compiler.py')
    path = re.search(self_path, compiler).group(1) + "enter.txt"

    with open(path, "r") as file1:
        v = file1.readlines()

    if count < len(v):
        read_filter = re.compile(r'^\s*(.*)$')
        if re.search(read_filter, v[count]):
            x = re.search(read_filter, v[count]).group(1)
            return x
        else:
            return None
    else:
        return "STOP"

def write(lines):
    with open("compiled.py", "a") as file:
        for line in lines:
            file.write(line + " \n")

def main():
    global indent, lines, check

    with open("compiled.py", "w") as file:
        file.write("\n")

    indent = 0
    lines = []
    filtered = ""
    count = 0

    check = """
def check(s):
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            if s == "True":
                return True
            elif s == "False":
                return False
            else:
                return s
"""
    lines.append(check)

    while filtered != "STOP":
        text = read(count)
        filtered = identify(text)

        if filtered != "STOP" and filtered is not None: 
            lines.append(filtered)

        count += 1

    lines.append("r = input() #line that halts execution so program won't close")

    write(lines)

    # Print the generated Python code (excluding the check function)
    for line in lines[1:]:
        print(line)

if __name__ == "__main__":
    main()
