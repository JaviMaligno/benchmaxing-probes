¡Claro! Vamos a resolverlo paso a paso.

## Paso 1: Entender la recursión

Tenemos la función \(f(i,j)\) definida para \(i \ge 0\) y \(0 \le j \le 4\).

- **Caso base** (\(i=0\)):  
  \[
  f(0,j) = (j+1) \bmod 5
  \]
  Como \(j \in \{0,1,2,3,4\}\), entonces:
  \[
  f(0,0)=1,\quad f(0,1)=2,\quad f(0,2)=3,\quad f(0,3)=4,\quad f(0,4)=0.
  \]

- **Caso recursivo** (\(i \ge 1\)):
  - Si \(j=0\):
    \[
    f(i,0) = f(i-1,1)
    \]
  - Si \(1 \le j \le 4\):
    \[
    f(i,j) = f(i-1, f(i,j-1))
    \]

Esto define, para cada \(i\), una función \(g_i(j) = f(i,j)\) sobre \(\{0,1,2,3,4\}\).

---

## Paso 2: Calcular \(f(1,j)\)

Para \(i=1\):

\[
f(1,0) = f(0,1) = 2.
\]

Luego, por la recursión:

\[
f(1,1) = f(0, f(1,0)) = f(0,2) = 3.
\]

\[
f(1,2) = f(0, f(1,1)) = f(0,3) = 4.
\]

\[
f(1,3) = f(0, f(1,2)) = f(0,4) = 0.
\]

\[
f(1,4) = f(0, f(1,3)) = f(0,0) = 1.
\]

Entonces \(f(1,\cdot)\) es la función:

\[
(0 \mapsto 2,\ 1 \mapsto 3,\ 2 \mapsto 4,\ 3 \mapsto 0,\ 4 \mapsto 1).
\]

---

## Paso 3: Interpretar como composición

Para cada \(i\), definimos la función \(g_i:\{0,1,2,3,4\}\to\{0,1,2,3,4\}\) mediante:

\[
g_i(j) = f(i,j).
\]

El caso base nos da:

\[
g_0(j) = (j+1)\bmod 5.
\]

La regla para \(i \ge 1\) puede reescribirse así:

- \(g_i(0) = g_{i-1}(1)\),
- \(g_i(j) = g_{i-1}(g_i(j-1))\) para \(1 \le j \le 4\).

Observemos que, al evaluar \(g_i(j)\), se aplica \(g_{i-1}\) al resultado \(g_i(j-1)\). Es decir:

\[
g_i(j) = g_{i-1}(g_i(j-1)).
\]

No es exactamente una potencia funcional simple, pero notemos que:

\[
g_i(1) = g_{i-1}(g_i(0)) = g_{i-1}(g_{i-1}(1)),
\]

porque \(g_i(0)=g_{i-1}(1)\). Denotemos la composición \(g_{i-1} \circ g_{i-1}\) como \(g_{i-1}^{\circ 2}\).

Entonces:

\[
g_i(1) = g_{i-1}^{\circ 2}(1).
\]

Siguiendo:

\[
g_i(2) = g_{i-1}(g_i(1)) = g_{i-1}\big(g_{i-1}^{\circ 2}(1)\big) = g_{i-1}^{\circ 3}(1).
\]

En general, parece que:

\[
g_i(j) = g_{i-1}^{\circ (j+1)}(1).
\]

Comprobemos para \(j=0\):  
\[
g_i(0) = g_{i-1}(1),
\]
que coincide con \(g_{i-1}^{\circ 1}(1)\). Así que para todo \(0 \le j \le 4\):

\[
g_i(j) = g_{i-1}^{\circ (j+1)}(1).
\]

---

## Paso 4: Relación entre \(g_i\) y \(g_{i-1}\)

Queremos ver cómo se transforma toda la función \(g_i\) a partir de \(g_{i-1}\).

Cada \(g_i\) es una permutación del conjunto \(\{0,1,2,3,4\}\), porque \(g_0\) es la traslación cíclica \(j \mapsto (j+1)\bmod 5\), que es una permutación, y la composición preserva esa propiedad.

Para una permutación \(g_{i-1}\), definimos:

\[
g_i(j) = g_{i-1}^{\circ (j+1)}(1).
\]

Como \(g_{i-1}\) es una permutación, su acción sobre el conjunto queda completamente determinada por cómo actúa sobre \(1\) bajo potencias. De hecho, \(g_i\) es "conjugada" a algo sencillo.

---

## Paso 5: Representar como permutaciones y calcular directamente

En vez de buscar una fórmula general elaborada, usemos la representación de permutaciones. Escribimos cada \(g_i\) como una lista:

\[
g_i = [g_i(0), g_i(1), g_i(2), g_i(3), g_i(4)].
\]

Ya tenemos:

\[
g_0 = [1,2,3,4,0].
\]

Para \(g_1\):

\[
g_1(0) = g_0(1) = 2,
\]
\[
g_1(1) = g_0(g_1(0)) = g_0(2) = 3,
\]
\[
g_1(2) = g_0(g_1(1)) = g_0(3) = 4,
\]
\[
g_1(3) = g_0(g_1(2)) = g_0(4) = 0,
\]
\[
g_1(4) = g_0(g_1(3)) = g_0(0) = 1.
\]

Entonces:

\[
g_1 = [2,3,4,0,1].
\]

Notemos que \(g_1(j) = (j+2)\bmod 5\).

---

## Paso 6: Calcular \(g_2\)

\[
g_2(0) = g_1(1) = 3.
\]

\[
g_2(1) = g_1(g_2(0)) = g_1(3) = 0.
\]

\[
g_2(2) = g_1(g_2(1)) = g_1(0) = 2.
\]

\[
g_2(3) = g_1(g_2(2)) = g_1(2) = 4.
\]

\[
g_2(4) = g_1(g_2(3)) = g_1(4) = 1.
\]

Así:

\[
g_2 = [3,0,2,4,1].
\]

---

## Paso 7: Calcular \(g_3\)

\[
g_3(0) = g_2(1) = 0.
\]

\[
g_3(1) = g_2(g_3(0)) = g_2(0) = 3.
\]

\[
g_3(2) = g_2(g_3(1)) = g_2(3) = 4.
\]

\[
g_3(3) = g_2(g_3(2)) = g_2(4) = 1.
\]

\[
g_3(4) = g_2(g_3(3)) = g_2(1) = 0.
\]

Así:

\[
g_3 = [0,3,4,1,0].
\]

Aquí vemos algo raro: \(g_3(0)=0\) y \(g_3(4)=0\). Esto significa que \(g_3\) **no es una permutación**. Entonces, a partir de \(g_2\), la propiedad de ser permutación no se mantiene.

---

## Paso 8: Calcular \(g_4\)

\[
g_4(0) = g_3(1) = 3.
\]

\[
g_4(1) = g_3(g_4(0)) = g_3(3) = 1.
\]

\[
g_4(2) = g_3(g_4(1)) = g_3(1) = 3.
\]

\[
g_4(3) = g_3(g_4(2)) = g_3(3) = 1.
\]

\[
g_4(4) = g_3(g_4(3)) = g_3(1) = 3.
\]

Así:

\[
g_4 = [3,1,3,1,3].
\]

---

## Paso 9: Calcular \(g_5\)

\[
g_5(0) = g_4(1) = 1.
\]

\[
g_5(1) = g_4(g_5(0)) = g_4(1) = 1.
\]

\[
g_5(2) = g_4(g_5(1)) = g_4(1) = 1.
\]

\[
g_5(3) = g_4(g_5(2)) = g_4(1) = 1.
\]

\[
g_5(4) = g_4(g_5(3)) = g_4(1) = 1.
\]

Así:

\[
g_5 = [1,1,1,1,1].
\]

---

## Paso 10: Encontrar el patrón para \(i \ge 5\)

Ahora que \(g_5\) es constante igual a \(1\), veamos qué ocurre con \(g_6\):

\[
g_6(0) = g_5(1) = 1.
\]

\[
g_6(1) = g_5(g_6(0)) = g_5(1) = 1.
\]

Igual para los demás:

\[
g_6 = [1,1,1,1,1].
\]

Por lo tanto, para todo \(i \ge 5\),

\[
g_i(j) = 1 \quad \text{para todo } j \in \{0,1,2,3,4\}.
\]

---

## Paso 11: Calcular \(f(2015,2)\)

Como \(2015 \ge 5\), tenemos:

\[
f(2015,2) = g_{2015}(2) = 1.
\]

Por lo tanto, la respuesta final es:

\[
\boxed{1}
\]