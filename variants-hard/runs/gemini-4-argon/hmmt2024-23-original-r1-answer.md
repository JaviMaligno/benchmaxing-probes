Para encontrar la longitud de la cuerda, planteemos el problema geométricamente paso a paso:

1. **Definición de elementos y posiciones en la cuerda:**
   Sea $O$ el centro de la circunferencia $\Omega$ (de radio $R = 123$).
   Supongamos que la recta que contiene a la cuerda corta a $\Omega$ en los puntos $A$ y $D$, y corta a $\omega$ (de radio $r = 61$) en los puntos $B$ y $C$, de tal forma que los puntos aparecen sobre la recta en el orden $A, B, C, D$.

2. **Relación entre las longitudes de los segmentos:**
   Los tres segmentos en los que queda dividida la cuerda son $AB$, $BC$ y $CD$. Dado que sus longitudes están en la razón $1 : 2 : 3$, podemos expresar sus medidas en función de una constante $x > 0$:
   $$AB = x, \quad BC = 2x, \quad CD = 3x$$
   La longitud total de la cuerda es:
   $$AD = x + 2x + 3x = 6x$$

3. **Propiedad del punto medio:**
   Sea $M$ la proyección perpendicular del centro $O$ sobre la cuerda $AD$. Sabemos que la perpendicular trazada desde el centro de una circunferencia a una cuerda la biseca, por lo que $M$ es el punto medio de $AD$, es decir:
   $$AM = MD = \frac{6x}{2} = 3x$$
   Observando las distancias desde el extremo $A$ a lo largo de la cuerda, tenemos que:
   $$AC = AB + BC = x + 2x = 3x$$
   Esto implica que los puntos $M$ y $C$ coinciden ($M = C$).

4. **Uso de la circunferencia $\omega$:**
   Como la cuerda $AD$ no es un diámetro de $\Omega$, el centro $O$ no pertenece a la recta $AD$ (por lo que $O \neq C$) y se cumple que $OC \perp AD$. 
   Dado que los puntos $O$, $B$ y $C$ pertenecen todos a la circunferencia $\omega$ y el ángulo inscrito $\angle OCB = 90^\circ$, por el teorema de Tales el segmento $OB$ debe ser un diámetro de $\omega$. Por lo tanto:
   $$OB = 2r = 2(61) = 122$$

5. **Aplicación del teorema de Pitágoras:**
   Sea $h = OC$ la distancia del centro $O$ a la cuerda.
   - En el triángulo rectángulo $\triangle OCB$ (recto en $C$):
     $$h^2 + BC^2 = OB^2 \implies h^2 + (2x)^2 = 122^2 \implies h^2 + 4x^2 = 122^2$$
   - En el triángulo rectángulo $\triangle OCD$ (recto en $C$, donde $OD = R = 123$ es el radio de $\Omega$):
     $$h^2 + CD^2 = OD^2 \implies h^2 + (3x)^2 = 123^2 \implies h^2 + 9x^2 = 123^2$$

6. **Resolución del sistema:**
   Restando la primera ecuación de la segunda:
   $$(h^2 + 9x^2) - (h^2 + 4x^2) = 123^2 - 122^2$$
   $$5x^2 = (123 - 122)(123 + 122)$$
   $$5x^2 = 1 \cdot 245 = 245$$
   $$x^2 = \frac{245}{5} = 49 \implies x = 7$$

Finalmente, la longitud de la cuerda $AD$ es $6x = 6(7) = 42$.

\boxed{42}