**Paso 1: Expresamos los primeros términos en función de $t = b_1$.**

$$b_2 = -\frac{1}{1+t}, \qquad b_3 = -\frac{1}{1+b_2} = -\frac{1}{1-\frac{1}{1+t}} = -\frac{1+t}{t}.$$

**Paso 2: Usamos la condición $b_3 = b_1 = t$.**

$$-\frac{1+t}{t} = t \;\Longrightarrow\; -(1+t) = t^2 \;\Longrightarrow\; t^2 + t + 1 = 0.$$

**Paso 3: Consecuencia clave de esa ecuación.**

Como $t \neq 0$ y $t \neq 1$ (pues $1^2+1+1 \neq 0$), y
$$(t-1)(t^2+t+1) = t^3 - 1,$$
obtenemos $t^3 = 1$. Es decir, $t$ es una raíz cúbica primitiva de la unidad: $t = e^{\pm 2\pi i/3}$.

**Paso 4: La sucesión es constante.**

Usando $1+t = -t^2$:
$$b_2 = -\frac{1}{1+t} = -\frac{1}{-t^2} = \frac{1}{t^2} = t \quad (\text{pues } t^3 = 1).$$
Como $b_3 = b_1$ también se cumple, por inducción $b_k = t$ para todo $k$. En particular,
$$b_9 = t.$$

*(Alternativamente: la condición $b_3 = b_1$ fuerza período 2, y $9$ es impar, así que $b_9 = b_1 = t$.)*

**Paso 5: Calculamos $(b_9)^9$.**

$$(b_9)^9 = t^9 = (t^3)^3 = 1^3 = 1.$$

$$\boxed{1}$$