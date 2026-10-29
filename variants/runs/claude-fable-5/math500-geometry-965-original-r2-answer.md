## Solución

**Configuración con la bisectriz y las paralelas.** Sea $\angle CAD = \theta$. Como $AC$ biseca $\angle BAD$, también $\angle BAC = \theta$. Por las paralelas $AD \parallel BC$, $\angle BCA = \angle CAD = \theta$ (ángulos alternos internos), así que el triángulo $ABC$ es isósceles con $AB = BC$.

**Coordenadas.** Pongo $A=(0,0)$, $D=(a,0)$. Como $\angle ACD = 90^\circ$ con hipotenusa $AD$, se tiene $AC = a\cos\theta$, $CD = a\sin\theta$, y
$$C = (a\cos^2\theta,\; a\cos\theta\sin\theta).$$
El punto $B$ está sobre el rayo que forma ángulo $2\theta$ con $AD$: $B = (t\cos 2\theta,\; t\sin 2\theta)$ con $t = AB$. Como $BC \parallel AD$, las alturas de $B$ y $C$ coinciden:
$$t\sin 2\theta = a\cos\theta\sin\theta \;\Rightarrow\; 2t\sin\theta\cos\theta = a\sin\theta\cos\theta \;\Rightarrow\; t = \frac{a}{2}.$$
Entonces $BC = C_x - B_x = a\cos^2\theta - \tfrac{a}{2}(2\cos^2\theta - 1) = \tfrac{a}{2}$.

**Áreas.** La altura del trapecio es $h = a\sin\theta\cos\theta$, luego
$$[ABCD] = \frac{1}{2}(AD + BC)\,h = \frac{1}{2}\left(a + \frac{a}{2}\right) a\sin\theta\cos\theta = \frac{3}{4}\,a^2\sin\theta\cos\theta = 42,$$
de donde $a^2\sin\theta\cos\theta = 56$.

Por otro lado,
$$[\triangle ACD] = \frac{1}{2}\,AC\cdot CD = \frac{1}{2}\,a^2\sin\theta\cos\theta = \frac{56}{2} = 28.$$

$$\boxed{28}$$