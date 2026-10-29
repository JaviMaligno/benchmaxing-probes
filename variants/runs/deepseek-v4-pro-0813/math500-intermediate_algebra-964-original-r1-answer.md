Voy a analizar la función recursiva por casos.

La función está definida como:

- \(f(0,j) = j+1 \pmod 5\) para \(0 \le j \le 4\).
- \(f(i,0) = f(i-1,1)\) para \(i \ge 1\).
- \(f(i,j) = f(i-1, f(i,j-1))\) para \(i \ge 1\) y \(1 \le j \le 4\).

Llamemos \(F_i(j) = f(i,j)\). Entonces la recurrencia es:

\[
F_i(0) = F_{i-1}(1)
\]
\[
F_i(j) = F_{i-1}(F_i(j-1))
\]

Y \(F_0(j) = j+1 \pmod 5\).

---

### Cálculo de \(F_1\)

Para \(i=1\):

- \(F_1(0) = F_0(1) = 2\).
- \(F_1(1) = F_0(F_1(0)) = F_0(2) = 3\).
- \(F_1(2) = F_0(F_1(1)) = F_0(3) = 4\).
- \(F_1(3) = F_0(F_1(2)) = F_0(4) = 0\).
- \(F_1(4) = F_0(F_1(3)) = F_0(0) = 1\).

Entonces:

\[
F_1 = [2,3,4,0,1]
\]

Es decir, \(F_1(j) = j+2 \pmod 5\).

---

### Cálculo de \(F_2\)

Para \(i=2\):

- \(F_2(0) = F_1(1) = 3\).
- \(F_2(1) = F_1(F_2(0)) = F_1(3) = 0\).
- \(F_2(2) = F_1(F_2(1)) = F_1(0) = 2\).
- \(F_2(3) = F_1(F_2(2)) = F_1(2) = 4\).
- \(F_2(4) = F_1(F_2(3)) = F_1(4) = 1\).

Entonces:

\[
F_2 = [3,0,2,4,1]
\]

---

### Cálculo de \(F_3\)

Para \(i=3\):

- \(F_3(0) = F_2(1) = 0\).
- \(F_3(1) = F_2(F_3(0)) = F_2(0) = 3\).
- \(F_3(2) = F_2(F_3(1)) = F_2(3) = 4\).
- \(F_3(3) = F_2(F_3(2)) = F_2(4) = 1\).
- \(F_3(4) = F_2(F_3(3)) = F_2(1) = 0\).

Entonces:

\[
F_3 = [0,3,4,1,0]
\]

---

### Cálculo de \(F_4\)

Para \(i=4\):

- \(F_4(0) = F_3(1) = 3\).
- \(F_4(1) = F_3(F_4(0)) = F_3(3) = 1\).
- \(F_4(2) = F_3(F_4(1)) = F_3(1) = 3\).
- \(F_4(3) = F_3(F_4(2)) = F_3(3) = 1\).
- \(F_4(4) = F_3(F_4(3)) = F_3(1) = 3\).

Entonces:

\[
F_4 = [3,1,3,1,3]
\]

---

### Detección de un patrón

Calculemos \(F_5\):

- \(F_5(0) = F_4(1) = 1\).
- \(F_5(1) = F_4(1) = 1\).
- \(F_5(2) = F_4(1) = 1\).
- \(F_5(3) = F_4(1) = 1\).
- \(F_5(4) = F_4(1) = 1\).

Así:

\[
F_5 = [1,1,1,1,1]
\]

Calculemos \(F_6\):

- \(F_6(0) = F_5(1) = 1\).
- \(F_6(1) = F_5(F_6(0)) = F_5(1) = 1\).
- Y así sucesivamente.

Así:

\[
F_6 = [1,1,1,1,1]
\]

Para \(i \ge 5\), la función se vuelve constante igual a \(1\):

\[
F_i(j) = 1 \quad \text{para todo } j.
\]

---

### Conclusión

Como \(2015 \ge 5\),

\[
f(2015,2) = F_{2015}(2) = 1.
\]

\[
\boxed{1}
\]