## Planteamiento

Coloco coordenadas con $O=(0,0)$, $M=(20,0)$ y $N=(0,20)$, de modo que la región del cuadrante $MON$ es el primer cuadrante limitado por el arco de radio 20.

**Semicírculo grande** (diámetro $OM$): su centro es el punto medio de $OM$,
$$C_1=(10,0),\qquad R_1=10.$$

**Semicírculo pequeño** (diámetro sobre $ON$, con un extremo en $N$): si su radio es $r$, su diámetro va de $N=(0,20)$ hasta $(0,20-2r)$, así que su centro está en
$$C_2=(0,\,20-r),\qquad R_2=r.$$

## Condición de tangencia

Los dos semicírculos son exteriores entre sí (no pueden ser tangentes internamente, pues $N$ está fuera del semicírculo grande). La tangencia externa exige que la distancia entre centros iguale la suma de los radios:

$$|C_1C_2| = 10 + r.$$

Calculando la distancia:
$$|C_1C_2| = \sqrt{(10-0)^2 + \big(0-(20-r)\big)^2} = \sqrt{100 + (20-r)^2}.$$

Entonces:
$$100 + (20-r)^2 = (10+r)^2$$
$$100 + 400 - 40r + r^2 = 100 + 20r + r^2$$
$$400 - 40r = 20r \quad\Longrightarrow\quad 400 = 60r \quad\Longrightarrow\quad r = \frac{20}{3}.$$

## Verificación

Con $r=\tfrac{20}{3}$: $C_2=(0,\tfrac{40}{3})$, y
$$|C_1C_2| = \sqrt{100+\tfrac{1600}{9}} = \sqrt{\tfrac{2500}{9}} = \tfrac{50}{3} = 10+\tfrac{20}{3}. \checkmark$$

El punto de tangencia es $(4,8)$, que efectivamente pertenece a ambos arcos: $(4-10)^2+8^2=100$ ✓ y $4^2+(8-\tfrac{40}{3})^2=\tfrac{400}{9}$ ✓. Además, todo el semicírculo pequeño queda dentro de la región del cuadrante.

$$\boxed{\dfrac{20}{3}}$$