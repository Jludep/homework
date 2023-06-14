def backspace_compare(first: str, second: str):

    def backspace(line: str):
        if '#' in line:
            if line.startswith('#'):
                line_changed = line.replace('#', '', 1)
                backspace(line_changed)

            line_list = list(line)
            for key, value in enumerate(line_list):
                if value == '#':
                    line_list[key-1] = ''
                    line_list[key] = ''
            line_list.remove('')
            return ''.join(line_list)
        else:
            return line

    return backspace(first) == backspace(second)
