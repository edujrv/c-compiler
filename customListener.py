# Generated from /home/marcos/Descargas/dhs/c-compiler/compiladores.g4 by ANTLR 4.9.2
from antlr4 import *
from compiladoresListener import compiladoresListener
from tablaSimbolos import TablaSimbolos, Variable, Function

if __name__ is not None and "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser

# This class defines a complete listener for a parse tree produced by compiladoresParser.
class customListener (compiladoresListener):
    #tabla de simbolos
    ts = TablaSimbolos()

    def guardar(self, contexto):
        for key in contexto:
                self.f.write(contexto[key].toString())
        self.f.write("\n")

    # Enter a parse tree produced by compiladoresParser#compiladores.
    def enterCompiladores(self, ctx:compiladoresParser.CompiladoresContext):
        self.f = open('./output/TablaDeSimbolos.txt','w')
        print("***comienza la compilacion***")
        self.ts.addContex()
        print(f"->addcontexto global")

    # Exit a parse tree produced by compiladoresParser#compiladores.
    def exitCompiladores(self, ctx:compiladoresParser.CompiladoresContext):
        print("***termina la compilacion***")
        self.guardar(self.ts.ts[-1])
        self.ts.removeContex()
        print(f"->removecontexto global")
        self.f.close()

    # Enter a parse tree produced by compiladoresParser#statement.
    def enterStatement(self, ctx:compiladoresParser.StatementContext):
        pass

    # Exit a parse tree produced by compiladoresParser#statement.
    def exitStatement(self, ctx:compiladoresParser.StatementContext):
        # print(f"-> statement(out) {ctx.getText()}")
        pass


    # Enter a parse tree produced by compiladoresParser#declaracion_variable.
    def enterDeclaracion_variable(self, ctx:compiladoresParser.Declaracion_variableContext):
        # print(f"-> declaracion_variable(in) {ctx.getText()}")
        pass

    # Exit a parse tree produced by compiladoresParser#declaracion_variable.
    def exitDeclaracion_variable(self, ctx:compiladoresParser.Declaracion_variableContext):
        print(f"-> declaracion_variable(out) {ctx.getText()}")
        # print(f"getchild0: {ctx.getChild(0).getChild(0)}")
        # print(f"getchild1: {ctx.getChild(1)}")
        # print(f"getchild2: {ctx.getChild(2)}")
        # print(f"getchild3: {ctx.getChild(3)}")
        var = Variable(ctx.getChild(1), ctx.getChild(0).getChild(0)) # (name, type)
        if ( ctx.getChild(2) is None):
            var.initialized = False
        else:
            var.initialized = True 

        self.ts.ts[-1][str(var.name)] = var


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


    # Enter a parse tree produced by compiladoresParser#prototipado_funcion.
    def enterPrototipado_funcion(self, ctx:compiladoresParser.Prototipado_funcionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#prototipado_funcion.
    def exitPrototipado_funcion(self, ctx:compiladoresParser.Prototipado_funcionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#lista_parametro.
    def enterLista_parametro(self, ctx:compiladoresParser.Lista_parametroContext):
        pass

    # Exit a parse tree produced by compiladoresParser#lista_parametro.
    def exitLista_parametro(self, ctx:compiladoresParser.Lista_parametroContext):
        pass


    # Enter a parse tree produced by compiladoresParser#declaracion_funcion.
    def enterDeclaracion_funcion(self, ctx:compiladoresParser.Declaracion_funcionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#declaracion_funcion.
    def exitDeclaracion_funcion(self, ctx:compiladoresParser.Declaracion_funcionContext):
        print(f"-> funcion(out) {ctx.getText()}")
        print(f"getchild0: {ctx.getChild(0).getChild(0)}")
        print(f"getchild1: {ctx.getChild(1)}")
        print(f"getchild2: {ctx.getChild(2)}")
        print(f"getchild3: {ctx.getChild(3)}")
        print(f"getchild4: {ctx.getChild(4)}")
        print(f"getchild5: {ctx.getChild(5)}")
        print(f"getchild6: {ctx.getChild(6)}")
        # print(f"->hola {str(ctx.lista_parametro())}") 
        # print(f"PARAMS: {params}")

        # var = Variable(ctx.getChild(1), ctx.getChild(0).getChild(0), ctx.getChild(3).get) # (name, type)
        # if ( ctx.getChild(2) is None):
        #     var.initialized = False
        # else:
        #     var.initialized = True 

        # self.ts.ts[-1][str(var.name)] = var 


    # Enter a parse tree produced by compiladoresParser#asignacion_variable.
    def enterAsignacion_variable(self, ctx:compiladoresParser.Asignacion_variableContext):
        pass

    # Exit a parse tree produced by compiladoresParser#asignacion_variable.
    def exitAsignacion_variable(self, ctx:compiladoresParser.Asignacion_variableContext):
        print(f"ASIGNACION getChild(0) -> {ctx.getChild(0)}")
        print(f"ASIGNACION getChild(1) -> {ctx.getChild(1)}")
        print(f"ASIGNACION getChild(2) -> {ctx.getChild(2)}")
        print(f"ASIGNACION getChild(3) -> {ctx.getChild(3)}")
        try:
            self.ts.ts[-1][str(ctx.getChild(0))].initialized = True     #Comprueba si esta en el contexto local
        except:
            try:
                self.ts.ts[0][str(ctx.getChild(0))].initialized = True   #Comprueba si esta en el contexto global
            except:
                print("Variable no inicializada en ningun contexto") 

        print("Asignacion ---> " + ctx.getText())


    # Enter a parse tree produced by compiladoresParser#bloque.
    def enterBloque(self, ctx:compiladoresParser.BloqueContext):
        pass

    # Exit a parse tree produced by compiladoresParser#bloque.
    def exitBloque(self, ctx:compiladoresParser.BloqueContext):
        pass

    # Enter a parse tree produced by compiladoresParser#bloques.
    def enterBloques(self, ctx:compiladoresParser.BloquesContext):
        self.ts.addContex()
        print(f"->addcontexto")

    # Exit a parse tree produced by compiladoresParser#bloques.
    def exitBloques(self, ctx:compiladoresParser.BloquesContext):
        self.guardar(self.ts.ts[-1])
        self.ts.removeContex()
        print(f"->removecontexto")

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
        print(f"operacion getChild(0) -> {ctx.getChild(0)}")
        print(f"operacion getChild(1) -> {ctx.getChild(1)}")
        print(f"operacion getChild(2) -> {ctx.getChild(2)}")
        print(f"operacion getChild(3) -> {ctx.getChild(3)}")
        if (self.ts.findByKey(str(ctx.getChild(0)))):
            self.ts.ts[-1][str(ctx.getChild(0))].used = True
        if (self.ts.findByKey(str(ctx.getChild(2)))):
            self.ts.ts[-1][str(ctx.getChild(2))].used = True
        


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