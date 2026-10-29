## Planteamiento

Numero las columnas $1,2,3,\dots$; cada una tiene 2 celdas. Philip empieza en la celda superior de la columna 1. Proceso las columnas de izquierda a derecha siguiendo el estado de conectividad de la columna $i$ (usando solo columnas $1..i$):

- **S2**: ambas celdas de la columna $i$ están en la componente de Philip (tamaño $s$).
- **S1**: una celda está en su componente (tamaño $s$); la otra pertenece a otra componente $O$ (tamaño $o$), que aún puede fusionarse más adelante dando la vuelta por la derecha.
- **S0**: muerto (su componente no llega a la columna $i$): ya nada más es alcanzable.

**Inicio** ($i=1$): con prob. $1/2$ S2 con $s=2$; con prob. $1/2$ S1 con $s=1,o=1$.

**Transiciones** (puertas $h_t,h_b,v$, cada una abierta con prob. $1/2$, 8 casos):

- Desde **S2**: $4/8\to$ S2 con $s+2$; $2/8\to$ S1 con $s+1,o=1$; $2/8\to$ muerto.
- Desde **S1**: $1/8\to$ S2 con $s+o+2$ (fusión); $1/8\to$ S2 con $s+2$; $1/8\to$ S1 con $s+1,o+1$; $1/8\to$ S1 con $s+1,o=1$; $4/8\to$ muerto.

## Resolución

Con $p_k(i)$ las probabilidades y $a_2=E[s\mathbf 1_{S2}]$, $a_1=E[s\mathbf 1_{S1}]$, $b_1=E[o\mathbf 1_{S1}]$, sumando las recurrencias sobre todo $i\ge 1$ ($P_k=\sum p_k$, etc.):

$$P_2=\tfrac85,\qquad P_1=\tfrac65,\qquad B_1=\tfrac{48}{35}$$

y del sistema
$$3A_1-A_2=\tfrac{24}{5},\qquad 2A_2-A_1=\tfrac{472}{35}$$
se obtiene $A_1=\dfrac{808}{175}$, $A_2=\dfrac{1584}{175}$.

El tamaño final esperado es lo acumulado al morir:
$$E=\tfrac14 A_2+\tfrac12 A_1=\frac{396}{175}+\frac{404}{175}=\frac{800}{175}=\frac{32}{7}$$

(Verificación numérica iterando la recurrencia: $1.5,\;2.5625,\;3.2578,\;3.7119,\;4.0089,\dots\to 4.5714$.)

\boxed{\dfrac{32}{7}}