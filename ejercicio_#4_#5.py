#comentario #1
#desarrolladores 
#Jhon Sleyder Amesquita
#David Esteban Patiño

#este codigo lo que hace es decirle al usuario que ingrese ciertas palabras para guardarlo en una lista 

palabras_ordenadas=str


palabras=[]
palabra=input("ingrese la palabra ")

for i in range(0,5):
    
    palabra=input("ingrese la palabra ")
    palabras.append(palabra)
    i+1
print(f"palabras de la lista {palabras}")

#comentario #2
#este codigo lo que hace es organizar de creciente a decreciente

def ordenar_por_tamaño(palabras):
    return sorted(palabras,key=len,reverse=True)

#comentario #3
#este codigo le da unas opciones de seleccion al usuario para hacer una funcion

while True:  
 print("\n selecione una opcion")
 print("1.Orden alfabetico")
 print("2.orden de tamaño,de la mas larga a la mas corta")
 print("3.orden aleatorio")
 print("4.ordenar inverso al ingresado")
 print("5.orden igual al ingresado")
 print("6.salir")
    
 seleccion=int(input(print("elija una opcion ")))
    
 match seleccion:
      case 1:
        palabras_ordenadas=sorted(palabras)
      case 2:
        palabras_ordenadas=ordenar_por_tamaño(palabras)
      case 3:
        import random
        random.shuffle(palabras)
        palabras_ordenadas=palabras
      case 4:
        palabras_ordenadas=list(reversed(palabras))
      case 5:
        palabras_ordenadas=palabras
      case 6:
        break;
      case _:
        print("opcion no valida.Elija una opcion de 1 a 6.")
        
        
        
#comentario #4
#este codigo mustra el resultado dependiendo la seleccion 

 print(f"ordenado segun la opcion anterior {palabras_ordenadas}")






    





