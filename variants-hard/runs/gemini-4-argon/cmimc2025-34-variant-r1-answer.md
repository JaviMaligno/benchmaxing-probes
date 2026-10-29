Para hallar el área máxima $a_{\max}$ y el área mínima $a_{\min}$ del hexágono simple (no autointersecante) $PLANET$, observemos primero la disposición geométrica de los seis puntos dados:

Los cuatro puntos
$$V_1 = (0,0), \quad V_2 = (12,0), \quad V_3 = (12,12), \quad V_4 = (0,12)$$
son los vértices de un cuadrado $S$ de lado $12$, cuya área total es:
$$\text{Área}(S) = 12 \times 12 = 144.$$

Los otros dos puntos, que llamaremos $A = (5,4)$ y $B = (8,2)$, se encuentran estrictamente en el interior del cuadrado $S$.

### 1. Estructura topológica del hexágono
Dado que $V_1, V_2, V_3, V_4$ forman la envolvente convexa del conjunto de los 6 vértices, cualquier polígono simple que tenga estos 6 puntos como vértices está contenido en el cuadrado $S$ y debe recorrer los vértices del cuadrado en su mismo orden cíclico $(V_1, V_2, V_3, V_4)$ (o su inverso). De lo contrario, dos caminos interiores conectarían vértices opuestos del cuadrado y se cruzarían necesariamente.

Por tanto, el hexágono se obtiene insertando los puntos interiores $A$ y $B$ en los 4 lados del cuadrado:
$$e_1 = V_1V_2, \quad e_2 = V_2V_3, \quad e_3 = V_3V_4, \quad e_4 = V_4V_1.$$
En cada configuración válida, el área del hexágono es $144$ menos el área de las regiones triangulares o poligonales recortadas del cuadrado.

Calculamos primero las áreas de los triángulos formados por $A(5,4)$ y $B(8,2)$ con cada lado del cuadrado:
- **Con $e_1 = V_1V_2$ (base $12$ sobre $y=0$):**
  $$[V_1V_2A] = \frac{1}{2}(12)(4) = 24, \qquad [V_1V_2B] = \frac{1}{2}(12)(2) = 12.$$
- **Con $e_2 = V_2V_3$ (base $12$ sobre $x=12$):**
  $$[V_2V_3A] = \frac{1}{2}(12)(12-5) = 42, \qquad [V_2V_3B] = \frac{1}{2}(12)(12-8) = 24.$$
- **Con $e_3 = V_3V_4$ (base $12$ sobre $y=12$):**
  $$[V_3V_4A] = \frac{1}{2}(12)(12-4) = 48, \qquad [V_3V_4B] = \frac{1}{2}(12)(12-2) = 60.$$
- **Con $e_4 = V_4V_1$ (base $12$ sobre $x=0$):**
  $$[V_4V_1A] = \frac{1}{2}(12)(5) = 30, \qquad [V_4V_1B] = \frac{1}{2}(12)(8) = 48.$$

También calculamos las áreas de los triángulos formados por $AB$ con cada vértice $V_i$. La recta que pasa por $A(5,4)$ y $B(8,2)$ es $2x + 3y - 22 = 0$, por lo que:
$$[V_iAB] = \frac{|2x_i + 3y_i - 22|}{2},$$
lo que nos da:
$$[V_1AB] = 11, \quad [V_2AB] = 1, \quad [V_3AB] = 19, \quad [V_4AB] = 7.$$

Notemos dos relaciones de contención importantes:
1. $B(8,2)$ está estrictamente en el interior de $\triangle V_1V_2A$, ya que $[V_1V_2B] + [V_1BA] + [V_2AB] = 12 + 11 + 1 = 24 = [V_1V_2A]$.
2. $A(5,4)$ está estrictamente en el interior de $\triangle V_4V_1B$, ya que $[V_4V_1A] + [V_1BA] + [V_4AB] = 30 + 11 + 7 = 48 = [V_4V_1B]$.

---

### 2. Caso 1: $A$ y $B$ se insertan en el mismo lado del cuadrado
Reemplazamos un lado $V_iV_{i+1}$ por la cadena poligonal $V_i - A - B - V_{i+1}$ o $V_i - B - A - V_{i+1}$:

1. **En el lado $e_1 = V_1V_2$:**
   - Orden $V_1 \to A \to B \to V_2$: es $x$-monótono ($0 < 5 < 8 < 12$), por lo que no se autointerseca. El área recortada es $[V_1V_2B] + [V_1BA] = 12 + 11 = 23$.
   - Orden $V_1 \to B \to A \to V_2$: como $B$ está en el interior de $\triangle V_1V_2A$, el segmento $V_1B$ queda estrictamente por debajo de $AV_2$ y no se cruzan. El área recortada es $[V_1V_2B] + [V_2BA] = 12 + 1 = 13$.

2. **En el lado $e_2 = V_2V_3$:**
   - Orden $V_2 \to B \to A \to V_3$: es $y$-monótono ($0 < 2 < 4 < 12$), válido. El área recortada es $[V_2V_3B] + [V_3BA] = 24 + 19 = 43$.
   - Orden $V_2 \to A \to B \to V_3$: los segmentos $V_2A$ y $BV_3$ se cruzan (inválido).

3. **En el lado $e_3 = V_3V_4$:**
   - Orden $V_3 \to B \to A \to V_4$: es $x$-monótono ($12 > 8 > 5 > 0$), válido. El área recortada es $[V_3V_4A] + [V_3BA] = 48 + 19 = 67$.
   - Orden $V_3 \to A \to B \to V_4$: los segmentos $V_3A$ y $BV_4$ son las diagonales del cuadrilátero convexo $V_3BAV_4$ y se cruzan (inválido).

4. **En el lado $e_4 = V_4V_1$:**
   - Orden $V_4 \to A \to B \to V_1$: es $y$-monótono ($12 > 4 > 2 > 0$), válido. El área recortada es $[V_4V_1A] + [V_1AB] = 30 + 11 = 41$.
   - Orden $V_4 \to B \to A \to V_1$: como $A$ está en el interior de $\triangle V_4V_1B$, los segmentos $V_4B$ y $AV_1$ no se cruzan. El área recortada es $[V_4V_1A] + [V_4BA] = 30 + 7 = 37$.

---

### 3. Caso 2: $A$ y $B$ se insertan en lados distintos del cuadrado
Si $A$ se inserta en el lado $e_i$ y $B$ en el lado $e_j$ ($i \neq j$), el hexágono es simple si y solo si los triángulos recortados $\triangle e_iA$ y $\triangle e_jB$ no se solapan (salvo en un vértice común del cuadrado). El área recortada es $[e_iA] + [e_jB]$.

- Como $B \in \text{int}(\triangle V_1V_2A)$, el triángulo $\triangle e_1A$ interseca a $\triangle e_jB$ para todo $j \neq 1$. Así, ningún par $(e_1, e_j)$ es válido.
- Como $A \in \text{int}(\triangle V_4V_1B)$, el triángulo $\triangle e_4B$ interseca a $\triangle e_iA$ para todo $i \neq 4$. Así, ningún par $(e_i, e_4)$ es válido.

Analizamos los 6 pares restantes:
1. $(e_2, e_1)$: en $V_2(12,0)$, la pendiente de $V_2A$ es $-4/7$ y la de $V_2B$ es $-1/2$, por lo que los triángulos no se solapan. Área recortada: $42 + 12 = 54$.
2. $(e_2, e_3)$: en $V_3(12,12)$, la pendiente de $V_3A$ es $8/7$ y la de $V_3B$ es $5/2 > 8/7$, por lo que los rayos se cruzan y los triángulos se solapan (inválido).
3. $(e_3, e_2)$: por el mismo cálculo de pendientes en $V_3$, los triángulos están separados. Área recortada: $48 + 24 = 72$.
4. $(e_3, e_1)$: en $\triangle V_3V_4A$ se cumple $y \ge 4$ y en $\triangle V_1V_2B$ se cumple $y \le 2$; son disjuntos. Área recortada: $48 + 12 = 60$.
5. $(e_4, e_1)$: en $V_1(0,0)$, la pendiente de $V_1A$ es $4/5$ y la de $V_1B$ es $1/4 < 4/5$; no se solapan. Área recortada: $30 + 12 = 42$.
6. $(e_4, e_2)$: en $\triangle V_4V_1A$ se cumple $x \le 5$ y en $\triangle V_2V_3B$ se cumple $x \ge 8$; son disjuntos. Área recortada: $30 + 24 = 54$.
7. $(e_4, e_3)$: en $V_4(0,12)$, todo punto de $\triangle V_4V_1A$ (salvo $V_4$) cumple $\frac{x}{12-y} \le \frac{5}{8} = 0.625$, mientras que todo punto de $\triangle V_3V_4B$ (salvo $V_4$) cumple $\frac{x}{12-y} \ge \frac{8}{10} = 0.8$. Por tanto, los dos triángulos sólo comparten el vértice $V_4$ y no se solapan. Área recortada: $30 + 60 = 90$.

---

### 4. Conclusión
- La **menor área recortada** es $13$ (con el hexágono $V_1 B A V_2 V_3 V_4$), lo que produce el área máxima:
  $$a_{\max} = 144 - 13 = 131.$$
- La **mayor área recortada** es $90$ (con el hexágono $V_1 V_2 V_3 B V_4 A$), lo que produce el área mínima:
  $$a_{\min} = 144 - 90 = 54.$$

Por lo tanto, la diferencia buscada es:
$$a_{\max} - a_{\min} = 131 - 54 = 77.$$

\boxed{77}