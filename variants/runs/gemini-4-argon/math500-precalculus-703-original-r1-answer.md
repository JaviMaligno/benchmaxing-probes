Para hallar las raíces del polinomio dado, observamos que la ecuación
\[z^8 - z^7 + z^6 - z^5 + z^4 - z^3 + z^2 - z + 1 = 0\]
corresponde a una suma geométrica de razón $-z$. Multiplicando ambos lados por $z + 1$ (con $z \neq -1$), obtenemos:
\[(z + 1)(z^8 - z^7 + z^6 - z^5 + z^4 - z^3 + z^2 - z + 1) = z^9 + 1 = 0.\]

Por lo tanto, las raíces del polinomio son las raíces novenas de $-1$, excluyendo $z = -1$:
\[z^9 = -1 = e^{i\pi}.\]

Sustituyendo $z = re^{i\theta}$ con $r > 0$ y $0 \le \theta < 2\pi$, tenemos que $r^9 = 1 \implies r = 1$, y los ángulos $\theta$ satisfacen:
\[9\theta = (2k + 1)\pi \implies \theta = \frac{(2k + 1)\pi}{9}, \quad \text{para } k \in \{0, 1, 2, 3, 4, 5, 6, 7, 8\}.\]

Debemos descartar la raíz $z = -1$, la cual corresponde a $\theta = \pi$ (cuando $k = 4$).

Los $8$ valores posibles de $\theta$ en el intervalo $[0, 2\pi)$ son:
\[\frac{\pi}{9}, \frac{3\pi}{9}, \frac{5\pi}{9}, \frac{7\pi}{9}, \frac{11\pi}{9}, \frac{13\pi}{9}, \frac{15\pi}{9}, \frac{17\pi}{9}.\]

Agrupando los términos simétricos (cada par suma $2\pi$):
\[\left(\frac{\pi}{9} + \frac{17\pi}{9}\right) + \left(\frac{3\pi}{9} + \frac{15\pi}{9}\right) + \left(\frac{5\pi}{9} + \frac{13\pi}{9}\right) + \left(\frac{7\pi}{9} + \frac{11\pi}{9}\right) = 4 \times 2\pi = 8\pi.\]

\boxed{8\pi}