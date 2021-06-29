"""Ejercicio 4
   Construir un algoritmo tal, que dado como dato la 
   calificación de un alumno en un examen, escriba"""

class Tarea4:
    def __init__(self):
        pass
    def Calificacion(self):
        print("____________________________________")
        cal=float(input("Ingrese la calificacion:"))
        if cal >= 7 :
            print("Felicidades haz aprobado!")
        print("____________________________")
        input("enter para salir")
tarea = Tarea4()
tarea.Calificacion()