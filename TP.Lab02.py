from itertools import product, permutations, combinations, combinations_with_replacement

# Ejercicio -3
# Realice un programa de python que genere las sucesiones decimales de 4 digitos, donde el 0 está permitido colocarlo
# del lado izquierdo
print("Ejercicio -3.")

#El conjunto de digitos con el que se trabaja
digits = "0123456789"

#a. Genere las sucesiones de 4 digitos diferentes e imprima su conteo
print("a. Genere las sucesiones de 4 digitos diferentes e imprima su conteo")

#Genera una lista de tuplas con todas las sucesiones de 4 digitos sin repeticiones
permutacionces_ej3 = list(permutations(digits, 4))

#Imprime la longitud de la lista
print("Conteo: " + str(len(permutacionces_ej3)))

#b. Genere las sucesiones de 4 digitos que contengan uno o mas digitos repetidos e imprima su conteo
print("b. Genere las sucesiones de 4 digitos que contengan uno o mas digitos repetidos e imprima su conteo")
#Genera la lista con todas las combinaciones posibles de 4 digitos permitiendo repeticiones
sucesiones_ej3 = list(product(digits, repeat=4))

# Verifica si hay repeticiones. Crea una lista y un set con los elementos de la tupla, si la cantidad de elementos
# difiere es porque al menos uno se repite.
def tiene_repeticiones(tuple):
    temp_list = list(tuple)
    if len(temp_list) == len(set(temp_list)):
        return False
    else:
        return True

# Crea una lista de las tuplas que tiene repeticiones.
def sucesiones_con_repeticion(tuple_list):
    to_return = []
    for tuple in tuple_list:
        if tiene_repeticiones(tuple):
            to_return.append(tuple)
    return to_return

print("Conteo: " + str(len(sucesiones_con_repeticion(sucesiones_ej3))))

#c. Imprima el conteo de elementos por cada una de las siguientes divisiones
print("c. Imprima el conteo de elementos por cada una de las siguientes divisiones")

#Utiliza la diferencia en cantidad de elementos de sets y listas de los elementos de la tupla para determinar el
# tipo de repeticiones. Retorna 3 si un elemento se repite 4 veces, 1 si un elemento se repite 2 veces y los demas
# son unicos, 2 si dos elementos se repiten 2 veces y 4 si un elemento se repite 3 veces.
def tipo_de_repeticiones(tuple):
    temp_list = list(tuple)
    if len(temp_list) - len(set(temp_list)) == 2:
        if temp_list.count(temp_list[0]) == 2:
            return 2
        else:
            return 4
    else:
        return len(temp_list) - len(set(temp_list))

#1. Se repite el digito 4 veces
print("1. Se repite el digito 4 veces")

#Retorna la lista de tuplas donde un elemento se repite 4 veces
def ejercicio_c1(tuple_list):
    to_return = []
    for tuple in tuple_list:
        if tipo_de_repeticiones(tuple) == 3:
            to_return.append(tuple)
    return to_return
print("Conteo: " + str(len(ejercicio_c1(sucesiones_con_repeticion(sucesiones_ej3)))))

#2. Se repiten dos digitos dos veces cada uno
print("2. Se repiten dos digitos dos veces cada uno")

#Retorna la lista de tuplas donde se repiten dos digitos dos veces cada uno
def ejercicio_c2(tuple_list):
    to_return = []
    for tuple in tuple_list:
        if tipo_de_repeticiones(tuple) == 2:
            to_return.append(tuple)
    return to_return

print("Conteo: " + str(len(ejercicio_c2(sucesiones_con_repeticion(sucesiones_ej3)))))

#3. Se repite un elemento dos veces y los otros no se repiten
print("Se repite un elemento dos veces y los otros no se repiten")

#Retorna la lista de tuplas donde se repite un elemento y los otros no se repiten
def ejercicio_c3(tuple_list):
    to_return = []
    for tuple in tuple_list:
        if tipo_de_repeticiones(tuple) == 1:
            to_return.append(tuple)
    return to_return

print("Conteo: " + str(len(ejercicio_c3(sucesiones_con_repeticion(sucesiones_ej3)))))

#4. Se repite un digito 3 veces y el otro no se repite
print("4. Se repite un digito 3 veces y el otro no se repite")

#Retorna la lista de tuplas donde se repite un elemento 3 veces y el otro no se repite
def ejercicio_c4(tuple_list):
    to_return = []
    for tuple in tuple_list:
        if tipo_de_repeticiones(tuple) == 4:
            to_return.append(tuple)
    return to_return

print("Conteo: " + str(len(ejercicio_c4(sucesiones_con_repeticion(sucesiones_ej3)))))

#Ejercicio -2

print("Ejercicio -2. Números primos de 1-100 utilizando inclusión - exclusión")

#Primos utilizando inclusion y exclusion

numeros = list(range(2,101))

#Funcion para obtener un set de multiplos de un numero
def multiplos_de(num):
    return set(i for i in numeros if (i%num==0 and i!=num))

#Se crean sets para los conjuntos de numeros multiplos de 2,3,5,7
dos = multiplos_de(2)
tres = multiplos_de(3)
cinco = multiplos_de(5)
siete = multiplos_de(7)

#Principio de inclusion exclusion, los numeros que NO cumplen la condicion de ser primos son igual al complemento
#de los numeros que cumplen cualquiera de las condiciones
numeros_primos = set(numeros) - (dos | tres | cinco | siete)

print(numeros_primos)
print("Conteo: " + str(len(numeros_primos)))

#Ejercicio 0

print("Ejercicio 0.")
n=7
m=5
k=0
digits = "1234567"

for i1 in range(1,n+1):
    for i2 in range(1,i1+1):
        for i3 in range(1,i2+1):
            for i4 in range(1,i3+1):
                for i5 in range(1,i4+1):
                    k=k+1
                    mytuple = (i5, i4, i3, i2, i1)
                    #print(mytuple)

combinaciones = list(combinations_with_replacement(digits, 5))

#for element in combinaciones:
#    print(element)

#Los metodos son identicos, n es el numero de elementos en el conjunto y m el numero de elementos seleccionados.
#k es el numero de elementos pertenecientes al conjunto.
print(k)
print(len(combinaciones))
print("Son identicos, n = elementos del conjunto, m = elementos seleccionados, k = numero de combinaciones con reemplazo")
