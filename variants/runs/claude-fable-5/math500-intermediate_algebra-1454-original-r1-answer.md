## Solución

Reescribo el tercer término completando cuadrados:
$$x^2 + y^2 - 80x - 100y + 4100 = (x-40)^2 + (y-50)^2.$$

Entonces la expresión es
$$\sqrt{x^2 + 20^2} + \sqrt{y^2 + 30^2} + \sqrt{(40-x)^2 + (50-y)^2}.$$

Interpreto cada término como la norma de un vector y aplico la desigualdad de Minkowski (desigualdad triangular para sumas de vectores), eligiendo los vectores
$$\vec{u} = (x,\, 20), \qquad \vec{v} = (30,\, y), \qquad \vec{w} = (40-x,\, 50-y).$$

Nótese que $|\vec{v}| = \sqrt{30^2 + y^2} = \sqrt{y^2+900}$, igual que el segundo término. La suma de los vectores es
$$\vec{u}+\vec{v}+\vec{w} = (x + 30 + 40 - x,\; 20 + y + 50 - y) = (70,\, 70),$$

que es **constante**. Por Minkowski:
$$|\vec{u}| + |\vec{v}| + |\vec{w}| \ge |\vec{u}+\vec{v}+\vec{w}| = \sqrt{70^2+70^2} = 70\sqrt{2}.$$

**Igualdad:** se alcanza cuando los tres vectores son paralelos y con el mismo sentido, es decir, proporcionales a $(1,1)$:
- $(x, 20) \parallel (1,1) \Rightarrow x = 20$,
- $(30, y) \parallel (1,1) \Rightarrow y = 30$,
- $(40-20,\, 50-30) = (20,20) \parallel (1,1)$ ✓.

Los valores $x=20$, $y=30$ cumplen las restricciones $0 \le x \le 40$, $0 \le y \le 50$. Verificación directa:
$$\sqrt{400+400} + \sqrt{900+900} + \sqrt{400+400} = 20\sqrt{2} + 30\sqrt{2} + 20\sqrt{2} = 70\sqrt{2}.$$

$$\boxed{70\sqrt{2}}$$