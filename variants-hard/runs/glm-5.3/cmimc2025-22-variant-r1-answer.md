# Planteamiento

**Paso 1: Ubicar las ocho bolas.**

Con arista $6$ y radio $\tfrac{3}{2}$, la configuración natural es colocar cada bola en una esquina del cubo, con su centro a distancia $\tfrac{3}{2}$ de las tres caras que se encuentran en esa esquina. Los centros son entonces los vértices de un cubo de arista $6 - 2\cdot\tfrac{3}{2} = 3$:

$$\left(\tfrac{3}{2},\,\tfrac{3}{2},\,\tfrac{3}{2}\right),\quad \left(\tfrac{9}{2},\,\tfrac{3}{2},\,\tfrac{3}{2}\right),\quad \dots\quad \left(\tfrac{9}{2},\,\tfrac{9}{2},\,\tfrac{9}{2}\right).$$

**Paso 2: Verificar la tangencia.**

Dos centros de bolas en esquinas que comparten una arista del cubo distan $3$ en una coordenada y coinciden en las otras dos, es decir, distan $3 = 2\cdot\tfrac{3}{2}$: las bolas son tangentes. Cada bola es tangente exactamente a las **tres** bolas de las esquinas adyacentes por cara (las diagonales del cubo miden $3\sqrt{3} > 3$, así que no hay contacto adicional). Esto satisface la condición del enunciado.

**Paso 3: Condición sobre la bola central.**

Sea $r$ el radio buscado y $P$ el centro de la bola grande. Para ser tangente exteriormente a las ocho bolas, $P$ debe cumplir:

$$|P - C_i| = r + \tfrac{3}{2} \quad \text{para los ocho centros } C_i.$$

Es decir, $P$ debe equidistar de los **ocho vértices de un cubo** (el cubo de centros, de arista $3$). El único punto equidistante de los ocho vértices de un cubo es su **centro**:

$$P = (3,\,3,\,3).$$

**Paso 4: Calcular el radio.**

La distancia de $P$ al centro más cercano (por ejemplo $\left(\tfrac{3}{2},\tfrac{3}{2},\tfrac{3}{2}\right)$) es:

$$\sqrt{3\left(\tfrac{3}{2}\right)^2} = \tfrac{3\sqrt{3}}{2}.$$

Por la tangencia:

$$r + \tfrac{3}{2} = \tfrac{3\sqrt{3}}{2} \implies r = \tfrac{3}{2}\left(\sqrt{3} - 1\right).$$

**Paso 5: Verificar que cabe en el cubo.**

El centro $(3,3,3)$ está a distancia $3$ de cada cara, y

$$r = \tfrac{3}{2}(\sqrt{3}-1) \approx 1.098 < 3,$$

así que la bola queda completamente dentro del cubo. Además, el radio quedó unívocamente determinado, por lo que esta es la única (y por tanto la mayor) bola posible.

# Respuesta

$$\boxed{\dfrac{3\left(\sqrt{3}-1\right)}{2}}$$