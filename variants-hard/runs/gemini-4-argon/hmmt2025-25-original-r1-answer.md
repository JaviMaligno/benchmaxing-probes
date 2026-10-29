Para calcular la longitud de $XP$, razonaremos paso a paso utilizando las propiedades geométricas del triángulo equilátero y su circunferencia circunscrita.

### Paso 1: Caracterizar el lugar geométrico del punto $P$
Sea $O$ el circuncentro del triángulo equilátero $\triangle ABC$ y $R$ su circunradio. Como el lado del triángulo mide $6$, el circunradio es:
$$R = \frac{6}{2 \sin 60^\circ} = \frac{6}{\sqrt{3}} = 2\sqrt{3}$$

Sea $A'$ el punto diametralmente opuesto a $A$ en la circunferencia circunscrita de $\triangle ABC$. Entonces, el segmento $AA'$ es un diámetro de longitud $2R = 4\sqrt{3}$, y $OA = OB = OC = OA' = R$.

Como $\triangle ABC$ es equilátero, los ángulos centrales cumplen $\angle AOB = \angle AOC = 120^\circ$. Dado que $AA'$ es una recta que pasa por $O$, los ángulos suplementarios son:
$$\angle A'OB = \angle A'OC = 180^\circ - 120^\circ = 60^\circ$$

Como además $OB = OC = OA' = R$, los triángulos $\triangle A'OB$ y $\triangle A'OC$ son equiláteros de lado $R$. En consecuencia:
$$A'B = A'O = A'C = R$$

Esto significa que la circunferencia con centro en $A'$ y radio $R$ pasa por los puntos $B$, $O$ y $C$. Como $\angle BOC = 120^\circ$ y $P$ está en el interior de $\triangle ABC$ con $\angle BPC = 120^\circ$, el punto $P$ debe pertenecer al arco $BOC$ de esta circunferencia centrada en $A'$. Por lo tanto, la distancia de $A'$ a $P$ es igual al radio $R$:
$$A'P = R = 2\sqrt{3}$$

### Paso 2: Demostrar que $X$, $P$ y $A'$ son colineales
Por el enunciado:
1. $X$ pertenece a la circunferencia de diámetro $\overline{AP}$ (con $X \neq A$), por lo que el ángulo inscrito que subtiende al diámetro es recto:
   $$\angle AXP = 90^\circ$$
2. $X$ también pertenece a la circunferencia circunscrita de $\triangle ABC$, en la cual $\overline{AA'}$ es un diámetro, por lo que:
   $$\angle AXA' = 90^\circ$$

Como ambos ángulos $\angle AXP$ y $\angle AXA'$ son rectos en $X$ y comparten el lado $AX$, los puntos $X$, $P$ y $A'$ son colineales. Dado que $P$ se encuentra en el interior de $\triangle ABC$ y $X$ y $A'$ están en la circunferencia circunscrita en lados opuestos respecto a $P$, el punto $P$ se ubica sobre el segmento $XA'$.

### Paso 3: Calcular $XP$
Aplicamos el teorema de Pitágoras en el triángulo rectángulo $\triangle AXA'$, donde la hipotenusa es $AA' = 2R = 4\sqrt{3}$ y el cateto conocido es $AX = 5$:
$$XA' = \sqrt{AA'^2 - AX^2} = \sqrt{(4\sqrt{3})^2 - 5^2} = \sqrt{48 - 25} = \sqrt{23}$$

Finalmente, como $P$ está en el segmento $XA'$ y $A'P = 2\sqrt{3}$, restamos las longitudes para obtener $XP$:
$$XP = XA' - A'P = \sqrt{23} - 2\sqrt{3}$$

\boxed{\sqrt{23}-2\sqrt{3}}