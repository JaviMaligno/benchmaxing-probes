## Planteamiento

Como $\overline{AB}$ es diámetro, $\angle ACB=\angle ADB=90^\circ$. Entonces en el triángulo $EAB$ (con $D\in \overline{AE}$, $C\in \overline{BE}$):

- $\cos\angle A=\dfrac{AD}{AB}=\dfrac{7}{20}$, $\sin\angle A=\dfrac{\sqrt{351}}{20}=\dfrac{3\sqrt{39}}{20}$
- $\cos\angle B=\dfrac{BC}{AB}=\dfrac{13}{20}$, $\sin\angle B=\dfrac{\sqrt{231}}{20}$

Por potencia de $E$: $EC\cdot EB=ED\cdot EA$, luego $\triangle ECD\sim\triangle EAB$ con razón $k=\dfrac{CD}{AB}$.

## Clave: $L$ cae sobre $\overline{AB}$

Si $E'$ es el excentro opuesto a $E$ en $ECD$, la tangente desde $E$ vale $s$ (semiperímetro de $ECD$), así que $EL=\dfrac{s}{\cos(E/2)}$, con
$$s=\tfrac{k}{2}(EA+EB+AB).$$

La bisectriz interior de $\angle E$ (la misma para ambos triángulos) corta a $\overline{AB}$ en $P$ con $EP=\dfrac{2\,EA\cdot EB\cos(E/2)}{EA+EB}$. Entonces $L=P$ equivale a
$$s(EA+EB)=EA\cdot EB(1+\cos E)=\tfrac12\big((EA+EB)^2-AB^2\big),$$
es decir a $(AB-CD)(EA+EB)=AB^2$.

Verifiquémoslo: con $\sin E=\sin(A+B)=\dfrac{39\sqrt{39}+7\sqrt{231}}{400}$ y la ley de senos,
$$EA+EB=\frac{\sqrt{231}+3\sqrt{39}}{\sin E}=\frac{400(\sqrt{231}+3\sqrt{39})}{39\sqrt{39}+7\sqrt{231}}\ \Longrightarrow\ \frac{AB^2}{EA+EB}=\frac{491-9\sqrt{1001}}{20}.$$
Y de las coordenadas $C=\left(\tfrac{31}{20},\tfrac{13\sqrt{231}}{20}\right)$, $D=\left(-\tfrac{151}{20},\tfrac{21\sqrt{39}}{20}\right)$ (con $O$ en el origen):
$$CD^2=\frac{89362-1638\sqrt{1001}}{400}\ \Longrightarrow\ CD=\frac{9\sqrt{1001}-91}{20}=20-\frac{491-9\sqrt{1001}}{20}.$$
La identidad se cumple exactamente, de modo que $L$ es el pie de la bisectriz de $\angle E$ sobre $\overline{AB}$.

## Cálculo de $OL$

$\dfrac{AL}{LB}=\dfrac{EA}{EB}=\dfrac{\sin B}{\sin A}=\dfrac{\sqrt{231}}{3\sqrt{39}}$, luego $AL=\dfrac{20\sqrt{231}}{\sqrt{231}+3\sqrt{39}}$ y
$$OL=\left|10-AL\right|=\frac{10\left(3\sqrt{39}-\sqrt{231}\right)}{3\sqrt{39}+\sqrt{231}}=\frac{10(582-6\sqrt{9009})}{120}=\frac{97-3\sqrt{1001}}{2}\approx 1.0421.$$

(Comprobación numérica directa del excentro con la fórmula $L=\frac{-e\,E+c\,C+d\,D}{-e+c+d}$ da $L\approx(-1.0421,\,0)$.)

$$\boxed{\dfrac{97-3\sqrt{1001}}{2}}$$