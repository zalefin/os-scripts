import lint


class Expr(object):
    def __init__(self, *args):
        self.vals = [v for v in args]
        self._valchild = None
        self._op_f = {
                '<': lambda a,b: a < b,
                '>': lambda a,b: a > b,
                '≤': lambda a,b: a <= b,
                '≥': lambda a,b: a >= b,
                '&': lambda a,b: a and b,
                '|': lambda a,b: a or b,
                '!': lambda a: not a,
                # 'NOOP': lambda a: a,
                }

    def __call__(self, values: dict):
        if not self._valchild:
            self._valchild = self.get_vals()
        for k, v in values.items():
            for child in self._valchild:
                if child.name == k:
                    child.set(v)
        return self.eval()

    def get_vals(self):
        out = []
        for v in self.vals:
            if isinstance(v, Val):
                out.append(v)
            else:
                out += v.get_vals()
        return out

    def get_val_names(self):
        return list(set(map(lambda v: v.name, self.get_vals())))

    def eval(self):
        l = len(self.vals)
        if l == 1:
            return self.vals[0].eval()
        elif l == 2:
            v1, op = self.vals
            return self._op_f[op.eval()](v1.eval())
        elif l == 3:
            v1, op, v2 = self.vals
            return self._op_f[op.eval()](v1.eval(), v2.eval())

    def print_walk(self, indent=0):
        print(''.join(['\t']*indent) + str(self))
        for v in self.vals:
            if isinstance(v, Expr): v.print_walk(indent=indent+1)



class Val(Expr):
    def __init__(self, *args):
        super().__init__(*args)
        self.name = self.vals[0]

    def eval(self):
        return self.vals[0]

    def set(self, val):
        self.vals[0] = val

    def print_walk(self, indent=0):
        print(''.join(['\t']*indent) + str(self.name))


def parse_constraint(c_tokens):
    if isinstance(c_tokens, list):
        vals = []
        l = len(c_tokens)
        for i in range(3 if l > 3 else l):
            vals.append(parse_constraint(c_tokens[i]))
        return Expr(*vals)
    else:
        return Val(c_tokens)


def parse_sems(sem_tokens):
    return {k: int(v) for k,v in sem_tokens}


def parse_terminal(t_tokens):
    return int(t_tokens)

