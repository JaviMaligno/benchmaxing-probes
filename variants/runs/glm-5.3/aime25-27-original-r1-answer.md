## Planteamiento

Sea $r_i = A_1A_i$ para $i=2,\dots,11$, y sea $\theta_i = \angle A_i A_1 A_{i+1}$ para $2\le i\le 10$.

**Paso 1: producto $r_i r_{i+1}$ constante.**
Como $\cos\theta_i = \tfrac{12}{13}$ y $0<\theta_i<\pi$, tenemos $\sin\theta_i = \tfrac{5}{13}$. El área $1$ da
$$\tfrac12 r_i r_{i+1}\sin\theta_i = 1 \;\Rightarrow\; r_i r_{i+1} = \frac{26}{5}\quad\text{para } i=2,\dots,10.$$

**Paso 2: los radios alternan.**
De $r_2r_3 = r_3r_4 = r_4r_5=\cdots$ se sigue $r_2=r_4=\cdots=r_{10}=:a$ y $r_3=r_5=\cdots=r_{11}=:b$, con
$$ab=\frac{26}{5}.$$
(Esto es independiente de cómo se dispongan los ángulos alrededor de $A_1$.)

**Paso 3: longitud de los lados $A_iA_{i+1}$.**
Por la ley de cosenos, para cada $i=2,\dots,10$:
$$s^2 = a^2+b^2 - 2ab\cdot\frac{12}{13} = a^2+b^2 - 2\cdot\frac{26}{5}\cdot\frac{12}{13} = a^2+b^2-\frac{48}{5}.$$
Los nueve lados interiores son iguales.

**Paso 4: usar el perímetro.**
$$20 = A_1A_2 + \sum_{i=2}^{10}A_iA_{i+1} + A_{11}A_1 = u + 9s,\qquad u := a+b.$$
Como $a^2+b^2 = u^2-2ab = u^2-\tfrac{52}{5}$,
$$s^2 = u^2 - \frac{52}{5}-\frac{48}{5} = u^2-20.$$
Entonces
$$u + 9\sqrt{u^2-20}=20.$$

**Paso 5: resolver.**
Con $9\sqrt{u^2-20}=20-u>0$ y elevando al cuadrado:
$$81u^2-1620 = u^2-40u+400 \;\Rightarrow\; 80u^2+40u-2020=0 \;\Rightarrow\; 4u^2+2u-101=0,$$
$$u = \frac{-2+\sqrt{1620}}{8} = \frac{18\sqrt5-2}{8} = \frac{9\sqrt5-1}{4}.$$
(La otra raíz es negativa. Verificación algebraica: con este $u$, $u^2-20=\tfrac{43-9\sqrt5}{8}$ y $81\cdot\tfrac{43-9\sqrt5}{8}=\tfrac{(81-9\sqrt5)^2}{16}=(20-u)^2$, y ambos lados son positivos. ✓)

**Comprobación de consistencia:** $ab=\tfrac{26}5$ con $u\approx 4.781$ da $a,b\approx 3.108,\ 1.673$ reales y positivos; con los rayos girando siempre $+\theta$, el abanico es simple, y como $a/b\approx 1.86>\tfrac{13}{12}$, la cuerda $A_2A_4$ sale de la región: el polígono es efectivamente no convexo.

**Paso 6: identificar los coeficientes.**
$$A_1A_2+A_1A_{11} = u = \frac{m\sqrt{n}-p}{q}=\frac{9\sqrt5-1}{4},$$
con $m=9$, $n=5$ (libre de cuadrados), $p=1$, $q=4$; $\gcd(9,1,4)=1$, así que no hay simplificación posible.

$$m+n+p+q = 9+5+1+4$$

$$\boxed{19}$$