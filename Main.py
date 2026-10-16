from antlr4 import InputStream, CommonTokenStream
from forLexer import forLexer
from forParser import forParser
from EvalVisitor import EvalVisitor

def ejecutar(codigo):
    lexer = forLexer(InputStream(codigo))
    tokens = CommonTokenStream(lexer)
    parser = forParser(tokens)
    tree = parser.prog()
    EvalVisitor().visit(tree)

if __name__ == "__main__":
    ejecutar("for 1 to 5 imprime 0")