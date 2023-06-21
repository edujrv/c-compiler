# Generated from /home/edu/workspaces/facu/dhs/dhs-compilador/compiladores.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser

# This class defines a complete generic visitor for a parse tree produced by compiladoresParser.

class compiladoresVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by compiladoresParser#s.
    def visitS(self, ctx:compiladoresParser.SContext):
        return self.visitChildren(ctx)



del compiladoresParser