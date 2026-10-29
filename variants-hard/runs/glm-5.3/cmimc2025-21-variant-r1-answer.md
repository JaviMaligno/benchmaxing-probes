# Planteamiento

**Paso 1: Identificar la red.** Un tetraedro regular tiene exactamente dos redes: el triángulo grande y el **paralelogramo**. Este último es una tira de 4 triángulos equiláteros de lado $a$, que forma un paralelogramo con lados $2a$ y $a$ con ángulo de $60^\circ$ (se comprueba cortando a lo largo del camino de aristas $12, 23, 34$ y desdoblando).

**Paso 2: Condición de encaje.** Para un paralelogramo con vectores lado $\mathbf{p}, \mathbf{q}$, la caja envolvente axial tiene dimensiones $|p_x|+|q_x|$ por $|p_y|+|q_y|$. Si $\mathbf{p}$ tiene longitud $2a$ en ángulo $\theta$ y $\mathbf{q}$ longitud $a$ en ángulo $\theta+60^\circ$, debe cumplirse (en el marco del cuadrado de lado $14$):

$$a\big(2|\cos\theta|+|\cos(\theta+60^\circ)|\big)\le 14,\qquad a\big(2|\sin\theta|+|\sin(\theta+60^\circ)|\big)\le 14.$$

**Paso 3: Optimizar $\theta$.** Sea $g(\theta)=\max(W(\theta),H(\theta))$ con $a=1$; hay que minimizar $g$. En $\theta\in[0^\circ,30^\circ]$ (donde todos los términos son positivos), $W$ decrece de $2.5$ y $H$ crece de $0.866$, así que el mínimo del máximo está en el cruce:

$$2\cos\theta+\cos(\theta+60^\circ)=2\sin\theta+\sin(\theta+60^\circ).$$

Reescribiendo: $2\cos(\theta+45^\circ)\cdot\sqrt2 - \sqrt2\sin(\theta+15^\circ)=0$... tras simplificar queda $2\cos(\theta+45^\circ)=\sin(\theta+15^\circ)$, es decir, con $\varphi=\theta+45^\circ$:

$$2\cos\varphi = \sin(\varphi-30^\circ)=\tfrac{\sqrt3}{2}\sin\varphi-\tfrac12\cos\varphi \;\Rightarrow\; \tan\varphi=\tfrac{5}{\sqrt3}.$$

Con $\sin\varphi = \tfrac{5}{\sqrt{28}}$, $\cos\varphi=\tfrac{\sqrt3}{\sqrt{28}}$:

$$g_{\min}=2\cos\theta+\cos(\theta+60^\circ)=\tfrac{5}{2}\cos\theta-\tfrac{\sqrt3}{2}\sin\theta=\frac{(5+\sqrt3)\cos\varphi+(5-\sqrt3)\sin\varphi}{2\sqrt2}=\frac{5\sqrt3+3+25-5\sqrt3}{2\sqrt{56}}=\frac{\sqrt{14}}{2}.$$

(Se verifica que otros intervalos angulares dan $g\ge 2 > \tfrac{\sqrt{14}}{2}\approx 1.871$, así que es el mínimo global.)

**Paso 4: Calcular.** El lado máximo del tetraedro es

$$a=\frac{14}{\sqrt{14}/2}=\frac{28}{\sqrt{14}}=2\sqrt{14},$$

y el área superficial del tetraedro regular es $\sqrt3\,a^2$:

$$\text{Área}=\sqrt3\,(2\sqrt{14})^2=56\sqrt3.$$

$$\boxed{56\sqrt{3}}$$