import parse
import lint


class Simulator(object):
    def __init__(self, prog_names, sems, terminal, constraints):
        self.prog_names = prog_names
        self.sems = sems
        self.terminal = terminal
        self.constraints = constraints

    @staticmethod
    def from_tokens(tokens):
        prog_names = None
        sems = None
        terminal = None
        constraints = []
        for code, t in tokens:
            if code == lint.CODES[0]:
                prog_names = t
            elif code == lint.CODES[1]:
                sems = parse.parse_sems(t)
            elif code == lint.CODES[2]:
                terminal = parse.parse_terminal(t)
            elif code == lint.CODES[3]:
                constraints.append(parse.parse_constraint(t))

        return Simulator(prog_names, sems, terminal, constraints)


class Env(object):
    def __init__(self, prog_names, sems, terminal, constraints):
        self.t = 0
        self.step = 0
