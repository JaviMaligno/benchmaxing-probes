Para encontrar el número de formas en que HMMTLand pudo haber construido las carreteras, podemos modelar el problema utilizando teoría de grafos. 

Sea $G = (V, E)$ un grafo simple con $|V| = 8$ vértices (las ciudades) y aristas $E$ (las carreteras). Las condiciones del problema se traducen en:
1. $G$ es un grafo $3$-regular (cada vértice tiene grado $3$).
2. Para cualquier par de vértices distintos $u, v \in V$, el número de vecinos comunes es $|N(u) \cap N(v)| \in \{0, 2\}$.

### Paso 1: Análisis de la estructura local
Fijemos un vértice cualquiera $u \in V$ y sean $x, y, z$ sus $3$ vecinos. 
Cada uno de los vértices $x, y, z$ tiene grado $3$, y como ya están conectados con $u$, a cada uno le quedan exactamente $2$ aristas adicionales. Esto significa que hay exactamente $3 \times 2 = 6$ caminos de longitud $2$ que comienzan en $u$ y terminan en algún vértice $v \neq u$. En otras palabras:
$$\sum_{v \neq u} |N(u) \cap N(v)| = 6$$

Dado que $|N(u) \cap N(v)|$ solo puede ser $0$ o $2$, debe haber exactamente $3$ vértices distintos de $u$ que tienen $2$ vecinos en común con $u$, y los otros $4$ vértices tienen $0$ vecinos en común con $u$.

Ahora dividimos el análisis dependiendo de si existen triángulos ($K_3$) en el grafo o no.

---

### Paso 2: Caso 1 (El grafo contiene al menos un triángulo)
Supongamos que dos vecinos de $u$, digamos $x$ e $y$, están conectados entre sí. 
- Entonces $y \in N(u) \cap N(x)$, lo que implica que $|N(u) \cap N(x)| \ge 1$. Por la condición del problema, necesariamente $|N(u) \cap N(x)| = 2$. Como $N(u) = \{x, y, z\}$, los dos vecinos comunes de $u$ y $x$ deben ser $y$ y $z$. Por lo tanto, $x$ también está conectado con $z$.
- De manera análoga, como $x \in N(u) \cap N(y)$, se tiene que $|N(u) \cap N(y)| = 2$, por lo que $y$ también está conectado con $z$.

Esto significa que $\{u, x, y, z\}$ forman un subgrafo completo $K_4$. Como cada vértice en este $K_4$ ya tiene grado $3$, no puede haber aristas entre estos $4$ vértices y los $4$ vértices restantes del grafo. 

Para que los $4$ vértices restantes también tengan grado $3$, deben estar todos conectados entre sí, formando un segundo $K_4$. Así, $G$ es la unión disjunta de dos grafos completos de $4$ vértices ($K_4 \sqcup K_4$).
- Si $u, v$ están en el mismo $K_4$, tienen exactamente $2$ vecinos en común.
- Si $u, v$ están en distintos $K_4$, tienen $0$ vecinos en común.

**Conteo del Caso 1:**
El número de formas de dividir los $8$ vértices etiquetados en dos grupos no ordenados de tamaño $4$ es:
$$\frac{1}{2} \binom{8}{4} = \frac{1}{2} \cdot 70 = 35$$

---

### Paso 3: Caso 2 (El grafo es libre de triángulos)
Si el grafo no contiene ningún triángulo, por el análisis del Caso 1 sabemos que para cualquier vértice $u$, no hay aristas entre sus vecinos $x, y, z$.

Por lo tanto, ninguno de $x, y, z$ tiene vecinos en común con $u$. Los $3$ vértices que comparten $2$ vecinos con $u$ deben ser otros tres vértices fuera de $\{u, x, y, z\}$, a los que llamaremos $a, b, c$.
- Cada uno de $a, b, c$ está conectado a $2$ vértices de $\{x, y, z\}$.
- Dos de ellos (por ejemplo, $a$ y $b$) no pueden estar conectados al mismo par de vértices (digamos $x$ e $y$), porque entonces $x$ e $y$ tendrían al menos $3$ vecinos en común ($u, a, b$), lo cual está prohibido.

Así, $a, b, c$ están conectados a los $3$ pares distintos de $\{x, y, z\}$ (por ejemplo, $a$ con $\{x,y\}$, $b$ con $\{y,z\}$ y $c$ con $\{z,x\}$). Con esto, los vértices $u, x, y, z$ ya tienen grado $3$.

El octavo vértice restante, llamémoslo $w$, necesita tener grado $3$ y solo puede conectarse a los únicos vértices que aún tienen grado $2$, que son $a, b, c$. 

El grafo resultante es bipartito con partes $A = \{u, a, b, c\}$ y $B = \{w, x, y, z\}$ de tamaño $4$ cada una. Observamos que cada vértice en $A$ está conectado a todos los vértices de $B$ excepto a uno (por ejemplo, $u$ no está conectado a $w$, $a$ no está conectado a $z$, etc.). Esto es un grafo bipartito completo $K_{4,4}$ al que se le ha eliminado un emparejamiento perfecto (lo cual es isomorfo al grafo del cubo tridimensional $Q_3$).
- Dos vértices en la misma parte comparten exactamente $2$ vecinos.
- Dos vértices en partes distintas comparten $0$ vecinos.

**Conteo del Caso 2:**
1. Primero elegimos cómo partir los $8$ vértices en dos conjuntos no ordenados $A$ y $B$ de $4$ vértices cada uno. Hay $\frac{1}{2}\binom{8}{4} = 35$ formas de hacerlo.
2. Luego, para formar el grafo a partir de $K_{4,4}$, debemos elegir qué emparejamiento perfecto entre $A$ y $B$ vamos a eliminar (es decir, asignar a cada vértice de $A$ el único vértice de $B$ con el que *no* tiene carretera). Hay $4! = 24$ emparejamientos perfectos posibles.

El número de grafos en este caso es:
$$35 \times 24 = 840$$

---

### Paso 4: Total de configuraciones
Sumando las posibilidades de ambos casos disjuntos, obtenemos el número total de formas en que HMMTLand pudo haber construido las carreteras:
$$35 + 840 = 875$$

\boxed{875}