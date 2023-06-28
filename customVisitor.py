# Generated from /home/marcos/Descargas/dhs/c-compiler/compiladores.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser

# This class defines a complete generic visitor for a parse tree produced by compiladoresParser.

class customVisitor (ParseTreeVisitor):
    tmp = 0 # generador de variables temporales, t<nro>
    label = [] # generador de etiquetas, e<nro>
    """para las funciones se usa una stack,
    se hace push de los argumentos al stack y luego el jump a la funcion.
    del otro lado se hace pop para sacar los args"""

    def get_temp_variable(self):
        temp = 't' + str(self.tmp)
        self.tmp += 1
        return temp
        
    # Visit a parse tree produced by compiladoresParser#programa.
    def visitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        self.f = open("./output/CodigoIntermedio.txt", "w")
        self.f.write("JUMP MAIN \n")
        
        self.visitChildren(ctx)
        self.f.close()


    # Visit a parse tree produced by compiladoresParser#instrucciones.
    def visitInstrucciones(self, ctx:compiladoresParser.InstruccionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#instruccion.
    def visitInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloques.
    def visitBloques(self, ctx:compiladoresParser.BloquesContext):
        # print(f"Bloques")
        # print(f"{ctx.getChild(0).getText()}")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#declaracion_variable.
    def visitDeclaracion_variable(self, ctx:compiladoresParser.Declaracion_variableContext):
        print(f"Declaracion variable: {ctx.getText()}")
    
        tipo = ctx.tipo().getText()
        id = ctx.ID().getText()
        asignacion = ctx.getChild(3)
        if asignacion != None:
            self.f.write(f"{id}={asignacion}\n")
        else:
            # tmp = f"{id}" #creo q esto no va xq es el ID solo
            pass
        return self.visitChildren(ctx)



    # Visit a parse tree produced by compiladoresParser#tipo.
    def visitTipo(self, ctx:compiladoresParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#argumento.
    def visitArgumento(self, ctx:compiladoresParser.ArgumentoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#argumento_proto.
    def visitArgumento_proto(self, ctx:compiladoresParser.Argumento_protoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#prototipado_funcion.
    def visitPrototipado_funcion(self, ctx:compiladoresParser.Prototipado_funcionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#lista_argumento.
    def visitLista_argumento(self, ctx:compiladoresParser.Lista_argumentoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#lista_argumento_proto.
    def visitLista_argumento_proto(self, ctx:compiladoresParser.Lista_argumento_protoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#declaracion_funcion.
    def visitDeclaracion_funcion(self, ctx:compiladoresParser.Declaracion_funcionContext):
        print(f"Declaracion_funcion => {ctx.getChild(1)}")

        tmp = str(ctx.getChild(1).getText()).upper()
        self.f.write(f'{tmp}:\n')
        for child in range(ctx.getChildCount()):
            self.visitChildren(ctx.getChild(child)) # sigue con el procesamiento de los nodos
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#parametros.
    def visitParametros(self, ctx:compiladoresParser.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#llamada_funcion.
    def visitLlamada_funcion(self, ctx:compiladoresParser.Llamada_funcionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#asignacion_variable.
    def visitAsignacion_variable(self, ctx:compiladoresParser.Asignacion_variableContext):
        print(f"Asignacion variable {ctx.getText()}")
        try:
            # para el caso de NUMERO
            numero = ctx.NUMERO().getText()
            # print(f"numero: {numero}")
            self.f.write(ctx.getText() + "\n")
            # self.visitChildren(ctx)
            # self.f.write(str(ctx.getChild(0)) + "=" + {numero} + "\n")
        except:
            # para el caso de OPERACION
            print(f"asig_var caso Operacion")
            pass
        # print(f"fin asignacion variable")
        # self.visitChildren(ctx)
        # self.tmp = 0
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloque.
    def visitBloque(self, ctx:compiladoresParser.BloqueContext):
        print(f"Bloque")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#return_func.
    def visitReturn_func(self, ctx:compiladoresParser.Return_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#condicion.
    def visitCondicion(self, ctx:compiladoresParser.CondicionContext):
        print(f"Condicion {ctx.getText()}")
        try:
            # para el caso de NUMERO
            numero = ctx.NUMERO().getText()
            # print(f"numero: {numero}")
            self.f.write("t" + str(self.tmp) + "=" + ctx.getText() + "\n")
            self.get_temp_variable()
        except:
            # para el caso de condicion o id
            pass
        try:
            # para el caso de ID
            id = ctx.ID()
            self.f.write("t" + str(self.tmp) + "=" + ctx.getText() + "\n")
            self.get_temp_variable()
        except:
            # para el caso de condicion SI o SI
            pass
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloque_if.
    def visitBloque_if(self, ctx:compiladoresParser.Bloque_ifContext):
        print(f"bloque IFFFFF: {ctx.getText()}")
        print(f"visita child2, condicion")
        self.visitCondicion(ctx.getChild(2))
        self.f.write("BEQZ t" + str(self.tmp) + " to " + "e0" + "\n")
        self.visitBloque(ctx.getChild(4))
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloque_if_else.
    def visitBloque_if_else(self, ctx:compiladoresParser.Bloque_if_elseContext):
        """
        <<entrada>>
        if (x>0)
            y = z * 9 - f
        else
            y = z * 9 + g

        <<tac>>
        t0 = x>0           #condicion
        beqz t0 to e0      #ifelse t lbl
                            #children
        t1 = z*9
        t2 = t1-f
        y = t2
        jmp e1            # ifelse
        lbl e0
        t3 = z*9
        t4 = t3+g
        y = t4
        lbl e1
        """
        print(f"IF_ELSE: {ctx.getText()}")
        # print(f"child0: {ctx.getChild(0).getText()}")
        # print(f"if: {ctx.bloque_if().getText()}")
        print(f"visita child0, if")
        # self.visitChildren(ctx.getChild(0)) # manda al IF
        self.visitBloque_if(ctx.getChild(0))
        self.f.write("JUMP e1" + "\n")
        self.f.write("LBL e0" + "\n")
        print(f"visita child2, bloque de else")
        self.visitChildren(ctx.getChild(2)) # manda a bloque else
        self.f.write("LBL e1" + "\n")
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloque_operacional.
    def visitBloque_operacional(self, ctx:compiladoresParser.Bloque_operacionalContext):
        print(f"bloque operacional: {ctx.getText()}")
        # operacion = ctx.operacion().getText()
        # print(f"op: {operacion}")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#operacion.
    # def visitOperacion(self, ctx:compiladoresParser.OperacionContext):

    #     if ctx.getChild(1) == "++":
    #         aux = f"{ctx.getChild(0)} = {ctx.getChild(0)} + 1"
    #     elif ctx.getChild(1) == "--":
    #         aux = f"{ctx.getChild(0)} = {ctx.getChild(0)} - 1"
        

    #     if ctx.getChild()

    #     return self.visitChildren(ctx)
    def visitOperacion(self, ctx:compiladoresParser.OperacionContext):
        """
        <<endrada>>
        int x = 0;
        int y = 5;

        x = y / 5 + y * 10;

        <<tac>>
        x = 0
        y = 5
        t0 = y/5
        t1 = y*10
        t2 = t0 + t1
        x = t2



        p = (x * 6) + x + y;

        p = bloque_operacional + x + y + 6

        t1 = x  * 6
        t2= x + y
        t3 = t2 + 6
        t4 = t1 + t3
        
        left = self.visitChildren(ctx.getChild(0)) #ver si es visit
        right = self.visitChildren(ctx.getChild(2))
        operando = ctx.getChild(1).getText()

        resultado = left operando right



        """
        print(f"operacion: {ctx.getText()}")

        # bloque_op = ctx.bloque_operacional()
        # print(f"bloqueee: {bloque_op}")
        # if (bloque_op == []):
        #     print("bloque op VACIO")
       
        contador = 0
        aux = ctx.getChild(0) # left_operand
        temporales = []
        for i in range(2, ctx.getChildCount(), 2):
            operator = ctx.getChild(i - 1).getText()
            right_operand = ctx.getChild(i)

            if (len(temporales) == 0):
                result = f"{aux}{operator}{right_operand}"
                self.f.write("t" + str(self.tmp) + "=" + result + "\n")
                temporales.append(self.tmp)
                self.tmp = self.tmp + 1
            else:
                result = f"t{temporales[-1]}{operator}{right_operand}"
                self.f.write("t" + str(self.tmp) + "=" + result + "\n")
                temporales.append(self.tmp)
                self.tmp = self.tmp + 1
        
        temporales.clear();

        # var = self.visitChildren(ctx)
        # print(f"AAAAAAAAAAAAAAAAAAA{var}")
        # try:
        return result
        # except:
            # pass

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



"""
<<entrada>>
for (x=0; x<10; x++)
    y = z*x

<<tac>>
x=0
lbl e0 #etiqueta para poder volver en cada iteracion
t0 = x<10
beqz t0 to e1
y = z*x
x = x+1
jmp e0
lbl e1
"""
"""
<<entrada>>
int calcular (int x, int y){
    reutnr x+y;
}
...
z = calcular(x,y);

<<tac>>
lbl e0 #etiqueta a la funcion
pop e1 #en el stack saco la etiqurta de donde me llamaron
pop y  # saco los argumentos de la pila, el primero en salir es y
pop x 
t0 = x+y
push t0
jmp e1

...
push x
push y
push e1
jmp e0
lbl e1
pop z # resultados
"""