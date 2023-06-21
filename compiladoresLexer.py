# Generated from /home/edu/workspaces/facu/dhs/dhs-compilador/compiladores.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\5")
        buf.write("#\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2")
        buf.write("\3\3\3\3\3\4\6\4\23\n\4\r\4\16\4\24\3\5\3\5\3\6\3\6\5")
        buf.write("\6\33\n\6\3\6\3\6\3\6\6\6 \n\6\r\6\16\6!\2\2\7\3\2\5\2")
        buf.write("\7\3\t\4\13\5\3\2\4\4\2C\\c|\3\2\62;\2%\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\3\r\3\2\2\2\5\17\3\2\2\2\7\22")
        buf.write("\3\2\2\2\t\26\3\2\2\2\13\32\3\2\2\2\r\16\t\2\2\2\16\4")
        buf.write("\3\2\2\2\17\20\t\3\2\2\20\6\3\2\2\2\21\23\5\5\3\2\22\21")
        buf.write("\3\2\2\2\23\24\3\2\2\2\24\22\3\2\2\2\24\25\3\2\2\2\25")
        buf.write("\b\3\2\2\2\26\27\13\2\2\2\27\n\3\2\2\2\30\33\5\3\2\2\31")
        buf.write("\33\7a\2\2\32\30\3\2\2\2\32\31\3\2\2\2\33\37\3\2\2\2\34")
        buf.write(" \5\3\2\2\35 \5\5\3\2\36 \7a\2\2\37\34\3\2\2\2\37\35\3")
        buf.write("\2\2\2\37\36\3\2\2\2 !\3\2\2\2!\37\3\2\2\2!\"\3\2\2\2")
        buf.write("\"\f\3\2\2\2\7\2\24\32\37!\2")
        return buf.getvalue()


class compiladoresLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NUMERO = 1
    OTRO = 2
    ID = 3

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "NUMERO", "OTRO", "ID" ]

    ruleNames = [ "LETRA", "DIGITO", "NUMERO", "OTRO", "ID" ]

    grammarFileName = "compiladores.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


