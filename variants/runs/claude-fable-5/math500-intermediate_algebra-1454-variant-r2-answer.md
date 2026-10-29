## Planteamiento

Primero completo el cuadrado en el tercer radical:

$$a^2 + b^2 - 70a - 80b + 2825 = (a-35)^2 + (b-40)^2,$$

ya que $1225 + 1600 = 2825$. La expresión queda:

$$\sqrt{a^2 + 15^2} + \sqrt{b^2 + 20^2} + \sqrt{(35-a)^2 + (40-b)^2}.$$

## Interpretación geométrica

Construyo un camino en el plano con tres segmentos cuyas longitudes son exactamente esos tres términos:

- De $(0,0)$ a $(a,\,15)$: longitud $\sqrt{a^2+225}$.
- De $(a,\,15)$ a $(a+20,\,15+b)$: longitud $\sqrt{20^2+b^2} = \sqrt{b^2+400}$.
- De $(a+20,\,15+b)$ a $(a+20+(35-a),\,15+b+(40-b)) = (55,\,55)$: longitud $\sqrt{(35-a)^2+(40-b)^2}$.

Los tres segmentos unen $(0,0)$ con el punto fijo $(55, 55)$, así que por la desigualdad triangular:

$$\sqrt{a^2+225} + \sqrt{b^2+400} + \sqrt{(35-a)^2+(40-b)^2} \ge \sqrt{55^2 + 55^2} = 55\sqrt{2}.$$

## Verificación de la igualdad

La igualdad se da cuando los tres segmentos son colineales en la dirección $(1,1)$:

- Primer segmento $(a, 15) \parallel (1,1) \Rightarrow a = 15$ ✓ (dentro de $[0,35]$).
- Segundo segmento $(20, b) \parallel (1,1) \Rightarrow b = 20$ ✓ (dentro de $[0,40]$).
- Tercer segmento: $(35-15,\, 40-20) = (20,20) \parallel (1,1)$ ✓.

Comprobación directa en $(a,b) = (15,20)$:

$$\sqrt{225+225} + \sqrt{400+400} + \sqrt{400+400} = 15\sqrt{2} + 20\sqrt{2} + 20\sqrt{2} = 55\sqrt{2}.$$

$$\boxed{55\sqrt{2}}$$