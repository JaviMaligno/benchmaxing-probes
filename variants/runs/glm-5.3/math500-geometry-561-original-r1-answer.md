Un octágono equiangulo tiene ángulos exteriores de \(360^\circ/8=45^\circ\).

Como los lados solo tienen dos longitudes y no puede haber dos consecutivos iguales, se alternan: \(1,\frac{\sqrt2}{2},1,\frac{\sqrt2}{2},\ldots\)

Tomemos los lados en direcciones \(0^\circ,45^\circ,90^\circ,\ldots\). Para el lado corto,

\[
\frac{\sqrt2}{2}\cos45^\circ=\frac{\sqrt2}{2}\cdot\frac{\sqrt2}{2}=\frac12
\]

así que sus componentes son \(\pm\frac12,\pm\frac12\).

Los vértices resultan:

\[
(0,0),(1,0),\left(\frac32,\frac12\right),\left(\frac32,\frac32\right),(1,2),(0,2),\left(-\frac12,\frac32\right),\left(-\frac12,\frac12\right)
\]

Usando la fórmula del shoelace,

\[
A=\frac12\left|\sum x_i y_{i+1}-y_i x_{i+1}\right|=\frac12(7)=\frac72
\]

\[
\boxed{\frac72}
\]