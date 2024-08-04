import numpy as np

print("Ejercicio  1")

# Numero 1
ej1 = np.array([
    [0.080, 0.184, 0.368, 0.368],
    [0.632, 0.368, 0, 0],
    [0.264, 0.368, 0.368, 0],
    [0.08, 0.184, 0.368, 0.368]
])

print("a) Matriz de transicion: ")

print(ej1)

print("b) Probabilidad que no haya celular en inventario despues de 2 semanas")
ej1_2 = np.linalg.matrix_power(ej1, 2)
print(ej1_2[1, 0])
print("c) Dado que se tienen 2 celulares al final de la semana, cual es la probabilidad de que haya 3 celulares en el almacen despues de 2 semanas?")
print(ej1_2[2, 3])
print("d) Probabilidad de que no haya celulares 4 semanas mas tarde")
P4 = np.linalg.matrix_power(ej1, 4)
print(P4[1, 0])
print("e) Probabilidad que haya 3 celulares en inventario despues de 2 semanas")
distribucion_inicial = np.array([0.25, 0.25, 0.25, 0.25])
distribucion_dos_semanas = distribucion_inicial.dot(ej1_2)
print(distribucion_dos_semanas[3])

print("Ejercicio 2")

# Se define la matriz de transicion
P = np.array([
    [1 / 4, 3 / 4, 0, 0, 0],
    [1 / 2, 1 / 2, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1 / 3, 2 / 3, 0],
    [1, 0, 0, 0, 0]
])

print("a) ¿Cuáles son los estados absorbentes? Explique por qué")

print("Hay un solo estado absorbente en P[2,2], ya que cuando entra a este estado no sale jamas")

print("b) ¿Cuáles son los estados recurrentes? Explique por qué")

print("Los estados recurrentes son P[4,0], P[0,1], P[1,0] y P[2,2] ya que luego de entrar al estado regresa a si mismo")

print("c) ¿Cuáles son los estados transitorios? Explique por qué")

print(
    "Los estados transitorios son P[4,0] y P[3,2], ya que luego de entrar a ese estado nunca regresa a el.\nen el caso de P[4,0] "
    "no hay ningun estado que vincule a 4 y en el caso de P[3,2] entra a un estado absorbente en P[2,2]")

print("d) ¿La cadena de Markov es irreducible? Explique por qué")

print("No es irreducible, algunos estados siguen sin ser accesibles.")

print("e) ¿La potencia de la matriz converge? Explique por qué")

tolerancia = 1e-6
P1 = P
P2 = P1 @ P
i = 2
while (np.linalg.norm(P1 - P2) > tolerancia and i < 206):
    P1 = P2
    P2 = P1 @ P
    i = i + 1
print(f"La matriz N se estabiliza en {i} iteraciones, sus valores empiezan a estabilizarse. La diferencia entre P^34 y")
print(
    "P^33 es menor a la tolerancia establecida (1e-6), los valores de la matriz empiezan a estabilizarse. La matriz converge.")

print(np.linalg.matrix_power(P, i))

print("f) Encuentre las probabilidades del estado estable")
print("Se toma en cuenta un % de error debido a la tolerancia descrita como criterio de estabilizacion de la matriz.")

# Se toma la matriz elevada a la potencia que es estable y se obtienen los vectores.
for i in range(0, 5):
    p = np.linalg.matrix_power(P, 34)[i]
    print(f"Estado {i}")
    print("Vector:", p)
    print("Suma del vector:", p.sum())

print("Ya que no es irreducible, se tienen dos vectores de probabilidad de estado estable:")
print("Estados 0, 1, 4:")
print("[0.4, 0.6, 0, 0, 0]")
print("Estados 2 y 3:")
print("0, 0, 1, 0, 0")
print("Esto tambien confirma que 2 es un estado absorbente")
