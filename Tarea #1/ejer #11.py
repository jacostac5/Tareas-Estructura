"""Ejercicio 11

Una escuela aplica dos exámenes a sus aspirantes, por lo 
que cada uno de ellos obtiene dos calificaciones denotadas
como C1 y C2. El aspirante que obtenga una calificación mayor
que 90 en cualquiera de los exámenes es aceptado; en caso contrario es rechazado."""

class Tarea11:
    def __init__ (self):
        pass
    def Variables(self):
        print("____________________________________")
        C1= float(input("Ingrese la primer Calificacion: "))
        C2= float(input("Ingrese la segunda Calificacion: "))
        print("____________________________________")
        if C1>=90 or C2>=90:
            print(("Sus calificaciones son: {} , {} ").format(C1,C2))
            print("haz sido aceptado!",)
        else:
            print(("Sus calificaciones son: {} , {} ").format(C1,C2))
            print("haz sido rechazado!")
        print("____________________________________")
        input("enter para salir") 
        
resultado = Tarea11()
resultado.Variables()