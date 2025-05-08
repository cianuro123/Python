import os
os.system("cls")

# Repite indefinidamente el codigo mientras se cumpla una condicion

print("Bucle while")

contador = 0

#while contador <= 5:
 #   print(contador)
   # contador += 

print("While con break")
while True:
    print(contador)
    contador+=1
    if contador == 5:
        print("Fin del bucle")
        break
    
# continue lo que hace es saltar a la siguiente iteracion para continuar con el bucle (ignorando el codigo intermedio)
print("\nBucle con continue")
contador = 0
while contador <10:
    contador+=1
    
    if contador%2==0:
        continue
    print(contador)
#cadaa vez que sea par, el "continue" saltará todo el codigo hasta llegar a la siguiente iteracion.
#en este caso, si el continue es true, el print es ignorado para ir directo al bucle while
#aunque este esté dentro del bucle.
    

print("\nElse en While")

contador=0
while contador<10:
    print(contador)
    contador+=1
    break
else:
    print("fin del bucle")
    
#El else no se ejecuta si hay un break dentro del while
numero=-1
while numero<0:
    try: 
#"try" es un antierrores, sirve para envolver el codigo problematico. Entonces, si falla, no cierra el programa
        numero = int(input("Escribe un numero: "))
        if numero < 0:
            print("El numero debe ser positivo. Reintenta")
            
    except: #aqui se produce la falla y en vez de cerrarse el programa se hará lo que este dentro del except
        print("lo que introduces debe ser un numero")
print(f"tu numero es {numero}")    
