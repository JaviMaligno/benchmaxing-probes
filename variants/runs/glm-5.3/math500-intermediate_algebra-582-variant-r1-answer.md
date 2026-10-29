# Solución

**Paso 1: Transformar a los recíprocos de las raíces.**

Sea $P(x) = x^{10} + (11x-1)^{10}$. Como el término constante es $(-1)^{10} = 1 \neq 0$, ninguna raíz es cero, así que podemos tomar recíprocos. Sustituyendo $x = 1/y$:

$$y^{10}P(1/y) = 1 + (11-y)^{10} =: Q(y).$$

Las raíces de $Q$ son exactamente los recíprocos de las raíces de $P$. Como $Q(y)=0$ equivale a $(y-11)^{10} = -1$, sus raíces son

$$y_k = 11 + \zeta_k, \qquad k = 1,\dots,10,$$

donde los $\zeta_k$ son las raíces décimas de $-1$: todos cumplen $|\zeta_k| = 1$ y $\sum_k \zeta_k = 0$ (son raíces de $z^{10}+1$, cuyo coeficiente de $z^9$ es nulo).

**Paso 2: Reescribir la suma pedida.**

Como $P$ (y por tanto $Q$) tiene coeficientes reales y ninguna raíz es real (si $x\in\mathbb{R}$, ambos términos son $\ge 0$ y no se anulan a la vez), las raíces de $Q$ se emparejan como $\left(\tfrac{1}{s_i},\ \tfrac{1}{\overline{s_i}}\right)$. Entonces:

$$\sum_{k=1}^{10}|y_k|^2 = \sum_{i=1}^{5}\left(\frac{1}{|s_i|^2} + \frac{1}{|\overline{s_i}|^2}\right) = 2\sum_{i=1}^{5}\frac{1}{s_i\overline{s_i}}.$$

**Paso 3: Calcular $\sum |y_k|^2$.**

$$|y_k|^2 = (11+\zeta_k)(11+\overline{\zeta_k}) = 121 + 11(\zeta_k + \overline{\zeta_k}) + |\zeta_k|^2.$$

Sumando sobre $k$:

$$\sum_{k=1}^{10}|y_k|^2 = 10\cdot 121 + 11\sum_k(\zeta_k + \overline{\zeta_k}) + 10\cdot 1 = 1210 + 22\,\mathrm{Re}\!\left(\sum_k \zeta_k\right) + 10 = 1210 + 0 + 10 = 1220.$$

**Paso 4: Conclusión.**

$$\sum_{i=1}^{5}\frac{1}{s_i\overline{s_i}} = \frac{1220}{2} = 610.$$

*(Verificación con el caso análogo $x^2+(3x-1)^2=0$: raíces $\frac{3\pm i}{10}$, y el método da $\frac{2\cdot 10}{2} = 10 = \frac{1}{|s|^2}$ ✓.)*

$$\boxed{610}$$