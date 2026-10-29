## Planteamiento

Sea $k$ el valor común:
$$2(a^2+1)=3(b^2+1)=4(c^2+1)=k \;\Longrightarrow\; a^2=\tfrac{k}{2}-1,\quad b^2=\tfrac{k}{3}-1,\quad c^2=\tfrac{k}{4}-1.$$

## Sustitución trigonométrica

Como $ab+bc+ca=1$ con $a,b,c>0$, existen ángulos con $\frac{A}{2}+\frac{B}{2}+\frac{C}{2}=\frac{\pi}{2}$ tales que $a=\tan\frac{A}{2},\ b=\tan\frac{B}{2},\ c=\tan\frac{C}{2}$ (identidad del semiángulo en un triángulo).

Entonces $a^2+1=\sec^2\frac{A}{2}$, y las ecuaciones dan, con $t=1/k$:
$$\cos^2\tfrac{A}{2}=2t,\qquad \cos^2\tfrac{B}{2}=3t,\qquad \cos^2\tfrac{C}{2}=4t.$$

De $\frac{A}{2}=\frac{\pi}{2}-\left(\frac{B}{2}+\frac{C}{2}\right)$ se obtiene $\cos\frac{A}{2}=\sin\left(\frac{B}{2}+\frac{C}{2}\right)$:
$$\sqrt{2t}=\sqrt{1-3t}\,\sqrt{4t}+\sqrt{3t}\,\sqrt{1-4t}.$$

Dividiendo entre $\sqrt{t}$:
$$\sqrt{2}=2\sqrt{1-3t}+\sqrt{3}\,\sqrt{1-4t}.$$

## Resolución

Aislando y elevando al cuadrado:
$$\left(\sqrt{2}-2\sqrt{1-3t}\right)^2=3(1-4t)\;\Longrightarrow\;2-4\sqrt{2}\sqrt{1-3t}+4-12t=3-12t,$$
$$\sqrt{1-3t}=\frac{3}{4\sqrt{2}}\;\Longrightarrow\;1-3t=\frac{9}{32}\;\Longrightarrow\;t=\frac{23}{96},\qquad k=\frac{96}{23}.$$

## Valores

$$a=\sqrt{\tfrac{48}{23}-1}=\frac{5}{\sqrt{23}},\qquad b=\sqrt{\tfrac{32}{23}-1}=\frac{3}{\sqrt{23}},\qquad c=\sqrt{\tfrac{24}{23}-1}=\frac{1}{\sqrt{23}}.$$

Verificación: $ab+bc+ca=\dfrac{15+3+5}{23}=1$ ✓

Por tanto $a+b+c=\dfrac{9}{\sqrt{23}}$.

$$\boxed{\dfrac{9\sqrt{23}}{23}}$$