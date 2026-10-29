Kevin empieza en la esquina inferior izquierda y su casa está en la esquina superior derecha de una cuadrícula $3\times 3$. Voy a etiquetar las casillas así:

$$\begin{matrix} A & B & C \\ D & E & F \\ G & H & I \end{matrix}$$

donde $G$ es la esquina inferior izquierda (inicio) y $C$ es la esquina superior derecha (casa). Las adyacencias relevantes son: $G$ conecta con $D,H$; $C$ conecta con $B,F$; $E$ (centro) conecta con $B,D,F,H$.

**Conteo total.** Hay 9 nenúfares, y debemos quitar 4 manteniendo $G$ y $C$. Es decir, elegimos qué 3 de los otros 7 nenúfares $\{A,B,D,E,F,H,I\}$ permanecen. El número total de configuraciones es
$$\binom{7}{3} = 35.$$

Ahora cuento en cuántas de esas configuraciones Kevin **sí** puede llegar a casa, y resto.

**Caso 1: $E$ permanece.** Elegimos 2 más de $\{A,B,D,F,H,I\}$. Para conectar $G$ con $C$ pasando por $E$, necesito uno de $\{D,H\}$ (para unir $G$ con $E$) y uno de $\{B,F\}$ (para unir $E$ con $C$). Esto da $2\cdot 2 = 4$ configuraciones:
$$\{E,D,B\},\ \{E,D,F\},\ \{E,H,B\},\ \{E,H,F\}.$$
Cualquier otra pareja deja a $G$ o a $C$ aislado (verificado: sin $D$ ni $H$, $G$ queda aislado; sin $B$ ni $F$, $C$ queda aislado). Así que este caso aporta 4 caminos.

**Caso 2: $E$ no permanece.** Elegimos 3 de $\{A,B,D,F,H,I\}$. Sin el centro, los 8 nenúfares restantes forman un único ciclo de longitud 8 alrededor del borde:
$$G\text{-}D\text{-}A\text{-}B\text{-}C\text{-}F\text{-}I\text{-}H\text{-}G.$$
Como $G$ y $C$ son opuestos en el ciclo, un camino de $G$ a $C$ requiere conservar uno de los dos arcos completos, cada uno con exactamente 3 casillas intermedias:
- Arco 1: $\{D,A,B\}$, camino $G\text{-}D\text{-}A\text{-}B\text{-}C$.
- Arco 2: $\{H,I,F\}$, camino $G\text{-}H\text{-}I\text{-}F\text{-}C$.

Como solo conservamos 3 nenúfares, no se puede completar más de un arco, así que este caso aporta 2 caminos.

**Total con camino:** $4 + 2 = 6$.

**Configuraciones donde Kevin NO puede llegar a casa:**
$$35 - 6 = 29.$$

$$\boxed{29}$$