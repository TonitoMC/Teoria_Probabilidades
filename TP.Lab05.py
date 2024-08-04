from sympy import oo, integrate, exp, diff, symbols
from sympy.stats import Exponential, E, variance, Poisson
import sympy as sp
# Definir el símbolo
t, lambda_ = symbols('t lambda')

print('Ejercicio 1.')

#Se define la variable aleatoria X1 con distribucion Poisson y parametro Lambda = 1/2
lamb = sp.S(1)/2
X1 = Poisson('X1', lamb)

print('Utilizando funcion E y variance:')

#Se obtiene el valor esperado de X1 utilizando la funcion E
print(f"Valor Esperado de X1: {E(X1.evalf())}")

#Se obtiene la varianza de X1 utilizando la funcion variance
print(f"Varianza de X1: {variance(X1.evalf())}")

#Se define la funcion generadora de momentos
mgf_X1 = exp(lamb*(exp('t') - 1))

#Se calcula el valor esperado y la varianza utilizando la funcion generadora de momentos
X1_expected = mgf_X1.diff(t).subs(t, 0).evalf()
X1_variance = (mgf_X1.diff(t, 2).subs(t, 0) - mgf_X1.diff(t).subs(t, 0)**2).evalf()

#Se imprimen los valores
print('Utilizando la funcion generadora de momentos:')
print("Valor Esperado:", X1_expected)
print('Varianza:', X1_variance)

print('Ejercicio 2.')
#Se define la variable aleatoria
beta = 5
lambda_value = 1/beta
X2 = Exponential('X', lambda_value)

print('Valor Esperado y Varianza:')

#Se obtiene el valor esperado de X2 utilizando la funcion E
print(f"Valor Esperado de X2: {E(X2.evalf())}")

#Se obtiene la varianza de X2 utilizando la funcion variance
print(f"Varianza de X2: {variance(X2.evalf())}")

# Definir la función generadora de momentos para una distribución exponencial
M_t = lambda_ / (lambda_ - t)

# Calcular la primera y segunda derivada de M_t con respecto a t
M_t_prime = diff(M_t, t).subs(lambda_, lambda_value)
M_t_double_prime = diff(M_t, t, t).subs(lambda_, lambda_value)

# Evaluar las derivadas en t = 0 para obtener los momentos
first_moment = M_t_prime.subs(t, 0)
second_moment = M_t_double_prime.subs(t, 0)

print('Primer y Segundo Momento:')
print('E[X] =', first_moment)
print('E[X^2] =', second_moment)