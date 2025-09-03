def afd(cadena):
    estado = 0
    for ch in cadena:
        if estado == 0:
            if ch == 'a':
                estado = 0
            elif ch == 'b':
                estado = 1
            elif ch == 'c':
                estado = 2
            else:
                return False
        elif estado == 1:
            if ch == 'b':
                estado = 1
            elif ch == 'c':
                estado = 2
            else:
                return False
        elif estado == 2:
            if ch == 'c':
                estado = 2
            else:
                return False
    return True
    
for siu in ["", "aaa", "aabbcc", "bbccc", "cc", "acb"]:
    print(siu, "=>", "ACEPTA" if afd(siu) else "RECHAZA")

