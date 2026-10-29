## Solución

**Configuración.** Sea $R$ el circunradio: $R=\frac{9}{\sqrt3}=3\sqrt3$.

**Paso 1: el lugar geométrico de $Q$.**
La cuerda $EF=9$ se ve bajo $120^\circ$ desde $Q$, así que $Q$ está en un arco de radio
$$\frac{EF}{2\sin 120^\circ}=\frac{9}{\sqrt3}=3\sqrt3=R .$$
El circuncentro $O$ cumple $\angle EOF=120^\circ$, luego pertenece a ese arco, y el centro del arco resulta ser el punto diametralmente opuesto a $D$ en el circuncírculo. Llamándolo $D'$:
$$D'Q = 3\sqrt3 .$$

**Paso 2: la recta $YQ$ pasa por $D'$.**
Como $DQ$ es diámetro del segundo círculo, $\angle DYQ = 90^\circ$. Si la recta $YQ$ corta de nuevo al circuncírculo en $Z$, entonces $\angle DYZ=90^\circ$, de modo que $DZ$ es diámetro, es decir $Z=D'$. Por tanto $Y$, $Q$ y $D'$ son colineales.

**Paso 3: cálculo.**
En el triángulo rectángulo $DYD'$ (con $DD'=2R=6\sqrt3$):
$$YD'=\sqrt{(6\sqrt3)^2-7^2}=\sqrt{108-49}=\sqrt{59}.$$

Como $Q$ está sobre el segmento $YD'$ con $D'Q=3\sqrt3$:
$$YQ=\sqrt{59}-3\sqrt3\approx 2.485 .$$

(La otra posibilidad, $\sqrt{59}+3\sqrt3$, daría $DQ\approx14.7>9$, imposible para un punto interior.)

**Verificación numérica:** con $D=(0,3\sqrt3)$, $E=(-4.5,-\tfrac{3\sqrt3}{2})$, $F=(4.5,-\tfrac{3\sqrt3}{2})$ se obtiene $Y\approx(5.174,0.481)$, $Q\approx(3.500,-1.356)$, que está dentro del triángulo y cumple $\angle EQF=120^\circ$ y $DY=7$.

$$\boxed{\sqrt{59}-3\sqrt{3}}$$