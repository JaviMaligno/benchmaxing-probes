**Respuesta: 16/35.**

Razonamiento:

**Coordenadas.** Coloco $Y=(0,0)$, $Z=(6,0)$. Con $XY=5$, $XZ=7$ se obtiene $X=(1,\,2\sqrt6)$ (pues $x^2+y^2=25$ y $(x-6)^2+y^2=49$ dan $x=1$, $y=2\sqrt6$).

**Condición de razón.** Sea $Q=(q,h)$. De $YQ/QZ = 1/2$:
$$q^2+h^2 = \tfrac14\big[(q-6)^2+h^2\big] \;\Longrightarrow\; q^2+h^2+4q-12=0,$$
que es el círculo de Apolonio $(q+2)^2+h^2=16$.

**Condición angular.** Igualando $\tan(\angle XYQ)=\tan(\angle XZQ)$ con productos cruz/punto de los vectores $YX=(1,2\sqrt6),\,YQ=(q,h)$ y $ZX=(-5,2\sqrt6),\,ZQ=(q-6,h)$ (con los signos correctos para $Q$ interior):
$$\frac{2\sqrt6\,q-h}{q+2\sqrt6\,h}=\frac{12\sqrt6-2\sqrt6\,q-5h}{30-5q+2\sqrt6\,h}.$$
Al desarrollar y simplificar queda
$$-4\sqrt6(q^2-h^2)+24\sqrt6\,q+29h(q-3)=0.$$
Sustituyendo $h^2 = 12-4q-q^2$ del círculo de Apolonio:
$$-8\sqrt6\,(q^2-q-6)+29h(q-3)=0 \;\Longrightarrow\; (q-3)\big[-8\sqrt6(q+2)+29h\big]=0.$$
La rama $q=3$ es imposible (daría $h^2=-9$), así que
$$h=\frac{8\sqrt6\,(q+2)}{29}.$$

**Resolver.** Sustituyendo en $q^2+h^2+4q-12=0$:
$$1225\,q^2+4900\,q-8556=0 \;\Longrightarrow\; q=\frac{-4900+8120}{2450}=\frac{46}{35},$$
y entonces
$$h=\frac{8\sqrt6}{29}\cdot\frac{116}{35}=\frac{32\sqrt6}{35}.$$

**Razón de áreas.** Ambos triángulos comparten la base $YZ$, así que la razón es la de las alturas: la de $X$ es $2\sqrt6$ y la de $Q$ es $h$:
$$\frac{[YQZ]}{[XYZ]}=\frac{32\sqrt6/35}{2\sqrt6}=\frac{16}{35}.$$

$$\boxed{\dfrac{16}{35}}$$