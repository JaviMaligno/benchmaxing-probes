# Solución paso a paso

**Planteamiento del juego:**
- Turno de Alice: gana si saca **cara** (probabilidad 1/2); si saca cruz, pasa a Bob.
- Turno de Bob: gana si saca **cruz** (probabilidad 1/2); si saca cara, vuelve a Alice.

**Definimos** $P$ = probabilidad de que Alice gane cuando es su turno.

**Ecuación de recursión:**

$$P = \underbrace{\frac{1}{2}}_{\text{Alice saca cara y gana}} \cdot 1 + \frac{1}{2} \cdot \left[ \underbrace{\frac{1}{2} \cdot 0}_{\text{Bob saca cruz y gana}} + \underbrace{\frac{1}{2} \cdot P}_{\text{Bob saca cara, vuelve a Alice}} \right]$$

**Resolviendo:**

$$P = \frac{1}{2} + \frac{1}{4}P \quad\Rightarrow\quad \frac{3}{4}P = \frac{1}{2} \quad\Rightarrow\quad P = \frac{2}{3}$$

**Verificación por suma de series:** Alice gana en su k-ésima tirada con probabilidad $\left(\frac{1}{2}\cdot\frac{1}{2}\right)^{k-1} \cdot \frac{1}{2} = \left(\frac{1}{4}\right)^{k-1}\cdot\frac{1}{2}$:

$$\sum_{k=1}^{\infty} \frac{1}{2}\left(\frac{1}{4}\right)^{k-1} = \frac{1}{2} \cdot \frac{1}{1-\frac{1}{4}} = \frac{1}{2}\cdot\frac{4}{3} = \frac{2}{3} \checkmark$$

\boxed{\dfrac{2}{3}}