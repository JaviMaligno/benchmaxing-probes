Para calcular el perímetro del triángulo órtico $\triangle DEF$, procedemos paso a paso utilizando las propiedades geométricas de las alturas de un triángulo acutángulo.

### Paso 1: Semejanza entre $\triangle AEF$ y $\triangle ABC$
Dado que $BE \perp AC$ y $CF \perp AB$, tenemos que $\angle BEC = \angle BFC = 90^\circ$. Esto implica que el cuadrilátero $BCEF$ es cíclico (inscrito en la circunferencia de diámetro $\overline{BC}$).

Por las propiedades de los cuadriláteros cíclicos:
$$\angle AEF = \angle ABC \quad \text{y} \quad \angle AFE = \angle ACB$$

Por lo tanto, $\triangle AEF \sim \triangle ABC$ (criterio AA). En el triángulo rectángulo $\triangle ABE$, tenemos que $\frac{AE}{AB} = \cos A$, por lo que la razón de semejanza entre $\triangle AEF$ y $\triangle ABC$ es $\cos A$.

### Paso 2: Cálculo de $\cos A$ y $\sin A$
En $\triangle ABC$, el segmento $\overline{AD}$ es la altura desde el vértice $A$ hacia el lado opuesto $\overline{BC}$. En el triángulo semejante $\triangle AEF$, el segmento $\overline{AQ}$ es la altura correspondiente desde el vértice $A$ hacia el lado opuesto $\overline{EF}$.

Dado que la razón entre las alturas correspondientes de dos triángulos semejantes es igual a su razón de semejanza, se cumple que:
$$\frac{AQ}{AD} = \cos A$$

Sustituyendo los valores dados $AQ = 20$ y $AD = 24$:
$$\cos A = \frac{20}{24} = \frac{5}{6}$$

Como el triángulo $\triangle ABC$ es acutángulo, $\sin A > 0$, y por la identidad pitagórica obtenemos:
$$\sin A = \sqrt{1 - \cos^2 A} = \sqrt{1 - \left(\frac{5}{6}\right)^2} = \sqrt{1 - \frac{25}{36}} = \frac{\sqrt{11}}{6}$$

### Paso 3: Perímetro del triángulo órtico $\triangle DEF$
Es una propiedad conocida que en todo triángulo acutángulo $\triangle ABC$, las alturas $\overline{AD}$, $\overline{BE}$ y $\overline{CF}$ son las bisectrices interiores de su triángulo órtico $\triangle DEF$, y los lados de $\triangle ABC$ son las bisectrices exteriores de $\triangle DEF$.

Si reflejamos el punto $D$ con respecto a la recta $AB$ para obtener $D_1$, y con respecto a la recta $AC$ para obtener $D_2$:
1. Por simetría axial, $D_1F = DF$ y $D_2E = DE$.
2. Como $\overline{AB}$ y $\overline{AC}$ son las bisectrices exteriores en $F$ y $E$, los puntos $D_1, F, E, D_2$ son colineales. Así, el perímetro del triángulo $\triangle DEF$ es igual a la longitud del segmento $\overline{D_1D_2}$:
   $$\text{Perímetro}(DEF) = DF + FE + ED = D_1F + FE + ED_2 = D_1D_2$$
3. Además, por las reflexiones tenemos que $AD_1 = AD$ y $AD_2 = AD$, y el ángulo $\angle D_1AD_2$ es:
   $$\angle D_1AD_2 = 2\angle BAD + 2\angle DAC = 2\angle BAC = 2A$$

En el triángulo isósceles $\triangle AD_1D_2$ (con $AD_1 = AD_2 = AD$), la base $D_1D_2$ mide:
$$\text{Perímetro}(DEF) = D_1D_2 = 2 \cdot AD \cdot \sin A$$

Sustituyendo $AD = 24$ y $\sin A = \frac{\sqrt{11}}{6}$:
$$\text{Perímetro}(DEF) = 2 \cdot 24 \cdot \frac{\sqrt{11}}{6} = 8\sqrt{11}$$

\boxed{8\sqrt{11}}