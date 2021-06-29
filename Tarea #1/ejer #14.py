"""Ejercicio 14

Diseñe un pseudocódigo para calcular
la suma y producto de N números enteros, 
utilizando un bucle controlado por el usuario.."""

class Tarea14:
    def __init__ (self):
        pass
    def Variables(self):
        print("_______________________________")

        prod=1
        suma=0
        resp=input(str("Quieres ingresar numeros?  (S/N)"))
        print("_______________________________")
        while resp != "n" and resp!= "N":
            
            num=int(input("Ingrese un numero: "))
            print("___________________________")
            suma=suma+num
            prod=prod*num
            resp=input(str("Desea continuar? (S/N)"))
            print("__________________________")
        print("""El promedio de la es:""",suma,"""
El total del producto es: """,prod)
          
        print("_______________________________________")
        input("enter para salir") 
        
resultado = Tarea14()
resultado.Variables()