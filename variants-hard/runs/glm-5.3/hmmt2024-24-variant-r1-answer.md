## Planteamiento

Coloco el cuadrado en coordenadas: $P=(0,s)$, $Q=(s,s)$, $R=(s,0)$, $S=(0,0)$, con lado $s$. El punto medio de $\overline{PQ}$ es $M=(s/2,\, s)$.

La recta $m$ pasa por $M$ con pendiente $k$:
$$kx - y + s - \tfrac{ks}{2} = 0.$$

Como $m$ interseca el segmento $\overline{QR}$ (donde $x=s$), se necesita $0 \le s + \tfrac{ks}{2} \le s$, es decir $-2 \le k \le 0$.

## Condiciones de distancia

**Distancia de $P=(0,s)$ a $m$ igual a 5:**
$$\frac{|{-s} + s - \tfrac{ks}{2}|}{\sqrt{k^2+1}} = \frac{-ks/2}{\sqrt{k^2+1}} = 5 \quad (\text{pues } k \le 0).$$

**Distancia de $R=(s,0)$ a $m$ igual a 8:**
$$\frac{|ks + s - \tfrac{ks}{2}|}{\sqrt{k^2+1}} = \frac{s(1+\tfrac{k}{2})}{\sqrt{k^2+1}} = 8 \quad (\text{pues } 1 + \tfrac{k}{2} \ge 0).$$

## Resolución

De la primera ecuación: $\dfrac{s}{\sqrt{k^2+1}} = -\dfrac{10}{k}$. Sustituyendo en la segunda:

$$-\frac{10\left(1+\tfrac{k}{2}\right)}{k} = 8 \;\Longrightarrow\; -10 - 5k = 8k \;\Longrightarrow\; k = -\frac{10}{13}.$$

(Válido, pues $-2 \le -\tfrac{10}{13} \le 0$.) Entonces:

$$\frac{s}{\sqrt{k^2+1}} = \frac{13}{\sqrt{269}/13} = \frac{169}{\sqrt{269}} = 13 \;\Longrightarrow\; s = \sqrt{269}.$$

**Verificación:** distancia de $P$: $\dfrac{(10/13)\sqrt{269}}{2\sqrt{269}/13} = 5$ ✓; distancia de $R$: $\dfrac{\sqrt{269}\cdot(8/13)}{\sqrt{269}/13} = 8$ ✓.

El área es $s^2 = 269$.

$$\boxed{269}$$