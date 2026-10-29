## Planteamiento

Modela el total acumulado de camarones como una caminata que empieza en $0$ y cada día avanza $+1$ o $+2$, cada uno con probabilidad $\tfrac12$.

Como los pasos son de 1 o 2, el **primer** día en que el total alcanza $\ge 10$, el total es exactamente $10$ o exactamente $11$:

- Si llega a $10$: la piel se rosiza y **no** se enferma ese día.
- Si llega a $11$ (solo posible viniendo de $9$ con un paso de $2$): se enferma ese mismo día.

Buscamos $P(\text{primera llegada a } \ge 10 \text{ es exactamente } 10)$.

## Recursión

Define $p_k$ = probabilidad de que, partiendo de un total $k$ (con $k<10$), la primera llegada al nivel $\ge 10$ aterrice exactamente en $10$.

Condiciones de frontera: $p_{10} = 1$, $p_{11} = 0$. Para $k \le 9$:

$$p_k = \tfrac12 p_{k+1} + \tfrac12 p_{k+2}$$

## Cálculo hacia atrás

$$p_9 = \tfrac12(p_{10}+p_{11}) = \tfrac12 \qquad p_8 = \tfrac12\left(\tfrac12+1\right)=\tfrac34 \qquad p_7 = \tfrac12\left(\tfrac34+\tfrac12\right)=\tfrac58$$

$$p_6 = \tfrac{11}{16} \qquad p_5 = \tfrac{21}{32} \qquad p_4 = \tfrac{43}{64} \qquad p_3 = \tfrac{85}{128}$$

$$p_2 = \tfrac{171}{256} \qquad p_1 = \tfrac{341}{512}$$

$$p_0 = \tfrac12\left(\tfrac{341}{512} + \tfrac{171}{256}\right) = \tfrac12 \cdot \tfrac{683}{512} = \tfrac{683}{1024}$$

## Verificación (vía complementaria)

La caminata enferma ese día solo si toca el estado $9$ y luego da un paso de $2$. La probabilidad de tocar $9$ es $q_9 = \tfrac{341}{512}$ (misma recurrencia $q_n = \tfrac{q_{n-1}+q_{n-2}}{2}$), así que $P(\text{enfermo}) = \tfrac{341}{1024}$ y el complemento es $1 - \tfrac{341}{1024} = \tfrac{683}{1024}$. ✓ Coincide.

$$\boxed{\dfrac{683}{1024}}$$