from sympy import init_printing, Symbol, Piecewise, integrate, diff, cos
from sympy.stats import FiniteRV, P, density, cdf, ContinuousRV, DiscreteUniform

#Crea un diccionario con la densidad de una variable aleatoria discreta con valores de 1-8 (Distribucion uniforme)
pp = DiscreteUniform("X", list(range (1, 9)))
densidad = density(pp).dict

#Crea la variable aleatoria utilizando el diccionario creado anteriormente
X1 = FiniteRV('X', densidad)

#Probabilidad que X1 == 2
print("a) P([X1=2])")
print(P(X1<=2) - P(X1<2))

#Probabilidad que que X1 > 2
print("b) P([X1>2])")
print(P(X1>2))

#Probabilidad que X1 < 2
print("c) P([X1<2])")
print(P(X1<2))

#Funcion densidad, es el diccionario que creamos anteriormente
print("d) Funcion de probabilidad P([X1=i]) para i pertenece a {1,2,3,4,5,6,7,8}")
print(densidad)

#Funcion densidad acumulada
print("e) Funcion de distribucion acumulada Fx1")
print(cdf(X1))

#Crea la variable aleatoria continua con una distribucion uniforme en el intervalo (8,10)
x = Symbol("x")
pdf = Piecewise((0.5,(x>8) & (x<10)),(0,True))
X2 = ContinuousRV(x,pdf)

print("f) P([X2=9])")
print(P(X2<=9)- P(X2<9))

print("g) P([X2>9])")
print(P(X2>9))

print("h) P([X2<9])")
print(P(X2<9))

print("i) Funcion de densidad de probabilidad Fx2")
print(density(X2)(x))

print("j) Funcion de distribucion acumulada Fx2")
print(cdf(X2)(x))

print("k) Funcion de distribucion acumulada de Fx3")
print("1/4*P(X1<=x) + 3/4*P(X2<=x)")

#Funcion de distribucion acumulada, toma un valor X y devuelve la distribucion acumulada hasta ese punto
def probX3(x):
    return 1/4*P(X1<=x) + 3/4*P(X2<=x)

print("l) P([X3=8])")
print(probX3(8) - probX3(7.99999))

print("m) P([X3>8])")
print(1-probX3(8))

print("n) P([X3<8])")
print(probX3(7.99999))