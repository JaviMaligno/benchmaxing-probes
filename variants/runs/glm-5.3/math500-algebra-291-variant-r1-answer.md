## Razonamiento paso a paso

**Probabilidades en cada turno:**
- Turno de Carla: gana con probabilidad $2/6 = \frac{1}{3}$ (saca 5 o 6); con probabilidad $\frac{2}{3}$ el turno pasa a Dev.
- Turno de Dev: gana con probabilidad $2/6 = \frac{1}{3}$ (saca 1 o 2); con probabilidad $\frac{2}{3}$ el turno vuelve a Carla.

**Planteamiento por recursión:**

Sea $p$ la probabilidad de que Carla gane cuando comienza su turno. El juego se reinicia en cada turno de Carla, así que $p$ es la probabilidad total de que Carla gane.

Carla gana si:
1. Gana en su turno actual (probabilidad $\frac{1}{3}$), **o**
2. No gana ($\frac{2}{3}$), Dev tampoco gana ($\frac{2}{3}$), y luego Carla gana desde el nuevo turno (probabilidad $p$).

Esto da la ecuación:
$$p = \frac{1}{3} + \frac{2}{3}\cdot\frac{2}{3}\cdot p = \frac{1}{3} + \frac{4}{9}p$$

**Resolución:**
$$p - \frac{4}{9}p = \frac{1}{3} \quad\Longrightarrow\quad \frac{5}{9}p = \frac{1}{3} \quad\Longrightarrow\quad p = \frac{3}{5}$$

**Verificación:** La probabilidad de que Dev gane es $\frac{2}{3}\cdot\frac{1}{3}\cdot\frac{1}{1-\frac{4}{9}} = \frac{2}{9}\cdot\frac{9}{5} = \frac{2}{5}$, y en efecto $\frac{3}{5}+\frac{2}{5}=1$. ✓

$$\boxed{\dfrac{3}{5}}$$