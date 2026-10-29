Para encontrar el valor esperado de $N$, el número de veces que debemos eliminar cartas, analicemos primero cuándo ocurre exactamente una eliminación al escanear la baraja de izquierda a derecha.

### 1. Condición para que ocurra una eliminación
Sea $c_1, c_2, \dots, c_{12}$ la secuencia de los valores de las $12$ cartas (donde hay cuatro $2$, cuatro $3$ y cuatro $4$). 

Cuando encontramos un doble en la posición $i$ (es decir, $c_i = c_{i-1}$ y la carta $c_{i-1}$ no ha sido eliminada previamente), eliminamos todas las cartas hasta la posición $i$ inclusive. Esto implica que el proceso de búsqueda de dobles se reinicia desde cero a partir de la carta $c_{i+1}$, por lo que las cartas anteriores al doble nunca pueden volverse adyacentes a las cartas posteriores al doble.

En consecuencia, las eliminaciones ocurren únicamente dentro de los bloques maximales de cartas consecutivas del mismo valor:
- Un bloque de $L=1$ carta de un mismo valor produce $\lfloor 1/2 \rfloor = 0$ eliminaciones.
- Un bloque de $L=2$ cartas iguales consecutivas produce $\lfloor 2/2 \rfloor = 1$ eliminación (las dos forman un doble y se eliminan).
- Un bloque de $L=3$ cartas iguales consecutivas produce $\lfloor 3/2 \rfloor = 1$ eliminación (las dos primeras se eliminan y la tercera queda sola).
- Un bloque de $L=4$ cartas iguales consecutivas produce $\lfloor 4/2 \rfloor = 2$ eliminaciones (las dos primeras se eliminan, y luego la tercera y cuarta forman otro doble y se eliminan).

En general, un bloque maximal de longitud $L$ de cartas con el mismo valor genera exactamente $\lfloor L/2 \rfloor$ eliminaciones.

---

### 2. Cálculo mediante linealidad de la esperanza (Inclusión-Exclusión)
Una eliminación ocurre en la posición $i$ si y solo si $c_i = c_{i-1}$ y **no** hubo una eliminación en la posición $i-1$. 
Sea $I_i$ la variable indicadora de que ocurre una eliminación en la posición $i$ (para $2 \le i \le 12$). Como hay a lo sumo $4$ cartas de cada valor, tenemos la relación exacta:
$$I_i = \mathbb{I}(c_i = c_{i-1}) - \mathbb{I}(c_i = c_{i-1} = c_{i-2}) + \mathbb{I}(c_i = c_{i-1} = c_{i-2} = c_{i-3})$$

Calculamos la esperanza de cada término sumando sobre todas las posiciones posibles:

1. **Pares adyacentes iguales:** Hay $11$ pares de posiciones adyacentes $(i-1, i)$. Para cualquier carta en la posición $i-1$, quedan $11$ cartas en la baraja, de las cuales $3$ tienen su mismo valor.
   $$\mathbb{E}[\text{pares}] = 11 \times \frac{3}{11} = 3$$

2. **Triples consecutivos iguales:** Hay $10$ triples de posiciones consecutivas $(i-2, i-1, i)$. La probabilidad de que tres cartas consecutivas tengan el mismo valor es $\frac{3}{11} \times \frac{2}{10} = \frac{3}{55}$.
   $$\mathbb{E}[\text{triples}] = 10 \times \frac{3}{55} = \frac{6}{11}$$

3. **Cuádruples consecutivos iguales:** Hay $9$ cuádruples de posiciones consecutivas $(i-3, i-2, i-1, i)$. La probabilidad de que cuatro cartas consecutivas tengan el mismo valor es $\frac{3}{11} \times \frac{2}{10} \times \frac{1}{9} = \frac{1}{165}$.
   $$\mathbb{E}[\text{cuádruples}] = 9 \times \frac{1}{165} = \frac{3}{55}$$

---

### 3. Resultado final
Por linealidad de la esperanza, el valor esperado de $N$ es:
$$\mathbb{E}[N] = \mathbb{E}[\text{pares}] - \mathbb{E}[\text{triples}] + \mathbb{E}[\text{cuádruples}] = 3 - \frac{6}{11} + \frac{3}{55} = \frac{165 - 30 + 3}{55} = \frac{138}{55}$$

\boxed{\frac{138}{55}}