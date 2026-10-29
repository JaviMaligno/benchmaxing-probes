Para determinar el número de componentes conexas $c_{n, k}$ del grafo $G_{n, k}$, podemos identificar el conjunto de vértices (las cadenas binarias de longitud $n$) con el espacio vectorial $\mathbb{F}_2^n$. 

En este contexto, dos vértices están conectados por una arista si y solo si su suma en $\mathbb{F}_2^n$ (equivalente a la operación XOR bit a bit) tiene peso de Hamming exactamente $k$ (es decir, tiene exactamente $k$ unos). Esto significa que $G_{n, k}$ es el grafo de Cayley del grupo aditivo $(\mathbb{F}_2^n, +)$ generado por el conjunto $S_{n, k}$ de todos los vectores de peso $k$.

La componente conexa que contiene al vector cero $\mathbf{0}$ es el subespacio vectorial $H_{n, k} = \langle S_{n, k} \rangle$ generado por $S_{n, k}$, y las demás componentes conexas son las clases laterales (cosets) de $H_{n, k}$ en $\mathbb{F}_2^n$. Por lo tanto, el número de componentes conexas es el índice del subespacio:
$$c_{n, k} = [\mathbb{F}_2^n : H_{n, k}] = 2^{n - \dim(H_{n, k})}$$

Analizamos ahora tres casos para $1 \leq k \leq n$:

1. **Caso $k = n$:**
   El único vector de peso $n$ es $\mathbf{1} = (1, 1, \dots, 1)$. Por lo tanto, $H_{n, n} = \{\mathbf{0}, \mathbf{1}\}$, que tiene dimensión $1$. Así:
   $$c_{n, n} = 2^{n - 1}$$

2. **Caso $1 \leq k < n$ con $k$ par:**
   Como $1 \leq k < n$, podemos elegir dos vectores de peso $k$ que compartan exactamente $k-1$ posiciones con valor $1$ y difieran en las dos posiciones de su último $1$. La suma de estos dos vectores en $\mathbb{F}_2^n$ es un vector de peso $2$. Como esto se puede hacer para cualquier par de coordenadas, $H_{n, k}$ contiene todos los vectores de peso $2$, los cuales generan el subespacio $E_n$ de todos los vectores de peso par (de dimensión $n-1$).
   Dado que $k$ es par, todos los generadores en $S_{n, k}$ tienen peso par, por lo que $H_{n, k} = E_n$. Entonces $\dim(H_{n, k}) = n - 1$, y:
   $$c_{n, k} = 2^{n - (n - 1)} = 2$$

3. **Caso $1 \leq k < n$ con $k$ impar:**
   Por el mismo argumento anterior, $E_n \subseteq H_{n, k}$. Sin embargo, como $k$ es impar, los vectores de $S_{n, k}$ no pertenecen a $E_n$. Dado que $\dim(E_n) = n - 1$, la única posibilidad es que $H_{n, k} = \mathbb{F}_2^n$, por lo que $\dim(H_{n, k}) = n$, y el grafo es conexo:
   $$c_{n, k} = 2^{n - n} = 1$$

---

### Cálculo de la suma

Para un $n$ fijo, sumamos $c_{n, k}$ para $1 \leq k \leq n$:
- Para $k = n$, el aporte es $2^{n-1}$.
- Para $1 \leq k \leq n-1$, hay $\left\lceil \frac{n-1}{2} \right\rceil$ valores impares (que aportan $1$ cada uno) y $\left\lfloor \frac{n-1}{2} \right\rfloor$ valores pares (que aportan $2$ cada uno). En total, los términos con $k < n$ suman $(n - 1) + \left\lfloor \frac{n-1}{2} \right\rfloor$.

Por lo tanto:
$$\sum_{k=1}^{n} c_{n, k} = 2^{n-1} + (n - 1) + \left\lfloor \frac{n-1}{2} \right\rfloor$$

Sumando ahora desde $n = 1$ hasta $n = 10$:
$$\sum_{n=1}^{10} \sum_{k=1}^{n} c_{n, k} = \sum_{n=1}^{10} 2^{n-1} + \sum_{n=1}^{10} (n - 1) + \sum_{n=1}^{10} \left\lfloor \frac{n-1}{2} \right\rfloor$$

Calculamos cada término por separado:
1. $\displaystyle \sum_{n=1}^{10} 2^{n-1} = 2^{10} - 1 = 1023$
2. $\displaystyle \sum_{n=1}^{10} (n - 1) = 0 + 1 + 2 + \dots + 9 = \frac{9 \times 10}{2} = 45$
3. $\displaystyle \sum_{n=1}^{10} \left\lfloor \frac{n-1}{2} \right\rfloor = 0 + 0 + 1 + 1 + 2 + 2 + 3 + 3 + 4 + 4 = 20$

Finalmente, sumamos los tres resultados:
$$1023 + 45 + 20 = 1088$$

\boxed{1088}