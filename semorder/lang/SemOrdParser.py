# Generated from SemOrd.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\24")
        buf.write("X\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2\34")
        buf.write("\n\2\7\2\36\n\2\f\2\16\2!\13\2\3\3\3\3\3\3\3\3\7\3\'\n")
        buf.write("\3\f\3\16\3*\13\3\3\4\3\4\3\4\3\4\7\4\60\n\4\f\4\16\4")
        buf.write("\63\13\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\5\bE\n\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\7\bO\n\b\f\b\16\bR\13\b\3\t\3\t\3\n\3\n\3\n\2\3")
        buf.write("\16\13\2\4\6\b\n\f\16\20\22\2\4\3\2\t\n\3\2\13\r\2U\2")
        buf.write("\24\3\2\2\2\4\"\3\2\2\2\6+\3\2\2\2\b\64\3\2\2\2\n8\3\2")
        buf.write("\2\2\f;\3\2\2\2\16D\3\2\2\2\20S\3\2\2\2\22U\3\2\2\2\24")
        buf.write("\25\5\4\3\2\25\26\7\23\2\2\26\27\5\6\4\2\27\30\7\23\2")
        buf.write("\2\30\37\5\n\6\2\31\33\7\23\2\2\32\34\5\f\7\2\33\32\3")
        buf.write("\2\2\2\33\34\3\2\2\2\34\36\3\2\2\2\35\31\3\2\2\2\36!\3")
        buf.write("\2\2\2\37\35\3\2\2\2\37 \3\2\2\2 \3\3\2\2\2!\37\3\2\2")
        buf.write("\2\"#\7\3\2\2#(\7\17\2\2$%\7\20\2\2%\'\7\17\2\2&$\3\2")
        buf.write("\2\2\'*\3\2\2\2(&\3\2\2\2()\3\2\2\2)\5\3\2\2\2*(\3\2\2")
        buf.write("\2+,\7\4\2\2,\61\5\b\5\2-.\7\20\2\2.\60\5\b\5\2/-\3\2")
        buf.write("\2\2\60\63\3\2\2\2\61/\3\2\2\2\61\62\3\2\2\2\62\7\3\2")
        buf.write("\2\2\63\61\3\2\2\2\64\65\7\17\2\2\65\66\7\22\2\2\66\67")
        buf.write("\7\16\2\2\67\t\3\2\2\289\7\5\2\29:\7\16\2\2:\13\3\2\2")
        buf.write("\2;<\7\6\2\2<=\5\16\b\2=\r\3\2\2\2>?\b\b\1\2?E\7\17\2")
        buf.write("\2@A\7\7\2\2AB\5\16\b\2BC\7\b\2\2CE\3\2\2\2D>\3\2\2\2")
        buf.write("D@\3\2\2\2EP\3\2\2\2FG\f\6\2\2GH\5\20\t\2HI\5\16\b\7I")
        buf.write("O\3\2\2\2JK\f\5\2\2KL\5\22\n\2LM\5\16\b\6MO\3\2\2\2NF")
        buf.write("\3\2\2\2NJ\3\2\2\2OR\3\2\2\2PN\3\2\2\2PQ\3\2\2\2Q\17\3")
        buf.write("\2\2\2RP\3\2\2\2ST\t\2\2\2T\21\3\2\2\2UV\t\3\2\2V\23\3")
        buf.write("\2\2\2\t\33\37(\61DNP")
        return buf.getvalue()


class SemOrdParser ( Parser ):

    grammarFileName = "SemOrd.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'process'", "'sem'", "'terminal'", "'constraint'", 
                     "'('", "')'", "'>'", "'<'", "'&'", "'|'", "'!'", "<INVALID>", 
                     "<INVALID>", "','", "';'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "GT", "LT", 
                      "LAND", "LOR", "LNOT", "INT", "ID", "COMMA", "SEMICOLON", 
                      "EQUALS", "NEWLINE", "WS" ]

    RULE_init = 0
    RULE_process = 1
    RULE_sem = 2
    RULE_defin = 3
    RULE_terminal = 4
    RULE_constraint = 5
    RULE_expr = 6
    RULE_cmp = 7
    RULE_boolop = 8

    ruleNames =  [ "init", "process", "sem", "defin", "terminal", "constraint", 
                   "expr", "cmp", "boolop" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    GT=7
    LT=8
    LAND=9
    LOR=10
    LNOT=11
    INT=12
    ID=13
    COMMA=14
    SEMICOLON=15
    EQUALS=16
    NEWLINE=17
    WS=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class InitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def process(self):
            return self.getTypedRuleContext(SemOrdParser.ProcessContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(SemOrdParser.NEWLINE)
            else:
                return self.getToken(SemOrdParser.NEWLINE, i)

        def sem(self):
            return self.getTypedRuleContext(SemOrdParser.SemContext,0)


        def terminal(self):
            return self.getTypedRuleContext(SemOrdParser.TerminalContext,0)


        def constraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SemOrdParser.ConstraintContext)
            else:
                return self.getTypedRuleContext(SemOrdParser.ConstraintContext,i)


        def getRuleIndex(self):
            return SemOrdParser.RULE_init

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInit" ):
                listener.enterInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInit" ):
                listener.exitInit(self)




    def init(self):

        localctx = SemOrdParser.InitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_init)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.process()
            self.state = 19
            self.match(SemOrdParser.NEWLINE)
            self.state = 20
            self.sem()
            self.state = 21
            self.match(SemOrdParser.NEWLINE)
            self.state = 22
            self.terminal()
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SemOrdParser.NEWLINE:
                self.state = 23
                self.match(SemOrdParser.NEWLINE)
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SemOrdParser.T__3:
                    self.state = 24
                    self.constraint()


                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProcessContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(SemOrdParser.ID)
            else:
                return self.getToken(SemOrdParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SemOrdParser.COMMA)
            else:
                return self.getToken(SemOrdParser.COMMA, i)

        def getRuleIndex(self):
            return SemOrdParser.RULE_process

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProcess" ):
                listener.enterProcess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProcess" ):
                listener.exitProcess(self)




    def process(self):

        localctx = SemOrdParser.ProcessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_process)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(SemOrdParser.T__0)
            self.state = 33
            self.match(SemOrdParser.ID)
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SemOrdParser.COMMA:
                self.state = 34
                self.match(SemOrdParser.COMMA)
                self.state = 35
                self.match(SemOrdParser.ID)
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def defin(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SemOrdParser.DefinContext)
            else:
                return self.getTypedRuleContext(SemOrdParser.DefinContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SemOrdParser.COMMA)
            else:
                return self.getToken(SemOrdParser.COMMA, i)

        def getRuleIndex(self):
            return SemOrdParser.RULE_sem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSem" ):
                listener.enterSem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSem" ):
                listener.exitSem(self)




    def sem(self):

        localctx = SemOrdParser.SemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_sem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(SemOrdParser.T__1)
            self.state = 42
            self.defin()
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SemOrdParser.COMMA:
                self.state = 43
                self.match(SemOrdParser.COMMA)
                self.state = 44
                self.defin()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefinContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SemOrdParser.ID, 0)

        def EQUALS(self):
            return self.getToken(SemOrdParser.EQUALS, 0)

        def INT(self):
            return self.getToken(SemOrdParser.INT, 0)

        def getRuleIndex(self):
            return SemOrdParser.RULE_defin

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefin" ):
                listener.enterDefin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefin" ):
                listener.exitDefin(self)




    def defin(self):

        localctx = SemOrdParser.DefinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_defin)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(SemOrdParser.ID)
            self.state = 51
            self.match(SemOrdParser.EQUALS)
            self.state = 52
            self.match(SemOrdParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TerminalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(SemOrdParser.INT, 0)

        def getRuleIndex(self):
            return SemOrdParser.RULE_terminal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerminal" ):
                listener.enterTerminal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerminal" ):
                listener.exitTerminal(self)




    def terminal(self):

        localctx = SemOrdParser.TerminalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_terminal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(SemOrdParser.T__2)
            self.state = 55
            self.match(SemOrdParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstraintContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(SemOrdParser.ExprContext,0)


        def getRuleIndex(self):
            return SemOrdParser.RULE_constraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstraint" ):
                listener.enterConstraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstraint" ):
                listener.exitConstraint(self)




    def constraint(self):

        localctx = SemOrdParser.ConstraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_constraint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(SemOrdParser.T__3)
            self.state = 58
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SemOrdParser.ID, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SemOrdParser.ExprContext)
            else:
                return self.getTypedRuleContext(SemOrdParser.ExprContext,i)


        def cmp(self):
            return self.getTypedRuleContext(SemOrdParser.CmpContext,0)


        def boolop(self):
            return self.getTypedRuleContext(SemOrdParser.BoolopContext,0)


        def getRuleIndex(self):
            return SemOrdParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SemOrdParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SemOrdParser.ID]:
                self.state = 61
                self.match(SemOrdParser.ID)
                pass
            elif token in [SemOrdParser.T__4]:
                self.state = 62
                self.match(SemOrdParser.T__4)
                self.state = 63
                self.expr(0)
                self.state = 64
                self.match(SemOrdParser.T__5)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 78
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 76
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = SemOrdParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 68
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 69
                        self.cmp()
                        self.state = 70
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = SemOrdParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 72
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 73
                        self.boolop()
                        self.state = 74
                        self.expr(4)
                        pass

             
                self.state = 80
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CmpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GT(self):
            return self.getToken(SemOrdParser.GT, 0)

        def LT(self):
            return self.getToken(SemOrdParser.LT, 0)

        def getRuleIndex(self):
            return SemOrdParser.RULE_cmp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmp" ):
                listener.enterCmp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmp" ):
                listener.exitCmp(self)




    def cmp(self):

        localctx = SemOrdParser.CmpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_cmp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            _la = self._input.LA(1)
            if not(_la==SemOrdParser.GT or _la==SemOrdParser.LT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolopContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LAND(self):
            return self.getToken(SemOrdParser.LAND, 0)

        def LOR(self):
            return self.getToken(SemOrdParser.LOR, 0)

        def LNOT(self):
            return self.getToken(SemOrdParser.LNOT, 0)

        def getRuleIndex(self):
            return SemOrdParser.RULE_boolop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolop" ):
                listener.enterBoolop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolop" ):
                listener.exitBoolop(self)




    def boolop(self):

        localctx = SemOrdParser.BoolopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_boolop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SemOrdParser.LAND) | (1 << SemOrdParser.LOR) | (1 << SemOrdParser.LNOT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         




