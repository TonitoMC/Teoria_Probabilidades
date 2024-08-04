import pandas as pd

df = pd.read_csv('MM Data.csv')
#print(data)

#Ejercicio 0.
print("Ejercicio 0.")

#Crea un DF con las columnas que cumplen con la condicion de R
def probR():
    result = df[df["Red"]>=10]
    return result

print("A) Probablidad que una bolsa tenga al menos 10 botonetas rojas:")
#La probabilidad de R es igual a la cantidad de elementos que cumplen R dividido la cantidad total de elementos
print (len(probR()) / len(df))

#Crea un DF con las columnas que cumplen con la condicion de T
def probT():
    result = df[df["Red"]+df["Green"]+df["Blue"]+df["Orange"]+df["Yellow"]+df["Brown"] >= 57]
    return result

print("B) Probablidad que una bolsa tenga al menos 57 botonetas en total")
#La probabilidad de T es igual a la cantidad de elementos que cumplen T dividido la cantidad total de elementos
print (len(probT()) / len(df))

#Crea un DF con las columnas que cumplen con la condicion de W
def probW():
    result = df[df["Weight"]>=50]
    return result

print("C) Probablidad que una bolsa pese al menos 50 gramos")
#La probabilidad de W es igual a la cantidad de elementos que cumplen W dividido la cantidad total de elementos
print (len(probW()) / len(df))

#Crea un DF con los elementos que cumplen ambas condiciones R y W
def probRintersectionT():
    result = pd.merge(probR(), probT(), how='inner')
    return result

print("D) Probablidad que una bolsa tenga al menos 10 botonetas rojas Y al menos 57 en total")
#La probabilidad de R interseccion W es igual a la cantidad de elementos que cumplen ambas condiciones
#dividido la cantidad total de elementos
print(len(probRintersectionT()) / len(df))

#Crea un DF con todos los elementos que cumplen R y NO cumplen W
def probTdiferenciaW():
    result = probT().drop(probW().index, errors='ignore')
    return result

print("E) Probablidad que una bolsa tenga al menos 57 botonetas en total y NO pese al menos 50 gramos")
#La probabilidad de R \ W es igual a la cantidad de elementos que cumplen R y NO W dividido la cantidad total
#de elementos
print(len(probTdiferenciaW()) / len(df))

#Ejercicio 1.

print("Ejercicio 1.")

#Probabilidad que sea elegida una urna
pu = [1 / 3, 1 / 3, 1 / 3]

#Probabilidad que sea una dona de limon dada cada urna
pl_u = [1 / 2, 2 / 5, 1 / 3]

#Probabilidad que sea en forma de toro dada que es de limon dada cada urna
p_lyu = [2 / 3, 1 / 2, 2 / 5]


# A. Que sea de limon y en forma de toro

# Returna la suma de las probabilidades que sea de limon y en forma de toro para cada indice (0,1,2)
def ej_1():
    valor = 0
    for i in range(3):
        valor = valor + (pu[i] * pl_u[i] * p_lyu[i])
    return valor

limon_y_toro = ej_1()

def ej_2(p):
    return (pu[p] * pl_u[p] * p_lyu[p]) / limon_y_toro


print("A. Probabilidad que sea de limon y en forma de toro:")
print(limon_y_toro)


# B. Probabilidad que una dona extraida de limon y en forma de toro sea de la urna 2

# Encuentra la probabilidad que sea de una urna especifica (indice p) y divide dentro de la probabilidad total que sea
# de limon en forma de toro
def ej_2(p):
    return (pu[p] * pl_u[p] * p_lyu[p]) / limon_y_toro


print("B. Probabilidad que una dona de limon en forma de toro haya sido extraida de la urna 2")
print(ej_2(2))

print("C. Probabilidad que una dona de limon y en forma de toro haya sido extraida de la urna 1")
print(ej_2(1))

print("D. Probabilidad que una dona de limon y en forma de toro haya sido extraida de la urna 0")
print(ej_2(0))

print("Extra: La suma de las probabilidades anteriores debe ser 1, verificando:")
print(ej_2(0) + ej_2(1) + ej_2(2))