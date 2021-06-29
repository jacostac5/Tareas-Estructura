"""Ejercicio 16

Determinar si un número entero proporcionado por 
el usuario es primo. Un número primo es un entero 
que no tiene más divisores que él mismo y la unidad."""

class Tarea16:
    def __init__ (self):
        pass
    def Variables(self):
        print("____________________________") 
        primo= 0
        divisor=2
        num=int(input("ingrese un numero entero : "))
        print("____________________________")
    
        while divisor < num and primo ==0 :
            Res= num%divisor
            print(Res)
            if Res == 0:
                primo+=1
            divisor+=1
        if primo ==0:
            print("El numero",num,"es primo")
        else:
            print("El numero",num,"no es primo")
                       
            print("___________________________")
                  
        print("_________________________")
        input("enter para salir") 
        
resultado = Tarea16()
resultado.Variables()