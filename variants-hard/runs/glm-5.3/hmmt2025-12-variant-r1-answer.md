## Planteamiento

Ubiquemos las casillas con coordenadas (fila, columna), fila 1 arriba:

- Kelvin (inicio) en $S=(3,1)$: **abajo-izquierda**
- Casa en $H=(1,2)$: **arriba-centro**

Las otras 7 casillas son:
$$A=(1,1),\ B=(1,3),\ C=(2,1),\ D=(2,2),\ E=(2,3),\ F=(3,2),\ G=(3,3)$$

Como $S$ y $H$ deben quedar, quitamos 4 de estas 7 casillas (quedan 3): hay $\binom{7}{3}=35$ configuraciones en total. Contamos las que **desconectan** $S$ de $H$.

**Adyacencias clave:**
- $S$ solo toca a $C$ y $F$
- $H$ solo toca a $A$, $D$ y $B$
- Aristas entre las 7: $A\!-\!C$, $B\!-\!E$, $C\!-\!D$, $D\!-\!E$, $D\!-\!F$, $E\!-\!G$, $F\!-\!G$

## Caso 1: $D$ queda

Entonces hay camino si $C$ o $F$ quedan (vía $S\!-\!C\!-\!D\!-\!H$ o $S\!-\!F\!-\!D\!-\!H$). 

Está **desconectado** solo si se quitan $C$ y $F$ (entonces $S$ queda aislado): las otras 2 casillas que quedan salen de $\{A,B,E,G\}$:
$$\binom{4}{2}=6 \text{ formas}$$

## Caso 2: $D$ se quita

Quedan 3 casillas de $\{A,B,C,E,F,G\}$: $\binom{6}{3}=20$ formas. Los únicos caminos posibles de $S$ a $H$ serían:

- $S\!-\!C\!-\!A\!-\!H$: requiere que queden $A$ y $C$
- $S\!-\!F\!-\!G\!-\!E\!-\!B\!-\!H$: requiere $F,G,E,B$ — 4 casillas, imposible

Así que hay conexión $\iff$ quedan $A$ y $C$ (tercera casilla cualquiera de $\{B,E,F,G}$): $4$ formas conectadas.

**Desconectadas:** $20-4=16$ formas.

## Verificación por enumeración

Las 13 configuraciones **conectadas** son: $\{A,B,C\}$, $\{A,C,E\}$, $\{A,C,F\}$, $\{A,C,G\}$, $\{A,C,D\}$, $\{B,C,D\}$, $\{C,D,E\}$, $\{C,D,F\}$, $\{C,D,G\}$, $\{A,D,F\}$, $\{B,D,F\}$, $\{D,E,F\}$, $\{D,F,G\}$. Las otras $35-13=22$ dejan a Kelvin sin camino a casa.

## Total

$$6+16=22$$

\boxed{22}