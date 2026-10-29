## Planteamiento con coordenadas

Coloco el trapecio con $D=(0,0)$, $C=(19,0)$, y $A=(x,h)$, $B=(x+11,h)$.

- $DA=4$: $x^2+h^2=16$
- $BC=8$: $(x+11-19)^2+h^2=64 \Rightarrow (x-8)^2+h^2=64$

Restando: $-16x+64=48 \Rightarrow x=1$, luego $h^2=15$, $h=\sqrt{15}$.

Entonces: $A=(1,\sqrt{15})$, $B=(12,\sqrt{15})$, $C=(19,0)$, $D=(0,0)$.

## Circuncentros

**$O_1$ ($\triangle ABC$):** la mediatriz de $AB$ es $x=\tfrac{13}{2}$. Usando la mediatriz de $BC$ (punto medio $(15.5,\tfrac{\sqrt{15}}2)$, pendiente $\tfrac{7}{\sqrt{15}}$):
$$y=\tfrac{\sqrt{15}}2+\tfrac{7}{\sqrt{15}}(6.5-15.5)=\tfrac{15/2-63}{\sqrt{15}}=-\tfrac{111}{2\sqrt{15}} \Rightarrow O_1=\left(\tfrac{13}{2},-\tfrac{111}{2\sqrt{15}}\right)$$

**$O_2$ ($\triangle BCD$):** mediatriz de $CD$: $x=\tfrac{19}{2}$. Con la mediatriz de $BD$:
$$y=\tfrac{\sqrt{15}}2-\tfrac{12}{\sqrt{15}}(9.5-6)=-\tfrac{69}{2\sqrt{15}} \Rightarrow O_2=\left(\tfrac{19}{2},-\tfrac{69}{2\sqrt{15}}\right)$$

**$O_3$ ($\triangle CDA$):** $x=\tfrac{19}{2}$; con la mediatriz de $DA$ (pendiente $-\tfrac1{\sqrt{15}}$):
$$y=\tfrac{\sqrt{15}}2-\tfrac{9}{\sqrt{15}}=-\tfrac{3}{2\sqrt{15}} \Rightarrow O_3=\left(\tfrac{19}{2},-\tfrac{3}{2\sqrt{15}}\right)$$

**$O_4$ ($\triangle DAB$):** $x=\tfrac{13}{2}$; con la misma mediatriz de $DA$:
$$y=\tfrac{\sqrt{15}}2-\tfrac{6}{\sqrt{15}}=\tfrac{3}{2\sqrt{15}} \Rightarrow O_4=\left(\tfrac{13}{2},\tfrac{3}{2\sqrt{15}}\right)$$

## Área

El cuadrilátero tiene dos lados verticales: en $x=\tfrac{13}{2}$ (longitud $\tfrac{111+3}{2\sqrt{15}}=\tfrac{57}{\sqrt{15}}$) y en $x=\tfrac{19}{2}$ (longitud $\tfrac{69-3}{2\sqrt{15}}=\tfrac{33}{\sqrt{15}}$), con distancia $3$ entre ellos. Es un trapecio:

$$\text{Área}=\frac{1}{2}\left(\frac{57}{\sqrt{15}}+\frac{33}{\sqrt{15}}\right)\cdot 3=\frac{135}{\sqrt{15}}=9\sqrt{15}$$

$$\boxed{9\sqrt{15}}$$