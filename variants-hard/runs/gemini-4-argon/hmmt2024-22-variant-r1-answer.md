Para hallar la longitud de la hipotenusa $QR$, analizamos las propiedades geométricas del triángulo rectángulo $PQR$ con $\angle QPR = 90^{\circ}$.

1. **Posición de los puntos y relación angular:**
   Supongamos sin pérdida de generalidad que $PQ < PR$. Entonces, los puntos sobre la hipotenusa $QR$ se encuentran en el orden $Q, X, Y, Z, R$.
   - Como $PX$ es la altura sobre la hipotenusa, en el triángulo rectángulo $PQX$ se cumple que $\angle QPX = 90^{\circ} - \angle Q = \angle R$.
   - Como $PY$ es la bisectriz de $\angle QPR = 90^{\circ}$, tenemos que $\angle QPY = \angle YPR = 45^{\circ}$.
   - Como $PZ$ es la mediana relativa a la hipotenusa de un triángulo rectángulo, se cumple que $PZ = QZ = RZ = \frac{1}{2}QR$. Por lo tanto, el triángulo $PZR$ es isósceles con $PZ = RZ$, lo que implica que $\angle ZPR = \angle R$.

   Observamos entonces que:
   $$\angle XPY = \angle QPY - \angle QPX = 45^{\circ} - \angle R$$
   $$\angle YPZ = \angle YPR - \angle ZPR = 45^{\circ} - \angle R$$
   Esto demuestra que $\angle XPY = \angle YPZ$, es decir, $PY$ también es la bisectriz del ángulo $\angle XPZ$ en el triángulo rectángulo $PXZ$.

2. **Aplicación del teorema de la bisectriz y el teorema de Pitágoras en $\triangle PXZ$:**
   Dado que $Y$ está entre $X$ y $Z$, la longitud del cateto $XZ$ en el triángulo rectángulo $PXZ$ (recto en $X$) es:
   $$XZ = XY + YZ = 5 + 13 = 18$$

   Por el teorema de la bisectriz aplicado al triángulo $PXZ$:
   $$\frac{PX}{PZ} = \frac{XY}{YZ} = \frac{5}{13}$$

   Podemos expresar $PX = 5k$ y $PZ = 13k$ para alguna constante positiva $k$. Aplicando el teorema de Pitágoras en $\triangle PXZ$:
   $$PX^2 + XZ^2 = PZ^2$$
   $$(5k)^2 + 18^2 = (13k)^2$$
   $$25k^2 + 324 = 169k^2$$
   $$144k^2 = 324 \implies 12k = 18 \implies k = \frac{3}{2}$$

3. **Cálculo de $QR$:**
   Con el valor de $k$, hallamos la longitud de la mediana $PZ$:
   $$PZ = 13k = 13 \cdot \frac{3}{2} = \frac{39}{2}$$

   Dado que en un triángulo rectángulo la hipotenusa mide el doble que la mediana relativa a ella:
   $$QR = 2 \cdot PZ = 2 \cdot \frac{39}{2} = 39$$

\boxed{39}