Sea $w=e^{i\theta}$. Como $|w|=1$:
$$|1+w|=|1+e^{i\theta}|=2\left|\cos\frac{\theta}{2}\right|.$$

Para el segundo término, usamos $2-2w+2w^2=2(1-w+w^2)$. Notemos que $1-w+w^2=\frac{1+w^3}{1+w}$ (para $w\ne -1$), lo que sugiere otro camino, pero trabajemos directo:
$$1-w+w^2 = w(w^{-1}-1+w) = w(2\cos\theta - 1),$$
donde $w^{-1}+w=2\cos\theta$. Luego
$$|2-2w+2w^2|=2|2\cos\theta-1|.$$

La expresión es
$$F(\theta)=2\left|\cos\frac{\theta}{2}\right|+2|2\cos\theta-1|.$$

Sea $c=\cos\theta$, con $\left|\cos\frac{\theta}{2}\right|=\sqrt{\frac{1+c}{2}}$. Entonces
$$F=2\sqrt{\frac{1+c}{2}}+2|2c-1|,\quad c\in[-1,1].$$

Distinguimos dos casos:

**Caso $c\le \frac12$:** $F=2\sqrt{\frac{1+c}{2}}+2(1-2c)$. Esta función decrece en $c$ (su derivada respecto a $c$ es $\frac{1}{\sqrt{2(1+c)}}-4$, que es negativa salvo cerca de $c=-1$; verificamos extremos). Su máximo en este intervalo ocurre en el mínimo de $c$, es decir $c=-1$, dando
$$F=2\cdot 0+2(1-2(-1))=6.$$

**Caso $c\ge \frac12$:** $F=2\sqrt{\frac{1+c}{2}}+2(2c-1)$. Su derivada es $\frac{1}{\sqrt{2(1+c)}}+4>0$, así que crece; su máximo en este intervalo es en $c=1$, dando
$$F=2+2=4.$$

Por tanto el máximo es $6$, alcanzado para $c=-1$, es decir $\theta=\pi$, $w=-1$. Verificamos: $|1+w|=0$ y $|2-2(-1)+2|=|6|=6$.

$$\boxed{6}$$