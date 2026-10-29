## Resolución

**Paso 1: Coordenadas.** Sea $A$ el origen, con $\overline{AB}$ sobre el eje $x$ y $\vec u, \vec v$ vectores unitarios a lo largo de $AB$ y $AC$, con ángulo $\theta$ entre ellos ($s = \sin\theta$):

- $D = 4\vec u,\quad E = 20\vec u,\quad B = 28\vec u$
- $F = 13\vec v,\quad G = 65\vec v,\quad C = 91\vec v$
- $M = 2F - D = 26\vec v - 4\vec u$ (reflexión de $D$ por $F$)
- $N = 2E - G = 40\vec u - 65\vec v$ (reflexión de $G$ por $E$)

**Paso 2: Usar el área de $DEGF$.** Con la fórmula del cordón (shoelace) en $D, E, G, F$:

$$[DEGF] = \tfrac12\big(20\cdot 65s + 0 - 4\cdot 13s\big) = 624s = 288 \implies s = \frac{6}{13}$$

**Paso 3: Descomponer el heptágono.** El heptágono $AFNBCEM$ se divide en tres piezas que comparten solo aristas (como en la figura): $\triangle AFM$, cuadrilátero $NEMF$ y cuadrilátero $NECB$.

- $\triangle AFM$: el término del cordón es $13c\cdot 26s - (26c-4)\cdot 13s = 52s$, así que $[AFM] = 26s$.
- $NEMF$: calculando término a término se obtiene $[NEMF] = 624s = 288$ (es un "gemelo" de $DEGF$, pues $E$ y $F$ son puntos medios de $GN$ y $DM$).
- $NECB$: análogamente, $[NECB] = 624s = 288$.

**Paso 4: Sumar.**

$$[AFNBCEM] = 26s + 624s + 624s = 1274s = 1274\cdot\frac{6}{13} = 588$$

(Verificación: el cordón directo sobre los siete vértices $A,F,N,B,C,E,M$ da $\tfrac12\cdot 2548s = 1274s$, coincidiendo.)

$$\boxed{588}$$