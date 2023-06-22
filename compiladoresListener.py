# Generated from /home/edu/workspaces/facu/dhs/c-compiler/compiladores.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser

# This class defines a complete listener for a parse tree produced by compiladoresParser.
class compiladoresListener(ParseTreeListener):

    # Enter a parse tree produced by compiladoresParser#declaracion_variable.
    def enterDeclaracion_variable(self, ctx:compiladoresParser.Declaracion_variableContext):
        pass

    # Exit a parse tree produced by compiladoresParser#declaracion_variable.
    def exitDeclaracion_variable(self, ctx:compiladoresParser.Declaracion_variableContext):
        pass


    # Enter a parse tree produced by compiladoresParser#tipo.
    def enterTipo(self, ctx:compiladoresParser.TipoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#tipo.
    def exitTipo(self, ctx:compiladoresParser.TipoContext):
        pass


    # Enter a parse tree produced by compiladoresParser#atributos.
    def enterAtributos(self, ctx:compiladoresParser.AtributosContext):
        pass

    # Exit a parse tree produced by compiladoresParser#atributos.
    def exitAtributos(self, ctx:compiladoresParser.AtributosContext):
        pass


    # Enter a parse tree produced by compiladoresParser#declaracion_funcion.
    def enterDeclaracion_funcion(self, ctx:compiladoresParser.Declaracion_funcionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#declaracion_funcion.
    def exitDeclaracion_funcion(self, ctx:compiladoresParser.Declaracion_funcionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#asignacion_variable.
    def enterAsignacion_variable(self, ctx:compiladoresParser.Asignacion_variableContext):
        pass

    # Exit a parse tree produced by compiladoresParser#asignacion_variable.
    def exitAsignacion_variable(self, ctx:compiladoresParser.Asignacion_variableContext):
        pass


    # Enter a parse tree produced by compiladoresParser#comentario.
    def enterComentario(self, ctx:compiladoresParser.ComentarioContext):
        pass

    # Exit a parse tree produced by compiladoresParser#comentario.
    def exitComentario(self, ctx:compiladoresParser.ComentarioContext):
        pass


    # Enter a parse tree produced by compiladoresParser#sentencia.
    def enterSentencia(self, ctx:compiladoresParser.SentenciaContext):
        pass

    # Exit a parse tree produced by compiladoresParser#sentencia.
    def exitSentencia(self, ctx:compiladoresParser.SentenciaContext):
        pass


    # Enter a parse tree produced by compiladoresParser#return_func.
    def enterReturn_func(self, ctx:compiladoresParser.Return_funcContext):
        pass

    # Exit a parse tree produced by compiladoresParser#return_func.
    def exitReturn_func(self, ctx:compiladoresParser.Return_funcContext):
        pass


    # Enter a parse tree produced by compiladoresParser#bloque.
    def enterBloque(self, ctx:compiladoresParser.BloqueContext):
        pass

    # Exit a parse tree produced by compiladoresParser#bloque.
    def exitBloque(self, ctx:compiladoresParser.BloqueContext):
        pass


    # Enter a parse tree produced by compiladoresParser#condicion.
    def enterCondicion(self, ctx:compiladoresParser.CondicionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#condicion.
    def exitCondicion(self, ctx:compiladoresParser.CondicionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#bloque_if.
    def enterBloque_if(self, ctx:compiladoresParser.Bloque_ifContext):
        pass

    # Exit a parse tree produced by compiladoresParser#bloque_if.
    def exitBloque_if(self, ctx:compiladoresParser.Bloque_ifContext):
        pass


    # Enter a parse tree produced by compiladoresParser#bloque_if_else.
    def enterBloque_if_else(self, ctx:compiladoresParser.Bloque_if_elseContext):
        pass

    # Exit a parse tree produced by compiladoresParser#bloque_if_else.
    def exitBloque_if_else(self, ctx:compiladoresParser.Bloque_if_elseContext):
        pass


    # Enter a parse tree produced by compiladoresParser#operacion.
    def enterOperacion(self, ctx:compiladoresParser.OperacionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#operacion.
    def exitOperacion(self, ctx:compiladoresParser.OperacionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#bloque_for.
    def enterBloque_for(self, ctx:compiladoresParser.Bloque_forContext):
        pass

    # Exit a parse tree produced by compiladoresParser#bloque_for.
    def exitBloque_for(self, ctx:compiladoresParser.Bloque_forContext):
        pass



del compiladoresParser