"""Ejercicio 6:

Dado el sueldo de un empleado, encontrar el nuevo sueldo si obtiene un aumento 
del 10% si su sueldo es inferior a $600, en caso contrario no tendrá aumento."""

class Tarea6:
    def __init__(self):
        pass
    def Calcular(self):
        print("___________________________________")
        SUELDO=float(input("Sueldo de los empleados:"))
        if SUELDO < 600:
            NS=SUELDO + SUELDO*0.1
            print()
        else:
            NS=SUELDO
            print()
        print("___________________________________")    
        print(NS)
        print("___________________________________")
        input("enter para salir")

tarea=Tarea6()
tarea.Calcular()
