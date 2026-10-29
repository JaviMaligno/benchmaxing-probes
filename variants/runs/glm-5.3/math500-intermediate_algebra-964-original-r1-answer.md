# Solución paso a paso

**Paso 1: Entender la estructura.**
Para cada $i$ fijo, define $g_i(j) = f(i,j)$. Las reglas dicen:
- $g_0(j) = j+1 \pmod 5$,
- $g_i(0) = g_{i-1}(1)$,
- $g_i(j) = g_{i-1}(g_i(j-1))$ para $j \ge 1$.

Es decir, $g_i(j) = g_{i-1}^{(j+1)}(1)$: la función $g_{i-1}$ aplicada $j+1$ veces al valor $1$.

**Paso 2: Calcular los primeros niveles.**

- $g_0(x) = x+1 \pmod 5$, un 5-ciclo.
- $g_1(j) = g_0^{(j+1)}(1) = 1 + (j+1) = j+2 \pmod 5$, es decir $g_1 = [2,3,4,0,1]$.
- $g_2(j) = g_1^{(j+1)}(1) = 1 + 2(j+1) = 2j+3 \pmod 5$, o sea $g_2 = [3,0,2,4,1]$.
  Como función: $0\to3\to4\to1\to0$ (4-ciclo) y $2$ es punto fijo.
- $g_3(j) = g_2^{(j+1)}(1)$: iterando $1 \to 0 \to 3 \to 4 \to 1$ (periodo 4):
  $$g_3 = [0, 3, 4, 1, 0].$$
- $g_4(j) = g_3^{(j+1)}(1)$: iterando $g_3$ desde $1$: $1 \to 3 \to 1 \to 3 \to \cdots$ (ciclo de longitud 2):
  $$g_4 = [3, 1, 3, 1, 3].$$

**Paso 3: Detectar la estabilización.**

- $g_5(0) = g_4(1) = 1$, y luego $g_5(j) = g_4(g_5(j-1)) = g_4(1) = 1$ para todo $j$:
  $$g_5 = [1, 1, 1, 1, 1].$$
- Como $g_5$ es constante igual a $1$, se cumple $g_6(j) = g_5^{(j+1)}(1) = 1$ para todo $j$, es decir $g_6 = g_5$. Por inducción:
  $$g_i = [1,1,1,1,1] \quad \text{para todo } i \ge 5.$$

**Paso 4: Concluir.**

Como $2015 \ge 5$, tenemos $f(2015, 2) = g_{2015}(2) = 1$.

$$\boxed{1}$$