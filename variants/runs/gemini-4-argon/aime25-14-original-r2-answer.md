Para hallar el valor mínimo posible de $f(X) = AX + BX + CX + DX + EX$, analizamos primero la geometría del pentágono convexo $ABCDE$.

### Paso 1: Análisis de los triángulos $\triangle ABC$ y $\triangle ADE$
1. En el triángulo $\triangle ABC$, tenemos $AB = 14$, $BC = 7$ y $\angle B = 60^{\circ}$. Como $AB = 2BC$ y el ángulo comprendido es de $60^{\circ}$, por la ley de cosenos:
   $$AC^2 = 14^2 + 7^2 - 2(14)(7)\cos 60^{\circ} = 196 + 49 - 98 = 147 \implies AC = 7\sqrt{3}$$
   Por lo tanto, $\triangle ABC$ es un triángulo rectángulo notable de $30^{\circ}\text{-}60^{\circ}\text{-}90^{\circ}$ con $\angle BCA = 90^{\circ}$ y $\angle BAC = 30^{\circ}$.

2. De manera análoga, en el triángulo $\triangle ADE$, tenemos $EA = 26$, $DE = 13$ y $\angle E = 60^{\circ}$. Como $EA = 2DE$, resulta que $\triangle ADE$ también es un triángulo rectángulo de $30^{\circ}\text{-}60^{\circ}\text{-}90^{\circ}$ con:
   $$AD = 13\sqrt{3}, \quad \angle EDA = 90^{\circ}, \quad \angle DAE = 30^{\circ}$$

---

### Paso 2: Análisis del triángulo $\triangle ACD$ y coordenadas
En el triángulo $\triangle ACD$, conocemos sus tres lados: $AC = 7\sqrt{3}$, $AD = 13\sqrt{3}$ y $CD = 24$. Aplicando la ley de cosenos para encontrar $\angle ADC$:
$$\cos(\angle ADC) = \frac{AD^2 + CD^2 - AC^2}{2 \cdot AD \cdot CD} = \frac{507 + 576 - 147}{2 \cdot 13\sqrt{3} \cdot 24} = \frac{936}{624\sqrt{3}} = \frac{3}{2\sqrt{3}} = \frac{\sqrt{3}}{2}$$
De aquí se deduce que $\angle ADC = 30^{\circ}$ (además, todos los ángulos de $\triangle ACD$ son agudos).

Situemos el pentágono en el plano cartesiano con origen en $D = (0,0)$, el rayo $DE$ sobre el eje $x$ positivo y el rayo $DA$ sobre el eje $y$ positivo (ya que $\angle EDA = 90^{\circ}$):
- $D = (0, 0)$
- $E = (13, 0)$
- $A = (0, 13\sqrt{3})$

Como $\angle CDE = \angle CDA + \angle ADE = 30^{\circ} + 90^{\circ} = 120^{\circ}$ y $CD = 24$:
- $C = (24\cos 120^{\circ}, 24\sin 120^{\circ}) = (-12, 12\sqrt{3})$

El vector $\overrightarrow{CA} = A - C = (12, \sqrt{3})$. Como $\angle BCA = 90^{\circ}$, $BC = \frac{1}{\sqrt{3}}AC$ y el pentágono es convexo, obtenemos $\overrightarrow{CB}$ girando $\overrightarrow{CA}$ un ángulo de $90^{\circ}$ en sentido antihorario y dividiendo por $\sqrt{3}$:
$$\overrightarrow{CB} = \frac{1}{\sqrt{3}}(-\sqrt{3}, 12) = (-1, 4\sqrt{3})$$
Por lo tanto:
- $B = C + \overrightarrow{CB} = (-13, 16\sqrt{3})$

---

### Paso 3: Minimización de $f(X)$
Agrupamos los términos de $f(X)$ en dos partes:
$$f(X) = (AX + CX + DX) + (BX + EX)$$

1. **Cota para $BX + EX$:**
   Por la desigualdad triangular, para todo punto $X$ en el plano:
   $$BX + EX \ge BE$$
   con igualdad si y solo si $X$ pertenece al segmento $BE$. Calculamos la longitud de $BE$:
   $$BE = \sqrt{(-13 - 13)^2 + (16\sqrt{3} - 0)^2} = \sqrt{676 + 768} = \sqrt{1444} = 38$$

2. **Cota para $AX + CX + DX$:**
   El mínimo de $AX + CX + DX$ se alcanza cuando $X$ es el punto de Fermat $X_0$ del triángulo $\triangle ACD$. Construyendo externamente sobre el lado $CD$ un triángulo equilátero $\triangle CDC'$ (con $C' = (-24, 0)$), una rotación de $60^{\circ}$ alrededor de $D$ muestra que:
   $$AX + CX + DX \ge AC'$$
   Como $\angle ADC' = \angle ADC + \angle CDC' = 30^{\circ} + 60^{\circ} = 90^{\circ}$, el triángulo $\triangle ADC'$ es rectángulo en $D$, por lo que:
   $$AC' = \sqrt{AD^2 + DC'^2} = \sqrt{(13\sqrt{3})^2 + 24^2} = \sqrt{507 + 576} = \sqrt{1083} = 19\sqrt{3}$$

3. **Verificación de que $X_0$ yace sobre el segmento $BE$:**
   El punto de Fermat $X_0$ de $\triangle ACD$ es la intersección de $AC'$ con $DP'$, donde $\triangle ACP'$ es el triángulo equilátero externo sobre $AC$. Usando las coordenadas de $A=(0, 13\sqrt{3})$ y $C=(-12, 12\sqrt{3})$, el tercer vértice es $P' = \left(-\frac{15}{2}, \frac{37}{2}\sqrt{3}\right)$.
   - La recta $DP'$ está dada por $(x, y) = (-15t, 37\sqrt{3}t)$.
   - Sustituyendo en la recta $AC'$ ($-13x + 8\sqrt{3}y = 312$), obtenemos $(195 + 888)t = 312 \implies t = \frac{104}{361}$.
   - Sustituyendo el mismo punto en la ecuación del segmento $BE$ ($8x + \frac{13}{\sqrt{3}}y = 104$), tenemos $(-120 + 481)t = 361t = 104$, con $x \approx -4.32 \in [-13, 13]$.

   Así, el punto de Fermat $X_0$ de $\triangle ACD$ pertenece exactamente al segmento $BE$, logrando simultáneamente la igualdad en ambas cotas.

---

### Paso 4: Resultado final
El valor mínimo de $f(X)$ es:
$$\min f(X) = BE + AC' = 38 + 19\sqrt{3}$$

Identificando $m = 38$, $n = 19$ y $p = 3$, obtenemos:
$$m + n + p = 38 + 19 + 3 = 60$$

\boxed{60}