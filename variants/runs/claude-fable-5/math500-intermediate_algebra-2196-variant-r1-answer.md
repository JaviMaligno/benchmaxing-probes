Queremos maximizar $f(a,b)=\dfrac{a-b}{a^4+b^4+96}$. Como el denominador es siempre positivo, el máximo requiere $a-b>0$.

**Condiciones de punto crítico.** Igualando las derivadas parciales a cero:

- Respecto a $a$: $(a^4+b^4+96) - (a-b)\cdot 4a^3 = 0$
- Respecto a $b$: $-(a^4+b^4+96) - (a-b)\cdot 4b^3 = 0$

Sumando ambas ecuaciones: $-4(a-b)(a^3+b^3)=0$. Como $a-b\neq 0$, se obtiene $a^3+b^3=0$, es decir $b=-a$.

**Sustituyendo $b=-a$.** La primera ecuación queda:
$$2a^4+96 = (2a)(4a^3)=8a^4 \;\Longrightarrow\; 6a^4=96 \;\Longrightarrow\; a^4=16 \;\Longrightarrow\; a=2,\; b=-2.$$

**Valor:**
$$\frac{2-(-2)}{2^4+(-2)^4+96}=\frac{4}{16+16+96}=\frac{4}{128}=\frac{1}{32}.$$

**Verificación de que es máximo.** Con $b=-a$, $g(a)=\dfrac{2a}{2a^4+96}=\dfrac{a}{a^4+48}$, y $g'(a)=\dfrac{48-3a^4}{(a^4+48)^2}$, que cambia de positivo a negativo en $a^4=16$, confirmando el máximo. Además $f\to 0$ cuando $|a|,|b|\to\infty$, así que el máximo global es este punto crítico.

$$\boxed{\dfrac{1}{32}}$$