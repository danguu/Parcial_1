def es_letra(ch):
    return ('a' <= ch <= 'z') or ('A' <= ch <= 'Z')

def es_digito(ch):
    return '0' <= ch <= '9'

def afd(cadena):
    if cadena == "":
        return False
    if not es_letra(cadena[0]):
        return False
    for ch in cadena[1:]:
        if not (es_letra(ch) or es_digito(ch)):
            return False
    return True

tests = ["hola", "X1", "abc123", "1casa", "_var"]
for pan in tests:
    print(pan, "=>", "ACEPTA" if afd(pan) else "RECHAZA")

