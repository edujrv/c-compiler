import sys
from antlr4 import *
from compiladoresLexer  import compiladoresLexer
from compiladoresParser import compiladoresParser
from compiladoresListener import compiladoresListener
from customListener import customListener
from customVisitor import customVisitor


def main(argv):
    archivo = "input/entrada.c"
    if len(argv) > 1 :
        archivo = argv[1]
    input = FileStream(archivo)
    lexer = compiladoresLexer(input)
    stream = CommonTokenStream(lexer)
    parser = compiladoresParser(stream)
    print(f"********** START LISTENER ***********")
    listener = customListener()
    parser.addParseListener(listener)
    # tree = parser.s()
    tree = parser.programa()
    print(f"********** END LISTENER ***********")
    print(f"********** START VISITOR ***********")
    visitor = customVisitor()
    visitor.visitPrograma(tree)
    print(f"********** END VISITOR ***********")
    # visitor.visit(tree)
    
    # print(tree.toStringTree(recog=parser)) #esto seria el compiladores

if __name__ == '__main__':
    main(sys.argv)