## Paso 1: Fracciones a lo largo de los lados

- $PQ = 3+9+6 = 18$, así que $D = \tfrac16 Q$ y $E = \tfrac23 Q$ (como vectores desde $P$).
- $PR = 5+15+10 = 30$, así que $F = \tfrac16 R$ y $G = \tfrac23 R$.

Las fracciones coinciden en ambos lados: $D,F$ al $\tfrac16$; $E,G$ al $\tfrac23$.

## Paso 2: El cuadrilátero $DEGF$

Como $D$ y $F$ están a la misma fracción, $DF \parallel QR$; igualmente $EG \parallel QR$. Entonces $DEGF$ es la "franja" de $\triangle PQR$ comprendida entre las rectas paralelas a $QR$ que cortan a los lados en las fracciones $\tfrac16$ y $\tfrac23$. Por semejanza (el triángulo próximo a $P$ recortado a fracción $t$ es semejante a $PQR$ con razón $t^2$):

$$[DEGF] = [PQR]\left(\left(\tfrac23\right)^2 - \left(\tfrac16\right)^2\right) = [PQR]\left(\tfrac49 - \tfrac1{36}\right) = \tfrac{5}{12}[PQR].$$

Por lo tanto $[PQR] = \tfrac{12}{5}\cdot 300 = 720$.

## Paso 3: El heptágono $PFNQREM$

Con $P$ como origen, sea $[q,r] = 2[PQR]$. Entonces:
- $F = \tfrac r6$, $Q = q$, $R = r$, $E = \tfrac{2q}3$,
- $M = 2F - D = \tfrac r3 - \tfrac q6$,
- $N = 2E - G = \tfrac{4q}3 - \tfrac{2r}3$.

El área del heptágono es $\tfrac12$ de la suma de productos cruzados de vértices consecutivos:

$$\sigma = [P,F] + [F,N] + [N,Q] + [Q,R] + [R,E] + [E,M] + [M,P].$$

Calculemos los términos de "excursión":
- $[F,N] + [E,M] = \left[\tfrac r6, \tfrac{4q}3 - \tfrac{2r}3\right] + \left[\tfrac{2q}3, \tfrac r3 - \tfrac q6\right] = -\tfrac29[q,r] + \tfrac29[q,r] = 0,$
- $[N,Q] + [R,E] = \left[\tfrac{4q}3 - \tfrac{2r}3,\, q\right] + \left[r,\, \tfrac{2q}3\right] = \tfrac23[q,r] - \tfrac23[q,r] = 0.$

Los términos se cancelan **por parejas**, de modo que $\sigma = [Q,R] = [q,r]$, y (verificando en un modelo afín normalizado, p. ej. un triángulo rectángulo, que el heptágono es simple):

$$[PFNQREM] = \tfrac12[q,r] = [PQR] = 720.$$

## Nota

Los datos métricos están sobredeterminados: $[PQR] = \tfrac12\cdot 18\cdot 30\cdot\sin\angle P = 720$ obliga a $\sin\angle P = \tfrac83 > 1$, o sea, la longitud dada $300$ excede el máximo posible ($112{.}5\,s$) para esas longitudes laterales. Esto es irrelevante para la respuesta: toda la configuración (puntos a fracciones fijas, reflecciones puntuales —que preservan puntos medios— y razones de áreas) es de naturaleza afín, así que la razón $[PFNQREM]/[DEGF] = 12/5$ queda fijada.

$$[PFNQREM] = \frac{12}{5}\cdot 300$$

\boxed{720}