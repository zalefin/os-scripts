ALL_OPS = ['<', '>', '&', '|', '!',]
CODES = ['process', 'sem', 'terminal', 'constraint']

def _check_line(i, line):
    code = line[0]
    if i in range(3):
        assert code == CODES[i]
    else:
        assert code == CODES[3]


def _lint_instr(i, instr):
    if i == 0:
        return instr.split(',')
    elif i == 1:
        return [v.split('=') for v in instr.split(',')]
    elif i == 2:
        return instr
    else:
        return _lint_contstraint(instr, 0)


def _lint_contstraint(instr, start):
    out = []
    s = ''
    n = start
    for i in range(start, len(instr)):
        if i == n:
            n += 1
        else:
            continue

        c = instr[i]
        if c == '(':
            ret, n = _lint_contstraint(instr, i+1)
            out.append(ret)

        elif c == ')':
            if s != '':
                out.append(s)
            return out, i+1
        else:
            if c in ALL_OPS:
                if s != '':
                    out.append(s)
                out.append(c)
                s = ''
            else:
                s += c

    if start == 0:
        return out
    else:
        return out, n


def lint_doc(doc_s):
    lines = doc_s.split('\n')
    lines = [v.split(' ') for v in lines]
    assert lines.pop() == ['']
    assert lines.pop() == ['']
    tokens = []
    for i, line in enumerate(lines):
        _check_line(i, line)
        t = [line[0], _lint_instr(i, line[1])]
        tokens.append(t)

    return tokens

