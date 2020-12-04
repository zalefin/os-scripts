from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from lang.SemOrdLexer import SemOrdLexer
from lang.SemOrdParser import SemOrdParser
from lang.SemOrdListener import SemOrdListener

import parse

class SOCollector(SemOrdListener):
    def __init__(self):
        self.proc_names = []
        self.semaphores = {}
        self.terminal = -1
        self.contstraints = []
        self.exprs = {}

    def enterProcess(self, ctx):
        for v in ctx.ID():
            self.proc_names.append(v.getText())

    def enterSem(self, ctx):
        for d in ctx.defin():
            self.semaphores[d.ID().getText()] = int(d.INT().getText())

    def enterTerminal(self, ctx):
        self.terminal = int(ctx.INT().getText())

    def exitExpr(self, ctx):
        nid = ctx.ID()
        bop = ctx.boolop()
        cop = ctx.cmp()
        if nid:
            self.exprs[ctx] = parse.Val(nid.getText())
        elif bop or cop:
            op = bop if bop else cop
            e1, e2 = ctx.expr()
            self.exprs[ctx] = parse.Expr(
                    self.exprs[e1],
                    parse.Val(op.getText()),
                    self.exprs[e2],
                    )
        else:
            # parenthesis case
            # dig 1 deeper
            self.exprs[ctx] = self.exprs[ctx.expr()[0]]

        if isinstance(ctx.parentCtx, SemOrdParser.ConstraintContext):
            self.contstraints.append(self.exprs[ctx])


if __name__ == '__main__':
    input_stream = FileStream('./test1.semord')
    lexer = SemOrdLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SemOrdParser(stream)
    tree = parser.init()
    walker = ParseTreeWalker()
    collector = SOCollector()
    walker.walk(collector, tree)
    vals = {
        'X_1': 1,
        'Y_1': 4,
        'Z_1': 3,
        }
    for c in collector.contstraints:
        c.print_walk()
        print(c(vals))
