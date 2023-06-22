# Generated from /home/edu/workspaces/facu/dhs/c-compiler/compiladores.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser

# This class defines a complete generic visitor for a parse tree produced by compiladoresParser.

class compiladoresVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by compiladoresParser#declaracion_variable.
    def visitDeclaracion_variable(self, ctx:compiladoresParser.Declaracion_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#tipo.
    def visitTipo(self, ctx:compiladoresParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#atributos.
    def visitAtributos(self, ctx:compiladoresParser.AtributosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#declaracion_funcion.
    def visitDeclaracion_funcion(self, ctx:compiladoresParser.Declaracion_funcionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#asignacion_variable.
    def visitAsignacion_variable(self, ctx:compiladoresParser.Asignacion_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#comentario.
    def visitComentario(self, ctx:compiladoresParser.ComentarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#sentencia.
    def visitSentencia(self, ctx:compiladoresParser.SentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#return_func.
    def visitReturn_func(self, ctx:compiladoresParser.Return_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloque.
    def visitBloque(self, ctx:compiladoresParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#condicion.
    def visitCondicion(self, ctx:compiladoresParser.CondicionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloque_if.
    def visitBloque_if(self, ctx:compiladoresParser.Bloque_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloque_if_else.
    def visitBloque_if_else(self, ctx:compiladoresParser.Bloque_if_elseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#operacion.
    def visitOperacion(self, ctx:compiladoresParser.OperacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloque_for.
    def visitBloque_for(self, ctx:compiladoresParser.Bloque_forContext):
        return self.visitChildren(ctx)



del compiladoresParser