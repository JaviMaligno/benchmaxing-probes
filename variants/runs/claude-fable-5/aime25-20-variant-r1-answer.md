## Resolución

**Configuración.** El circuncírculo de $\triangle DEF$ (triángulo medial) es la circunferencia de los nueve puntos de $\triangle PQR$. Como el segmento $\overline{QD}$ está sobre el lado $QR$, el segundo punto de corte $G$ es el pie de la altura desde $P$; análogamente, $H$ es el pie de la altura desde $Q$ (sobre $PR$) y $J$ el pie de la altura desde $R$ (sobre $PQ$).

**Coordenadas.** Con $Q=(0,0)$, $R=(\sin 80^\circ,0)$, $P=(\sin 42^\circ\cos 58^\circ,\ \sin 42^\circ\sin 58^\circ)$:

- $D=(0.4924,\,0)$, $E=(0.6697,\,0.2837)$, $F=(0.1773,\,0.2837)$
- $G=(0.3546,\,0)$, $H=(0.4409,\,0.4897)$, $J=(0.2765,\,0.4426)$

El centro de los nueve puntos resulta $N=(0.4235,\,0.2403)$ con radio $0.25$ (la mitad del circunradio, como debe ser).

**Ángulos centrales** de cada punto respecto a $N$ (medidos con atan2, y todos caen exactamente en grados enteros):

$$\theta_G=-106^\circ,\quad \theta_D=-74^\circ,\quad \theta_E=10^\circ,\quad \theta_H=86^\circ,\quad \theta_J=126^\circ,\quad \theta_F=170^\circ$$

El orden cíclico es $G, D, E, H, J, F$, consistente con el enunciado. Los seis arcos menores son:

$$\wideparen{GD}=32^\circ,\quad \wideparen{DE}=84^\circ,\quad \wideparen{EH}=76^\circ,\quad \wideparen{HJ}=40^\circ,\quad \wideparen{JF}=44^\circ,\quad \wideparen{FG}=84^\circ$$

(suman $360^\circ$ ✓; además $\wideparen{DE}=2\angle DFE=2\angle R=84^\circ$ confirma la exactitud).

**Cálculo final.**

$$\wideparen{DE} + 2\cdot\wideparen{HJ} + 3\cdot\wideparen{FG} = 84 + 2(40) + 3(84) = 84 + 80 + 252 = 416$$

$$\boxed{416}$$