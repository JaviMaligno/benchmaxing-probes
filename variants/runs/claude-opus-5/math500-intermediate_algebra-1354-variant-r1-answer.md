## Razonamiento

**1. 2027 es primo.** Basta comprobar divisores hasta $\sqrt{2027}\approx 45$: ninguno de $2,3,5,7,11,13,17,19,23,29,31,37,41,43$ lo divide (p. ej. $43\cdot 47=2021$, $41\cdot 49=2009$). Por tanto, si $z^{2027}=1$ con $z\neq 1$, entonces $z$ es una raíz **primitiva** de orden 2027.

**2. Los términos recorren todas las raíces.** Como $z$ tiene orden 2027, las potencias $z^1, z^2,\dots,z^{2027}$ son exactamente las 2027 raíces de $x^{2027}=1$, cada una una sola vez (incluyendo $z^{2027}=1$). Así que la suma pedida es
$$S=\sum_{w^{2027}=1}\frac{1}{1+w}.$$

Nótese que $1+w\neq 0$ siempre, pues $w=-1$ no es raíz (2027 es impar).

**3. Emparejamiento $w \leftrightarrow w^{-1}$.** La inversión permuta el conjunto de raíces, y
$$\frac{1}{1+w}+\frac{1}{1+w^{-1}}=\frac{1}{1+w}+\frac{w}{w+1}=\frac{1+w}{1+w}=1.$$

El único punto fijo de esta involución es $w=1$ (ya que $w^2=1$ y $w=-1$ no es raíz), que aporta $\frac{1}{1+1}=\frac12$. Las $2026$ raíces restantes forman $1013$ parejas, cada una con suma $1$.

**4. Total:**
$$S=\frac12+1013=\frac{2027}{2}.$$

$$\boxed{\dfrac{2027}{2}}$$