# Solución paso a paso

**Planteamiento.** Sea $C$ la probabilidad de que Carla gane cuando es su turno, y $D$ la probabilidad de que Carla gane cuando es el turno de Dev.

**Turno de Carla:**
- Gana inmediatamente con probabilidad $\tfrac{2}{6} = \tfrac{1}{3}$ (saca 5 o 6).
- Con probabilidad $\tfrac{2}{3}$ el turno pasa a Dev, y entonces Carla gana con probabilidad $D$.

$$C = \frac{1}{3} + \frac{2}{3}D$$

**Turno de Dev:**
- Dev gana (Carla pierde) con probabilidad $\tfrac{2}{6} = \tfrac{1}{3}$ (saca 1 o 2).
- Con probabilidad $\tfrac{2}{3}$ el turno vuelve a Carla, y Carla gana con probabilidad $C$.

$$D = 0 \cdot \frac{1}{3} + \frac{2}{3}C = \frac{2}{3}C$$

**Resolviendo el sistema:**

$$C = \frac{1}{3} + \frac{2}{3} \cdot \frac{2}{3}C = \frac{1}{3} + \frac{4}{9}C$$

$$C - \frac{4}{9}C = \frac{1}{3} \quad\Longrightarrow\quad \frac{5}{9}C = \frac{1}{3} \quad\Longrightarrow\quad C = \frac{3}{5}$$

**Verificación.** La probabilidad de que gane Dev es $D_{\text{dev}} = \tfrac{2}{3}\left(\tfrac{1}{3} + \tfrac{2}{3}D_{\text{dev}}\right)$, que da $D_{\text{dev}} = \tfrac{2}{5}$. En efecto, $\tfrac{3}{5} + \tfrac{2}{5} = 1$. ✓

$$\boxed{\dfrac{3}{5}}$$