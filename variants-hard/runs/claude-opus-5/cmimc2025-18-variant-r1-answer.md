## Razonamiento

**1. El polígono es un zonógono.** Un 6720-gono regular es centralmente simétrico, con $n = 3360$ direcciones de lado distintas, formando ángulos
$$\theta_k = \frac{k\pi}{3360}, \qquad k = 0,1,\dots,3359.$$

**2. Rigidez de los teselados por paralelogramos.** Por el resultado clásico de de Bruijn, en cualquier descomposición de un zonógono en paralelogramos cada lado de cada pieza es paralelo a uno de los lados del polígono, y las piezas quedan en correspondencia biyectiva con los pares de direcciones: hay exactamente $\binom{n}{2}$ paralelogramos, uno por cada par $\{i,j\}$ de direcciones. (Comprobación: el octágono se corta siempre en $\binom{4}{2}=6$ piezas; el hexágono, en $3$.)

**3. ¿Cuándo una pieza es rectángulo?** El paralelogramo asociado al par $\{j,k\}$ es un rectángulo exactamente si esas dos direcciones son perpendiculares:
$$\frac{(k-j)\pi}{3360} = \frac{\pi}{2} \iff k-j = 1680.$$

**4. Conteo.** Los pares con $k - j = 1680$ y $0 \le j < k \le 3359$ son
$$j = 0,1,\dots,1679,$$
es decir $1680$ pares.

Como el número de piezas de cada tipo no depende del teselado elegido, $R$ no es minimizable: vale siempre $1680$.

(Verificación del método con el octágono, $n=4$: las parejas perpendiculares son $(0^\circ,90^\circ)$ y $(45^\circ,135^\circ)$, o sea $n/2 = 2$ rectángulos, lo que coincide con lo observado.)

$$\boxed{1680}$$