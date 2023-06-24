import sys
from antlr4 import *
from compiladoresLexer  import compiladoresLexer
from compiladoresParser import compiladoresParser
from compiladoresListener import compiladoresListener
from customListener import customListener


def main(argv):
    archivo = "input/entrada.c"
    if len(argv) > 1 :
        archivo = argv[1]
    input = FileStream(archivo)
    lexer = compiladoresLexer(input)
    stream = CommonTokenStream(lexer)
    parser = compiladoresParser(stream)
    #antes de construir el parseo armamos el listener
    listener = customListener()
    parser.addParseListener(listener)
    # tree = parser.s()
    tree = parser.compiladores()
    # print(tree.toStringTree(recog=parser)) #esto seria el compiladores

if __name__ == '__main__':
    main(sys.argv)