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
    numero_contexto = 0

    def guardar(self, contexto):
        self.f.write(f"Contexto nro {self.numero_contexto}\n")
        self.f.write(f"Nombre\tTipo\tInicializada\tUsada\tClasificacion\tImplementada\tParametros\n")
        for key in contexto:
                self.f.write(f"{contexto[key].toString()}\n")
        self.f.write("\n\n")
        self.numero_contexto = self.numero_contexto + 1
    
        # Enter a parse tree produced by compiladoresParser#programa.
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        self.f = open('./output/TablaDeSimbolos.txt','w')
        self.ts.addContex()

    # Exit a parse tree produced by compiladoresParser#programa.
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        for inst in self.ts.ts[-1]:
            var = self.ts.returnKey(inst)
            if not var.initialized :
                print(f"ERROR: variable o funcion '{var.name}' no inicializada")
            if not var.used :
                print(f"ERROR: variable  o funcion'{var.name}' no utilizada")
            
            try:
                if not var.implemented :
                    print(f"ERROR: funcion'{var.name}' no implementada")
            except:
                pass

        self.guardar(self.ts.ts[-1])
        self.ts.removeContex()
        self.f.close()
    
    def enterBloques(self, ctx:compiladoresParser.BloquesContext):
        self.ts.addContex()

    def exitBloques(self, ctx:compiladoresParser.BloquesContext):
        for inst in self.ts.ts[-1]:
            var = self.ts.returnKey(inst)
            if not var.initialized :
                print(f"ERROR: variable '{var.name}' indefinida")
            if not var.used :
                print(f"ERROR: variable '{var.name}' no utilizada")

        self.guardar(self.ts.ts[-1]) # escribir en la tabla
        self.ts.removeContex()

    def exitBloque(self, ctx:compiladoresParser.BloqueContext):
        pass
        

    def exitDeclaracion_variable(self, ctx:compiladoresParser.Declaracion_variableContext):
        var = Variable(ctx.getChild(1), ctx.getChild(0).getChild(0)) # (name, type)
        if ( ctx.getChild(2) is None):
            var.initialized = False
        else:
            var.initialized = True 
        self.ts.ts[-1][str(var.name)] = var

    def exitAsignacion_variable(self, ctx:compiladoresParser.Asignacion_variableContext):
        name = str(ctx.getChild(0))
        index = self.ts.getDicByKey(name)
        if ( self.ts.findByKey(name) ):
            self.ts.ts[index][name].initialized = True
            self.ts.ts[index][name].used = True
        else:
            print(f"ERROR: variable '{name}' no definida")

    def exitCondicion(self, ctx:compiladoresParser.CondicionContext):
        if (self.ts.findByKey(str(ctx.getChild(0)))):
            self.ts.ts[self.ts.getDicByKey(str(ctx.getChild(0)))][str(ctx.getChild(0))].used = True
        if (self.ts.findByKey(str(ctx.getChild(2)))):
            self.ts.ts[self.ts.getDicByKey(str(ctx.getChild(2)))][str(ctx.getChild(2))].used = True


    def exitOperacion(self, ctx:compiladoresParser.OperacionContext):
        if (self.ts.findByKey(str(ctx.getChild(0)))):
            self.ts.ts[self.ts.getDicByKey(str(ctx.getChild(0)))][str(ctx.getChild(0))].used = True
        if (self.ts.findByKey(str(ctx.getChild(2)))):
            self.ts.ts[self.ts.getDicByKey(str(ctx.getChild(2)))][str(ctx.getChild(2))].used = True

    def exitReturn_func(self, ctx:compiladoresParser.Return_funcContext):
        try:
            name = ctx.ID().getText()
            variable = self.ts.returnKey(name)
            exist = self.ts.findByKey(name)
            if exist:
                variable.used = True
            else:
                print(f"La variable '{name}' no esta definida")
        except:
            pass 

    def exitArgumento_proto(self, ctx:compiladoresParser.Argumento_protoContext):
        var = Variable(ctx.getChild(1), ctx.getChild(0).getChild(0))   
        var.initialized = True     
        self.parametros.append(var)         


    def exitPrototipado_funcion(self, ctx:compiladoresParser.Prototipado_funcionContext):
        lis = []
        for par in self.parametros:
            lis.append(par.toString())

        fun = Function(ctx.getChild(1), ctx.getChild(0).getChild(0), self.parametros.copy()) # (name, type, params)
        fun.initialized = True
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
        variable = self.ts.returnKey(name)
        if (name != 'main' and ( not self.ts.findByKey(name) or variable.varFunc == 'variable')):
            print(f"ERROR: funcion '{name}' no prototipada")
        elif (variable):
            variable.implemented = True            

    def exitLlamada_funcion(self, ctx:compiladoresParser.Llamada_funcionContext):
        name = str(ctx.getChild(0))
        variable = self.ts.returnKey(name)
        exist = self.ts.findByKey(name)
        if exist:
            if ( variable.varFunc == 'variable'):
                print(f"ERROR: funcion '{name}' no existe")
            elif not variable.initialized :
                print(f"ERROR: funcion '{name}' no prototipada")
            else:
                variable.used = True
        else:
            print(f"ERROR: funcion '{name}' no existe")

del compiladoresParser