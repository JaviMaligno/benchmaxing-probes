Para encontrar el valor mínimo de la expresión dada, primero reescribimos los términos dentro de las raíces cuadradas completando cuadrados:

1. El primer término es:
   \[\sqrt{a^2 + 225} = \sqrt{a^2 + 15^2}\]

2. El segundo término es:
   \[\sqrt{b^2 + 400} = \sqrt{20^2 + b^2}\]

3. Para el tercer término, agrupamos los términos en $a$ y en $b$:
   \[a^2 + b^2 - 70a - 80b + 2825 = (a^2 - 70a + 1225) + (b^2 - 80b + 1600) = (35 - a)^2 + (40 - b)^2\]
   Por lo tanto, el tercer radical se puede escribir como:
   \[\sqrt{(35 - a)^2 + (40 - b)^2}\]

Ahora podemos interpretar cada término como la norma euclidiana de un vector en $\mathbb{R}^2$. Definimos los vectores:
\[\vec{u} = (a, 15), \quad \vec{v} = (20, b), \quad \vec{w} = (35 - a, 40 - b)\]

Por la desigualdad triangular (o desigualdad de Minkowski), la suma de las longitudes de estos tres vectores es mayor o igual que la longitud de su suma:
\[\|\vec{u}\| + \|\vec{v}\| + \|\vec{w}\| \ge \|\vec{u} + \vec{v} + \vec{w}\|\]

Calculamos la suma de los tres vectores:
\[\vec{u} + \vec{v} + \vec{w} = (a + 20 + 35 - a,\, 15 + b + 40 - b) = (55, 55)\]

La norma del vector resultante es:
\[\|(55, 55)\| = \sqrt{55^2 + 55^2} = 55\sqrt{2}\]

La igualdad se alcanza si y solo si los vectores $\vec{u}$, $\vec{v}$ y $\vec{w}$ tienen la misma dirección y sentido (es decir, son múltiplos escalares positivos de $(1, 1)$). Esto ocurre cuando sus componentes son iguales:
- Para $\vec{u} = (a, 15)$: $a = 15$ (que cumple $0 \le 15 \le 35$).
- Para $\vec{v} = (20, b)$: $b = 20$ (que cumple $0 \le 20 \le 40$).
- Para $\vec{w} = (35 - a, 40 - b)$: al sustituir $a = 15$ y $b = 20$, obtenemos $\vec{w} = (20, 20)$, que también es un múltiplo positivo de $(1, 1)$.

Dado que la cota inferior se alcanza dentro de los intervalos permitidos para $a$ y $b$, concluimos que el valor mínimo es:

\boxed{55\sqrt{2}}