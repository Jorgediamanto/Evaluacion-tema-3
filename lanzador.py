import sys

def lanzador():
    a = int(input("Que apartado desea resolver? \n Ejercicio 1 \n Ejercicio 2: "))

    if a == 1:
        import ejercicios.ev3ej1
        lanzador()

    elif a == 2:
        import ejercicios.ev3ej2
        lanzador

    else:
        sys.exit()

lanzador()