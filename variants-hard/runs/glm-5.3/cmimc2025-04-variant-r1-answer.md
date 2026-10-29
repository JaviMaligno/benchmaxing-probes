# Solución

## Planteamiento

Defino las variables auxiliares:
$$a = \log_x y, \qquad b = \log_y z, \qquad c = \log_z x.$$

Como $x, y, z \neq 1$ (todos los logaritmos existen), se cumple la identidad clave:
$$abc = \log_x y \cdot \log_y z \cdot \log_z x = 1.$$

## Traducción de las condiciones

**Condición 1:** $\log_x y + \log_y z + \log_z x = 10$ se convierte en:
$$a + b + c = 10. \tag{1}$$

**Condición 3:** como $\log_z y = \frac{1}{\log_y z} = \frac{1}{b}$ y $\log_x z = \frac{1}{\log_z x} = \frac{1}{c}$:
$$\frac{1}{b} + \frac{1}{c} = 25. \tag{2}$$

**Condición 2:** la base es $\log_y x = \frac{1}{a}$ (positiva y distinta de 1, pues $a \neq 1$). Entonces
$$\log_{1/a} z = -3 \;\Longrightarrow\; \left(\tfrac{1}{a}\right)^{-3} = z \;\Longrightarrow\; z = a^3. \tag{3}$$

## Resolución

De $abc = 1$ obtengo $bc = \frac{1}{a}$. La ecuación (2) se reescribe como:
$$\frac{b+c}{bc} = 25 \;\Longrightarrow\; b + c = 25 \cdot \frac{1}{a} = \frac{25}{a}.$$

Sustituyendo en (1), donde $b + c = 10 - a$:
$$10 - a = \frac{25}{a} \;\Longrightarrow\; 10a - a^2 = 25 \;\Longrightarrow\; a^2 - 10a + 25 = 0 \;\Longrightarrow\; (a-5)^2 = 0,$$

de modo que $a = 5$ (único).

## Valor de $z$

De (3):
$$z = a^3 = 5^3 = 125.$$

## Verificación de consistencia

Con $a=5$: $bc = \frac{1}{5}$ y $b+c = 5$, así que $b, c$ son las raíces de $t^2 - 5t + \frac{1}{5} = 0$, ambas reales positivas ($t = \frac{5\sqrt{5} \pm 11}{2\sqrt{5}}$). Tomando $x = e^{c\ln 125}$, $y = x^5$, $z = 125$, se cumplen las tres condiciones; por ejemplo, la base $\log_y x = \frac{1}{5}$ y $\log_{1/5} 125 = -3$. ✓

$$\boxed{125}$$