# Generated from /home/edu/workspaces/facu/dhs/dhs-compilador/compiladores.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\5")
        buf.write("\21\4\2\t\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5")
        buf.write("\2\17\n\2\3\2\2\2\3\2\2\2\2\22\2\16\3\2\2\2\4\5\7\5\2")
        buf.write("\2\5\6\b\2\1\2\6\17\5\2\2\2\7\b\7\3\2\2\b\t\b\2\1\2\t")
        buf.write("\17\5\2\2\2\n\13\7\4\2\2\13\f\b\2\1\2\f\17\5\2\2\2\r\17")
        buf.write("\7\2\2\3\16\4\3\2\2\2\16\7\3\2\2\2\16\n\3\2\2\2\16\r\3")
        buf.write("\2\2\2\17\3\3\2\2\2\3\16")
        return buf.getvalue()


class compiladoresParser ( Parser ):

    grammarFileName = "compiladores.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "NUMERO", "OTRO", "ID" ]

    RULE_s = 0

    ruleNames =  [ "s" ]

    EOF = Token.EOF
    NUMERO=1
    OTRO=2
    ID=3

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token
            self._NUMERO = None # Token
            self._OTRO = None # Token

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def s(self):
            return self.getTypedRuleContext(compiladoresParser.SContext,0)


        def NUMERO(self):
            return self.getToken(compiladoresParser.NUMERO, 0)

        def OTRO(self):
            return self.getToken(compiladoresParser.OTRO, 0)

        def EOF(self):
            return self.getToken(compiladoresParser.EOF, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS" ):
                listener.enterS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS" ):
                listener.exitS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitS" ):
                return visitor.visitS(self)
            else:
                return visitor.visitChildren(self)




    def s(self):

        localctx = compiladoresParser.SContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_s)
        try:
            self.state = 12
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [compiladoresParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2
                localctx._ID = self.match(compiladoresParser.ID)
                print("ID ->" + (None if localctx._ID is None else localctx._ID.text) + "<--") 
                self.state = 4
                self.s()
                pass
            elif token in [compiladoresParser.NUMERO]:
                self.enterOuterAlt(localctx, 2)
                self.state = 5
                localctx._NUMERO = self.match(compiladoresParser.NUMERO)
                print("NUMERO ->" + (None if localctx._NUMERO is None else localctx._NUMERO.text) + "<--") 
                self.state = 7
                self.s()
                pass
            elif token in [compiladoresParser.OTRO]:
                self.enterOuterAlt(localctx, 3)
                self.state = 8
                localctx._OTRO = self.match(compiladoresParser.OTRO)
                print("Otro ->" + (None if localctx._OTRO is None else localctx._OTRO.text) + "<--") 
                self.state = 10
                self.s()
                pass
            elif token in [compiladoresParser.EOF]:
                self.enterOuterAlt(localctx, 4)
                self.state = 11
                self.match(compiladoresParser.EOF)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





