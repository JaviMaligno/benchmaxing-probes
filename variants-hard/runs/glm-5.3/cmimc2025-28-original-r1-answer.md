## Planteamiento

Coloco $A=(0,0)$, $B=(20,0)$, entonces $O=(10,0)$ y $\omega$ tiene radio 10.

**Puntos C y D** (por el ángulo en semicírculo, $\angle ACB=\angle ADB=90^\circ$):
- $AC=\sqrt{400-169}=\sqrt{231}$, así que $C=\left(\frac{231}{20},\frac{13\sqrt{231}}{20}\right)$
- $BD=\sqrt{400-49}=\sqrt{351}$, así que $D=\left(\frac{49}{20},\frac{21\sqrt{39}}{20}\right)$

**Punto E** (intersección de $\overleftrightarrow{BC}$ y $\overleftrightarrow{AD}$): resolviendo las dos rectas,
$$E=\left(\frac{273\sqrt{1001}-3773}{800},\ \frac{1521\sqrt{231}-1617\sqrt{39}}{800}\right)\approx(6.080,\,16.274).$$

**Lados del triángulo $ECD$**, escribiendo $s=\sqrt{1001}$:
- $EC=EB-BC=\dfrac{s(s-21)}{40}$, $\quad ED=EA-AD=\dfrac{39(s-21)}{40}$
- $CD=\dfrac{9s-91}{20}$ (por Ptolomeo: $\sqrt{231}\cdot\sqrt{351}=20\cdot CD+91$, ya que $\sqrt{231\cdot351}=9s$)

**Excentro opuesto a E**: con $a=CD$, $b=ED$, $c=EC$,
$$L=\frac{-aE+bC+cD}{-a+b+c},\qquad -a+b+c=\frac{91}{10}.$$

**Coordenada y**: el numerador (multiplicado por 16000) es
$$-(9s-91)(1521\sqrt{231}-1617\sqrt{39})+10140(s-21)\sqrt{231}+420\,s(s-21)\sqrt{39}.$$
Usando $s\sqrt{231}=77\sqrt{39}$ y $s\sqrt{39}=13\sqrt{231}$, los coeficientes de $\sqrt{39}$ ($-1201200+780780+420420$) y de $\sqrt{231}$ ($327600-212940-114660$) son ambos **cero**. Por tanto $L$ está sobre $\overline{AB}$: ¡$y_L=0$! (verificado numéricamente: $L\approx(8.958,\,0)$, y sus distancias a las rectas $BC$, $AD$, $CD$ coinciden $\approx 8.39$).

**Coordenada x**: el numerador es
$$\frac{7s(39-s)}{20}\quad\Longrightarrow\quad x_L=\frac{10}{91}\cdot\frac{7s(39-s)}{20}=\frac{s(39-s)}{26}.$$

**Cálculo de OL**:
$$OL=10-x_L=10-\frac{s(39-s)}{26}=\frac{260-39s+s^2}{26}=\frac{1261-39s}{26}=\frac{13(97-3s)}{26}=\frac{97-3\sqrt{1001}}{2}.$$

Numéricamente: $OL\approx(97-94.916)/2\approx 1.042$ ✓ (consistente con $L\approx(8.958,0)$, $O=(10,0)$).

$$\boxed{\dfrac{97-3\sqrt{1001}}{2}}$$