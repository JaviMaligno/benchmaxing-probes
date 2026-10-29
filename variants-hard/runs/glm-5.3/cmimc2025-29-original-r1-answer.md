## Planteamiento

Coloco el trapecio en coordenadas: $D=(0,0)$, $C=(130,0)$, $A=(0,33)$, $B=(18,33)$. Se cumple $AB=18$, $AD=33$, $CD=130$ y $\angle ADC=90^\circ$.

## Paso 1: Familia de cónicas por los cuatro vértices

Una cónica general es $ax^2+bxy+cy^2+dx+ey+f=0$.

- Por $D=(0,0)$: $f=0$.
- Por $A=(0,33)$: $1089c+33e=0\Rightarrow e=-33c$.
- Por $C=(130,0)$: $16900a+130d=0\Rightarrow d=-130a$.
- Por $B=(18,33)$: $324a+594b+1089c+18d+33e=0$, es decir
$$324a+594b+1089c-2340a-1089c=0 \Rightarrow 594b=2016a \Rightarrow b=\tfrac{112}{33}a.$$

Fijando $a=1$ y escribiendo $t=c$:

$$x^2+\tfrac{112}{33}xy+ty^2-130x-33ty=0.$$

## Paso 2: Condición de elipse

La parte cuadrática tiene matriz
$$Q=\begin{pmatrix}1 & \tfrac{56}{33}\\[2pt] \tfrac{56}{33} & t\end{pmatrix},$$
que es definida positiva si y solo si $t-\left(\tfrac{56}{33}\right)^2>0$. Sea $b=\tfrac{56}{33}$; toda $t>b^2$ da una elipse real por los cuatro vértices.

## Paso 3: Razón de ejes

Los semiejes de la elipse son $\sqrt{k/\lambda_i}$ donde $\lambda_1,\lambda_2$ son los autovalores de $Q$. Por tanto la razón buscada es
$$\sqrt{\frac{\lambda_{\max}}{\lambda_{\min}}}.$$

Con $s=1+t$ y $\Delta=\sqrt{(1-t)^2+4b^2}$, los autovalores son $\tfrac{s\pm\Delta}{2}$, así que hay que minimizar $r(t)=\dfrac{s+\Delta}{s-\Delta}$.

Derivando: $r'(t)=0$ equivale a $\Delta' \cdot s = \Delta$, y como $\Delta' = \tfrac{t-1}{\Delta}$:

$$(t-1)(t+1)=\Delta^2=(1-t)^2+4b^2 \Rightarrow t^2-1=1-2t+t^2+4b^2 \Rightarrow t=1+2b^2.$$

(Es el único punto crítico; $r\to\infty$ cuando $t\to b^{2+}$ y cuando $t\to\infty$, así que es el mínimo.)

## Paso 4: Valor mínimo

Con $t=1+2b^2$:
$$\Delta^2=4b^4+4b^2=4b^2(1+b^2),\qquad s=2(1+b^2),$$
$$\lambda_\pm=\sqrt{1+b^2}\left(\sqrt{1+b^2}\pm b\right).$$

Entonces
$$\sqrt{\frac{\lambda_+}{\lambda_-}}=\sqrt{\frac{\sqrt{1+b^2}+b}{\sqrt{1+b^2}-b}}=\sqrt{1+b^2}+b,$$

pues $\left(\sqrt{1+b^2}+b\right)\left(\sqrt{1+b^2}-b\right)=1$.

Con $b=\tfrac{56}{33}$: $\sqrt{1+b^2}=\sqrt{\tfrac{4225}{1089}}=\tfrac{65}{33}$ (trío pitagórico $33$-$56$-$65$):

$$\frac{65}{33}+\frac{56}{33}=\frac{121}{33}=\frac{11}{3}.$$

\boxed{\dfrac{11}{3}}