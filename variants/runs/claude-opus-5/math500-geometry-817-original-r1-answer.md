## Planteamiento

Coloco $Q$ en el origen, con $A=(14,0)$ y $B=(0,14)$.

**Semicírculo grande:** tiene como diámetro el radio $QA$, así que su centro es $(7,0)$ y su radio es $7$.

**Semicírculo pequeño:** tiene su diámetro sobre $QB$, centro $(0,c)$ y radio $r$.

## Condiciones de tangencia

1. **Tangencia interna con la circunferencia mayor** (radio 14): la distancia del centro $Q$ al centro del semicírculo pequeño más su radio da el radio total:
$$c + r = 14 \quad\Longrightarrow\quad c = 14 - r$$

2. **Tangencia externa con el semicírculo grande:** la distancia entre centros es la suma de radios:
$$\sqrt{7^2 + c^2} = 7 + r$$

## Resolución

Sustituyendo $c = 14 - r$:

$$49 + (14-r)^2 = (7+r)^2$$
$$49 + 196 - 28r + r^2 = 49 + 14r + r^2$$
$$196 - 28r = 14r$$
$$196 = 42r$$
$$r = \frac{196}{42} = \frac{14}{3}$$

Verificación: el centro queda en $(0, 28/3)$ y el diámetro va de $(0,14/3)$ a $(0,14)$, es decir, es tangente a la circunferencia justo en el punto $B$ y cabe dentro del radio $QB$.

$$\boxed{\dfrac{14}{3}}$$