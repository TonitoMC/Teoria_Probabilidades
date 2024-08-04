# Laboratorio 10. Cadenas de Markov
 
## Salida
```
Ejercicio  1
a) Matriz de transicion:
[[0.08  0.184 0.368 0.368]
 [0.632 0.368 0.    0.   ]
 [0.264 0.368 0.368 0.   ]
 [0.08  0.184 0.368 0.368]]
b) Probabilidad que no haya celular en inventario despues de 2 semanas
0.283136
c) Dado que se tienen 2 celulares al final de la semana, cual es la probabilidad de que haya 3 celulares en el almacen despues de 2 semanas?
0.097152
d) Probabilidad de que no haya celulares 4 semanas mas tarde
0.28142424064
e) Probabilidad que haya 3 celulares en inventario despues de 2 semanas
0.164864
Ejercicio 2
a) ¿Cuáles son los estados absorbentes? Explique por qué
Hay un solo estado absorbente en P[2,2], ya que cuando entra a este estado no sale jamas
b) ¿Cuáles son los estados recurrentes? Explique por qué
Los estados recurrentes son P[4,0], P[0,1], P[1,0] y P[2,2] ya que luego de entrar al estado regresa a si mismo
c) ¿Cuáles son los estados transitorios? Explique por qué
Los estados transitorios son P[4,0] y P[3,2], ya que luego de entrar a ese estado nunca regresa a el.
en el caso de P[4,0] no hay ningun estado que vincule a 4 y en el caso de P[3,2] entra a un estado absorbente en P[2,2]
d) ¿La cadena de Markov es irreducible? Explique por qué
No es irreducible, algunos estados siguen sin ser accesibles.
e) ¿La potencia de la matriz converge? Explique por qué
La matriz N se estabiliza en 34 iteraciones, sus valores empiezan a estabilizarse. La diferencia entre P^34 y
P^33 es menor a la tolerancia establecida (1e-6), los valores de la matriz empiezan a estabilizarse. La matriz converge.
[[4.00000000e-01 6.00000000e-01 0.00000000e+00 0.00000000e+00
  0.00000000e+00]
 [4.00000000e-01 6.00000000e-01 0.00000000e+00 0.00000000e+00
  0.00000000e+00]
 [0.00000000e+00 0.00000000e+00 1.00000000e+00 0.00000000e+00
  0.00000000e+00]
 [0.00000000e+00 0.00000000e+00 9.99998970e-01 1.03014223e-06
  0.00000000e+00]
 [4.00000000e-01 6.00000000e-01 0.00000000e+00 0.00000000e+00
  0.00000000e+00]]
f) Encuentre las probabilidades del estado estable
Se toma en cuenta un % de error debido a la tolerancia descrita como criterio de estabilizacion de la matriz.
Estado 0
Vector: [0.4 0.6 0.  0.  0. ]
Suma del vector: 1.0
Estado 1
Vector: [0.4 0.6 0.  0.  0. ]
Suma del vector: 1.0
Estado 2
Vector: [0. 0. 1. 0. 0.]
Suma del vector: 1.0
Estado 3
Vector: [0.00000000e+00 0.00000000e+00 9.99998970e-01 1.03014223e-06
 0.00000000e+00]
Suma del vector: 1.0
Estado 4
Vector: [0.4 0.6 0.  0.  0. ]
Suma del vector: 1.0
Ya que no es irreducible, se tienen dos vectores de probabilidad de estado estable:
Estados 0, 1, 4:
[0.4, 0.6, 0, 0, 0]
Estados 2 y 3:
0, 0, 1, 0, 0
Esto tambien confirma que 2 es un estado absorbente
