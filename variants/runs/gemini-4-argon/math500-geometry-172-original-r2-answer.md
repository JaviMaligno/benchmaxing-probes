Para encontrar el área del triángulo $ENG$, podemos analizar las proporciones de los segmentos y las áreas dentro del triángulo $ABC$:

1. **Propiedades del baricentro ($G$):**
   Las medianas $AD$, $BE$ y $CF$ dividen al triángulo $ABC$ en áreas proporcionales. En particular, el baricentro $G$ divide a cada mediana en una razón de $2:1$, por lo que:
   $$\frac{AG}{AD} = \frac{2}{3}$$
   Además, el baricentro divide al triángulo $ABC$ en tres triángulos de igual área ($\triangle AGB$, $\triangle BGC$ y $\triangle AGC$). Dado que el área de $\triangle ABC$ es $144$, tenemos que:
   $$\text{Área}(\triangle AGC) = \frac{1}{3} \text{Área}(\triangle ABC) = \frac{144}{3} = 48$$

2. **Posición de los puntos $E$ y $N$ sobre el lado $AC$:**
   - Como $BE$ es una mediana, $E$ es el punto medio del lado $AC$, lo que significa que:
     $$AE = \frac{1}{2} AC$$
   - Como la recta $MN$ pasa por $G$ y es paralela a $BC$, por el teorema de Tales (o por semejanza entre $\triangle AGN$ y $\triangle ADC$), tenemos que:
     $$\frac{AN}{AC} = \frac{AG}{AD} = \frac{2}{3} \implies AN = \frac{2}{3} AC$$

3. **Longitud del segmento $EN$:**
   Dado que los puntos $A, E, N, C$ son colineales en ese orden sobre el lado $AC$, la longitud de $EN$ es:
   $$EN = AN - AE = \frac{2}{3} AC - \frac{1}{2} AC = \frac{1}{6} AC$$

4. **Área del triángulo $ENG$:**
   Los triángulos $ENG$ y $AGC$ comparten la misma altura trazada desde el vértice $G$ hacia la recta que contiene al lado $AC$. Por lo tanto, la razón entre sus áreas es igual a la razón entre sus bases:
   $$\frac{\text{Área}(\triangle ENG)}{\text{Área}(\triangle AGC)} = \frac{EN}{AC} = \frac{1}{6}$$
   Sustituyendo el área de $\triangle AGC$:
   $$\text{Área}(\triangle ENG) = \frac{1}{6} \times 48 = 8$$

\boxed{8}