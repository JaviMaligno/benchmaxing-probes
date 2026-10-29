Para encontrar la longitud de $YQ$, podemos analizar las propiedades geométricas de la configuración paso a paso:

### Paso 1: Circunferencia circunscrita de $\triangle DEF$
Sea $\omega$ la circunferencia circunscrita al triángulo equilátero $\triangle DEF$, con centro $O$ y circunradio $R$. Dado que el lado del triángulo es $a = 9$, el circunradio es:
$$R = \frac{a}{\sqrt{3}} = \frac{9}{\sqrt{3}} = 3\sqrt{3}$$

Sea $D'$ el punto diametralmente opuesto a $D$ en $\omega$, de modo que $\overline{DD'}$ es un diámetro de $\omega$ de longitud $2R = 6\sqrt{3} = \sqrt{108}$.

### Paso 2: Lugar geométrico del punto $Q$
En la circunferencia $\omega$, dado que $\triangle DEF$ es equilátero y $D'$ es el punto medio del arco menor $\widehat{EF}$:
- Los ángulos inscritos cumplen $\angle ED'D = \angle FD'D = 30^{\circ}$, por lo que $\angle ED'F = 60^{\circ}$? No: como $D$ y $D'$ están en lados opuestos de $EF$ y $\angle EDF = 60^{\circ}$, el cuadrilátero $DED'F$ es cíclico, por lo que $\angle ED'F = 180^{\circ} - 60^{\circ} = 120^{\circ}$.
- Además, en los triángulos rectángulos $\triangle DED'$ y $\triangle DFD'$, tenemos $D'E = D'F = DD' \sin(30^{\circ}) = 2R \cdot \frac{1}{2} = R$.
- Asimismo, la distancia de $D'$ al circuncentro $O$ es $D'O = R$.

Por lo tanto, la circunferencia con centro en $D'$ y radio $R$ pasa por los puntos $E$, $O$ y $F$. Como el circuncentro $O$ cumple $\angle EOF = 120^{\circ}$ y se encuentra en el interior de $\triangle DEF$, el arco $\widehat{EF}$ de esta circunferencia (contenido dentro de $\triangle DEF$) es precisamente el lugar geométrico de los puntos $Q$ interiores a $\triangle DEF$ tales que $\angle EQF = 120^{\circ}$.

En consecuencia, para cualquier punto $Q$ que cumpla la condición del problema, se tiene que:
$$D'Q = R = 3\sqrt{3}$$

### Paso 3: Colinealidad de $D'$, $Q$ e $Y$
1. Como $Y$ pertenece a la circunferencia de diámetro $\overline{DQ}$ ($Y \neq D$), el ángulo inscrito es recto:
   $$\angle DYQ = 90^{\circ}$$
2. Como $Y$ también pertenece a la circunferencia circunscrita $\omega$ de diámetro $\overline{DD'}$, tenemos:
   $$\angle DYD' = 90^{\circ}$$

Dado que tanto $YQ$ como $YD'$ son perpendiculares a $DY$ en el punto $Y$, los puntos $D'$, $Q$ e $Y$ son colineales. Más aún, como $Q$ está en el interior de $\triangle DEF$ e $Y$ está en el arco $\widehat{EDF}$ de $\omega$, el punto $Q$ se encuentra sobre el segmento $\overline{D'Y}$.

### Paso 4: Cálculo de $YQ$
Aplicando el teorema de Pitágoras en el triángulo rectángulo $\triangle DYD'$ (recto en $Y$), con $DD' = 6\sqrt{3}$ y $DY = 7$:
$$D'Y = \sqrt{DD'^2 - DY^2} = \sqrt{(6\sqrt{3})^2 - 7^2} = \sqrt{108 - 49} = \sqrt{59}$$

Finalmente, como $Q$ está en el segmento $\overline{D'Y}$:
$$YQ = D'Y - D'Q = \sqrt{59} - 3\sqrt{3}$$

\boxed{\sqrt{59} - 3\sqrt{3}}