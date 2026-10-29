Para encontrar la probabilidad de que los segmentos $PQ$, $RS$ y $TU$ se intersecan por pares, podemos analizar la disposición circular de los seis puntos.

**Paso 1: Reducción a posiciones fijas en la circunferencia**
Dado que los seis puntos $P, Q, R, S, T, U$ se eligen de forma aleatoria e independiente sobre la circunferencia, la probabilidad de que dos puntos coincidan es $0$. Si fijamos las $6$ ubicaciones elegidas en la circunferencia y las numeramos en sentido horario como $1, 2, 3, 4, 5, 6$, por simetría todas las $6! = 720$ formas de asignar las etiquetas $P, Q, R, S, T, U$ a estas $6$ posiciones son igualmente probables.

**Paso 2: Contar el número total de emparejamientos**
Ignorando el orden dentro de cada segmento (ya que el segmento $PQ$ es el mismo que $QP$) y el orden entre los tres segmentos, el número total de formas de dividir las $6$ posiciones en $3$ pares de cuerdas disjuntas es:
$$\frac{6!}{2^3 \cdot 3!} = \frac{720}{8 \cdot 6} = 15$$
Cada una de estas $15$ configuraciones de $3$ cuerdas agrupa exactamente el mismo número de permutaciones de las etiquetas ($2^3 \cdot 3! = 48$ asignaciones), por lo que cada configuración de $3$ cuerdas es igualmente probable.

**Paso 3: Identificar las configuraciones favorables**
Dos cuerdas de un círculo se intersecan si y solo si sus extremos se alternan a lo largo de la circunferencia. Para que las tres cuerdas $PQ$, $RS$ y $TU$ se intersequen todas entre sí (por pares), cada cuerda debe ser cruzada por las otras dos. 

Esto implica que para cualquiera de las tres cuerdas, debe haber exactamente $2$ puntos a un lado de la cuerda y $2$ puntos al otro lado. En nuestras posiciones numeradas del $1$ al $6$ en orden circular, la única forma de lograr esto es conectando puntos opuestos:
- $(1, 4)$
- $(2, 5)$
- $(3, 6)$

Por lo tanto, de las $15$ formas posibles de emparejar los $6$ puntos en $3$ cuerdas, **solo $1$ configuración** cumple que los tres segmentos se crucen mutuamente.

**Paso 4: Calcular la probabilidad**
Como hay $1$ configuración favorable de un total de $15$ configuraciones igualmente probables, la probabilidad buscada es:
$$P = \frac{1}{15}$$

\boxed{\frac{1}{15}}