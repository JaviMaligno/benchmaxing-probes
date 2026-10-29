Para encontrar las raíces de la ecuación dada:
\[z^8 - z^7 + z^6 - z^5 + z^4 - z^3 + z^2 - z + 1 = 0,\]
podemos observar que el lado izquierdo es la suma de una progresión geométrica con razón común $-z$. Multiplicando ambos lados de la ecuación por $(z + 1)$ (asumiendo que $z \neq -1$), obtenemos:
\[(z + 1)(z^8 - z^7 + z^6 - z^5 + z^4 - z^3 + z^2 - z + 1) = 0\]
\[z^9 + 1 = 0\]
\[z^9 = -1.\]

Por lo tanto, las raíces del polinomio original son todas las raíces novenas de $-1$, excepto $z = -1$ (ya que al sustituir $z = -1$ en la ecuación original se obtiene $9 \neq 0$).

Escribiendo $z = re^{i\theta}$ y $-1 = e^{i(\pi + 2k\pi)}$ para $k \in \mathbb{Z}$, tenemos:
\[r^9 e^{i9\theta} = e^{i(2k+1)\pi}.\]

Igualando los módulos y los argumentos:
1. $r^9 = 1 \implies r = 1$ (dado que $r > 0$).
2. $9\theta = (2k+1)\pi \implies \theta = \frac{(2k+1)\pi}{9}.$

Para que $0 \le \theta < 2\pi$, $k$ puede tomar los valores $k = 0, 1, 2, 3, 4, 5, 6, 7, 8$, lo que nos da los siguientes ángulos:
\[\theta \in \left\{ \frac{\pi}{9}, \frac{3\pi}{9}, \frac{5\pi}{9}, \frac{7\pi}{9}, \frac{9\pi}{9}, \frac{11\pi}{9}, \frac{13\pi}{9}, \frac{15\pi}{9}, \frac{17\pi}{9} \right\}.\]

Excluyendo la raíz $z = -1$, que corresponde a $k = 4$ ($\theta = \frac{9\pi}{9} = \pi$), nos quedan 8 valores posibles para $\theta$:
\[\frac{\pi}{9}, \frac{3\pi}{9}, \frac{5\pi}{9}, \frac{7\pi}{9}, \frac{11\pi}{9}, \frac{13\pi}{9}, \frac{15\pi}{9}, \frac{17\pi}{9}.\]

Agrupando los ángulos simétricos en pares que suman $2\pi$:
\[\left(\frac{\pi}{9} + \frac{17\pi}{9}\right) + \left(\frac{3\pi}{9} + \frac{15\pi}{9}\right) + \left(\frac{5\pi}{9} + \frac{13\pi}{9}\right) + \left(\frac{7\pi}{9} + \frac{11\pi}{9}\right) = 2\pi + 2\pi + 2\pi + 2\pi = 8\pi.\]

\boxed{8\pi}