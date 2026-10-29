Vamos a resolver el problema paso a paso.

Tenemos que

\[
\sqrt{\underline{abcde}} = a\sqrt{\underline{bcde}},
\]

donde \(\underline{abcde}\) es un número de cinco dígitos y \(a\neq 0\).

---

## 1. Escribimos la ecuación en forma algebraica

Sea

\[
n = \underline{abcde} = 10000a + 1000b + 100c + 10d + e.
\]

Y el número de cuatro dígitos:

\[
m = \underline{bcde} = 1000b + 100c + 10d + e.
\]

La condición es:

\[
\sqrt{n} = a\sqrt{m}.
\]

Elevando al cuadrado:

\[
n = a^2 m.
\]

Es decir:

\[
10000a + m = a^2 m.
\]

Reordenamos:

\[
10000a = a^2 m - m = m(a^2 - 1).
\]

Por lo tanto:

\[
m = \frac{10000a}{a^2 - 1}.
\]

---

## 2. Analizamos los posibles valores de \(a\)

Como \(m = \underline{bcde}\) debe ser un entero de cuatro dígitos, es decir \(1000 \le m \le 9999\), y además \(b\) puede ser 0, probamos con los dígitos \(a=1,2,\dots,9\).

La fórmula:

\[
m = \frac{10000a}{a^2 - 1}.
\]

### \(a=1\)

El denominador \(a^2-1=0\), no válido.

### \(a=2\)

\[
m = \frac{20000}{4-1} = \frac{20000}{3},
\]

no entero.

### \(a=3\)

\[
m = \frac{30000}{9-1} = \frac{30000}{8} = 3750.
\]

Este es entero y de cuatro dígitos. Entonces \(n = 30000 + 3750 = 33750\).  
Verificamos: \(\sqrt{33750}\) y \(3\sqrt{3750}\).  
\(\sqrt{3750} = 5\sqrt{150} = 25\sqrt{6}\), no parece simplificarse igual que \(\sqrt{33750}\), pero la condición era elevar al cuadrado, así que basta \(33750 = 9\cdot 3750\). En efecto \(9\cdot 3750 = 33750\). Correcto.

### \(a=4\)

\[
m = \frac{40000}{16-1} = \frac{40000}{15},
\]

no entero.

### \(a=5\)

\[
m = \frac{50000}{25-1} = \frac{50000}{24} = \frac{12500}{6},
\]

no entero.

### \(a=6\)

\[
m = \frac{60000}{36-1} = \frac{60000}{35},
\]

no entero.

### \(a=7\)

\[
m = \frac{70000}{49-1} = \frac{70000}{48} = \frac{8750}{6},
\]

no entero.

### \(a=8\)

\[
m = \frac{80000}{64-1} = \frac{80000}{63},
\]

no entero.

### \(a=9\)

\[
m = \frac{90000}{81-1} = \frac{90000}{80} = 1125.

\]

Entero y de cuatro dígitos. Entonces \(n = 90000 + 1125 = 91125\).  
Verificamos: \(9\cdot 1125 = 10125 \neq 91125\). 

Espera, cuidado: la condición era \(n = a^2 m\). Veamos:

\[
n = 90000 + m = 90000 + 1125 = 91125.
\]

Y:

\[
a^2 m = 81 \cdot 1125 = 91125.
\]

Correcto.

---

## 3. Soluciones encontradas

Hemos encontrado dos números:

\[
33750 \quad\text{y}\quad 91125.
\]

Verifiquemos las raíces:

Para \(33750\):

\[
\sqrt{33750} = \sqrt{9 \cdot 3750} = 3\sqrt{3750}.
\]

Para \(91125\):

\[
\sqrt{91125} = \sqrt{81 \cdot 1125} = 9\sqrt{1125}.
\]

Ambas cumplen la condición.

---

## 4. Suma final

\[
33750 + 91125 = 124875.
\]

Por lo tanto, la suma de todos los posibles números de cinco dígitos es:

\[
\boxed{124875}
\]

*Fecha: 2026-10-29*