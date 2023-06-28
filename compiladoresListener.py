# Generated from /home/marcos/Descargas/dhs/c-compiler/compiladores.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser

# This class defines a complete listener for a parse tree produced by compiladoresParser.
class compiladoresListener(ParseTreeListener):

    # Enter a parse tree produced by compiladoresParser#programa.
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        pass

    # Exit a parse tree produced by compiladoresParser#programa.
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        pass


    # Enter a parse tree produced by compiladoresParser#instrucciones.
    def enterInstrucciones(self, ctx:compiladoresParser.InstruccionesContext):
        pass

    # Exit a parse tree produced by compiladoresParser#instrucciones.
    def exitInstrucciones(self, ctx:compiladoresParser.InstruccionesContext):
        pass


    # Enter a parse tree produced by compiladoresParser#instruccion.
    def enterInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#instruccion.
    def exitInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#bloques.
    def enterBloques(self, ctx:compiladoresParser.BloquesContext):
        pass

    # Exit a parse tree produced by compiladoresParser#bloques.
    def exitBloques(self, ctx:compiladoresParser.BloquesContext):
        pass


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


    # Enter a parse tree produced by compiladoresParser#argumento.
    def enterArgumento(self, ctx:compiladoresParser.ArgumentoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#argumento.
    def exitArgumento(self, ctx:compiladoresParser.ArgumentoContext):
        pass


    # Enter a parse tree produced by compiladoresParser#argumento_proto.
    def enterArgumento_proto(self, ctx:compiladoresParser.Argumento_protoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#argumento_proto.
    def exitArgumento_proto(self, ctx:compiladoresParser.Argumento_protoContext):
        pass


    # Enter a parse tree produced by compiladoresParser#prototipado_funcion.
    def enterPrototipado_funcion(self, ctx:compiladoresParser.Prototipado_funcionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#prototipado_funcion.
    def exitPrototipado_funcion(self, ctx:compiladoresParser.Prototipado_funcionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#lista_argumento.
    def enterLista_argumento(self, ctx:compiladoresParser.Lista_argumentoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#lista_argumento.
    def exitLista_argumento(self, ctx:compiladoresParser.Lista_argumentoContext):
        pass


    # Enter a parse tree produced by compiladoresParser#lista_argumento_proto.
    def enterLista_argumento_proto(self, ctx:compiladoresParser.Lista_argumento_protoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#lista_argumento_proto.
    def exitLista_argumento_proto(self, ctx:compiladoresParser.Lista_argumento_protoContext):
        pass


    # Enter a parse tree produced by compiladoresParser#declaracion_funcion.
    def enterDeclaracion_funcion(self, ctx:compiladoresParser.Declaracion_funcionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#declaracion_funcion.
    def exitDeclaracion_funcion(self, ctx:compiladoresParser.Declaracion_funcionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#parametros.
    def enterParametros(self, ctx:compiladoresParser.ParametrosContext):
        pass

    # Exit a parse tree produced by compiladoresParser#parametros.
    def exitParametros(self, ctx:compiladoresParser.ParametrosContext):
        pass


    # Enter a parse tree produced by compiladoresParser#llamada_funcion.
    def enterLlamada_funcion(self, ctx:compiladoresParser.Llamada_funcionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#llamada_funcion.
    def exitLlamada_funcion(self, ctx:compiladoresParser.Llamada_funcionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#asignacion_variable.
    def enterAsignacion_variable(self, ctx:compiladoresParser.Asignacion_variableContext):
        pass

    # Exit a parse tree produced by compiladoresParser#asignacion_variable.
    def exitAsignacion_variable(self, ctx:compiladoresParser.Asignacion_variableContext):
        pass


    # Enter a parse tree produced by compiladoresParser#bloque.
    def enterBloque(self, ctx:compiladoresParser.BloqueContext):
        pass

    # Exit a parse tree produced by compiladoresParser#bloque.
    def exitBloque(self, ctx:compiladoresParser.BloqueContext):
        pass


    # Enter a parse tree produced by compiladoresParser#return_func.
    def enterReturn_func(self, ctx:compiladoresParser.Return_funcContext):
        pass

    # Exit a parse tree produced by compiladoresParser#return_func.
    def exitReturn_func(self, ctx:compiladoresParser.Return_funcContext):
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


    # Enter a parse tree produced by compiladoresParser#bloque_operacional.
    def enterBloque_operacional(self, ctx:compiladoresParser.Bloque_operacionalContext):
        pass

    # Exit a parse tree produced by compiladoresParser#bloque_operacional.
    def exitBloque_operacional(self, ctx:compiladoresParser.Bloque_operacionalContext):
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


    # Enter a parse tree produced by compiladoresParser#bloque_while.
    def enterBloque_while(self, ctx:compiladoresParser.Bloque_whileContext):
        pass

    # Exit a parse tree produced by compiladoresParser#bloque_while.
    def exitBloque_while(self, ctx:compiladoresParser.Bloque_whileContext):
        pass


    # Enter a parse tree produced by compiladoresParser#bloque_do_while.
    def enterBloque_do_while(self, ctx:compiladoresParser.Bloque_do_whileContext):
        pass

    # Exit a parse tree produced by compiladoresParser#bloque_do_while.
    def exitBloque_do_while(self, ctx:compiladoresParser.Bloque_do_whileContext):
        pass


    # Enter a parse tree produced by compiladoresParser#bloque_switch.
    def enterBloque_switch(self, ctx:compiladoresParser.Bloque_switchContext):
        pass

    # Exit a parse tree produced by compiladoresParser#bloque_switch.
    def exitBloque_switch(self, ctx:compiladoresParser.Bloque_switchContext):
        pass


    # Enter a parse tree produced by compiladoresParser#bloque_case.
    def enterBloque_case(self, ctx:compiladoresParser.Bloque_caseContext):
        pass

    # Exit a parse tree produced by compiladoresParser#bloque_case.
    def exitBloque_case(self, ctx:compiladoresParser.Bloque_caseContext):
        pass



del compiladoresParser