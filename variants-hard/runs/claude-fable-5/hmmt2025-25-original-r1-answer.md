Resolvamos el problema paso a paso.

**Configuración.** Sea $O$ el circuncentro de $\triangle ABC$. Como el lado es $6$, el circunradio es $R = \dfrac{6}{\sqrt{3}} = 2\sqrt{3}$.

**Paso 1: localizar $P$ mediante la condición $\angle BPC = 120^\circ$.**
El lugar geométrico de los puntos interiores con $\angle BPC = 120^\circ$ es un arco de la circunferencia que pasa por $B$ y $C$ cuyo ángulo central es $2(180^\circ - 120^\circ) = 120^\circ$. Su radio $r$ cumple $6 = 2r\sin 60^\circ$, es decir $r = 2\sqrt{3}$, y su centro es la reflexión de $O$ sobre $BC$. Con coordenadas $B=(0,0)$, $C=(6,0)$, $A=(3,3\sqrt{3})$, se tiene $O=(3,\sqrt{3})$ y ese centro es $(3,-\sqrt{3})$, que es exactamente $A'$, el punto **antípoda de $A$** en la circunferencia circunscrita. Por lo tanto:
$$A'P = 2\sqrt{3}.$$

**Paso 2: usar la circunferencia de diámetro $AP$.**
Como $X$ está en la circunferencia de diámetro $\overline{AP}$, se cumple $\angle AXP = 90^\circ$, o sea $XP \perp XA$. Pero $X$ también está en la circunferencia circunscrita, y la cuerda que pasa por $X$ perpendicular a $XA$ debe pasar por el antípoda de $A$ (ángulo inscrito en semicircunferencia). Entonces la recta $XP$ pasa por $A'$: los puntos $X$, $P$, $A'$ son colineales.

**Paso 3: calcular $XA'$.**
Como $AA'$ es diámetro, $\angle AXA' = 90^\circ$, así que en el triángulo rectángulo $AXA'$:
$$XA' = \sqrt{AA'^2 - AX^2} = \sqrt{(4\sqrt{3})^2 - 5^2} = \sqrt{48-25} = \sqrt{23}.$$

**Paso 4: concluir.**
Como $P$ está dentro del triángulo y $A'$ fuera (debajo de $BC$), $P$ queda entre $X$ y $A'$ sobre esa recta. Por lo tanto:
$$XP = XA' - PA' = \sqrt{23} - 2\sqrt{3}.$$

$$\boxed{\sqrt{23}-2\sqrt{3}}$$