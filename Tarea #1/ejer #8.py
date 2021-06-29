"""Ejercicio 8

Leer tres números enteros diferentes entre sí y 
determinar el número mayor de los tres."""

class Tarea8:
    def __init__ (self):
        pass
    def NumeroMayor(self):
        print("______________________________________")
        n1= int(input("Ingrese primer numero entero: "))
        n2= int(input("Ingrese segundo numero entero: "))
        n3= int(input("Ingrese tercer numero entero: "))
        print("______________________________________")
        if n1>n2 and n1>n3:
            nM=n1
        else:
            if n2>n3:
                nM=n2
            else:
                nM=n3
        print("El numero mayor es:",nM)
        print("_____________________________________")
        input("enter para salir") 
objeto = Tarea8()
objeto.NumeroMayor()