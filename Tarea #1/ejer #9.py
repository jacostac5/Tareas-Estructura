"""Ejercicio 9

Diseñar un algoritmo tal que dados como datos
dos variables de tipo entero, obtenga el resultado 
de la siguiente función:"""

class Tarea9:
    def __init__ (self):
        pass
    def Variables(self):
        print("__________________________________")
        NUM= int(input("Ingrese el primer variable: "))
        V= int(input("Ingrese el segunda Variable: "))
        print("__________________________________")
        if NUM== 1:
            Resp=100*V
        elif NUM==2:
            Resp=pow(100,V)
        elif NUM==3:
            Resp=100/V
        else:
            Resp=0
                
        print("Su resultado es:",Resp)
        print("__________________________________")
        input("enter para salir") 
resultado = Tarea9()
resultado.Variables()