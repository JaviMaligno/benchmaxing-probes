Analicemos la función por casos.

**Rama lineal (x < a):** f(x) = ax + 2a. Para que la gráfica pueda cubrir valores arbitrariamente negativos o positivos, necesitamos a ≠ 0 (si a = 0, f es constante 0 y no cruza casi ninguna recta horizontal). Supongamos a > 0 (buscamos el valor más grande). Entonces, cuando x → −∞, f(x) → −∞, y cuando x → a⁻, f(x) → a² + 2a. Esta rama cubre el intervalo (−∞, a² + 2a).

**Rama cuadrática (x ≥ a):** f(x) = ax². Con a > 0, en el dominio x ≥ a > 0 la función es creciente, así que su mínimo es f(a) = a·a² = a³, y cubre el intervalo [a³, ∞).

**Condición de cobertura total:** para que juntas cubran todo ℝ, no debe haber hueco entre las dos ramas:
$$a^3 \leq a^2 + 2a$$

Dividiendo entre a > 0:
$$a^2 \leq a + 2 \quad\Longrightarrow\quad a^2 - a - 2 \leq 0 \quad\Longrightarrow\quad (a-2)(a+1) \leq 0$$

Esto da −1 ≤ a ≤ 2. Como buscamos el mayor valor con a > 0, el máximo es a = 2. Verificación: con a = 2, la rama lineal cubre (−∞, 8) y la cuadrática cubre [8, ∞), exactamente todo ℝ.

$$\boxed{2}$$