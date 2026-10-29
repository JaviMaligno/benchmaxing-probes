Para hallar el valor mínimo posible de $f(X) = AX + BX + CX + DX + EX$, analizamos primero las propiedades geométricas del pentágono convexo $ABCDE$.

### Paso 1: Análisis de los triángulos $\triangle ABC$, $\triangle ADE$ y $\triangle ACD$
1. En el triángulo $\triangle ABC$, tenemos $AB = 14$, $BC = 7$ y $\angle B = 60^{\circ}$. Por la ley de cosenos:
   $$AC^2 = 14^2 + 7^2 - 2(14)(7)\cos 60^{\circ} = 196 + 49 - 98 = 147 \implies AC = 7\sqrt{3}.$$
   Como $BC^2 + AC^2 = 49 + 147 = 196 = AB^2$, el triángulo $\triangle ABC$ es rectángulo en $C$ ($\angle BCA = 90^{\circ}$) con $\angle BAC = 30^{\circ}$.

2. En el triángulo $\triangle ADE$, tenemos $EA = 26$, $DE = 13$ y $\angle E = 60^{\circ}$. De manera análoga:
   $$AD^2 = 26^2 + 13^2 - 2(26)(13)\cos 60^{\circ} = 676 + 169 - 338 = 507 \implies AD = 13\sqrt{3}.$$
   Como $DE^2 + AD^2 = 169 + 507 = 676 = EA^2$, el triángulo $\triangle ADE$ es rectángulo en $D$ ($\angle ADE = 90^{\circ}$) con $\angle DAE = 30^{\circ}$.

3. En el triángulo $\triangle ACD$, conocemos sus tres lados: $AC = 7\sqrt{3}$, $AD = 13\sqrt{3}$ y $CD = 24$. Calculamos $\angle ADC$ mediante la ley de cosenos:
   $$\cos(\angle ADC) = \frac{AD^2 + CD^2 - AC^2}{2 \cdot AD \cdot CD} = \frac{507 + 576 - 147}{2 \cdot 13\sqrt{3} \cdot 24} = \frac{936}{624\sqrt{3}} = \frac{\sqrt{3}}{2}.$$
   Por lo tanto, $\angle ADC = 30^{\circ}$. Además, todos los ángulos de $\triangle ACD$ son agudos (menores que $120^{\circ}$).

---

### Paso 2: Coordenadas de los vértices y longitud de $BE$
Situamos el segmento $CD$ sobre el eje $x$ con $C = (0,0)$ y $D = (24,0)$, y el pentágono en el semiplano superior:
- Como $\angle ADC = 30^{\circ}$ y $AD = 13\sqrt{3}$, el vértice $A$ tiene coordenadas:
  $$A = \left(24 - 13\sqrt{3}\cos 30^{\circ},\; 13\sqrt{3}\sin 30^{\circ}\right) = \left(\frac{9}{2},\; \frac{13\sqrt{3}}{2}\right).$$
- En $D$, el ángulo interior del pentágono es $\angle CDE = \angle ADC + \angle ADE = 30^{\circ} + 90^{\circ} = 120^{\circ}$. Como $DE = 13$, el vector $\overrightarrow{DE}$ forma un ángulo de $60^{\circ}$ con el semieje positivo $x$:
  $$E = \left(24 + 13\cos 60^{\circ},\; 13\sin 60^{\circ}\right) = \left(\frac{61}{2},\; \frac{13\sqrt{3}}{2}\right).$$
- En $C$, como $\angle BCA = 90^{\circ}$ y $BC = \frac{1}{\sqrt{3}}AC$, el vector $\overrightarrow{CB}$ se obtiene rotando $\overrightarrow{CA} = \left(\frac{9}{2}, \frac{13\sqrt{3}}{2}\right)$ un ángulo de $90^{\circ}$ en sentido antihorario y dividiendo por $\sqrt{3}$:
  $$B = \frac{1}{\sqrt{3}}\left(-\frac{13\sqrt{3}}{2},\; \frac{9}{2}\right) = \left(-\frac{13}{2},\; \frac{3\sqrt{3}}{2}\right).$$

Calculamos la longitud de la diagonal $BE$:
$$BE = \sqrt{\left(\frac{61}{2} - \left(-\frac{13}{2}\right)\right)^2 + \left(\frac{13\sqrt{3}}{2} - \frac{3\sqrt{3}}{2}\right)^2} = \sqrt{37^2 + (5\sqrt{3})^2} = \sqrt{1369 + 75} = \sqrt{1444} = 38.$$

---

### Paso 3: Minimización de $f(X)$ mediante el punto de Fermat
Separamos la suma en dos partes:
$$f(X) = (BX + EX) + (AX + CX + DX).$$

1. Por la desigualdad triangular, $BX + EX \ge BE = 38$, alcanzándose la igualdad si y solo si $X$ pertenece al segmento $BE$.
2. Para minimizar $AX + CX + DX$ en el triángulo $\triangle ACD$ (cuyos ángulos son todos menores que $120^{\circ}$), construimos un triángulo equilátero exterior $\triangle ADC'$ sobre el lado $AD$. El mínimo de $AX + CX + DX$ es igual a la longitud del segmento $CC'$ y se alcanza en el punto de Fermat $X_F$ de $\triangle ACD$.

Como $\angle ADC = 30^{\circ}$ y $\angle ADC' = 60^{\circ}$, tenemos $\angle CDC' = 30^{\circ} + 60^{\circ} = 90^{\circ}$ y $DC' = AD = 13\sqrt{3}$, por lo que $C' = (24, 13\sqrt{3})$. Aplicando el teorema de Pitágoras en $\triangle CDC'$:
$$CC' = \sqrt{CD^2 + (DC')^2} = \sqrt{24^2 + (13\sqrt{3})^2} = \sqrt{576 + 507} = \sqrt{1083} = 19\sqrt{3}.$$

Comprobamos que el punto de Fermat $X_F$ de $\triangle ACD$ pertenece efectivamente al segmento $BE$:
- La recta $CC'$ pasa por $(0,0)$ y $(24, 13\sqrt{3})$, luego tiene ecuación $y = \frac{13\sqrt{3}}{24}x$.
- Construyendo el triángulo equilátero exterior $\triangle ACD'$ sobre $AC$, su vértice es $D' = \left(-\frac{15}{2}, \frac{11\sqrt{3}}{2}\right)$, y la recta $DD'$ tiene ecuación $y = -\frac{11\sqrt{3}}{63}(x - 24)$.
- La intersección de $CC'$ y $DD'$ nos da el punto de Fermat $X_F = \left(\frac{2112}{361}, \frac{1144\sqrt{3}}{361}\right)$.
- La recta $BE$ tiene ecuación $y - \frac{3\sqrt{3}}{2} = \frac{5\sqrt{3}}{37}\left(x + \frac{13}{2}\right) \iff y = \frac{\sqrt{3}}{37}(5x + 88)$. Sustituyendo $x = \frac{2112}{361}$:
  $$y = \frac{\sqrt{3}}{37}\left(\frac{10560 + 31768}{361}\right) = \frac{\sqrt{3}}{37} \cdot \frac{42328}{361} = \frac{1144\sqrt{3}}{361}.$$

Como $X_F$ yace en el interior del segmento $BE$, ambas cotas inferiores se alcanzan simultáneamente en $X = X_F$.

---

### Paso 4: Resultado final
El valor mínimo posible de $f(X)$ es:
$$\min f(X) = BE + CC' = 38 + 19\sqrt{3}.$$

Identificando $m = 38$, $n = 19$ y $p = 3$, obtenemos:
$$m + n + p = 38 + 19 + 3 = 60.$$

\boxed{60}