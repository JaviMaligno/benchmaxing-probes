Para encontrar el número de lados del polígono convexo, sigamos estos pasos:

1. **Suma de los ángulos interiores:** Sea $n$ el número de lados del polígono. La suma total de los ángulos interiores de un polígono de $n$ lados está dada por la fórmula:
   $$S = (n - 2) \times 180^{\circ}$$

2. **Condición de convexidad:** En un polígono convexo, cada ángulo interior $\theta$ cumple que:
   $$0^{\circ} < \theta < 180^{\circ}$$

3. **Planteamiento de la desigualdad:** Sabemos que la suma de todos los ángulos interiores excepto uno ($\theta$) es $1550^{\circ}$. Por lo tanto, la suma total es:
   $$(n - 2) \times 180^{\circ} = 1550^{\circ} + \theta$$

   Como $0^{\circ} < \theta < 180^{\circ}$, tenemos:
   $$1550^{\circ} < (n - 2) \times 180^{\circ} < 1550^{\circ} + 180^{\circ}$$
   $$1550^{\circ} < (n - 2) \times 180^{\circ} < 1730^{\circ}$$

4. **Resolución para $n$:** Dividimos toda la desigualdad entre $180^{\circ}$:
   $$\frac{1550}{180} < n - 2 < \frac{1730}{180}$$
   $$8.61 < n - 2 < 9.61$$

   Dado que $n$ debe ser un número entero, el único valor entero posible para $n - 2$ es $9$:
   $$n - 2 = 9 \implies n = 11$$

   *(Verificación: Si $n = 11$, la suma total es $9 \times 180^{\circ} = 1620^{\circ}$, por lo que el ángulo faltante mide $1620^{\circ} - 1550^{\circ} = 70^{\circ}$, lo cual es válido para un polígono convexo).*

\boxed{11}