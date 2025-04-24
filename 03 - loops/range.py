import os
os.system("cls")

###
#  03 - range()
#  Permite crear una secuencia de numeros. Muy util para for, pero no solo para eso
###


print("\nrange():")

nums=range(5) #NO CREA UNA LISTA
print(type(nums)) #class 'range'

#range(inicio,fin)

#Genera una secuencia de numeros de 0 a 10
for num in range(10): ## range(10) = range(0,10)
   print(num)

#Genera una secuencia de numeros del 2 al 8    
for num in range(2,4):
    print(num)

#range(inicio,fin,paso)
for i in range(0,4,2): #Devuelve (0,2,4,6,8) NO INCLUYE EL 10
     print (i)

for i in range(-4,0): #se puede tener numeros negativos
     print(i)

for i in range(3,0,-1): #es util para hacer cuentas regresivas
     print(i)

nums=range(0,15,2)
#para pasar de rango a lista se utiliza el metodo list() 
list_of_nums=list(nums)
print(list_of_nums, type(list_of_nums))
print(nums, type(nums))

# para hacer x veces algo
### con while:
contador=5
while contador>0:
    print("hago esto cinco veces")
    contador-=1
    
###Con range():
for _ in range(5):
    print("\nhago esto 5 veces mas. Con range()")