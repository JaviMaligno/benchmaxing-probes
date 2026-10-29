## Solución

Etiqueto las posiciones como coordenadas $(x,y)$ con $(0,0)$ abajo a la izquierda. Kelvin está en $A=(0,0)$ y su casa es $H=(1,2)$ (centro de la fila superior). Hay que quitar 4 de los 7 nenúfares restantes: en total $\binom{7}{4}=35$ formas, equivalente a elegir qué **3 nenúfares intermedios se conservan**.

**Paridad clave.** Coloreando por paridad de $x+y$, $A$ tiene paridad 0 y $H$ tiene paridad 1, así que todo camino entre ellos tiene longitud impar: 3, 5, 7, … Un camino de longitud 3 usa 2 intermedios; uno de longitud 5 usaría 4 intermedios distintos, pero solo quedan 3. Por tanto, **Kelvin llega a casa si y solo si sobrevive algún camino de longitud 3**.

**Caminos de longitud 3.** El desplazamiento neto es $(+1,+2)$ en 3 pasos, así que los pasos son exactamente una R y dos U en algún orden:

- R, U, U: intermedios $\{(1,0),(1,1)\}$
- U, R, U: intermedios $\{(0,1),(1,1)\}$
- U, U, R: intermedios $\{(0,1),(0,2)\}$

**Conteo por inclusión-exclusión** de los conjuntos de 3 celdas conservadas que contienen alguno de esos pares:

- Cada par fijo deja libre 1 celda de las 5 restantes: $3 \times 5 = 15$.
- Pares de pares: $\{(1,0),(1,1)\} \cup \{(0,1),(1,1)\}$ tiene 3 celdas (1 conjunto); $\{(0,1),(1,1)\} \cup \{(0,1),(0,2)\}$ tiene 3 celdas (1 conjunto); la otra unión tiene 4 celdas (0 conjuntos). Resto $2$.
- Intersección triple: 4 celdas, imposible con 3 conservadas: $0$.

Conjuntos conectados: $15 - 2 + 0 = 13$.

Conjuntos donde Kelvin **no** puede llegar: $35 - 13 = 22$.

$$\boxed{22}$$