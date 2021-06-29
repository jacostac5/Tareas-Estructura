"""Ejercicio 2:
En una tienda se ofrece un descuento del 15% sobre el 
total de la compra y un cliente desea saber cuánto deberá 
pagar finalmente por su compra."""
class Tarea2:
    def __init__(self):
        pass
    def Calcular(self):

        print("_______________________________________")
        TC=float(input("Ingrese el total de la compra:"))
        D=TC*0.15
        CP=TC-D
        print()
        print("La cantidad a pagar es: ")
        print("$",CP)
        print("___________________________________")
        input("enter para salir")

tarea = Tarea2()
tarea.Calcular()