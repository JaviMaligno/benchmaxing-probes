Vamos a razonar paso a paso.

Sea $P$ un polinomio mónico, no constante, con coeficientes enteros, tal que

\[
P(\sqrt{3}+\sqrt{2}) = P(\sqrt{3}-\sqrt{2}).
\]

Queremos el elemento de grado mínimo y después calcular $Q(10)-Q(0)$.

---

## 1. Interpretación algebraica

Los números $\sqrt{3}+\sqrt{2}$ y $\sqrt{3}-\sqrt{2}$ son conjugados algebraicos. De hecho,

\[
\sqrt{3}+\sqrt{2} \quad\text{y}\quad \sqrt{3}-\sqrt{2}
\]

son conjugados bajo $\mathbb{Q}(\sqrt2,\sqrt3)$, pues corresponden a los cambios de signo de $\sqrt2$.

Por tanto, la condición $P(a)=P(b)$ con $a\neq b$ y enteros, implica que $P$ no es inyectivo sobre los conjugados, lo que fuerza relaciones en los coeficientes.

---

## 2. Polinomio mínimo de grado pequeño

Si $P$ tiene grado $1$, es $P(x)=x+c$, pero entonces

\[
(\sqrt3+\sqrt2)+c = (\sqrt3-\sqrt2)+c
\]

implicaría $\sqrt2=0$, absurdo. Luego grado $1$ no sirve.

Probamos grado $2$. Sea $P(x)=x^{2}+ax+b$, con $a,b\in\mathbb{Z}$.

Condición:

\[
(\sqrt3+\sqrt2)^2+a(\sqrt3+\sqrt2)+b = (\sqrt3-\sqrt2)^2+a(\sqrt3-\sqrt2)+b.
\]

Calculamos:

\[
(\sqrt3+\sqrt2)^2 = 3+2+2\sqrt6 = 5+2\sqrt6,
\]
\[
(\sqrt3-\sqrt2)^2 = 3+2-2\sqrt6 = 5-2\sqrt6.
\]

Entonces:

\[
5+2\sqrt6+a\sqrt3+a\sqrt2+b 
=
5-2\sqrt6+a\sqrt3-a\sqrt2+b.
\]

Cancelando $5$, $a\sqrt3$, $b$:

\[
2\sqrt6+a\sqrt2 = -2\sqrt6-a\sqrt2.
\]

Pasamos todo:

\[
4\sqrt6+2a\sqrt2=0.
\]

Dividimos entre $2$:

\[
2\sqrt6+a\sqrt2=0.
\]

Factorizamos $\sqrt2$:

\[
\sqrt2\,(2\sqrt3+a)=0.
\]

Como $\sqrt2\neq0$:

\[
2\sqrt3+a=0 \implies a=-2\sqrt3.
\]

Pero $a$ debe ser entero, así que no hay solución de grado $2$.

---

## 3. Grado 3

Probamos un polinomio cúbico mónico

\[
P(x)=x^{3}+ax^{2}+bx+c,\qquad a,b,c\in\mathbb{Z}.
\]

La condición $P(\sqrt3+\sqrt2)=P(\sqrt3-\sqrt2)$ debe imponer restricciones enteras.

En vez de desarrollar todo, observemos que los números

\[
\alpha=\sqrt3+\sqrt2,\qquad \beta=\sqrt3-\sqrt2
\]

satisfacen

\[
\alpha\beta = 3-2=1.
\]

Por tanto $\beta=1/\alpha$. Entonces la condición es

\[
P(\alpha)=P(1/\alpha).
\]

Para un polinomio mónico de grado $n$:

\[
P(\alpha)=P(1/\alpha)
\]

equivale, tras multiplicar por $\alpha^{n}$:

\[
\alpha^{n}P(1/\alpha) = \alpha^{n}P(\alpha)
\]

y como $P$ es mónico, $\alpha^{n}P(1/\alpha)$ es el polinomio recíproco de $P$.

---

## 4. Uso del polinomio recíproco

Para $P(x)=x^{3}+ax^{2}+bx+c$, el recíproco es

\[
x^{3}P(1/x)=1+ax+bx^{2}+cx^{3}.
\]

La igualdad $P(\alpha)=P(1/\alpha)$ equivale a

\[
P(\alpha)=\frac{1+ a\alpha + b\alpha^2 + c\alpha^3}{\alpha^{3}}.
\]

Multiplicando por $\alpha^{3}$:

\[
\alpha^{3}P(\alpha)=1+a\alpha+b\alpha^{2}+c\alpha^{3}.
\]

Es decir,

\[
\alpha^{3}(\alpha^{3}+a\alpha^{2}+b\alpha+c)
=
1+a\alpha+b\alpha^{2}+c\alpha^{3}.
\]

Agrupamos y usamos el polinomio mínimo de $\alpha$.

---

## 5. Polinomio mínimo de $\alpha=\sqrt3+\sqrt2$

\[
\alpha^2=5+2\sqrt6
\]

y

\[
\alpha^4=(\alpha^2)^2 = (5+2\sqrt6)^2=25+24+20\sqrt6=49+20\sqrt6.
\]

Observamos:

\[
\alpha^4-10\alpha^2 = 49+20\sqrt6 - 50 -20\sqrt6 = -1.
\]

Por tanto

\[
\alpha^4-10\alpha^2+1=0.
\]

Así $\alpha$ satisface $x^{4}-10x^{2}+1=0$. Este polinomio es irreducible sobre $\mathbb{Q}$, así que $[\mathbb{Q}(\alpha):\mathbb{Q}]=4$.

---

## 6. Condición de grado mínimo

El grado de $P$ que funciona debe ser al menos... veamos. El polinomio

\[
x^{4}-10x^{2}+1
\]

es mónico, no constante, y cumple

\[
P(\alpha)=P(\beta)
\]

porque tanto $\alpha$ como $\beta$ son raíces de $x^{4}-10x^{2}+1$ (ambos dan $0$). Entonces $P(\alpha)=P(\beta)=0$.

¿Hay algún polinomio de grado $3$ o menor que funcione? Acabamos de ver que $1$ y $2$ no. Revisando grado $3$.

---

## 7. Grado 3: ¿existe solución?

La igualdad debe cumplirse para todo par de conjugados que difieren en el signo de $\sqrt2$, así que fuerza

\[
P(\sqrt3+\sqrt2)-P(\sqrt3-\sqrt2)=0.
\]

Expandiendo $P(x)=x^{3}+ax^{2}+bx+c$:

\[
P(\alpha)-P(\beta)
=(\alpha^3-\beta^3)+a(\alpha^2-\beta^2)+b(\alpha-\beta).
\]

Con

\[
\alpha-\beta=2\sqrt2,
\]
\[
\alpha+\beta=2\sqrt3,
\]
\[
\alpha^2-\beta^2=(\alpha-\beta)(\alpha+\beta)=2\sqrt2\cdot 2\sqrt3=4\sqrt6,
\]
\[
\alpha^3-\beta^3=(\alpha-\beta)(\alpha^2+\alpha\beta+\beta^2).
\]

Ya vimos $\alpha\beta=1$ y $\alpha^2+\beta^2=(\alpha+\beta)^2-2\alpha\beta=(2\sqrt3)^2-2=12-2=10$. Entonces

\[
\alpha^2+\alpha\beta+\beta^2=10+1=11.
\]

Luego

\[
\alpha^3-\beta^3 = 2\sqrt2 \cdot 11 = 22\sqrt2.
\]

Entonces:

\[
P(\alpha)-P(\beta)
=22\sqrt2+4a\sqrt6+2b\sqrt2.
\]

Factorizando $\sqrt2$:

\[
\sqrt2\,(22+2b+4a\sqrt3)=0.
\]

Luego

\[
22+2b+4a\sqrt3=0.
\]

Separando parte racional e irracional, necesitamos $a=0$ y $22+2b=0$, es decir $b=-11$.

Por tanto el polinomio mónico de grado $3$ sería

\[
P(x)=x^{3}-11x+c.
\]

Veamos si cumple exactamente:

\[
P(\alpha)-P(\beta)=\alpha^3-\beta^3 -11(\alpha-\beta).
\]

\[
\alpha^3-\beta^3=22\sqrt2,\qquad 11(\alpha-\beta)=22\sqrt2.
\]

Así que la diferencia es $0$. Entonces sí cumple para todo $c\in\mathbb{Z}$.

---

## 8. Grado mínimo

Hemos encontrado grado $3$. Grado $1$ y $2$ no funcionan. Por tanto el grado mínimo es $3$.

Entonces el polinomio de grado mínimo tiene la forma

\[
Q(x)=x^{3}-11x+c,
\]

con $c\in\mathbb{Z}$ y $Q$ mónico.

---

## 9. Comprobar que solo hay un valor posible de $Q(10)-Q(0)$

Calculamos:

\[
Q(10)-Q(0)
=
(10^{3}-11\cdot 10+c) - (0^{3}-11\cdot 0+c).
\]

\[
10^{3}=1000,\qquad 11\cdot10=110.
\]

Entonces

\[
Q(10)-Q(0)
=
(1000-110+c)-(c)
=
890.
\]

El término $c$ se cancela, así que el valor es único.

---

Por tanto, la respuesta es

\[
\boxed{890}
\]