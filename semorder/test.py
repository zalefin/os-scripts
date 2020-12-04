import lint
import parse
from simulator import Simulator

if __name__ == '__main__':
    with open('./test1.semord', 'r') as f:
        doc_s = f.read()

    tokens = lint.lint_doc(doc_s)
    simulator = Simulator.from_tokens(tokens)
    for c in simulator.constraints:
        c.print_walk()
        print()

    # print(tokens)
    # constraint = parse.parse_constraint(tokens[-1][1])
    # o = constraint({
    #     'X_1': 3,
    #     'Y_1': 2,
    #     'Z_1': 3,
    #     })
    # print(o)
