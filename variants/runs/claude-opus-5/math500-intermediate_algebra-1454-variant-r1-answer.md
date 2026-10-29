## Reescritura del tercer radical

Completando cuadrados:

$$a^2+b^2-70a-80b+2825=(a-35)^2+(b-40)^2+2825-1225-1600=(35-a)^2+(40-b)^2$$

Así, la expresión es

$$\sqrt{a^2+15^2}+\sqrt{b^2+20^2}+\sqrt{(35-a)^2+(40-b)^2}.$$

## Interpretación vectorial

Elijo los vectores

$$u=(15,\;a),\qquad v=(b,\;20),\qquad w=(40-b,\;35-a),$$

cuyas normas son exactamente los tres radicales. Su suma es constante:

$$u+v+w=(15+b+40-b,\;a+20+35-a)=(55,\;55).$$

Por la desigualdad triangular,

$$\|u\|+\|v\|+\|w\|\ \ge\ \|u+v+w\|=\sqrt{55^2+55^2}=55\sqrt{2}.$$

## Caso de igualdad

Se alcanza cuando los tres vectores son paralelos a $(1,1)$: $a=15$, $b=20$, lo que da $w=(20,20)$. Ambos valores cumplen $0\le a\le 35$, $0\le b\le 40$.

Verificación: $\sqrt{450}+\sqrt{800}+\sqrt{800}=15\sqrt2+20\sqrt2+20\sqrt2=55\sqrt2\approx 77.78$.

\boxed{55\sqrt{2}}