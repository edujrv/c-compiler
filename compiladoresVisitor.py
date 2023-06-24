# Generated from /home/marcos/Descargas/dhs/c-compiler/compiladores.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser

# This class defines a complete generic visitor for a parse tree produced by compiladoresParser.

class compiladoresVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by compiladoresParser#compiladores.
    def visitCompiladores(self, ctx:compiladoresParser.CompiladoresContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#statement.
    def visitStatement(self, ctx:compiladoresParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloques.
    def visitBloques(self, ctx:compiladoresParser.BloquesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#declaracion_variable.
    def visitDeclaracion_variable(self, ctx:compiladoresParser.Declaracion_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#tipo.
    def visitTipo(self, ctx:compiladoresParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#atributos.
    def visitAtributos(self, ctx:compiladoresParser.AtributosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#prototipado_funcion.
    def visitPrototipado_funcion(self, ctx:compiladoresParser.Prototipado_funcionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#lista_parametro.
    def visitLista_parametro(self, ctx:compiladoresParser.Lista_parametroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#id_funcion.
    def visitId_funcion(self, ctx:compiladoresParser.Id_funcionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#declaracion_funcion.
    def visitDeclaracion_funcion(self, ctx:compiladoresParser.Declaracion_funcionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#asignacion_variable.
    def visitAsignacion_variable(self, ctx:compiladoresParser.Asignacion_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloque.
    def visitBloque(self, ctx:compiladoresParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#return_func.
    def visitReturn_func(self, ctx:compiladoresParser.Return_funcContext):
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


    # Visit a parse tree produced by compiladoresParser#bloque_operacional.
    def visitBloque_operacional(self, ctx:compiladoresParser.Bloque_operacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#operacion.
    def visitOperacion(self, ctx:compiladoresParser.OperacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloque_for.
    def visitBloque_for(self, ctx:compiladoresParser.Bloque_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloque_while.
    def visitBloque_while(self, ctx:compiladoresParser.Bloque_whileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloque_do_while.
    def visitBloque_do_while(self, ctx:compiladoresParser.Bloque_do_whileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloque_switch.
    def visitBloque_switch(self, ctx:compiladoresParser.Bloque_switchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloque_case.
    def visitBloque_case(self, ctx:compiladoresParser.Bloque_caseContext):
        return self.visitChildren(ctx)



del compiladoresParser