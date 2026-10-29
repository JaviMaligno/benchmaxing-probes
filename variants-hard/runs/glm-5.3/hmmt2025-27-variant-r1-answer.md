## Planteamiento

Sean los ángulos del triángulo: $\alpha=\angle XYZ$, $\beta=\angle XZQ$… más precisely $\beta=\angle XZY$, $\gamma=\angle YXZ$. Por la ley de coseno:

- $\cos\alpha=\dfrac{XY^2+YZ^2-XZ^2}{2\cdot XY\cdot YZ}=\dfrac{25+36-49}{60}=\dfrac15$, $\quad\sin\alpha=\dfrac{2\sqrt6}{5}$
- $\cos\beta=\dfrac{XZ^2+YZ^2-XY^2}{2\cdot XZ\cdot YZ}=\dfrac{60}{84}=\dfrac57$, $\quad\sin\beta=\dfrac{2\sqrt6}{7}$
- $\cos\gamma=\dfrac{25+49-36}{2\cdot35}=\dfrac{19}{35}$, $\quad\sin\gamma=\dfrac{12\sqrt6}{35}$, $\quad [XYZ]=\tfrac12\cdot35\cdot\sin\gamma=6\sqrt6$

## Condición angular

Sea $\varphi=\angle XYQ=\angle XZQ$. Como $Q$ es interior, la ceviana $YQ$ divide $\alpha$ en $\varphi$ y $\alpha-\varphi$, y $ZQ$ divide $\beta$ en $\varphi$ y $\beta-\varphi$.

En $\triangle YQZ$ los ángulos son $\alpha-\varphi$ (en $Y$), $\beta-\varphi$ (en $Z$) y $\gamma+2\varphi$ (en $Q$). Por la ley de seno:

$$\frac{YQ}{QZ}=\frac{\sin(\beta-\varphi)}{\sin(\alpha-\varphi)}=\frac12 \;\Longrightarrow\; 2\sin(\beta-\varphi)=\sin(\alpha-\varphi)$$

Expandiendo:

$$2\sin\beta\cos\varphi-2\cos\beta\sin\varphi=\sin\alpha\cos\varphi-\cos\alpha\sin\varphi$$

$$(2\sin\beta-\sin\alpha)\cos\varphi=(2\cos\beta-\cos\alpha)\sin\varphi$$

$$\tan\varphi=\frac{2\cdot\frac{2\sqrt6}{7}-\frac{2\sqrt6}{5}}{2\cdot\frac57-\frac15}=\frac{\frac{6\sqrt6}{35}}{\frac{43}{35}}=\frac{6\sqrt6}{43}$$

Entonces $\sin\varphi=\dfrac{6\sqrt6}{\sqrt{2065}}$, $\cos\varphi=\dfrac{43}{\sqrt{2065}}$.

## Cálculo de los senos auxiliares

**Ángulos en $Y$ y $Z$:**
$$\sin(\alpha-\varphi)=\frac{2\sqrt6}{5}\cdot\frac{43}{\sqrt{2065}}-\frac15\cdot\frac{6\sqrt6}{\sqrt{2065}}=\frac{16\sqrt6}{\sqrt{2065}},\qquad \sin(\beta-\varphi)=\frac{8\sqrt6}{\sqrt{2065}}$$

(verificando: efectivamente $\sin(\beta-\varphi)=\tfrac12\sin(\alpha-\varphi)$ ✓)

**Ángulo en $Q$:** con $\cos 2\varphi=\dfrac{1633}{2065}$, $\sin 2\varphi=\dfrac{516\sqrt6}{2065}$:

$$\sin(\gamma+2\varphi)=\sin\gamma\cos 2\varphi+\cos\gamma\sin 2\varphi=\frac{12\sqrt6\cdot 1633+19\cdot 516\sqrt6}{35\cdot 2065}=\frac{168\sqrt6}{413}$$

## Razón de áreas

De nuevo por ley de seno en $\triangle YQZ$ (con $YZ=6$):

$$YQ=\frac{6\sin(\beta-\varphi)}{\sin(\gamma+2\varphi)},\qquad QZ=\frac{6\sin(\alpha-\varphi)}{\sin(\gamma+2\varphi)}$$

Por lo tanto:

$$\frac{[YQZ]}{[XYZ]}=\frac{\tfrac12\,YQ\cdot QZ\cdot\sin(\gamma+2\varphi)}{\tfrac12\cdot XY\cdot XZ\cdot\sin\gamma}
=\frac{36\,\sin(\beta-\varphi)\sin(\alpha-\varphi)}{35\,\sin\gamma\,\sin(\gamma+2\varphi)}$$

$$=\frac{36\cdot\dfrac{8\sqrt6\cdot 16\sqrt6}{2065}}{35\cdot\dfrac{12\sqrt6}{35}\cdot\dfrac{168\sqrt6}{413}}
=\frac{36\cdot 768\cdot 413}{2065\cdot 12096}
=\frac{36\cdot 768}{5\cdot 12096}
=\frac{16}{35}$$

**Comprobación numérica:** $\varphi\approx18.87°$ da $YQ\approx 2.60$, $QZ\approx 5.19$ (razón $\approx 0.5$ ✓) y $[YQZ]/[XYZ]\approx 0.4571\approx 16/35$ ✓.

$$\boxed{\dfrac{16}{35}}$$