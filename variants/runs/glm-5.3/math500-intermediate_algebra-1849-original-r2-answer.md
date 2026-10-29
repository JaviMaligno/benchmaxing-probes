## Razonamiento

**Planteamiento.** La ecuación es $\log(kx) = 2\log(x+2)$. El dominio exige:
- $x > -2$ (para $\log(x+2)$),
- $kx > 0$ (para $\log(kx)$).

En el dominio, la ecuación equivale a $kx = (x+2)^2$, es decir:
$$x^2 + (4-k)x + 4 = 0$$

**Análisis por casos.**

El discriminante es $(4-k)^2 - 16 = k(k-8)$, así que hay raíces reales solo si $k \le 0$ o $k \ge 8$. Notemos que el producto de raíces es $4 > 0$ (ambas del mismo signo) y la suma es $k-4$.

**Caso $k > 8$:** ambas raíces son positivas (suma $k-4>0$), luego cumplen $x>-2$ y $kx>0$. Hay **dos** soluciones válidas → no cuenta.

**Caso $k = 8$:** raíz doble $x = 2$. Verificamos: $\log(16) = 2\log 4 = \log 16$ ✓. Hay **exactamente una** solución real → cuenta.

**Caso $k = 0$:** $\log(kx)$ no está definida; además $kx = (x+2)^2$ daría $x = -2$, fuera del dominio. **Cero** soluciones → no cuenta.

**Caso $0 < k < 8$:** discriminante negativo → no cuenta.

**Caso $k < 0$:** ambas raíces son negativas (suma $k-4 < 0$). Evaluando $f(x) = x^2+(4-k)x+4$:
- $f(-2) = 2k < 0$,
- $f(0) = 4 > 0$.

Como la parábola abre hacia arriba y $f(-2)<0$, el punto $x=-2$ está entre las dos raíces: la raíz menor es $< -2$ (inválida) y la raíz mayor está en $(-2, 0)$ (válida, pues con $k<0$ y $x<0$ se cumple $kx>0$). Por tanto hay **exactamente una** solución válida para cada $k < 0$.

Verificación con $k=-1$: $x^2+5x+4=0 \Rightarrow x=-1,-4$. Solo $x=-1$ es válida: $\log(1) = 2\log(1) = 0$ ✓.

**Conteo.**
- $k \in \{-500, \dots, -1\}$: $500$ valores.
- $k = 8$: $1$ valor.

Total: $500 + 1 = 501$.

$$\boxed{501}$$