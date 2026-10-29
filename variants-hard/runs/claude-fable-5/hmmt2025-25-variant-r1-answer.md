## Solución

**Configuración clave.** Coloco el lugar geométrico de $Q$: como $\angle EQF = 120^\circ$ y $\angle EOF = 120^\circ$ (donde $O$ es el circuncentro), $Q$ está sobre la circunferencia que pasa por $E$, $O$, $F$. Para un triángulo equilátero de lado $9$, el circunradio es $R = \tfrac{9}{\sqrt 3} = 3\sqrt 3$, y el centro de esa circunferencia resulta ser $D'$, el punto diametralmente opuesto a $D$ en el circuncírculo, con radio $3\sqrt 3$. Es decir:
$$D'Q = 3\sqrt{3}.$$

**Colinealidad.** Como $\overline{DQ}$ es diámetro de la circunferencia pequeña, $\angle DYQ = 90^\circ$. Como $\overline{DD'}$ es diámetro del circuncírculo, $\angle DYD' = 90^\circ$. Ambos ángulos rectos en $Y$ respecto a $\overline{DY}$ implican que $Y$, $Q$, $D'$ son colineales.

**Cálculo.** En el triángulo rectángulo $DYD'$ con $DD' = 2R = 6\sqrt 3$ y $DY = 7$:
$$YD' = \sqrt{(6\sqrt3)^2 - 7^2} = \sqrt{108 - 49} = \sqrt{59}.$$

Como $Q$ está dentro del triángulo (y por tanto entre $Y$ y $D'$ sobre esa cuerda):
$$YQ = YD' - D'Q = \sqrt{59} - 3\sqrt{3}.$$

**Verificación numérica.** Con coordenadas $E=(-4.5,0)$, $F=(4.5,0)$, $D=(0,\tfrac{9\sqrt3}{2})$, se obtiene $Q \approx (3.500,\ 1.242)$ (interior, con $\angle EQF = 120.0^\circ$ exacto) e $Y \approx (5.174,\ 3.079)$ con $DY = 7$ y $\angle DYQ = 90^\circ$, dando $YQ \approx 2.485 = \sqrt{59} - 3\sqrt{3}$. ✓

$$\boxed{YQ = \sqrt{59} - 3\sqrt{3}}$$