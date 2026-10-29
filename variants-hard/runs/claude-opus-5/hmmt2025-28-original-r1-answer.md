## Planteamiento

Coloco $CD$ sobre el eje $x$ y uso la simetría del trapecio isósceles (el centro de la circunferencia está en el eje $y$):

- $D=(-c,0)$, $C=(c,0)$ con $c>2$
- $A=(-2,h)$, $B=(2,h)$
- $E=(-c-2,0)$ (pues $DE=2$ y $D$ está entre $E$ y $C$)
- $M=\left(-\tfrac{c+4}{2},\ \tfrac{h}{2}\right)$
- Centro $O=(0,k)$, radio $5$

## Ecuaciones

**Por $D$ (y $C$):**
$$c^2+k^2=25$$

**Por $A$ (y $B$):**
$$4+(h-k)^2=25\ \Longrightarrow\ (h-k)^2=21$$

**Por $M$:**
$$\frac{(c+4)^2}{4}+\left(\frac h2-k\right)^2=25\ \Longrightarrow\ (c+4)^2+(h-2k)^2=100$$

Desarrollando la última y usando $c^2=25-k^2$:
$$8c+h^2-4hk+3k^2=59$$

De $(h-k)^2=21$ se obtiene $h^2=21+2hk-k^2$; al sustituir:
$$8c-2hk+2k^2=38\ \Longrightarrow\ hk-k^2=4c-19$$

## Cálculo de $MD$

$$MD^2=\left(\frac{4-c}{2}\right)^2+\frac{h^2}{4}=\frac{(4-c)^2+h^2}{4}$$

Numerador:
$$16-8c+c^2+h^2 = 16-8c+(25-k^2)+(21+2hk-k^2)=62-8c+2(hk-k^2)$$

Y como $hk-k^2=4c-19$:
$$=62-8c+8c-38=24$$

Por tanto $MD^2=\dfrac{24}{4}=6$.

(Verificación numérica: $c\approx 4{,}99541$, $k\approx 0{,}21421$, $h\approx 4{,}79679$, que cumplen las tres condiciones y dan $MD\approx 2{,}4495$.)

\boxed{\sqrt{6}}