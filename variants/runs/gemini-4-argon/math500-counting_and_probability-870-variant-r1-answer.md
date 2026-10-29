Para encontrar la probabilidad de que los segmentos $PQ$, $RS$ y $TU$ se intersecan entre sí por pares, podemos analizar únicamente el orden circular en el que caen los seis puntos alrededor de la circunferencia.

1. **Reducción a emparejamientos sobre 6 puntos fijos:**
   Con probabilidad 1, los seis puntos elegidos al azar son distintos. Si consideramos las 6 posiciones que ocupan estos puntos en la circunferencia, asignarles las etiquetas $P, Q, R, S, T, U$ de forma aleatoria induce una partición equiprobable de los 6 puntos en 3 pares (que forman las cuerdas $PQ$, $RS$ y $TU$).

2. **Número total de formas de formar 3 cuerdas:**
   El número total de maneras de dividir 6 puntos en 3 pares sin importar el orden de los pares ni el orden dentro de cada par es:
   $$\frac{6!}{2! \cdot 2! \cdot 2! \cdot 3!} = \frac{720}{8 \cdot 6} = 15$$

3. **Condición para que las 3 cuerdas se crucen por pares:**
   Dos cuerdas en un círculo se intersecan si y solo si sus extremos se alternan a lo largo de la circunferencia. Para que las tres cuerdas $PQ$, $RS$ y $TU$ se crucen todas entre sí, los extremos de cada cuerda deben ser opuestos combinatoriamente (es decir, separados por exactamente dos puntos a cada lado a lo largo del círculo). 
   
   Para un conjunto fijo de 6 puntos en la circunferencia numerados en orden cíclico como $1, 2, 3, 4, 5, 6$, existe **únicamente 1** forma de emparejarlos de modo que las tres cuerdas se crucen mutuamente: conectando $(1,4)$, $(2,5)$ y $(3,6)$.

4. **Cálculo de la probabilidad:**
   Dado que solo 1 de las 15 posibles configuraciones de tres cuerdas cumple la condición y todas son igualmente probables, la probabilidad buscada es:
   $$P = \frac{1}{15}$$

\boxed{\frac{1}{15}}