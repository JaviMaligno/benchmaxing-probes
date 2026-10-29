Para hallar la longitud de la hipotenusa $BC$, analizamos las propiedades geométricas de las líneas notables trazadas desde el vértice del ángulo recto $A$:

1. **Relación entre la altura, la bisectriz y la mediana:**
   En el triángulo rectángulo $ABC$ con $\angle BAC = 90^{\circ}$, $F$ es el punto medio de la hipotenusa $BC$, por lo que $F$ es el circuncentro del triángulo y se cumple que:
   $$AF = BF = CF = \frac{BC}{2}$$
   De esto se deduce que el triángulo $AFC$ es isósceles ($AF = CF$), por lo que $\angle CAF = \angle C$.
   Por otro lado, como $AD$ es la altura sobre la hipotenusa, en el triángulo rectángulo $ABD$ tenemos que $\angle BAD = 90^{\circ} - \angle B = \angle C$.
   Por lo tanto, $\angle BAD = \angle CAF$.

2. **La bisectriz en el triángulo $ADF$:**
   Como $AE$ es la bisectriz de $\angle BAC$ ($\angle BAE = \angle CAE$) y acabamos de ver que $\angle BAD = \angle CAF$, al restar estos ángulos obtenemos:
   $$\angle DAE = \angle BAE - \angle BAD = \angle CAE - \angle CAF = \angle FAE$$
   Esto demuestra que $AE$ es también la bisectriz del ángulo $\angle DAF$ en el triángulo rectángulo $ADF$ (recto en $D$). Además, el punto $E$ se encuentra entre $D$ y $F$, por lo que:
   $$DF = DE + EF = 3 + 5 = 8$$

3. **Teorema de la bisectriz y Teorema de Pitágoras:**
   Aplicando el teorema de la bisectriz en el triángulo $ADF$:
   $$\frac{AD}{AF} = \frac{DE}{EF} = \frac{3}{5} \implies AD = \frac{3}{5}AF$$
   Como $\angle ADF = 90^{\circ}$, aplicamos el teorema de Pitágoras en $\triangle ADF$:
   $$AD^2 + DF^2 = AF^2$$
   Sustituyendo $AD = \frac{3}{5}AF$ y $DF = 8$:
   $$\left(\frac{3}{5}AF\right)^2 + 8^2 = AF^2$$
   $$\frac{9}{25}AF^2 + 64 = AF^2$$
   $$\frac{16}{25}AF^2 = 64 \implies AF^2 = 64 \cdot \frac{25}{16} = 100 \implies AF = 10$$

4. **Cálculo de $BC$:**
   Dado que la mediana relativa a la hipotenusa mide la mitad de esta:
   $$BC = 2 \cdot AF = 2 \cdot 10 = 20$$

\boxed{20}