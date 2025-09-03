from antlr4 import *
from FiboLexer import FiboLexer
from FiboParser import FiboParser

def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)

def main():
    entrada = InputStream(input("Ingresa operación (ej: FIBO(8)): "))
    lexer = FiboLexer(entrada)
    tokens = CommonTokenStream(lexer)
    parser = FiboParser(tokens)
    tree = parser.prog()

    texto = entrada.getText(5, entrada.size-2)  # número entre paréntesis
    n = int(texto)
    seq = [fib(i) for i in range(n)]
    print("FIBO(", n, ") =", ", ".join(map(str, seq)))

if __name__ == "__main__":
    main()

