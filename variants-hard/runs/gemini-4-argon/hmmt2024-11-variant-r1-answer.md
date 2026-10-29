Para hallar el número de formas de particionar un rectángulo de $20 \times 28$ en rectángulos de $4 \times 5$, ubiquemos el rectángulo grande en el plano cartesiano como la región $[0, 28] \times [0, 20]$, de modo que su ancho sea $28$ y su altura sea $20$. Cada pieza de $4 \times 5$ puede colocarse en dos orientaciones:
- **Horizontal** ($5 \times 4$): ancho $5$ y altura $4$.
- **Vertical** ($4 \times 5$): ancho $4$ y altura $5$.

### Paso 1: Análisis de las secciones verticales
Consideremos cualquier línea vertical $x = k + 0.5$ (para $k \in \{0, 1, \dots, 27\}$), que atraviesa el interior de la primera hasta la última fila de piezas. Las alturas de las piezas que intersectan esta línea vertical deben sumar $20$. Si la línea atraviesa $c$ piezas de altura $4$ y $d$ piezas de altura $5$, entonces:
$$4c + 5d = 20$$
Buscamos las soluciones en enteros no negativos $(c, d)$:
- Si $d = 0$, entonces $4c = 20 \implies c = 5$.
- Si $d = 4$, entonces $4c = 0 \implies c = 0$.

Como no existen otras soluciones enteras no negativas, ninguna línea vertical puede atravesar simultáneamente piezas de altura $4$ y piezas de altura $5$.

### Paso 2: Descomposición en franjas verticales
Observemos el borde izquierdo del rectángulo en $x = 0$:
1. Si la columna unitaria $[0, 1] \times [0, 20]$ está cubierta por $5$ piezas de altura $4$ ($c=5, d=0$), cada una de esas $5$ piezas tiene necesariamente ancho $5$. Como todas comienzan en $x = 0$, todas terminan exactamente en la línea vertical $x = 5$, formando una franja vertical completa de dimensiones $5 \times 20$.
2. Si la columna unitaria $[0, 1] \times [0, 20]$ está cubierta por $4$ piezas de altura $5$ ($c=0, d=4$), cada una de esas $4$ piezas tiene necesariamente ancho $4$. Como todas comienzan en $x = 0$, todas terminan exactamente en la línea vertical $x = 4$, formando una franja vertical completa de dimensiones $4 \times 20$.

Por inducción sobre el ancho restante, cualquier partición del rectángulo de $28 \times 20$ se descompone de manera única en una sucesión de franjas verticales de ancho $4$ (cada una dividida en $4$ rectángulos de $4 \times 5$) y franjas verticales de ancho $5$ (cada una dividida en $5$ rectángulos de $5 \times 4$).

### Paso 3: Conteo de configuraciones
El número de particiones equivale al número de formas de escribir $28$ como una suma ordenada de sumandos iguales a $4$ y $5$. Si usamos $a$ franjas de ancho $4$ y $b$ franjas de ancho $5$, debemos resolver:
$$4a + 5b = 28 \quad (a, b \in \mathbb{Z}_{\ge 0})$$
Analizando módulo $4$, tenemos $5b \equiv 0 \pmod 4 \implies b \equiv 0 \pmod 4$. Como $5b \le 28$, los posibles valores para $b$ son:
- **$b = 0$**: $4a = 28 \implies a = 7$. Esto corresponde a $7$ franjas de ancho $4$, lo cual da:
  $$\binom{7 + 0}{0} = 1 \text{ forma.}$$
- **$b = 4$**: $4a + 20 = 28 \implies 4a = 8 \implies a = 2$. Esto corresponde a ordenar $2$ franjas de ancho $4$ y $4$ franjas de ancho $5$, lo cual da:
  $$\binom{2 + 4}{2} = \binom{6}{2} = \frac{6 \times 5}{2} = 15 \text{ formas.}$$

Sumando ambos casos, obtenemos un total de $1 + 15 = 16$ particiones posibles.

\boxed{16}