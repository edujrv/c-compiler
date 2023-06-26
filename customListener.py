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
    parametros = []

    def guardar(self, contexto):
        self.f.write("{")
        for key in contexto:
                self.f.write(contexto[key].toString())
        self.f.write("}\n")
    
        # Enter a parse tree produced by compiladoresParser#programa.
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        self.f = open('./output/TablaDeSimbolos.txt','w')
        print("***comienza la compilacion***")
        self.ts.addContex()
        # print(f"->addcontexto global")

    # Exit a parse tree produced by compiladoresParser#programa.
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print("***termina la compilacion***")
        self.guardar(self.ts.ts[-1])
        self.ts.removeContex()
        # print(f"->removecontexto global")
        self.f.close()
    
    def enterBloques(self, ctx:compiladoresParser.BloquesContext):
        self.ts.addContex()
        print(f"->addcontexto")

    def exitBloques(self, ctx:compiladoresParser.BloquesContext):
        # print(f"-> BLOQUESSSS (out) {ctx.getText()}")
        
        for inst in self.ts.ts[-1]:
            var = self.ts.returnKey(inst)
            if not var.initialized :
                print(f"ERROR: variable '{var.name}' indefinida")
            if not var.used :
                print(f"ERROR: variable '{var.name}' no utilizada")
    
            # print(f"-> FOR EXIT BLOQUES(out) {self.ts.returnKey(inst).toString()}")

        self.guardar(self.ts.ts[-1]) # escribir en la tabla
        self.ts.removeContex()
        print(f"->removecontexto")

    def exitBloque(self, ctx:compiladoresParser.BloqueContext):
        # print(f"-> EXIT BLOQUE(out) {ctx.getText()}")
        pass
        

    def exitDeclaracion_variable(self, ctx:compiladoresParser.Declaracion_variableContext):
        # print(f"-> Declaracion_variable(out) {ctx.getText()}")
        var = Variable(ctx.getChild(1), ctx.getChild(0).getChild(0)) # (name, type)
        if ( ctx.getChild(2) is None):
            var.initialized = False
        else:
            var.initialized = True 

        self.ts.ts[-1][str(var.name)] = var


    def exitAsignacion_variable(self, ctx:compiladoresParser.Asignacion_variableContext):
        # print(f"-> asignacion(out) {ctx.getText()}")
        name = str(ctx.getChild(0))
        if ( self.ts.findByKey(name) ):
            self.ts.ts[-1][name].initialized = True
            self.ts.ts[-1][name].used = True
        else:
            print(f"ERROR: variable '{name}' no definida")

    def exitCondicion(self, ctx:compiladoresParser.CondicionContext):
        # print(f"-> condicion(out) {ctx.getText()}")
        if (self.ts.findByKey(str(ctx.getChild(0)))):
            self.ts.ts[self.ts.getDicByKey(str(ctx.getChild(0)))][str(ctx.getChild(0))].used = True
        if (self.ts.findByKey(str(ctx.getChild(2)))):
            self.ts.ts[self.ts.getDicByKey(str(ctx.getChild(2)))][str(ctx.getChild(2))].used = True


    def exitOperacion(self, ctx:compiladoresParser.OperacionContext):
        # print(f"-> operacion(out) {ctx.getText()}")
        if (self.ts.findByKey(str(ctx.getChild(0)))):
            self.ts.ts[self.ts.getDicByKey(str(ctx.getChild(0)))][str(ctx.getChild(0))].used = True
        if (self.ts.findByKey(str(ctx.getChild(2)))):
            self.ts.ts[self.ts.getDicByKey(str(ctx.getChild(2)))][str(ctx.getChild(2))].used = True

    def exitReturn_func(self, ctx:compiladoresParser.Return_funcContext):
        name = ctx.ID().getText()
        variable = self.ts.returnKey(name)
        exist = self.ts.findByKey(name)
        if exist:
            variable.used = True
        else:
            print(f"La variable '{name}' no esta definida")
        # print(f"soy el id: {id}")


    def exitArgumento_proto(self, ctx:compiladoresParser.Argumento_protoContext):
        print(f"-> Prototipado_funcion(out) {ctx.getText()}")
        var = Variable(ctx.getChild(1), ctx.getChild(0).getChild(0))   
        var.initialized = True     
        self.parametros.append(var)         


    def exitPrototipado_funcion(self, ctx:compiladoresParser.Prototipado_funcionContext):
        print(f"-> Prototipado_funcion(out) {ctx.getText()}")
        lis = []
        for par in self.parametros:
            lis.append(par.toString())
        # print(f"PARAMETROS -> {lis}")
        # print(f"-> ctx.getChild(0)) {ctx.getChild(0)}")
        # print(f"-> ctx.getChild(1)) {ctx.getChild(1)}")
        # print(f"-> ctx.getChild(2)) {ctx.getChild(2)}")
        # print(f"-> ctx.getChild(3)) {ctx.getChild(3).getChild(0).getChild(0).getChild(0)}")
        # print(f"-> ctx.getChild(3)) {ctx.getChild(3).getChild(0).getChild(0).getChild(1)}")
        # print(f"-> ctx.getChild(4)) {ctx.getChild(4)}")
        fun = Function(ctx.getChild(1), ctx.getChild(0).getChild(0), self.parametros.copy()) # (name, type, params)
        self.ts.ts[-1][str(fun.name)] = fun
        self.parametros.clear()

    def exitArgumento(self, ctx:compiladoresParser.ArgumentoContext):
        var = Variable(ctx.getChild(1), ctx.getChild(0).getChild(0)) # (name, type)
        var.initialized = True
        self.ts.ts[-1][str(var.name)] = var


    def enterDeclaracion_funcion(self, ctx:compiladoresParser.Declaracion_funcionContext):
        pass

    def exitDeclaracion_funcion(self, ctx:compiladoresParser.Declaracion_funcionContext):
        name = str(ctx.getChild(1))
        print(f"name: {name}")
        variable = self.ts.returnKey(name)
        if (name != 'main' and ( not self.ts.findByKey(name) or variable.varFunc == 'variable')):
            # if ( not self.ts.findByKey(name) or variable.varFunc == 'variable'):
            print(f"ERROR: funcion '{name}' no prototipada")
        elif (variable):
            variable.implemented = True
            

    def exitLlamada_funcion(self, ctx:compiladoresParser.Llamada_funcionContext):
        print(f"LLamada funcion {ctx.getText()}")
        name = str(ctx.getChild(0))
        variable = self.ts.returnKey(name)
        exist = self.ts.findByKey(name)
        if exist:
            if ( variable.varFunc == 'variable'):
                print(f"ERROR: funcion '{name}' no existe")
            elif ( not variable.implemented) :
                print(f"ERROR: funcion '{name}' no implementada")
            elif not variable.initialized :
                print(f"ERROR: funcion '{name}' no prototipada")
        else:
            print(f"ERROR: funcion '{name}' no existe")





del compiladoresParser