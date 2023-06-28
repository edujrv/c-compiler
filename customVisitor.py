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
    cont_lbl = 0
    """para las funciones se usa una stack,
    se hace push de los argumentos al stack y luego el jump a la funcion.
    del otro lado se hace pop para sacar los args"""
    aux_if = 'else'

    def get_temp_variable(self):
        self.tmp += 1
        temp = 't' + str(self.tmp)
        return temp

    def get_lbl_variable(self):
        self.cont_lbl += 1
        return self.cont_lbl
        
    # Visit a parse tree produced by compiladoresParser#programa.
    def visitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        self.f = open("./output/CodigoIntermedio.txt", "w")
        self.f.write("JUMP MAIN ")
        
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
            print(f"AAAAAA{ctx.getText()} => {asignacion.getChildCount()}")
            if asignacion.getChildCount() == 4:
                # FUNCION
                print("ES FUNCION")
                print(f"AAAAAA{ctx.getText()} => {asignacion.getChildCount()}")
                self.f.write(f"\n{id} = ")
                return self.visitChildren(ctx)

            else:
                # self.f.write(f"\n{id}={asignacion}")
                try:
                    # para el caso de NUMERO
                    numero = ctx.NUMERO().getText()
                    
                    # print(f"numero: {numero}")
                    self.f.write(f"\n{id} = {numero}")
                    # self.visitChildren(ctx)
                    # self.f.write(str(ctx.getChild(0)) + "=" + {numero} + "\n")
                except:
                    # para el caso de OPERACION
                    print(f"asig_var caso Operacion")
                    self.visitChildren(ctx)
                    return self.f.write(f"\n{id} = t{self.tmp-1}")
                # self.visitChildren(ctx)
                # return self.f.write(f"\n{id} = t{self.tmp}")
        else:
            # tmp = f"{id}" #creo q esto no va xq es el ID solo
            pass
        self.visitChildren(ctx)
        



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
        self.f.write(f'\n{tmp}:')
        for child in range(ctx.getChildCount()):
            self.visitChildren(ctx.getChild(child)) # sigue con el procesamiento de los nodos
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#parametros.
    def visitParametros(self, ctx:compiladoresParser.ParametrosContext):
        self.f.write(f', {ctx.getChild(0)}')

        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#llamada_funcion.
    def visitLlamada_funcion(self, ctx:compiladoresParser.Llamada_funcionContext):
        # tmpAux = f"t{self.tmp}"
        self.f.write(f'call {ctx.getChild(0)}')

        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#asignacion_variable.
    def visitAsignacion_variable(self, ctx:compiladoresParser.Asignacion_variableContext):
        # print(f"Asignacion variable {ctx.getText()}")
        # try:
        #     # para el caso de NUMERO
        #     numero = ctx.NUMERO().getText()
        #     # print(f"numero: {numero}")
        #     self.f.write("\n" + ctx.getText())
        #     # self.visitChildren(ctx)
        #     # self.f.write(str(ctx.getChild(0)) + "=" + {numero} + "\n")
        # except:
        #     # para el caso de OPERACION
        #     print(f"asig_var caso Operacion")
        #     pass
        # # print(f"fin asignacion variable")
        # # self.visitChildren(ctx)
        # # self.tmp = 0
        # return self.visitChildren(ctx)
        print(f"Asignacion variable: {ctx.getText()}")
        # print(f"Asignacion variable: {ctx.getChild(2)}")
    
        id = ctx.getChild(0)
        asignacion = ctx.getChild(2)
        if asignacion != None:
            print(f"AAAAAA   ASIGNACIOOOOOOOOOOOON {ctx.getText()} => {asignacion.getChildCount()}")
            if asignacion.getChildCount() == 4:
                # FUNCION
                print("ES FUNCION ASIGNACIOOOOOOOOOOOON")
                print(f"AAAAAA{ctx.getText()} => {asignacion.getChildCount()}")
                self.f.write(f"\n{id} = ")
                return self.visitChildren(ctx)

            # elif asignacion.getChildCount() == 3:
            else:
                try:
                    # para el caso de NUMERO
                    print(f"asig_var caso Numero")
                    numero = ctx.NUMERO().getText()
                    self.f.write(f"\n{id} = {numero}")
                except:
                    # para el caso de OPERACION
                    print(f"asig_var caso Operacion")
                    self.visitChildren(ctx)
                    return self.f.write(f"\n{id} = t{self.tmp-1}")
        else:
            # tmp = f"{id}" #creo q esto no va xq es el ID solo
            pass
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloque.
    def visitBloque(self, ctx:compiladoresParser.BloqueContext):
        print(f"Bloque")
        self.visitChildren(ctx)
        # self.f.write("LBL bloque e1" + "\n")

    # Visit a parse tree produced by compiladoresParser#return_func.
    def visitReturn_func(self, ctx:compiladoresParser.Return_funcContext):
        print(f"RETURN: {ctx.getText()}")
        try:
            #caso operacion
            self.visitChildren(ctx)
            operacion = ctx.operacion().getText()
            self.f.write(f"\nreturn t{self.tmp-1}")
        except:
            pass
        try:
            id = ctx.ID().getText()
            self.f.write(f"\nreturn {id}")
        except:
            pass
        try:
            numero = ctx.NUMERO().getText()
            self.f.write(f"\nreturn {numero}")
        except:
            pass
        try:
            true = ctx.TRUE().getText()
            self.f.write(f"\nreturn {true}")
        except:
            pass
        try:
            false = ctx.FALSE().getText()
            self.f.write(f"\nreturn {false}")
        except:
            pass
        if (ctx.getChildCount() == 2):
            #caso return;
            self.f.write(f"\nreturn")


    # Visit a parse tree produced by compiladoresParser#condicion.
    def visitCondicion(self, ctx:compiladoresParser.CondicionContext):
        print(f"Condicion {ctx.getText()}")
        try:
            # para el caso de NUMERO
            numero = ctx.NUMERO().getText()
            # print(f"numero: {numero}")
            self.f.write("\nt" + str(self.tmp) + "=" + ctx.getText())
            self.get_temp_variable()
        except:
            # para el caso de condicion o id
            pass
        try:
            # para el caso de ID
            id = ctx.ID()
            self.f.write("\nt" + str(self.tmp) + "=" + ctx.getText())
            self.get_temp_variable()
        except:
            # para el caso de condicion SI o SI
            pass
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloque_if.
    def visitBloque_if(self, ctx:compiladoresParser.Bloque_ifContext):
        if ( ctx.getText() != 'else' and self.aux_if == 'if'):
            print(f"bloque IFFF, de ifelse: {ctx.getText()}")
            print(f"visita child2, condicion")
            self.visitCondicion(ctx.getChild(2))
            self.f.write("\nBEQZ t"+str(self.tmp) + " to " + "e"+str(self.cont_lbl))
            self.label.append(self.cont_lbl)
            self.get_lbl_variable()
            self.aux_if = 'else'
            self.visitBloque(ctx.getChild(4))

        elif ( ctx.getText() != 'else' and self.aux_if == 'else' ):
            print(f"bloque IF SOLO: {ctx.getText()}")
            print(f"visita child2, condicion")
            self.visitCondicion(ctx.getChild(2))
            self.f.write("\nBEQZ t"+str(self.tmp) + " to " + "e"+str(self.cont_lbl))
            self.label.append(self.cont_lbl)
            self.get_lbl_variable()
            self.visitBloque(ctx.getChild(4))
            self.f.write("\nLBL e"+str(self.label[0]))
            self.label.pop(0)
            print(f"label: {self.label}")
            print(f"contador_lbl: {self.cont_lbl}")
       
        if ( ctx.getText() == 'else'):
            self.aux_if = 'if'
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
        print(f"visita child0, if")
        self.visitBloque_if(ctx.getChild(1)) #mando ELSE a if
        self.visitBloque_if(ctx.getChild(0)) # mando a IF sus cosas
        # self.f.write("BEQZ t"+str(self.tmp) + " to " + "e"+str(self.cont_lbl) + "\n")
        self.f.write("\nJUMP e"+str(self.cont_lbl))
        self.label.append(self.cont_lbl)
        self.get_lbl_variable()
        self.f.write("\nLBL e"+str(self.label[0]))
        self.label.pop(0)
        print(f"visita child2, bloque de else")
        self.visitChildren(ctx.getChild(2)) # manda a bloque else
        self.f.write("\nLBL e"+str(self.label[0]))
        self.label.pop(0)
        print(f"label: {self.label}")
        print(f"contador_lbl: {self.cont_lbl}")
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

        # print(f"getchildren1: {ctx.getChild(1)}")
        if str(ctx.getChild(1)) == "++":
            result = f"\n{aux} = {aux} + 1"
            self.f.write(result)
        if str(ctx.getChild(1)) == "--":
            result = f"\n{aux} = {aux} - 1"
            self.f.write(result)
        else:

            for i in range(2, ctx.getChildCount(), 2):
                operator = ctx.getChild(i - 1).getText()
                right_operand = ctx.getChild(i)

                if (len(temporales) == 0):
                    result = f"{aux}{operator}{right_operand}"
                    self.f.write("\nt" + str(self.tmp) + "=" + result)
                    temporales.append(self.tmp)
                    self.tmp = self.tmp + 1
                else:
                    result = f"t{temporales[-1]}{operator}{right_operand}"
                    self.f.write("\nt" + str(self.tmp) + "=" + result)
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
        """  FOR PAR_ABRE (declaracion_variable | asignacion_variable)? PYC condicion? PYC operacion? PAR_CIERRE bloque
        
            for (int i = 0; i <= 5; i++) {
                 int x = 0;
            }

            i=0
            lbl e0 #empieza for
            breq ***condicion*** e1
            ... bloque ...
            t5=i+1
            i=t5
            jump e0
            lbl e1
        """
        print(f"FOR: {ctx.getText()}")
        #asignacion o declaracion variable
        try:
            self.visitDeclaracion_variable(ctx.getChild(2))
        except:
            self.visitAsignacion_variable(ctx.getChild(2))
        self.f.write("\nLBL e"+str(self.cont_lbl)) #etiqueta de start for
        self.label.append(self.cont_lbl)
        self.get_lbl_variable()

        self.visitCondicion(ctx.getChild(4)) #condicion del for
        self.f.write("\nBEQZ t"+str(self.tmp) + " to " + "e"+str(self.cont_lbl))
        self.label.append(self.cont_lbl)
        self.get_lbl_variable()

        self.visitBloque(ctx.getChild(8)) #visita bloque del for (resto del code)

        self.visitOperacion(ctx.getChild(6)) #visita operacion

        self.f.write("\nJUMP e"+str(self.label[0])) #salto a start for
        self.label.pop(0)
        self.f.write("\nLBL e"+str(self.label[0])) #label end for
        self.label.pop(0)
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloque_while.
    def visitBloque_while(self, ctx:compiladoresParser.Bloque_whileContext):
        """bloque_while:      WHILE PAR_ABRE condicion PAR_CIERRE bloque
            
            while(x>0){
                y = 5;
            }

            lbl e0 #empieza el while
            t0=x>0
            beqz ****comparacion*** e1
            ....while
            jump e0
            lbl e1 #sale del while
        """
        print(f"WHILE: {ctx.getText()}")
        self.f.write("\nLBL e"+str(self.cont_lbl)) #etiqueta de start while
        self.label.append(self.cont_lbl)
        self.get_lbl_variable()

        self.visitCondicion(ctx.getChild(2)) #condicion del while
        self.f.write("\nBEQZ t"+str(self.tmp) + " to " + "e"+str(self.cont_lbl))
        self.label.append(self.cont_lbl)
        self.get_lbl_variable()

        self.visitBloque(ctx.getChild(4)) #visita bloque del while (resto del code)

        self.f.write("\nJUMP e"+str(self.label[0])) #salto a start while
        self.label.pop(0)
        self.f.write("\nLBL e"+str(self.label[0])) #label end while
        self.label.pop(0)
        # return self.visitChildren(ctx)


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