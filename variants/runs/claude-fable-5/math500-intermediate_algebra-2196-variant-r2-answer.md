## Solución

**Planteamiento.** Queremos maximizar
$$f(a,b)=\frac{a-b}{a^4+b^4+96}.$$

Para que el valor sea positivo necesitamos $a>b$, así que buscamos la mejor cota de la forma $a^4+b^4+96 \ge C(a-b)$.

**Simetría.** La expresión es invariante bajo el cambio $(a,b)\mapsto(-b,-a)$. En un punto crítico, al igualar las derivadas parciales a cero:
- $\partial_a$: $(a^4+b^4+96) - (a-b)\cdot 4a^3 = 0$
- $\partial_b$: $-(a^4+b^4+96) - (a-b)\cdot 4b^3 = 0$

Sumando ambas: $-4(a-b)(a^3+b^3)=0$. Como $a\ne b$ en el máximo, se obtiene $b=-a$.

**Reducción a una variable.** Con $b=-a$:
$$f(a,-a)=\frac{2a}{2a^4+96}=\frac{a}{a^4+48}.$$
Derivando: $\dfrac{(a^4+48)-4a^4}{(a^4+48)^2}=0 \Rightarrow a^4=16 \Rightarrow a=2$ (tomamos la raíz positiva), lo que da
$$f(2,-2)=\frac{2}{16+48}=\frac{2}{64}=\frac{1}{32}.$$

**Verificación por AM–GM (cota global).** Por la desigualdad de medias:
$$a^4+16+16+16 \ge 4\sqrt[4]{a^4\cdot 16^3}=32|a|\ge 32a,$$
$$b^4+16+16+16 \ge 32|b|\ge -32b.$$
Sumando: $a^4+b^4+96 \ge 32(a-b)$, con igualdad en $a=2,\ b=-2$. Por tanto
$$\frac{a-b}{a^4+b^4+96}\le \frac{1}{32}$$
para todos los reales $a,b$, y el valor se alcanza.

$$\boxed{\dfrac{1}{32}}$$