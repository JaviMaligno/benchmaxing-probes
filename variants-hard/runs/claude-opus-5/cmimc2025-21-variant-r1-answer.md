## Planteamiento

**El net en forma de paralelogramo.** Cuatro triángulos equiláteros de lado $a$ dispuestos en tira forman un paralelogramo con lados $a$ y $2a$ y ángulos de $60^\circ/120^\circ$, que efectivamente se plega en un tetraedro regular de arista $a$. Con vértices:

$$P_1=(0,0),\quad P_2=(2a,0),\quad P_3=\left(\tfrac{5a}{2},\tfrac{\sqrt3}{2}a\right),\quad P_4=\left(\tfrac{a}{2},\tfrac{\sqrt3}{2}a\right)$$

**Diagonal mayor.** $|P_1P_3|=a\sqrt{\tfrac{25}{4}+\tfrac34}=a\sqrt7$.

**Cota inferior para el cuadrado.** Un cuadrado de lado $s$ tiene diámetro $s\sqrt2$, así que si contiene el paralelogramo debe contener el segmento $P_1P_3$:
$$s\sqrt2\ \ge\ a\sqrt7\quad\Longrightarrow\quad s\ \ge\ a\sqrt{7/2}$$

**La cota se alcanza.** Basta colocar la diagonal $P_1P_3$ sobre la diagonal del cuadrado, es decir girar el paralelogramo un ángulo $\varphi=45^\circ-\arctan\frac{\sqrt3/2}{5/2}\approx 25.89^\circ$. Con $a=1$ los vértices quedan en
$$P_1=(0,0),\; P_2\approx(1.799,\,0.873),\; P_3\approx(1.871,\,1.871),\; P_4\approx(0.072,\,0.998)$$
Todas las coordenadas caen en $[0,\;1.8708]$, con $1.8708=\sqrt{7/2}$. Luego el cuadrado mínimo que lo contiene tiene lado exactamente $a\sqrt{7/2}$.

## Arista máxima y área

$$a\sqrt{7/2}=14\quad\Longrightarrow\quad a=14\sqrt{\tfrac27},\qquad a^2=196\cdot\tfrac27=56$$

Superficie del tetraedro regular: $S=4\cdot\frac{\sqrt3}{4}a^2=\sqrt3\,a^2=56\sqrt3\approx 96.99$.

$$\boxed{56\sqrt{3}}$$