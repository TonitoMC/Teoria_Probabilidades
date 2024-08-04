# Laboratorio 4. Variable Aleatoria
## Instrucciones

Ejercicio 0.

Sea X1 una variable aleatoria distribuida uniformemente en {1,2,3,4,5,6,7,8} y sea X2 una
variable aleatoria uniforme en (8,10) y X3 = {X1 con probabilidad de ¼; X2 con probabilidad
de ¾}

Encontrar:

a) P([X1=2])

b) P([X1>2])

c) P([X1<2])

d) Función de probabilidad P([X1=i]) para i pertenece a {1,2,3,4,5,6,7,8}

e) Función de distribución acumulada Fx1

f) P([X2=9])

g) P([X2>9])

h) P([X2<9])

i) Función de densidad de probabilidad Fx2

j) Función de distribución acumulada Fx2

k) Función de distribución acumulada de Fx3

l) P([X3=8])

m) P([X3>8])

n) P([X3<8])
 
## Salida
```
a) P([X1=2])
1/8
b) P([X1>2])
3/4
c) P([X1<2])
1/8
d) Funcion de probabilidad P([X1=i]) para i pertenece a {1,2,3,4,5,6,7,8}
{1: 1/8, 2: 1/8, 3: 1/8, 4: 1/8, 5: 1/8, 6: 1/8, 7: 1/8, 8: 1/8}
e) Funcion de distribucion acumulada Fx1
{1: 1/8, 2: 1/4, 3: 3/8, 4: 1/2, 5: 5/8, 6: 3/4, 7: 7/8, 8: 1}
f) P([X2=9])
0
g) P([X2>9])
0.500000000000000
h) P([X2<9])
0.500000000000000
i) Funcion de densidad de probabilidad Fx2
Piecewise((Piecewise((0.5, (x > 8) & (x < 10)), (0, True)), (x > -oo) & (x < oo)), (0, True))
j) Funcion de distribucion acumulada Fx2
-0.5*Min(8, x) + 0.5*Min(10, x)
k) Funcion de distribucion acumulada de Fx3
1/4*P(X1<=x) + 3/4*P(X2<=x)
l) P([X3=8])
0.0312500000000000
m) P([X3>8])
0.750000000000000
n) P([X3<8])
0.218750000000000
