## Resolución

**Planteamiento.** Como $\omega$ es una raíz primitiva 13-ésima de la unidad, calculamos

$$|\omega^a+\omega^b+\omega^c+\omega^d|^2 = 4 + \sum_{\substack{i\neq j}} \omega^{x_i-x_j},$$

donde $\{x_i\}=\{a,b,c,d\}$. Igualando a $3$, la suma de los 12 términos $\omega^{x_i-x_j}$ debe valer $-1$.

**Condición de conjunto de diferencias.** Escribiendo la suma en términos de $c_k=\omega^k+\omega^{-k}$ ($k=1,\dots,6$), que son linealmente independientes sobre $\mathbb{Q}$ (son 6 elementos que generan el subcuerpo real de grado 6 de $\mathbb{Q}(\omega)$) y satisfacen $c_1+\cdots+c_6=-1$, la única forma de obtener $-1$ es que **cada diferencia no nula módulo 13 aparezca exactamente una vez**. Es decir, $\{a,b,c,d\}$ módulo 13 debe ser un *conjunto perfecto de diferencias* (como $\{0,1,3,9\}$, el conjunto planar clásico). Un análisis similar descarta que dos exponentes coincidan módulo 13.

**Criterio práctico.** Las 6 diferencias por pares, reducidas a distancias circulares en $\{1,\dots,6\}$, deben ser exactamente $\{1,2,3,4,5,6\}$.

**Búsqueda del mínimo.** Como $1000a$ domina, minimizamos primero $a$, luego $b$, $c$, $d$ (todos impares, $a>b>c>d\ge 1$):

- $a=7$: única opción $\{7,5,3,1\}$, distancias $\{2,4,6,2,4,2\}$ — falla.
- $a=9$: las cuatro opciones $\{9,\cdot,\cdot,\cdot\}\subset\{1,3,5,7,9\}$ repiten distancias — fallan.
- $a=11$: las diez combinaciones con $\{1,3,5,7,9\}$ fallan todas (siempre hay distancia repetida).
- $a=13$ ($\equiv 0$): con $b=5$ y $b=7$ todas las opciones fallan. Con $b=9$, $c=3$, $d=1$:
  $$\{13,9,3,1\}\equiv\{0,9,3,1\} \pmod{13},$$
  diferencias $9,3,1,6,8,2 \to$ distancias $\{4,3,1,6,5,2\}=\{1,2,3,4,5,6\}$ ✓.

Es precisamente el conjunto de diferencias $\{0,1,3,9\}$, y en efecto
$$|1+\omega+\omega^3+\omega^9|^2 = 4+\sum_{k=1}^{12}\omega^k = 4-1 = 3.$$

**Resultado.** Con $a=13$, $b=9$, $c=3$, $d=1$:

$$1000(13)+100(9)+10(3)+1 = 13931.$$

$$\boxed{13931}$$