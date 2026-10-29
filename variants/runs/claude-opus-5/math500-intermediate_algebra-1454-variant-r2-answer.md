## Reescritura del tercer término

Completando cuadrados:

$$a^2 + b^2 - 70a - 80b + 2825 = (a-35)^2 + (b-40)^2 + 2825 - 1225 - 1600 = (a-35)^2 + (b-40)^2$$

Así, la expresión es

$$\sqrt{a^2+15^2} + \sqrt{b^2+20^2} + \sqrt{(35-a)^2 + (40-b)^2}.$$

## Desigualdad de Minkowski

Interpretamos cada raíz como la norma de un vector, eligiéndolos de modo que la suma sea constante:

$$\mathbf{u} = (a,\,15), \qquad \mathbf{v} = (35-a,\,40-b), \qquad \mathbf{w} = (20,\,b)$$

con $|\mathbf{u}| = \sqrt{a^2+225}$, $|\mathbf{v}| = \sqrt{(35-a)^2+(40-b)^2}$, $|\mathbf{w}| = \sqrt{b^2+400}$, y

$$\mathbf{u}+\mathbf{v}+\mathbf{w} = (a + 35 - a + 20,\; 15 + 40 - b + b) = (55,\,55).$$

Por la desigualdad triangular,

$$|\mathbf{u}| + |\mathbf{v}| + |\mathbf{w}| \ge |\mathbf{u}+\mathbf{v}+\mathbf{w}| = \sqrt{55^2+55^2} = 55\sqrt{2}.$$

## Caso de igualdad

La igualdad requiere que los tres vectores sean paralelos y del mismo sentido:

- $(a,15) \parallel (20,b) \Rightarrow ab = 300$
- $(a,15) \parallel (35-a, 40-b) \Rightarrow a(40-b) = 15(35-a) \Rightarrow 40a - 300 = 525 - 15a \Rightarrow a = 15$

Entonces $b = 20$, valores admisibles ($0 \le 15 \le 35$, $0 \le 20 \le 40$). Verificación directa:

$$\sqrt{225+225} + \sqrt{400+400} + \sqrt{400+400} = 15\sqrt2 + 20\sqrt2 + 20\sqrt2 = 55\sqrt2.$$

$$\boxed{55\sqrt{2}}$$