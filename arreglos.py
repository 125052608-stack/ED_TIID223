""" 
#Declaran un arreglo
numeros=[10,20,30,40,50]

#Imprimir el tercer elemento del arreglo
print(numeros[2])

#Modificar el cuarto elemento del arreglo  
numeros[3]=15
print(numeros)

#Agregar un elemento al final del arreglo
numeros.append(60)
print(numeros) 

#Eliminar el segundo elemento del arreglo
numeros.pop(1)
print(numeros)

#Eliminar un elemento por valor
numeros.remove(30)
print(numeros) """

frutas=["Mango","Manzana","Uva","Pera","Maracuya"]

frutas.remove("Uva")
print(frutas)

frutas.pop(2)
print(frutas)

frutas.append("Kiwi")
print(frutas)

frutas[2]="Piña"
print(frutas)

arreglo=[]
#input aparece en terminal
n = int(input("Ingrese el tamaño del arreglo: "))
n1 = int(input("Ingrese el primer elemento del arreglo: "))
arreglo.append(n1)
print(arreglo)

