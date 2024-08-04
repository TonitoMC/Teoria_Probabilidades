# Parcial 4: Cadenas de Markov y Ley de Grandes Números
## Instrucciones
El examen consiste en seleccionar uno de los 4 probleas y resolverlo de 2 formas, utilizando cadenas de Markov y utilizando la Ley de los Grandes Números

### Problema Seleccionado
Menganita quiere impresionar a Chispudito con sus conocimientos de probabilidad. Ella decide utilizar la máquina de Galton con 6 niveles de clavos y 7 casilleros donde caen las pelotitas para mostrárselo a Chispudito.
  
Para ayudarle a Menganita. debe encontrar la probabilidad de que la pelotita caiga en cada uno de los casilleros.

### Resolución
El programa diseñado puede calcular las probabilidades para una máquina de galton de N niveles, generando su matriz de transición para la sección de Cadenas de Markov y realizando la simulación correspondiente para la Ley de los Grandes Números. Las explicaciones matemáticas más a detalle se encuentran en el archivo TP.Parcial4.pdf dentro del repositorio.

### Salida
```
Ley de Grandes Numeros
Intentos: 1000000
Casillero 21: 15430
Casillero 22: 93954
Casillero 23: 233861
Casillero 24: 312883
Casillero 25: 234453
Casillero 26: 93678
Casillero 27: 15741
% Casillero 21: 0.01543
% Casillero 22: 0.093954
% Casillero 23: 0.233861
% Casillero 24: 0.312883
% Casillero 25: 0.234453
% Casillero 26: 0.093678
% Casillero 27: 0.015741
Cadenas de Markov
Casillero 21: 0.015625
Casillero 22: 0.09375
Casillero 23: 0.234375
Casillero 24: 0.3125
Casillero 25: 0.234375
Casillero 26: 0.09375
Casillero 27: 0.015625
Valor Esperado: 24.0
```
