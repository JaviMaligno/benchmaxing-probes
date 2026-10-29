

Sea  
\[
A=\angle YXZ,\qquad B=\angle XYZ,\qquad C=\angle XZY,
\]
y también
\[
a=YZ=16,\qquad b=ZX,\qquad c=XY.
\]
Como el triángulo es agudo, los pies de las alturas están sobre los lados.

### 1. Determinar el ángulo \(A\)

En el triángulo rectángulo \(XYR\), la hipotenusa es \(XY=c\) y el ángulo en \(X\) es \(A\), así que
\[
XR=c\cos A.
\]
En el triángulo rectángulo \(XZS\), la hipotenusa es \(XZ=b\), luego
\[
XS=b\cos A.
\]

Así, los triángulos \(XRS\) y \(XYZ\) tienen el mismo ángulo \(A\) y los lados que lo forman son proporcionales con razón \(\cos A\):
\[
\frac{XR}{XY}=\cos A,\qquad \frac{XS}{XZ}=\cos A.
\]
Por semejanza LAL, \(\triangle XRS\sim \triangle XYZ\) con razón \(\cos A\). Por tanto, la altura desde \(X\) hasta \(RS\) es \(\cos A\) veces la altura desde \(X\) hasta \(YZ\):
\[
XT=XP\cos A.
\]
Con \(XT=15\) y \(XP=20\),
\[
\cos A=\frac{15}{20}=\frac34.
\]
Entonces
\[
\sin A=\sqrt{1-\left(\frac34\right)^2}=\frac{\sqrt7}{4}.
\]

### 2. Lados del triángulo órtico \(PRS\)

Por la semejanza anterior,
\[
RS=YZ\cos A=a\cos A.
\]

Para \(PR\): como \(\angle XPY=\angle XRY=90^\circ\), los puntos \(X,P,Y,R\) están en una circunferencia de diámetro \(XY=c\). La cuerda \(PR\) subtiende el ángulo \(\angle PYR\). Como \(YP\) está sobre \(YZ\) y \(YR\perp XZ\),
\[
\angle PYR=90^\circ-C.
\]
En una circunferencia de diámetro \(d\), una cuerda que subtiende un ángulo inscrito \(\theta\) mide \(d\sin\theta\). Así,
\[
PR=c\sin(90^\circ-C)=c\cos C.
\]

Análogamente, \(X,P,Z,S\) están en la circunferencia de diámetro \(XZ=b\), y se obtiene
\[
PS=b\cos B.
\]

Por lo tanto, el perímetro \(p\) de \(\triangle PRS\) es
\[
p=a\cos A+b\cos B+c\cos C.
\]

### 3. Evaluar el perímetro

Sea \(\rho\) el circunradio de \(\triangle XYZ\). Por la ley de los senos extendida,
\[
a=2\rho\sin A,\quad b=2\rho\sin B,\quad c=2\rho\sin C.
\]
Entonces
\[
p=2\rho(\sin A\cos A+\sin B\cos B+\sin C\cos C)
=\rho(\sin 2A+\sin 2B+\sin 2C).
\]
Como \(A+B+C=\pi\),
\[
\sin 2A+\sin 2B+\sin 2C=4\sin A\sin B\sin C.
\]
Luego
\[
p=4\rho\sin A\sin B\sin C.
\]
El área \(\Delta\) de \(\triangle XYZ\) satisface
\[
\Delta=\frac{abc}{4\rho}=2\rho^2\sin A\sin B\sin C,
\]
así que
\[
p=\frac{2\Delta}{\rho}.
\]

Ahora,
\[
\Delta=\frac12\cdot YZ\cdot XP=\frac12\cdot 16\cdot 20=160,
\]
y
\[
\rho=\frac{a}{2\sin A}=\frac{16}{2\cdot \frac{\sqrt7}{4}}=\frac{32}{\sqrt7}.
\]
Por tanto,
\[
p=\frac{2\cdot 160}{32/\sqrt7}=10\sqrt7.
\]

\[
\boxed{10\sqrt{7}}
\]