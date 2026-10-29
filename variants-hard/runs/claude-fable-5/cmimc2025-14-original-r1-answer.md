## Planteamiento

$G_{n,k}$ es un grafo de Cayley sobre el grupo $(\mathbb{F}_2^n, \oplus)$ con conjunto de conexión $S$ = vectores de peso exactamente $k$. Por lo tanto, sus componentes conexas son las clases laterales del subgrupo $H = \langle S \rangle$, y

$$c_{n,k} = \frac{2^n}{|H|}.$$

## Cálculo de $H$

**Caso $k = n$:** el único vector de peso $n$ es el todo-unos, así que $H = \{0, \mathbf{1}\}$, $|H| = 2$, y $c_{n,n} = 2^{n-1}$.

**Caso $k < n$:** tomando dos vectores de peso $k$ que comparten $k-1$ unos (posible porque $k+1 \le n$), su suma tiene peso $2$. Como $S$ es invariante bajo permutaciones de coordenadas, $H$ contiene **todos** los vectores de peso $2$, los cuales generan el subgrupo de peso par (de tamaño $2^{n-1}$).

- Si $k$ es **par**, todos los generadores tienen peso par, así que $H$ es exactamente el subgrupo de peso par: $c_{n,k} = 2$.
- Si $k$ es **impar**, $H$ contiene además un vector de peso impar, luego $H = \mathbb{F}_2^n$: $c_{n,k} = 1$.

Esto concuerda con el ejemplo: $G_{3,2}$ tiene $2$ componentes. ✓

## Suma

$$\sum_{n=1}^{10}\sum_{k=1}^{n} c_{n,k} = \sum_{n=1}^{10} 2^{n-1} + \sum_{n=1}^{10}\Big(\underbrace{\#\{k<n \text{ impar}\}}_{\times 1} + \underbrace{\#\{k<n \text{ par}\}}_{\times 2}\Big).$$

La primera suma es $2^{10} - 1 = 1023$.

Para la segunda, con $k = 1, \dots, n-1$:

| $n$ | impares | pares | aporte $= \text{imp} + 2\cdot\text{par}$ |
|---|---|---|---|
| 1 | 0 | 0 | 0 |
| 2 | 1 | 0 | 1 |
| 3 | 1 | 1 | 3 |
| 4 | 2 | 1 | 4 |
| 5 | 2 | 2 | 6 |
| 6 | 3 | 2 | 7 |
| 7 | 3 | 3 | 9 |
| 8 | 4 | 3 | 10 |
| 9 | 4 | 4 | 12 |
| 10 | 5 | 4 | 13 |

Total de la tabla: $0+1+3+4+6+7+9+10+12+13 = 65$.

$$1023 + 65 = 1088$$

$$\boxed{1088}$$