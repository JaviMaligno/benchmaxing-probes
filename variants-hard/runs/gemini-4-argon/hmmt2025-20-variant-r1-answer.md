Para hallar el número esperado de segundos hasta que solo quede una serpiente, analicemos las longitudes de los espacios vacíos (arcos libres) entre serpientes consecutivas.

### 1. Formulación del proceso en términos de los espacios vacíos
Inicialmente hay $12$ serpientes de longitud $1$ ubicadas cada tres arcos a lo largo de los $36$ arcos de la pista circular. Esto significa que entre cada par de serpientes adyacentes hay un espacio vacío de exactamente $2$ arcos libres, y la suma total de las longitudes de los $12$ espacios vacíos es:
$$36 - 12 \times 1 = 24 \text{ arcos.}$$

Cuando hay $m \ge 2$ serpientes en la pista, sean $g_1, g_2, \dots, g_m$ las longitudes (en arcos) de los $m$ espacios vacíos entre serpientes consecutivas. En cada segundo, la serpiente $i$ se desplaza $\xi_i \in \{-1, +1\}$ arcos con probabilidad $\frac{1}{2}$ cada uno, de manera independiente para cada serpiente. Por lo tanto, el espacio $g_i$ entre la serpiente $i$ y la serpiente $i+1$ cambia en:
$$\Delta g_i = \xi_{i+1} - \xi_i \in \{-2, 0, +2\}.$$

Como inicialmente cada $g_i = 2$ es par y en cada paso varía en un múltiplo de $2$, todos los $g_i$ son siempre pares. Dos serpientes se tocan y se fusionan exactamente cuando el espacio vacío entre ellas se reduce a $g_i = 0$ (es decir, pasan a ocupar arcos contiguos), momento en el cual dicho espacio desaparece y la longitud total de las serpientes sigue siendo $12$, por lo que la suma de los espacios vacíos restantes se mantiene constante e igual a $24$.

### 2. Construcción de una martingala
Definamos $y_i = \frac{g_i}{2}$ para cada espacio vacío.
- Inicialmente, en $t = 0$, hay $m = 12$ espacios con $y_1 = y_2 = \dots = y_{12} = 1$.
- En todo instante $t$, la suma de las variables $y_i$ es invariante:
$$\sum_{i=1}^m y_i = \frac{24}{2} = 12.$$
- En cada segundo, mientras haya $m \ge 2$ serpientes, las dos serpientes que delimitan el espacio $y_i$ son distintas, por lo que sus desplazamientos $\xi_i$ y $\xi_{i+1}$ son independientes. En consecuencia, el cambio $\Delta y_i = \frac{\xi_{i+1} - \xi_i}{2}$ toma los valores:
$$
\Delta y_i = 
\begin{cases}
+1 & \text{con probabilidad } \frac{1}{4}, \\
0 & \text{con probabilidad } \frac{1}{2}, \\
-1 & \text{con probabilidad } \frac{1}{4}.
\end{cases}
$$
- Cuando algún $y_i$ llega a $0$, ese espacio desaparece (o equivalentemente permanece en $0$). El proceso termina en el tiempo de parada $\tau$ en que queda una sola serpiente, lo que corresponde a que un único espacio alcance el valor $y = 12$ y todos los demás sean $0$.

Consideremos la función $f(y) = y^3$. Nótese que $f(0) = 0$ (de modo que los espacios que llegan a $0$ no aportan a la suma) y, para cualquier espacio $y_i \ge 1$:
$$\mathbb{E}\left[(y_i + \Delta y_i)^3 - y_i^3 \,\middle|\, y_i\right] = \frac{1}{4}(y_i+1)^3 + \frac{1}{2}y_i^3 + \frac{1}{4}(y_i-1)^3 - y_i^3 = \frac{1}{4}(6y_i) = \frac{3}{2}y_i.$$

Sumando sobre todos los $m$ espacios activos en el instante $t < \tau$ y usando la linealidad de la esperanza junto con el invariante $\sum_{i=1}^m y_i(t) = 12$, obtenemos:
$$\mathbb{E}\left[\sum_{i=1}^m y_i(t+1)^3 - \sum_{i=1}^m y_i(t)^3 \,\middle|\, \mathcal{F}_t\right] = \frac{3}{2} \sum_{i=1}^m y_i(t) = \frac{3}{2} \cdot 12 = 18.$$

Por lo tanto, si definimos el potencial
$$\Phi(t) = \frac{1}{18} \sum_{i=1}^m y_i(t)^3,$$
entonces $M_t = \Phi(t) - t$ es una martingala hasta el tiempo de parada $\tau$.

### 3. Cálculo del tiempo esperado
Dado que el espacio de estados es finito y $\mathbb{E}[\tau] < \infty$, por el teorema de parada opcional de Doob se cumple que $\mathbb{E}[M_\tau] = \mathbb{E}[M_0]$, es decir:
$$\mathbb{E}[\tau] = \mathbb{E}[\Phi(\tau)] - \Phi(0).$$

Evaluamos $\Phi$ en el estado inicial ($12$ espacios con $y_i = 1$) y en el estado final ($1$ espacio con $y_1 = 12$):
$$\Phi(0) = \frac{1}{18} \sum_{i=1}^{12} 1^3 = \frac{12}{18} = \frac{2}{3},$$
$$\Phi(\tau) = \frac{1}{18} \cdot 12^3 = \frac{1728}{18} = 96.$$

Finalmente:
$$\mathbb{E}[\tau] = 96 - \frac{2}{3} = \frac{286}{3}.$$

\boxed{\frac{286}{3}}