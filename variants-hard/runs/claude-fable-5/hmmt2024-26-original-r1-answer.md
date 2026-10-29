## Solución

**Paso 1: Potencia del punto A.**
Como $A$, $B'$, $B$ son colineales, la potencia de $A$ respecto a la circunferencia de diámetro $BB'$ es $AB' \cdot AB$; análogamente, respecto a la de diámetro $CC'$ es $AC' \cdot AC$. Por la potencia de $A$ respecto a $\omega$, ambas cantidades son iguales ($AB' \cdot AB = AC' \cdot AC$), así que $A$ está sobre el eje radical de las dos circunferencias pequeñas. Como estas son tangentes en $T$, el eje radical es la tangente común en $T$, y por tanto:

$$AT^2 = AB' \cdot AB = AC' \cdot AC = 144.$$

De aquí $AB' = 144/18 = 8$ y $AC' = 144/36 = 4$.

**Paso 2: Condición de tangencia externa.**
Los radios son $r_1 = \tfrac{BB'}{2} = \tfrac{18-8}{2} = 5$ y $r_2 = \tfrac{CC'}{2} = \tfrac{36-4}{2} = 16$. Los centros son los puntos medios $M_B$ (a distancia $\tfrac{8+18}{2}=13$ de $A$ sobre $AB$) y $M_C$ (a distancia $\tfrac{4+36}{2}=20$ de $A$ sobre $AC$). La tangencia externa da $M_BM_C = 5+16 = 21$, y por ley de cosenos en el ángulo $A$:

$$441 = 13^2 + 20^2 - 2\cdot 13 \cdot 20 \cos A \;\Rightarrow\; \cos A = \frac{128}{520} = \frac{16}{65}, \quad \sin A = \frac{63}{65}.$$

**Paso 3: Coordenadas y centro $O$.**
Con $A=(0,0)$, $B=(18,0)$, $B'=(8,0)$, $C = \left(\tfrac{576}{65}, \tfrac{2268}{65}\right)$, $C' = \left(\tfrac{64}{65}, \tfrac{252}{65}\right)$.

- La mediatriz de $BB'$ da $x_O = 13$.
- La mediatriz de $CC'$ pasa por $\left(\tfrac{64}{13}, \tfrac{252}{13}\right)$ con dirección perpendicular a $(16,63)$. Imponiendo $x=13$ se obtiene $y_O = \tfrac{52}{3}$.

Entonces:

$$AO^2 = 13^2 + \left(\frac{52}{3}\right)^2 = \frac{1521 + 2704}{9} = \frac{4225}{9}.$$

**Verificación:** $OB^2 = 25 + \tfrac{2704}{9} = \tfrac{2929}{9} = R^2$, y en efecto $AO^2 - R^2 = \tfrac{4225-2929}{9} = 144 = AT^2$. ✓

$$\boxed{AO = \dfrac{65}{3}}$$