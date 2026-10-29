## Solución

**Configuración angular.** Llamo $\alpha=\angle QWX=\angle QZW$, $\beta=\angle QXW=\angle QYX$, $\gamma=\angle QXY=\angle QYZ$, $\zeta=\angle QWZ=\angle QZY$. Sumando los ángulos del cuadrilátero: $2(\alpha+\beta+\gamma+\zeta)=360°$, así que $\alpha+\beta+\gamma+\zeta=180°$.

**Ley de senos en los cuatro triángulos** ($QWX$, $QXY$, $QYZ$, $QZW$):

- $\dfrac{QX}{\sin\alpha}=\dfrac{QW}{\sin\beta}\Rightarrow \sin\alpha=\tfrac{5}{3}\sin\beta$
- $\dfrac{QY}{\sin\gamma}=\dfrac{QX}{\sin\beta}\Rightarrow \sin\gamma=2\sin\beta$
- Combinando los triángulos $QYZ$ y $QZW$ para eliminar $QZ$: $\sin^2\zeta=\tfrac{10}{3}\sin\gamma\cdot\tfrac{10}{3}\sin\beta\cdot\frac{\sin\alpha}{\sin\gamma}\cdots$ da $\sin\zeta=\tfrac{10}{3}\sin\beta$, y de paso $QZ=6$.

**Resolver la restricción.** Con $s=\sin\beta$, $c_a=\cos\alpha$, $c_b=\cos\beta$, $c_g=\cos\gamma$, la condición $\alpha+\beta+\gamma=180°-\zeta$ (con $\zeta$ obtuso, lo cual es forzoso pues con los cuatro ángulos agudos la suma no llega a $180°$) equivale a $\sin(\alpha+\beta+\gamma)=\tfrac{10}{3}s$ con coseno positivo. Expandiendo y escribiendo $y=\cos\beta$, $P=\sqrt{4y^2-3}$, $S=\tfrac{1}{3}\sqrt{25y^2-16}\cdot 3$, la ecuación se factoriza como
$$\left(\sqrt{4y^2-3}+2y\right)\left(\sqrt{25y^2-16}+5y\right)=20.$$
Racionalizando cada factor se obtiene además $(2y-\sqrt{4y^2-3})(5y-\sqrt{25y^2-16})=\tfrac{12}{5}$; restando y luego elevando al cuadrado, todos los términos en $y$ se cancelan salvo uno y queda
$$85\,y^2=\frac{1936}{25}\quad\Rightarrow\quad \cos^2\beta=\frac{1936}{2125},\qquad \sin^2\beta=\frac{189}{2125}.$$

Entonces, con denominador común $\sqrt{2125}=5\sqrt{85}$:
$$\cos\beta=\frac{44}{\sqrt{2125}},\qquad \cos\alpha=\sqrt{1-\tfrac{25}{9}\sin^2\beta}=\frac{40}{\sqrt{2125}},\qquad \cos\gamma=\sqrt{1-4\sin^2\beta}=\frac{37}{\sqrt{2125}}.$$

**Lados.** De cada triángulo, $\;WX=3\frac{\sin(\alpha+\beta)}{\sin\beta}=5\cos\beta+3\cos\alpha$, y usando $\alpha+\beta+\gamma+\zeta=180°$ resulta $YZ=WX$, $XY=5(\cos\gamma+2\cos\beta)$, $ZW=\tfrac{9}{5}(\cos\gamma+2\cos\beta)$. Por tanto
$$\text{Perímetro}=\frac{118}{5}\cos\beta+6\cos\alpha+\frac{34}{5}\cos\gamma=\frac{\tfrac{5192+1258}{5}+240}{\sqrt{2125}}=\frac{1530}{5\sqrt{85}}=\frac{306}{\sqrt{85}}.$$

Es decir, el perímetro es $\dfrac{18\sqrt{85}}{5}\approx 33.19$ (verificado numéricamente con los ángulos $\alpha\approx29.8°$, $\beta\approx17.4°$, $\gamma\approx36.6°$, $\zeta\approx96.2°$).

$$\boxed{\dfrac{18\sqrt{85}}{5}}$$