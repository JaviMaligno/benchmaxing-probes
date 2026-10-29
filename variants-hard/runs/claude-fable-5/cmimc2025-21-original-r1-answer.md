## Planteamiento

El desarrollo (net) en forma de paralelogramo de un tetraedro regular de arista $a$ es una tira de 4 triángulos equiláteros: un paralelogramo de lados $2a$ y $a$ con ángulo de $60°$.

## Cota superior

La diagonal larga del paralelogramo (de un vértice agudo al otro) mide
$$|u+v| = a\sqrt{4+1+2\cdot 2\cdot 1\cdot \cos 60°} = a\sqrt{7}.$$
Cualquier segmento contenido en el cuadrado de lado $7$ mide a lo más la diagonal $7\sqrt{2}$, así que
$$a\sqrt{7} \le 7\sqrt{2} \quad\Longrightarrow\quad a \le \sqrt{14}.$$

## La cota se alcanza

Coloco el paralelogramo inclinado con vectores de lado $u = 2a(\cos\theta, \sin\theta)$ y $v = a(\cos(\theta+60°), \sin(\theta+60°))$. Su caja envolvente mide $a\,f(\theta) \times a\,g(\theta)$ con
$$f = 2\cos\theta + \cos(\theta+60°), \qquad g = 2\sin\theta + \sin(\theta+60°).$$
Igualando $f = g$ se obtiene $\tan(\theta + 45°) = \tfrac{5}{\sqrt{3}}$, es decir $\theta \approx 25.9°$, y con $\sin(\theta+45°) = \tfrac{5}{2\sqrt{7}}$, $\cos(\theta+45°) = \tfrac{\sqrt{3}}{2\sqrt{7}}$ se calcula
$$f = g = \frac{\sqrt{14}}{2}.$$
Con $a = \sqrt{14}$ la caja envolvente mide exactamente $7 \times 7$. Verificación numérica de los vértices: $(0,0)$, $u \approx (6.73,\,3.27)$, $v \approx (0.27,\,3.73)$, $u+v = (7,7)$ — todos dentro del cuadrado, y la diagonal larga $a\sqrt{7} = \sqrt{98} = 7\sqrt{2}$ coincide exactamente con la diagonal del cuadrado.

## Área superficial

El tetraedro resultante tiene arista $a = \sqrt{14}$, y su área superficial es
$$4 \cdot \frac{\sqrt{3}}{4}a^2 = \sqrt{3}\cdot 14.$$

$$\boxed{14\sqrt{3}}$$