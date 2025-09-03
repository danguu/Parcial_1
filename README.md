# Parcial_1

## Pregunta 1

**Archivo:** `afd_abc.py`
**Ejecución:**

```bash
python3 afd_abc.py
```
Pruebas incluidas en el código.

## Pregunta 2

**Expresión regular de identificadores:**

**Archivo:** `afd_id.py`
**Ejecución:**

```bash
python3 afd_id.py
```
Ya con las pruebas en el código

## Pregunta 3

**Calculadora raíz cuadrada con flex y bison**.

* **Archivo léxico:** `calc.l`
* **Archivo sintáctico:** `calc.y`

**Compilación:**

```bash
flex calc.l
bison -d calc.y
gcc lex.yy.c calc.tab.c -o calc -lm
```

**Ejecución:**

```bash
./calc 
```


## Pregunta 4

**Comparación rendimiento compilado vs interpretado** 
* **C compilado:** `fib.c`

```bash
gcc fib.c -o fib
time ./fib
```

* **Python interpretado:** `fib.py`

```bash
time python3 fib.py
```
<img width="756" height="329" alt="image" src="https://github.com/user-attachments/assets/f67ac920-94c3-4818-9a9f-22d1889b01af" />


**Observación:** C es más rápido porque es compilado, Python más lento porque es interpretado.

## Pregunta 5

**ANTLR – Fibonacci**

* **Gramática:** `Fibo.g4`
* **Programa principal:** `test.py`

**Generar el parser:**

```bash
antlr4 -Dlanguage=Python3 Fibo.g4
```

**Ejecutar:**

```bash
python3 test.py
```

Ejemplo de uso:

```
Ingresa operación (ej: FIBO(8)): FIBO(8)
FIBO( 8 ) = 0, 1, 1, 2, 3, 5, 8, 13
```
