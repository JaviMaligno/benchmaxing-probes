## Planteamiento

Coloco el prisma como $[0,A]\times[0,B]\times[0,C]$ y el plano como $px+qy+rz=s$ con $p,q,r>0$. Para una sección hexagonal, el plano corta las seis caras, y los lados opuestos del hexágono están en caras paralelas. Los vértices del hexágono, en orden, están en las aristas:

$$V_1=\Big(A,\tfrac{s-pA}{q},0\Big),\ V_2=\Big(\tfrac{s-qB}{p},B,0\Big),\ V_3=\Big(0,B,\tfrac{s-qB}{r}\Big),$$
$$V_4=\Big(0,\tfrac{s-rC}{q},C\Big),\ V_5=\Big(\tfrac{s-rC}{p},0,C\Big),\ V_6=\Big(A,0,\tfrac{s-pA}{r}\Big).$$

## Longitudes de los lados

Calculando cada lado directamente, con $P=\tfrac1{p^2}+\tfrac1{q^2}$, $Q=\tfrac1{p^2}+\tfrac1{r^2}$, $R=\tfrac1{q^2}+\tfrac1{r^2}$:

- $S_1^2=(s-pA-qB)^2\,P$ y $S_4^2=(s-rC)^2\,P$ (par $45,55$),
- $S_2^2=(s-qB)^2\,Q$ y $S_5^2=(s-pA-rC)^2\,Q$ (par $66,54$),
- $S_3^2=(s-qB-rC)^2\,R$ y $S_6^2=(s-pA)^2\,R$ (par $63,77$).

Para que el hexágono exista: $s-qB,\ s-rC,\ s-pA\ge 0$ y $s-pA-qB,\ s-pA-rC,\ s-qB-rC\le 0$.

## Observación clave

Sea $K=pA+qB+rC-2s$. En cada par, los dos parámetros suman lo mismo:

$$(s-pA-qB)+(s-rC)=(s-pA-rC)+(s-qB)=(s-qB-rC)+(s-pA)=-K.$$

Con los signos indicados, tomando $k=|K|$:

$$\frac{55-45}{\sqrt{P}}=\frac{10}{\sqrt{P}}=k,\qquad \frac{66-54}{\sqrt{Q}}=\frac{12}{\sqrt{Q}}=k,\qquad \frac{77-63}{\sqrt{R}}=\frac{14}{\sqrt{R}}=k.$$

Entonces $P=\dfrac{100}{k^2}$, $Q=\dfrac{144}{k^2}$, $R=\dfrac{196}{k^2}$, y resolviendo el sistema:

$$\frac1{p^2}=\frac{P+Q-R}{2}=\frac{24}{k^2},\qquad \frac1{q^2}=\frac{76}{k^2},\qquad \frac1{r^2}=\frac{120}{k^2}.$$

Es decir, $p^2=\tfrac{k^2}{24}$, $q^2=\tfrac{k^2}{76}$, $r^2=\tfrac{k^2}{120}$.

## Distancia al centro

El centro es $\big(\tfrac A2,\tfrac B2,\tfrac C2\big)$, así que la distancia es

$$d=\frac{|K|}{2\sqrt{p^2+q^2+r^2}}=\frac{k}{2k\sqrt{\tfrac1{24}+\tfrac1{76}+\tfrac1{120}}}=\frac{1}{2\sqrt{\tfrac1{24}+\tfrac1{76}+\tfrac1{120}}}.$$

Con denominador común $2280$: $\tfrac1{24}+\tfrac1{76}+\tfrac1{120}=\tfrac{95+30+19}{2280}=\tfrac{144}{2280}=\tfrac{6}{95}$.

Por lo tanto,

$$d=\frac{1}{2}\sqrt{\frac{95}{6}}=\frac{\sqrt{570}}{12}.$$

$$\boxed{\dfrac{\sqrt{570}}{12}}$$