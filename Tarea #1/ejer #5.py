"""Ejercicio 5:
 Dado como dato la calificación de un alumno en un examen, 
 escriba “aprobado” si su calificación es mayor o igual que 7 
 y “Reprobado” en caso contrario."""

class Tarea5:
    def __init__(self):
        pass
    def Calcular(self):
        print("____________________________________")
        cal=float(input("Ingrese la calificacion:"))
        if cal >= 7 :
            print()
            print("Felicidades haz aprobado!")
        else:
            print()
            print("Que mal , haz reprobado !")
        print("____________________________________")
        input("enter para salir")

tarea = Tarea5()
tarea.Calcular()