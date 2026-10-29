Voy a razonar el problema paso a paso.

Sea

\[
g(x)=c_nx^n+c_{n-1}x^{n-1}+\cdots+c_2x^2+c_1x+c_0
\]

un polinomio con coeficientes enteros, cuyas raíces son todas **enteras y distintas**.

Además \(c_n=2\) y \(c_0=78\).

Como las raíces son todas enteras y distintas, podemos escribir

\[
g(x)=2\prod_{i=1}^{n}(x-r_i),
\]

donde \(r_i\in\mathbb Z\) son todas distintas.

Nos piden el menor valor posible de

\[
|c_{n-1}|.
\]

---

## 1. Relación con las raíces

Comparando coeficientes:

\[
g(x)=2x^n - 2(r_1+\cdots+r_n)x^{n-1}+\cdots
\]

Por tanto

\[
c_{n-1}=-2\sum_{i=1}^{n}r_i.
\]

Así,

\[
|c_{n-1}|=2\left|\sum_{i=1}^{n}r_i\right|.
\]

Además, el término constante:

\[
c_0=g(0)=2\prod_{i=1}^{n}(0-r_i)
=2(-1)^n\prod_{i=1}^{n}r_i.
\]

Como \(c_0=78\), tenemos

\[
2(-1)^n\prod_{i=1}^{n}r_i=78.
\]

Por tanto

\[
\prod_{i=1}^{n}r_i = 39(-1)^n.
\]

Es decir, el producto de las raíces es \(\pm 39\).

Las factorizaciones enteras de \(39\) son

\[
39 = 1\cdot 3\cdot 13 = 1\cdot 39 = 3\cdot 13.
\]

---

## 2. Buscamos minimizar la suma de las raíces

Queremos minimizar

\[
|r_1+\cdots+r_n|.
\]

Como el producto de los valores absolutos debe ser \(39=3\cdot 13\), los posibles conjuntos de valores absolutos de las raíces, sin contar ceros, son:

- \(\{1,3,13\}\)
- \(\{1,39\}\)
- \(\{3,13\}\)

Además, como el producto debe ser \(\pm 39\), dependiendo de \(n\) podríamos incluir raíces igual a \(0\). Pero si una raíz fuera \(0\), entonces \(c_0=0\), lo cual es imposible porque \(c_0=78\). Por tanto **ninguna raíz puede ser \(0\)**.

Entonces los conjuntos de valores absolutos posibles son los tres de arriba.

---

## 3. Minimizar la suma

### Caso A: \(\{1,3,13\}\)

Aquí \(n=3\). Tenemos \(3\) raíces con valores absolutos \(1,3,13\).

El producto debe ser \(39(-1)^3=-39\). Entonces el producto de las raíces debe ser \(-39\).

Con valores absolutos \(1,3,13\), el producto con signo será \(\pm 39\). Para que sea \(-39\), debe haber un número impar de raíces negativas.

Las combinaciones posibles y su suma:

- \(1,3,-13\): suma \(1+3-13=-9\)
- \(1,-3,13\): suma \(1-3+13=11\)
- \(-1,3,13\): suma \(-1+3+13=15\)
- \(-1,-3,-13\): suma \(-17\)

También podrían ser negativas en parejas, pero eso daría producto positivo, lo cual no sirve aquí.

El mínimo valor absoluto de la suma es \(9\).

### Caso B: \(\{1,39\}\)

Aquí \(n=2\). El producto debe ser \(39(-1)^2=39\), positivo.

Combinaciones:

- \(1,39\): suma \(40\)
- \(-1,-39\): suma \(-40\)

Mínimo valor absoluto: \(40\).

### Caso C: \(\{3,13\}\)

Aquí \(n=2\). El producto debe ser \(39\), positivo.

Combinaciones:

- \(3,13\): suma \(16\)
- \(-3,-13\): suma \(-16\)

Mínimo valor absoluto: \(16\).

---

## 4. Conclusión

El menor valor absoluto de la suma de las raíces es \(9\), obtenido, por ejemplo, con raíces

\[
1,\ 3,\ -13.
\]

Entonces

\[
|c_{n-1}|=2\cdot 9=18.
\]

Por tanto, la respuesta es:

\[
\boxed{18}
\]