import sys

def lanzador():
    a = int(input("Que apartado desea resolver? \n Ejercicio 1 \n Ejercicio 2: "))

    if a == 1:
        import ejercicios.EJ1.ev3ej1
        lanzador()

    elif a == 2:
        import ejercicios.EJ2.ev3ej2
        lanzador()
    elif a == 3:
        import ejercicios.EJ3.ev3ej3
        lanzador()
    elif a == 4:
        import ejercicios.EJ4.ev3ej4
        lanzador()
    elif a == 5:
        import ejercicios.EJ5.ev3ej5
        lanzador()

    else:
        sys.exit()

lanzador()