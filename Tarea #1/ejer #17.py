"""Ejercicio 17

Determinar si un número entero proporcionado por 
el usuario es primo. Un número primo es un entero 
que no tiene más divisores que él mismo y la unidad."""

class Tarea17:
    def __init__ (self):
        pass
    def Variables(self):
        print("___________________________") 
        serie= 0
        l=1
        n=int(input("ingrese un numero para la serie: "))
        band='T'
        while l>n:
            if band=='T':
                serie=serie+(1/l)
                band=='F'
            else:
                serie=serie-(1/l)
                band=='T'
            l=l+1

                  
        print("________________________________")
        input("enter para salir") 
        
resultado = Tarea17()
resultado.Variables()