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
    
        # Enter a parse tree produced by compiladoresParser#programa.
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        self.f = open('./output/TablaDeSimbolos.txt','w')
        print("***comienza la compilacion***")
        self.ts.addContex()
        print(f"->addcontexto global")

    # Exit a parse tree produced by compiladoresParser#programa.
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print("***termina la compilacion***")
        self.guardar(self.ts.ts[-1])
        self.ts.removeContex()
        print(f"->removecontexto global")
        self.f.close()

    def exitDeclaracion_variable(self, ctx:compiladoresParser.Declaracion_variableContext):
        print(f"-> Declaracion_variable(out) {ctx.getText()}")
        var = Variable(ctx.getChild(1), ctx.getChild(0).getChild(0)) # (name, type)
        if ( ctx.getChild(2) is None):
            var.initialized = False
        else:
            var.initialized = True 

        self.ts.ts[-1][str(var.name)] = var


    def exitAsignacion_variable(self, ctx:compiladoresParser.Asignacion_variableContext):
        print(f"-> asignacion(out) {ctx.getText()}")
        self.ts.ts[-1][str(ctx.getChild(0))].initialized = True
        self.ts.ts[-1][str(ctx.getChild(0))].used = True

    def exitCondicion(self, ctx:compiladoresParser.CondicionContext):
        print(f"-> condicion(out) {ctx.getText()}")
        if (self.ts.findByKey(str(ctx.getChild(0)))):
            self.ts.ts[self.ts.getDicByKey(str(ctx.getChild(0)))][str(ctx.getChild(0))].used = True
        if (self.ts.findByKey(str(ctx.getChild(2)))):
            self.ts.ts[self.ts.getDicByKey(str(ctx.getChild(2)))][str(ctx.getChild(2))].used = True


    def exitOperacion(self, ctx:compiladoresParser.OperacionContext):
        print(f"-> operacion(out) {ctx.getText()}")
        if (self.ts.findByKey(str(ctx.getChild(0)))):
            self.ts.ts[self.ts.getDicByKey(str(ctx.getChild(0)))][str(ctx.getChild(0))].used = True
        if (self.ts.findByKey(str(ctx.getChild(2)))):
            self.ts.ts[self.ts.getDicByKey(str(ctx.getChild(2)))][str(ctx.getChild(2))].used = True



    def enterBloques(self, ctx:compiladoresParser.BloquesContext):
        self.ts.addContex()
        print(f"->addcontexto")

    def exitBloques(self, ctx:compiladoresParser.BloquesContext):
        self.guardar(self.ts.ts[-1])
        self.ts.removeContex()
        print(f"->removecontexto")





del compiladoresParser