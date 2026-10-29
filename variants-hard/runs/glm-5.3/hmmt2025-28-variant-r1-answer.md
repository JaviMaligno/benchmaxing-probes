# Resolución

**Configuración de coordenadas.** Por la simetría del trapecio isósceles, pongamos el eje de simetría en el eje $y$:

- $S=(-a,0)$, $R=(a,0)$, con $RS=2a>6$, es decir, $a>3$;
- $P=(-3,h)$, $Q=(3,h)$, con $PQ=6$.

Como el trapecio es isósceles, $P,Q,R,S$ son cíclicos y el centro de su circunferencia está en el eje de simetría: sea $(0,k)$ el centro, con radio $7$.

**Punto $T$.** Como $ST=3$ y $S$ está entre $T$ y $R$, el punto $T$ queda del lado opuesto a $R$: $T=(-a-3,\,0)$. Entonces el punto medio de $\overline{PT}$ es

$$N=\left(-\frac{a+6}{2},\ \frac{h}{2}\right).$$

**Ecuaciones del problema.**

1. $S$ en la circunferencia: $\;a^2+k^2=49$.
2. $P$ en la circunferencia: $\;9+(h-k)^2=49$, y si escribimos $u=h-k$ (con lo cual $h=u+k$): $\;u^2=40$.
3. $N$ en la circunferencia: $\left(\frac{a+6}{2}\right)^2+\left(\frac h2-k\right)^2=49$, es decir,
$$(a+6)^2+(h-2k)^2=196.$$

Como $h-2k=u-k$, al expandir la ecuación 3 y usar la ecuación 1:

$$a^2+12a+36+\underbrace{u^2-2uk+k^2}_{40-2uk+k^2}=196 \;\Longrightarrow\; 49+12a+76-2uk=196 \;\Longrightarrow\; uk=\frac{12a-71}{2}.$$

**Cálculo de $NS$.** Con $N=\left(-\frac{a+6}{2},\frac h2\right)$ y $S=(-a,0)$:

$$NS^2=\left(\frac{a-6}{2}\right)^2+\left(\frac h2\right)^2=\frac{(a-6)^2+h^2}{4}.$$

Ahora, usando $h=u+k$, junto con $u^2=40$, $k^2=49-a^2$ y $uk=\frac{12a-71}{2}$:

$$(a-6)^2+h^2=(a^2-12a+36)+\underbrace{(u^2+2uk+k^2)}_{h^2}=a^2+k^2-12a+36+40+(12a-71)$$

y los términos en $a$ se cancelan:

$$(a-6)^2+h^2=49+36+40-71=54.$$

**Conclusión.** Por lo tanto

$$NS^2=\frac{54}{4}=\frac{27}{2}\qquad\Longrightarrow\qquad NS=\frac{3\sqrt6}{2}.$$

(Verificación numérica: la configuración válida tiene $a\approx 6.93$, $h\approx 7.29$, y en efecto $NS\approx 3.67=\frac{3\sqrt6}{2}$.)

$$\boxed{\dfrac{3\sqrt{6}}{2}}$$