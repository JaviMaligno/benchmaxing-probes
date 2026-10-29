Voy a razonar el problema paso a paso.

## 1. Entender la configuración

Tenemos tres semicírculos encajados:

- $\omega_1$ está inscrito en $\omega_2$
- $\omega_2$ está inscrito en $\omega_3$

Recordemos la definición dada: una semicircunferencia está inscrita en otra si el diámetro de la menor es una cuerda de la mayor, y el arco de la menor es tangente al diámetro de la mayor.

Datos:
- $r_1 = 3$ (radio de $\omega_1$)
- $r_3 = 12$ (radio de $\omega_3$)
- Los diámetros de $\omega_1$ y $\omega_3$ son paralelos

$P$ y $Q$ son los extremos del diámetro de $\omega_3$, y $T$ es el punto donde el arco de $\omega_2$ toca al segmento $PQ$.

Queremos calcular $PT \cdot TQ$.

## 2. Relación entre semicírculos inscritos

**Lema:** Si un semicírculo de radio $r$ está inscrito en un semicírculo de radio $R$, y el diámetro del menor es paralelo al diámetro del mayor, entonces:

El diámetro del semicírculo menor es una cuerda del mayor. El arco del menor es tangente al diámetro del mayor.

Pensemos geométricamente. Consideremos $\omega_3$ como el semicírculo superior con diámetro $PQ$ sobre el eje $x$, centrado en el origen. Entonces $P = (-12, 0)$ y $Q = (12, 0)$.

El semicírculo $\omega_2$ tiene su diámetro como cuerda de $\omega_3$ (paralelo a $PQ$), y su arco tangente a $PQ$ (el diámetro de $\omega_3$).

El semicírculo $\omega_2$ es el semicírculo inferior con su diámetro como una cuerda horizontal de $\omega_3$ a cierta altura, y su arco tocando el eje $x$ (donde está $PQ$).

## 3. Coordenadas del semicírculo $\omega_2$

Sea $\omega_2$ un semicírculo con centro en $(0, h)$ y radio $r_2$, con su arco apuntando hacia abajo (tocando $PQ$). Su punto más bajo toca $PQ$, así que está en $T = (0, 0)$ si su centro está directamente sobre $T$.

Como el diámetro de $\omega_2$ debe ser una cuerda de $\omega_3$: los extremos del diámetro de $\omega_2$ están sobre la semicircunferencia $\omega_3$.

El diámetro de $\omega_2$ es horizontal (paralelo a $PQ$), de longitud $2r_2$, centrado en $(0, h)$. Sus extremos están en $(\pm r_2, h)$.

La semicircunferencia $\omega_3$ tiene ecuación $x^2 + y^2 = 144$ con $y \geq 0$.

Los extremos $(\pm r_2, h)$ están sobre $\omega_3$:
$$r_2^2 + h^2 = 144$$

Además, el arco de $\omega_2$ (semicírculo inferior centrado en $(0, h)$ con radio $r_2$) es tangente a $PQ$ (el eje $x$). El punto más bajo de $\omega_2$ está en $y = h - r_2$. Como es tangente al eje $x$:
$$h - r_2 = 0 \quad \Rightarrow \quad h = r_2$$

Esto significa que $T$ está directamente debajo del centro de $\omega_2$, en $(0, 0)$.

Sustituyendo $h = r_2$:
$$r_2^2 + r_2^2 = 144$$
$$2r_2^2 = 144$$
$$r_2 = \frac{12}{\sqrt{2}} = 6\sqrt{2}$$

## 4. Coordenadas del semicírculo $\omega_1$

Ahora $\omega_1$ está inscrito en $\omega_2$, con diámetro paralelo al de $\omega_2$ (y por tanto al de $\omega_3$).

El semicírculo $\omega_2$ es el inferior, centrado en $(0, r_2)$ con radio $r_2 = 6\sqrt{2}$, y su diámetro es la cuerda de $\omega_3$ a altura $y = r_2$.

El diámetro de $\omega_2$ está a altura $h = r_2 = 6\sqrt{2}$, con extremos en $(\pm r_2, r_2)$.

El semicírculo $\omega_1$ tiene su diámetro como cuerda de $\omega_2$, paralelo al diámetro de $\omega_2$. El arco de $\omega_1$ es tangente al diámetro de $\omega_2$ (la línea horizontal $y = r_2$).

$\omega_2$ es el semicírculo inferior centrado en $(0, r_2)$ con radio $r_2$. Su ecuación es:
$$x^2 + (y - r_2)^2 = r_2^2, \quad y \leq r_2$$

El diámetro de $\omega_1$ es una cuerda horizontal de $\omega_2$ a cierta altura $y = k$. El arco de $\omega_1$ apunta hacia arriba (hacia el diámetro de $\omega_2$, que está en $y = r_2$).

Espera, necesito reconsiderar. El diámetro de $\omega_1$ es una cuerda de $\omega_2$ (la mayor), y el arco de $\omega_1$ es tangente al diámetro de $\omega_2$ (la mayor).

El diámetro de $\omega_2$ es la cuerda horizontal en $y = r_2 = 6\sqrt{2}$ desde $x = -r_2$ hasta $x = r_2$.

El arco de $\omega_1$ debe ser tangente a esta cuerda (diámetro de $\omega_2$). Así que el semicírculo $\omega_1$ está orientado hacia arriba (convexo hacia arriba), con su arco tocando la línea $y = r_2$ desde abajo.

Sea el centro de $\omega_1$ en $(0, c)$ con radio $r_1 = 3$. Su arco apunta hacia arriba, y su diámetro es una cuerda horizontal de $\omega_2$ en $y = c$ (extremos en $(\pm 3, c)$).

El diámetro de $\omega_1$ está en $y = c$, con extremos $(\pm 3, c)$ sobre la semicircunferencia $\omega_2$:
$$3^2 + (c - r_2)^2 = r_2^2$$
$$9 + (c - r_2)^2 = r_2^2$$

El arco de $\omega_1$ es tangente al diámetro de $\omega_2$ (línea $y = r_2$). El punto más alto de $\omega_1$ está en $y = c + 3$. Como es tangente a $y = r_2$:
$$c + 3 = r_2$$
$$c = r_2 - 3 = 6\sqrt{2} - 3$$

Verifiquemos la condición de cuerda:
$$9 + (c - r_2)^2 = 9 + (r_2 - 3 - r_2)^2 = 9 + 9 = 18$$
$$\text{¿Es } r_2^2 = (6\sqrt{2})^2 = 72?$$

$18 \neq 72$. Hmm, eso no funciona. Algo está mal con mi suposición.

## 5. Reconsiderar la geometría

El problema es que $\omega_1$ no tiene por qué estar centrado en el mismo eje vertical. Déjame pensar de nuevo.

Cuando un semicírculo está inscrito en otro, no necesariamente los centros están alineados verticalmente. El diámetro del menor es una cuerda del mayor, y el arco del menor es tangente al diámetro del mayor.

Consideremos dos semicírculos: el mayor con centro $O$ y radio $R$, y el menor con centro $o$ y radio $r$.

El diámetro del mayor es una línea. El arco del menor es tangente a esta línea en un punto $T$.

El diámetro del menor es una cuerda del mayor, así que sus extremos están sobre el arco del mayor.

Esto significa que el semicírculo menor está "acostado" sobre el diámetro del mayor, tocándolo en $T$, y su diámetro se extiende hasta tocar el arco del mayor.

**Análisis correcto:**

Sea el semicírculo mayor con diámetro sobre el eje $x$, de $x=0$ a $x=2R$, centrado en $(R, 0)$, arco superior (semicírculo superior).

El diámetro del mayor es el segmento de $(0,0)$ a $(2R, 0)$.

El semicírculo menor está inscrito: su diámetro es una cuerda del arco mayor, y su arco es tangente al diámetro del mayor (el eje $x$) en un punto $T$.

Así que el semicírculo menor es un semicírculo inferior, con su arco tocando el eje $x$ en $T$, y su diámetro es una cuerda horizontal del semicírculo mayor a altura $r$ (el radio del menor).

El centro del menor está en $(x_0, r)$ y su radio es $r$. El diámetro es horizontal, a altura $r$, con extremos $(x_0 - r, r)$ y $(x_0 + r, r)$.

Estos extremos están sobre el arco mayor:
$$(x_0 - r - R)^2 + r^2 = R^2 \quad \text{y} \quad (x_0 + r - R)^2 + r^2 = R^2$$

De ambas:
$$(x_0 - r)^2 - 2R(x_0 - r) + R^2 + r^2 = R^2$$
$$(x_0 - r)^2 - 2R(x_0 - r) + r^2 = 0$$

y similarmente para $x_0 + r$.

Restando ambas ecuaciones:
$$(x_0 + r)^2 - (x_0 - r)^2 - 2R(x_0 + r - x_0 + r) = 0$$
$$4x_0 r - 4Rr = 0$$
$$x_0 = R$$

Así que el centro está en $x_0 = R$, alineado verticalmente con el centro del mayor. Entonces:

$$(R - r - R)^2 + r^2 = R^2$$
$$r^2 + r^2 = R^2$$
$$R = r\sqrt{2}$$

¡Interesante! Entonces cuando un semicírculo está inscrito en otro con esta configuración (diámetros paralelos), la relación de radios es $R_{\text{mayor}} = r_{\text{menor}}\sqrt{2}$.

## 6. Aplicar a nuestro problema

Para $\omega_3$ (radio $12$) y $\omega_2$:
$$12 = r_2 \sqrt{2}$$
$$r_2 = \frac{12}{\sqrt{2}} = 6\sqrt{2}$$

Para $\omega_2$ (radio $6\sqrt{2}$) y $\omega_1$ (radio $3$):
$$6\sqrt{2} = 3\sqrt{2} = 3 \cdot 2 = 6\sqrt{2}$$

Verifiquemos: $3\sqrt{2} \approx 4.24$, pero $6\sqrt{2} \approx 8.49$. Espera, eso no es correcto.

$r_1 \sqrt{2} = 3\sqrt{2} \approx 4.24$, pero $r_2 = 6\sqrt{2} \approx 8.49$.

$6\sqrt{2} \neq 3\sqrt{2}$

Hmm, esto sugiere que quizás la relación $R = r\sqrt{2}$ no es la correcta, o que $\omega_1$ no tiene por qué estar inscrito de la manera que asumí.

Déjame reconsiderar. Tal vez el diámetro de $\omega_1$ no es paralelo al diámetro de $\omega_2$. El problema dice que los diámetros de $\omega_1$ y $\omega_3$ son paralelos, pero no dice nada sobre el de $\omega_2$.

Ah, pero espera. Si $\omega_1$ está inscrito en $\omega_2$ y el diámetro de $\omega_1$ es paralelo al de $\omega_3$, y $\omega_2$ está inscrito en $\omega_3$... no sabemos la orientación del diámetro de $\omega_2$.

Sin embargo, hay una condición que relaciona los radios. Si $R = r\sqrt{2}$ para semicírculos inscritos con diámetros paralelos:

Si $\omega_2$ está inscrito en $\omega_3$ con diámetros paralelos, entonces $r_2 = 12/\sqrt{2} = 6\sqrt{2}$.

Si $\omega_1$ está inscrito en $\omega_2$, y el diámetro de $\omega_1$ es paralelo al diámetro de $\omega_3$... pero ¿es paralelo al diámetro de $\omega_2$? No necesariamente.

Espera, necesito revisar. El diámetro de $\omega_2$ es una cuerda de $\omega_3$. Si el diámetro de $\omega_2$ no es paralelo al de $\omega_3$, entonces $r_2 > 6\sqrt{2}$ o $r_2 < 6\sqrt{2}$ según sea el caso.

Hmm, pero en realidad, para que un semicírculo esté inscrito en otro, el diámetro del menor es una cuerda del mayor. La cuerda más larga que puede tener un semicírculo menor (con arco tangente al diámetro del mayor) es cuando el diámetro del menor es paralelo al diámetro del mayor, lo que da la relación $R = r\sqrt{2}$.

Si el diámetro del menor no es paralelo, entonces la cuerda es más corta relativamente, y $r$ sería menor para el mismo $R$.

Dado que $r_3 = 12$ y $r_2$ es lo que sea, y luego $r_1 = 3$ con diámetro de $\omega_1$ paralelo al de $\omega_3$:

Si el diámetro de $\omega_1$ es paralelo al de $\omega_2$, entonces $r_2 = r_1 \sqrt{2} = 3\sqrt{2}$.

Si el diámetro de $\omega_1$ es paralelo al de $\omega_3$, y el de $\omega_2$ es paralelo al de $\omega_3$, entonces tanto $\omega_2$ está inscrito en $\omega_3$ con diámetros paralelos como $\omega_1$ está inscrito en $\omega_2$ con diámetros paralelos. Esto daría $r_2 = 6\sqrt{2}$ y $r_2 = 3\sqrt{2}$, lo cual es contradictorio.

Por lo tanto, los diámetros de $\omega_2$ y $\omega_3$ NO son paralelos. El diámetro de $\omega_2$ está en una orientación diferente.

## 7. Enfoque con tangencia

Voy a abordar esto de manera más sistemática usando la relación entre semicírculos inscritos.

**Lema general:** Si un semicírculo de radio $r$ está inscrito en un semicírculo de radio $R$, con su diámetro formando un ángulo $\theta$ con el diámetro del mayor, y tocando el diámetro del mayor en el punto $T$, entonces hay una relación entre $r$, $R$, la posición de $T$, y $\theta$.

Déjame establecer un sistema de coordenadas.

**Semicírculo mayor $\omega_3$:** diámetro $PQ$ en el eje $x$, centrado en el origen: $P=(-12,0)$, $Q=(12,0)$. Arco superior: $x^2 + y^2 = 144$, $y \geq 0$.

**Semicírculo $\omega_2$:** radio $r_2$ (desconocido). Su arco es tangente a $PQ$ (eje $x$) en el punto $T = (t, 0)$. El diámetro de $\omega_2$ es una cuerda de $\omega_3$, con extremos sobre el arco de $\omega_3$.

El centro de $\omega_2$ está en $(t, r_2)$ (asumiendo que el arco de $\omega_2$ está debajo de su diámetro, y toca el eje $x$ desde arriba — es decir, $\omega_2$ es un semicírculo inferior).

Espera, necesito ser más cuidadoso. El arco de $\omega_2$ es tangente a $PQ$, y $T$ es el punto de tangencia. El semicírculo $\omega_2$ tiene su diámetro como cuerda de $\omega_3$.

Si el arco de $\omega_2$ está por encima de $PQ$ (en el interior del semicírculo $\omega_3$), entonces $\omega_2$ es un semicírculo que se abre hacia abajo (semicírculo inferior), con su extremo libre (el arco) tocando $PQ$.

El centro de $\omega_2$ está en $(t, r_2)$ donde $r_2$ es su radio. Su diámetro es horizontal (paralelo a $PQ$) si asumimos que el diámetro de $\omega_2$ es horizontal... pero no sabemos eso.

Espera, en realidad el diámetro de $\omega_2$ es una cuerda de $\omega_3$. Una cuerda puede estar en cualquier orientación.

Hmm, pero el problema dice que el diámetro de $\omega_1$ es paralelo al de $\omega_3$. No dice nada sobre el de $\omega_2$.

Necesito determinar la configuración única que satisface todas las condiciones.

## 8. Relación clave

Déjame pensar en esto desde una perspectiva diferente. 

Para un semicírculo inscrito en otro, hay una propiedad hermosa. Consideremos el semicírculo mayor con diámetro $AB$ y radio $R$. El semicírculo menor con diámetro $CD$ (cuerda del mayor) y arco tangente al diámetro $AB$ en $T$.

**Propiedad:** El producto de las distancias de $T$ a los extremos del diámetro del mayor es igual al cuadrado del radio del menor... no, déjame verificar.

Usando el lema que demostré antes: si el diámetro del menor es paralelo al del mayor, entonces $R = r\sqrt{2}$ y el punto de tangencia $T$ es el punto medio del diámetro del mayor.

Pero si el diámetro no es paralelo, la configuración es diferente. En general, si el punto de tangencia está a distancia $a$ de un extremo y $b$ del otro (con $a + b = 2R$), y el radio del menor es $r$, entonces hay una relación.

Déjame derivar esto. Sea el semicírculo mayor con centro en el origen, radio $R$, diámetro en el eje $x$ de $-R$ a $R$. El punto de tangencia $T = (t, 0)$.

El semicírculo menor tiene su centro en $(t, r)$ (directamente sobre $T$), radio $r$, y su arco toca el eje $x$ en $T$.

El diámetro del menor es una cuerda del mayor. La cuerda es perpendicular al radio desde el centro del menor hasta la cuerda... espera, no. El diámetro del semicírculo menor es una línea recta a través del centro $(t, r)$ del menor. Los extremos de este diámetro están sobre el arco del semicírculo mayor.

La cuerda del mayor que es el diámetro del menor pasa por $(t, r)$ y tiene longitud $2r$. Sea $\theta$ el ángulo que forma esta cuerda con la horizontal.

Los extremos de la cuerda están en $(t \pm r\cos\theta, r \pm r\sin\theta)$.

Estos extremos están sobre el arco mayor:
$$(t \pm r\cos\theta)^2 + (r \pm r\sin\theta)^2 = R^2$$

Hmm, pero la cuerda del mayor no pasa necesariamente por el punto $(t, r)$. Espera, sí: el diámetro del semicírculo menor pasa por su centro $(t, r)$, y es una cuerda del mayor.

En realidad, la cuerda del semicírculo mayor que conecta los extremos del diámetro del semicírculo menor pasa por el centro del semicírculo menor (ya que es su diámetro). Pero ¿la cuerda pasa por el punto medio? El centro del semicírculo menor es el punto medio de su diámetro, que es la cuerda.

Así que la cuerda del mayor tiene punto medio en $(t, r)$ y longitud $2r$. Los extremos son $(t + r\cos\theta, r + r\sin\theta)$ y $(t - r\cos\theta, r - r\sin\theta)$ para algún ángulo $\theta$.

Para que ambos estén sobre el arco mayor:
$$(t + r\cos\theta)^2 + (r + r\sin\theta)^2 = R^2$$
$$(t - r\cos\theta)^2 + (r - r\sin\theta)^2 = R^2$$

Restando:
$$(t + r\cos\theta)^2 - (t - r\cos\theta)^2 + (r + r\sin\theta)^2 - (r - r\sin\theta)^2 = 0$$
$$4tr\cos\theta + 4r^2\sin\theta = 0$$
$$t\cos\theta + r\sin\theta = 0$$

Sumando:
$$2t^2 + 2r^2\cos^2\theta + 2r^2 + 2r^2\sin^2\theta = 2R^2$$
$$t^2 + r^2(\cos^2\theta + \sin^2\theta) + r^2 = 2R^2/2 = R^2$$
$$t^2 + 2r^2 = R^2$$

¡Excelente! Así que:
$$t^2 + 2r^2 = R^2$$

donde $t$ es la coordenada $x$ del punto de tangencia $T = (t, 0)$.

También, $t\cos\theta + r\sin\theta = 0$, lo que da $\tan\theta = -t/r$. Esto es consistente: la cuerda es perpendicular al radio desde el centro del mayor hasta su punto medio... En realidad, para una cuerda del mayor, el radio desde el centro del mayor hasta el punto medio de la cuerda es perpendicular a la cuerda. El punto medio de la cuerda es $(t, r)$, y la perpendicular a la cuerda (en dirección al centro del mayor) tiene pendiente que satisface $\tan\theta \cdot \text{pendiente perpendicular} = -1$.

Esto confirma que $t^2 + 2r^2 = R^2$ es la relación general.

Cuando $t = 0$ (diámetro paralelo),
$$2r^2 = R^2, \quad r = R/\sqrt{2}$$

lo cual coincide con nuestro resultado anterior.

## 9. Aplicar a $\omega_2$ en $\omega_3$

Para $\omega_2$ (radio $r_2$) inscrito en $\omega_3$ (radio $R_3 = 12$), con punto de tangencia $T = (t, 0)$:
$$t^2 + 2r_2^2 = 144$$

## 10. Aplicar a $\omega_1$ en $\omega_2$

Ahora, $\omega_1$ (radio $r_1 = 3$) está inscrito en $\omega_2$ (radio $r_2$).

El diámetro de $\omega_1$ es paralelo al diámetro de $\omega_3$ (que es el eje $x$). En el marco de referencia del semicírculo $\omega_2$, necesitamos entender qué significa esto.

El diámetro de $\omega_2$ es la cuerda de $\omega_3$ con ángulo $\theta$ respecto al eje horizontal. El diámetro de $\omega_1$ es paralelo al diámetro de $\omega_3$ (horizontal), que forma un ángulo $-\theta$ con el diámetro de $\omega_2$.

En el marco del semicírculo $\omega_2$, el diámetro de $\omega_2$ es la "base", y el diámetro de $\omega_1$ es una cuerda de $\omega_2$ en ángulo $-\theta$ con la base de $\omega_2$.

Aplicando nuestra relación general en el marco de $\omega_2$: si el punto de tangencia de $\omega_1$ con el diámetro de $\omega_2$ está a distancia $s$ del centro del diámetro de $\omega_2$ (a lo largo del diámetro de $\omega_2$), entonces:
$$s^2 + 2r_1^2 = r_2^2$$

donde $s$ es la distancia (con signo) desde el centro del diámetro de $\omega_2$ hasta el punto de tangencia, medida a lo largo del diámetro de $\omega_2$.

Ahora, necesitamos relacionar $s$ con $t$ y $\theta$.

## 11. Relacionar las dos tangencias

El punto de tangencia de $\omega_1$ con el diámetro de $\omega_2$ está en algún punto del diámetro de $\omega_2$. 

Usemos la relación que encontramos: para $\omega_2$ en $\omega_3$:
$$t\cos\theta + r_2\sin\theta = 0$$

Esto nos da la orientación del diámetro de $\omega_2$. En particular, la cuerda (diámetro de $\omega_2$) pasa por el punto $(t, r_2)$ y tiene pendiente $\tan\theta$.

El diámetro de $\omega_2$ es una línea que pasa por $(t, r_2)$ con pendiente $\tan\theta$. Los extremos están en $(t \pm r_2\cos\theta, r_2 \pm r_2\sin\theta)$.

Ahora, el semicírculo $\omega_1$ está inscrito en $\omega_2$ (que es un semicírculo inferior con centro $(t, r_2)$ y radio $r_2$).

La "base" de $\omega_2$ es su diámetro (la cuerda). El arco de $\omega_2$ es el semicírculo inferior, que toca el eje $x$ en $T = (t, 0)$.

El semicírculo $\omega_1$ está dentro de $\omega_2$, con su diámetro como cuerda de $\omega_2$ (del arco de $\omega_2$), y su arco tangente al diámetro de $\omega_2$ (la cuerda).

**Punto de tangencia:** El arco de $\omega_1$ toca el diámetro de $\omega_2$ en algún punto. Llamémoslo $U$.

El centro de $\omega_1$ está directamente sobre (o bajo) $U$, a distancia $r_1 = 3$ de $U$ (hacia el interior de $\omega_2$).

Como $\omega_1$ está dentro del semicírculo inferior $\omega_2$, el arco de $\omega_1$ toca el diámetro de $\omega_2$ desde abajo (hacia el interior de $\omega_2$).

El centro de $\omega_1$ está en $U + \vec{n}$ donde $\vec{n}$ es la normal al diámetro de $\omega_2$ apuntando hacia el interior (hacia abajo), con $|\vec{n}| = r_1 = 3$.

## 12. Diámetro de $\omega_1$ paralelo al diámetro de $\omega_3$

El diámetro de $\omega_1$ es paralelo al eje $x$ (diámetro de $\omega_3$). El diámetro de $\omega_1$ es una cuerda del arco de $\omega_2$.

El diámetro de $\omega_1$ es una línea horizontal que pasa por el centro de $\omega_1$. Sus extremos están sobre el arco de $\omega_2$ (semicírculo inferior).

El arco de $\omega_2$ es la parte inferior del círculo centrado en $(t, r_2)$ con radio $r_2$.

El diámetro de $\omega_1$ es la cuerda horizontal del círculo de $\omega_2$ a la altura del centro de $\omega_1$. Si el centro de $\omega_1$ está en $(x_1, y_1)$, entonces el diámetro de $\omega_1$ está en $y = y_1$ con extremos $(x_1 \pm 3, y_1)$.

Estos extremos están sobre el círculo de $\omega_2$:
$$(x_1 \pm 3 - t)^2 + (y_1 - r_2)^2 = r_2^2$$

Esto da:
$$(x_1 - t + 3)^2 + (y_1 - r_2)^2 = r_2^2$$
$$(x_1 - t - 3)^2 + (y_1 - r_2)^2 = r_2^2$$

Restando: $(x_1 - t + 3)^2 = (x_1 - t - 3)^2$, lo que da $x_1 - t = 0$, es decir, $x_1 = t$.

Sumando:
$$9 + (y_1 - r_2)^2 = r_2^2$$
$$(y_1 - r_2)^2 = r_2^2 - 9$$

El punto más bajo del arco de $\omega_1$ (el punto de tangencia con el diámetro de $\omega_2$) está en $(x_1, y_1 - 3) = (t, y_1 - 3)$.

Este punto está sobre el diámetro de $\omega_2$. El diámetro de $\omega_2$ es la línea con pendiente $\tan\theta$ que pasa por $(t, r_2)$.

La ecuación paramétrica del diámetro de $\omega_2$: $(t + u\cos\theta, r_2 + u\sin\theta)$ para $u \in [-r_2, r_2]$.

El punto de tangencia $(t, y_1 - 3)$ está sobre esta línea, así que:
$$(t, y_1 - 3) = (t + u\cos\theta, r_2 + u\sin\theta)$$

Esto da:
$$t = t + u\cos\theta \Rightarrow u\cos\theta = 0$$
$$y_1 - 3 = r_2 + u\sin\theta$$

Si $\cos\theta = 0$, entonces $\theta = \pm \pi/2$. De $t\cos\theta + r_2 \sin\theta = 0$, si $\cos\theta = 0$ entonces $r_2 \sin\theta = 0$, lo que da $\sin\theta = 0$ (porque $r_2 \neq 0$), contradictorio. Así que $\cos\theta \neq 0$, y por tanto $u = 0$.

Entonces, el punto de tangencia es $(t, r_2 + 0 \cdot \sin\theta) = (t, r_2)$ con $u=0$, pero eso daría $y_1 - 3 = r_2$.

Espera, $u = 0$ corresponde al centro del diámetro de $\omega_2$. Así que el punto de tangencia es el centro del diámetro de $\omega_2$, en $(t, r_2)$.

Pero $(t, r_2)$ es el centro del círculo de $\omega_2$, que es el punto medio del diámetro. El punto de tangencia del arco de $\omega_1$ con el diámetro de $\omega_2$ está en el punto medio del diámetro de $\omega_2$.

Hmm, pero esto es raro. Si $\omega_1$ toca el diámetro de $\omega_2$ en su punto medio, entonces el centro de $\omega_1$ está directamente debajo de $(t, r_2)$ a distancia 3: el centro de $\omega_1$ está en $(t, r_2 - 3)$.

Entonces $y_1 = r_2 - 3$, y de la condición de cuerda:
$$(y_1 - r_2)^2 = r_2^2 - 9$$
$$9 = r_2^2 - 9$$
$$r_2^2 = 18$$
$$r_2 = \sqrt{18} = 3\sqrt{2}$$

Ahora, usando $t^2 + 2r_2^2 = R^2$:
$$t^2 + 2(18) = 144$$
$$t^2 + 36 = 144$$
$$t^2 = 108$$
$$|t| = 6\sqrt{3}$$

## 13. Calcular $PT \cdot TQ$

Tenemos $P = (-12, 0)$, $Q = (12, 0)$, $T = (t, 0)$ con $t = \pm 6\sqrt{3}$.

$$PT \cdot TQ = |t - (-12)| \cdot |12 - t| = |t + 12| \cdot |12 - t|$$

Para $t = 6\sqrt{3} \approx 10.39$ (o $-6\sqrt{3}$, que da el mismo producto por simetría):
$$PT = t + 12 = 6\sqrt{3} + 12$$
$$TQ = 12 - t = 12 - 6\sqrt{3}$$

$$PT \cdot TQ = (12 + 6\sqrt{3})(12 - 6\sqrt{3}) = 144 - 108 = 36$$

Para $t = -6\sqrt{3}$:
$$PT = t + 12 = 12 - 6\sqrt{3}$$
$$TQ = 12 - t = 12 + 6\sqrt{3}$$
$$PT \cdot TQ = 36$$

## 14. Verificación

Verifiquemos la configuración completa:

- $\omega_3$: semicírculo superior, centro $(0,0)$, radio $12$, diámetro en $[-12, 12]$.
- $\omega_2$: centro $(t, r_2) = (6\sqrt{3}, 3\sqrt{2})$, radio $r_2 = 3\sqrt{2} \approx 4.24$.
  - Su arco toca el eje $x$ en $T = (6\sqrt{3}, 0)$.
  - Su diámetro es una cuerda de $\omega_3$ con pendiente $\tan\theta$ donde $\tan\theta = -t/r_2 = -6\sqrt{3}/(3\sqrt{2}) = -2\sqrt{3/2} = -\sqrt{6}$.
  
  Verifiquemos los extremos del diámetro de $\omega_2$ sobre $\omega_3$:
  - $\cos\theta = 1/\sqrt{1 + \tan^2\theta} = 1/\sqrt{1+6} = 1/\sqrt{7}$
  - $\sin\theta = \tan\theta/\sqrt{1+\tan^2\theta} = -\sqrt{6}/\sqrt{7}$
  
  Extremos: $(t \pm r_2\cos\theta, r_2 \pm r_2\sin\theta)$.
  
  $r_2\cos\theta = 3\sqrt{2}/\sqrt{7} = 3\sqrt{2/7}$
  $r_2\sin\theta = 3\sqrt{2} \cdot (-\sqrt{6}/\sqrt{7}) = -3\sqrt{12}/\sqrt{7} = -6\sqrt{3}/\sqrt{7}$
  
  Extremo 1: $(6\sqrt{3} + 3\sqrt{2/7}, 3\sqrt{2} - 6\sqrt{3/7})$
  Verificar que esté sobre $x^2 + y^2 = 144$... (esto es complicado de verificar a mano, pero la derivación es correcta).

- $\omega_1$: centro $(t, r_2 - 3) = (6\sqrt{3}, 3\sqrt{2} - 3)$, radio $3$.
  - Su diámetro es horizontal (paralelo al eje $x$), con extremos $(t \pm 3, r_2 - 3)$.
  - Estos están sobre el círculo de $\omega_2$.
  - Su arco toca el diámetro de $\omega_2$ en $(t, r_2)$.

Verifiquemos que los extremos del diámetro de $\omega_1$ están sobre el arco de $\omega_2$:
$(t \pm 3 - t)^2 + (r_2 - 3 - r_2)^2 = 9 + 9 = 18 = r_2^2$. ✓

Verifiquemos que el diámetro de $\omega_1$ es efectivamente una cuerda del semicírculo $\omega_2$ (inferior): el centro de $\omega_1$ está en $y = r_2 - 3 = 3\sqrt{2} - 3 \approx 1.24$, que está debajo del centro de $\omega_2$ en $y = r_2 \approx 4.24$. Los extremos del diámetro de $\omega_1$ están en $y = r_2 - 3 \approx 1.24$, que está por debajo del diámetro de $\omega_2$ (en $y \approx 4.24$). El semicírculo $\omega_2$ incluye todos los puntos con $y \leq r_2$ dentro del círculo, así que los extremos están en $\omega_2$. ✓

Verifiquemos que el arco de $\omega_1$ (semicírculo superior centrado en $(t, r_2 - 3)$ con radio 3) es tangente al diámetro de $\omega_2$ en $(t, r_2)$:
El punto más alto del arco de $\omega_1$ está en $(t, r_2 - 3 + 3) = (t, r_2)$. ✓
El diámetro de $\omega_2$ pasa por $(t, r_2)$ (que es el punto medio). ✓
La tangente en el punto más alto de un semicírculo es horizontal, y el diámetro de $\omega_2$ tiene pendiente $-\sqrt{6} \neq 0$. 

¡Espera! Esto es un problema. Si el diámetro de $\omega_2$ tiene pendiente $-\sqrt{6}$ (no horizontal), y el arco de $\omega_1$ tiene tangente horizontal en su punto más alto $(t, r_2)$, entonces el arco de $\omega_1$ NO es tangente al diámetro de $\omega_2$.

Hmm, esto sugiere que mi suposición de que el centro de $\omega_1$ está directamente debajo del punto de tangencia es incorrecta, o que la tangencia no es en el punto más alto.

Espera, déjame pensar de nuevo. El arco de $\omega_1$ es un semicírculo con centro $(t, y_1)$ y radio 3. El punto de tangencia con el diámetro de $\omega_2$ es donde la distancia desde $(t, y_1)$ al diámetro de $\omega_2$ es exactamente 3, y el vector desde $(t, y_1)$ al punto de tangencia es perpendicular al diámetro de $\omega_2$.

En mi derivación, asumí que la tangencia ocurre en el punto más bajo del semicírculo $\omega_1$ (directamente debajo del centro), pero eso solo es correcto si el diámetro de $\omega_2$ es horizontal.

Como el diámetro de $\omega_2$ tiene pendiente no horizontal, el punto de tangencia no está directamente debajo del centro de $\omega_1$. El punto de tangencia está donde la normal al diámetro de $\omega_2$ intersecta el arco de $\omega_1$.

Esto significa que mi derivación anterior tiene un error. Déjame rehacer.

## 15. Rehacer la derivación de $\omega_1$ en $\omega_2$

El centro de $\omega_1$ está en $(x_1, y_1)$, y su radio es $r_1 = 3$.

**Condición 1:** El diámetro de $\omega_1$ es horizontal (paralelo al eje $x$). Por tanto, el centro está en el punto medio de la cuerda horizontal, y $x_1 = t$ (por simetría como antes, ya que los extremos $\pm 3$ del diámetro deben estar sobre el círculo de $\omega_2$, lo que requiere $x_1 = t$).

Así que el centro de $\omega_1$ está en $(t, y_1)$.

**Condición 2:** Los extremos del diámetro de $\omega_1$ están sobre el círculo de $\omega_2$:
$$(y_1 - r_2)^2 + 9 = r_2^2$$
$$(y_1 - r_2)^2 = r_2^2 - 9$$

**Condición 3:** El arco de $\omega_1$ es tangente al diámetro de $\omega_2$. El arco de $\omega_1$ es el semicírculo superior centrado en $(t, y_1)$ con radio 3 (ya que $\omega_1$ está dentro del semicírculo inferior $\omega_2$, su arco debe apuntar hacia arriba hacia el diámetro de $\omega_2$).

La distancia desde el centro $(t, y_1)$ al diámetro de $\omega_2$ debe ser exactamente 3 (para que el arco sea tangente).

El diámetro de $\omega_2$ es la línea que pasa por $(t, r_2)$ con pendiente $\tan\theta$. La ecuación de esta línea:
$$(y - r_2) = \tan\theta (x - t)$$
$$y - r_2 = (-\sqrt{6})(x - t) \quad \text{(usando } \tan\theta = -t/r_2 \text{)}$$

Espera, déjame calcular $\tan\theta$. De $t \cos\theta + r_2 \sin\theta = 0$:
$$\tan\theta = -t/r_2$$

Con $t = 6\sqrt{3}$ y $r_2 = 3\sqrt{2}$:
$$\tan\theta = -6\sqrt{3}/(3\sqrt{2}) = -2\sqrt{3/2} = -\sqrt{6}$$

Así que el diámetro de $\omega_2$ tiene pendiente $-\sqrt{6}$ y pasa por $(t, r_2)$:
$$y - r_2 = -\sqrt{6}(x - t)$$

**Distancia desde $(t, y_1)$ a esta línea:**

La distancia $d$ desde un punto $(x_0, y_0)$ a la línea $ax + by + c = 0$ es $|ax_0 + by_0 + c|/\sqrt{a^2 + b^2}$.

La línea es: $y - r_2 = -\sqrt{6}(x - t)$, es decir, $\sqrt{6}x + y - \sqrt{6}t - r_2 = 0$.

Distancia desde $(t, y_1)$:
$$d = \frac{|\sqrt{6}t + y_1 - \sqrt{6}t - r_2|}{\sqrt{6 + 1}} = \frac{|y_1 - r_2|}{\sqrt{7}}$$

Para tangencia, $d = 3$:
$$\frac{|y_1 - r_2|}{\sqrt{7}} = 3$$
$$|y_1 - r_2| = 3\sqrt{7}$$

Pero de la Condición 2:
$$(y_1 - r_2)^2 = r_2^2 - 9$$

Combinando:
$$r_2^2 - 9 = (3\sqrt{7})^2 = 63$$
$$r_2^2 = 72$$
$$r_2 = 6\sqrt{2}$$

## 16. Calcular $t$

De $t^2 + 2r_2^2 = 144$:
$$t^2 + 2(72) = 144$$
$$t^2 + 144 = 144$$
$$t^2 = 0$$
$$t = 0$$

Esto significa que $T = (0, 0)$, ¡el punto medio del diámetro de $\omega_3$!

## 17. Calcular $PT \cdot TQ$

$P = (-12, 0)$, $Q = (12, 0)$, $T = (0, 0)$.

$$PT = 12, \quad TQ = 12$$
$$PT \cdot TQ = 144$$

## 18. Verificación completa

- $\omega_3$: centro $(0,0)$, radio $12$, semicírculo superior.
- $\omega_2$: centro $(0, r_2) = (0, 6\sqrt{2})$, radio $6\sqrt{2}$.
  - $t = 0$, así que $T = (0, 0)$.
  - De $t\cos\theta + r_2\sin\theta = 0$: $0 + r_2\sin\theta = 0$, así que $\sin\theta = 0$, $\theta = 0$. El diámetro de $\omega_2$ es horizontal (paralelo al de $\omega_3$).
  - El diámetro de $\omega_2$ está en $y = r_2 = 6\sqrt{2}$, con extremos $(\pm r_2, r_2) = (\pm 6\sqrt{2}, 6\sqrt{2})$.
  - Verificar que están sobre $\omega_3$: $(6\sqrt{2})^2 + (6\sqrt{2})^2 = 72 + 72 = 144$. ✓
  - El arco de $\omega_2$ es el semicírculo inferior tocando el eje $x$ en $(0, 0)$. ✓

- $\omega_1$: centro $(t, y_1) = (0, y_1)$, radio $3$.
  - De la Condición 2: $(y_1 - r_2)^2 = r_2^2 - 9 = 72 - 9 = 63$. Así que $y_1 - r_2 = \pm 3\sqrt{7}$.
  - Como $\omega_1$ está dentro de $\omega_2$ (semicírculo inferior), el centro de $\omega_1$ está debajo del centro de $\omega_2$: $y_1 = r_2 - 3\sqrt{7} = 6\sqrt{2} - 3\sqrt{7}$.
  - El diámetro de $\omega_1$ está en $y = y_1 = 6\sqrt{2} - 3\sqrt{7} \approx 8.49 - 7.94 = 0.55$, con extremos $(\pm 3, y_1)$.
  - Verificar que están sobre $\omega_2$: $(3)^2 + (y_1 - r_2)^2 = 9 + 63 = 72 = r_2^2$. ✓
  - El arco de $\omega_1$ es el semicírculo superior, tangente al diámetro de $\omega_2$ (línea horizontal $y = r_2 = 6\sqrt{2}$) en $(0, r_2)$.
  - El punto más alto de $\omega_1$ está en $(0, y_1 + 3) = (0, 6\sqrt{2} - 3\sqrt{7} + 3)$.
  
  ¡Espera! Para tangencia con el diámetro de $\omega_2$, necesitamos que el punto más alto del arco de $\omega_1$ esté en $y = r_2 = 6\sqrt{2}$:
  $$y_1 + 3 = 6\sqrt{2}$$
  $$y_1 = 6\sqrt{2} - 3$$

  Pero antes calculé $y_1 = 6\sqrt{2} - 3\sqrt{7}$. Estos no son iguales: $3 \neq 3\sqrt{7}$.

  ¡Hay una contradicción! Esto significa que mi derivación aún tiene un error.

Hmm, déjame reconsiderar. 

El problema es que usé dos condiciones diferentes: 
1. La distancia del centro $(t, y_1)$ al diámetro de $\omega_2$ es 3 (para tangencia).
2. El punto más alto del arco de $\omega_1$ está en el diámetro de $\omega_2$.

Estas condiciones son equivalentes solo si la perpendicular desde el centro al diámetro pasa por el punto más alto, lo cual ocurre solo cuando el diámetro de $\omega_2$ es horizontal.

Cuando $\theta = 0$ (diámetro de $\omega_2$ horizontal), las condiciones son consistentes:
- Tangencia: $|y_1 - r_2| = 3$
- Cuerda: $(y_1 - r_2)^2 + 9 = r_2^2$, así que $(y_1 - r_2)^2 = r_2^2 - 9$
- Combinando: $(y_1 - r_2)^2 = 9$, así que $r_2^2 - 9 = 9$, $r_2^2 = 18$, $r_2 = 3\sqrt{2}$.

Esto es lo que obtuve en el paso 12. Pero luego en el paso 15 obtuve $r_2 = 6\sqrt{2}$, lo que requeriría $\theta \neq 0$ con la condición de tangencia correcta.

El problema es que en el paso 15, usé la condición de "distancia = 3" para tangencia, pero con $\theta$ general. Luego resultó que $t = 0$ y $\theta = 0$, lo que llevó a la contradicción porque $\theta = 0$ implica $r_2 = 3\sqrt{2}$ (por las condiciones de $\omega_1$ en $\omega_2$), pero $t = 0$ y la relación de $\omega_2$ en $\omega_3$ implican $r_2 = R/\sqrt{2} = 6\sqrt{2}$.

Así que algo no es consistente. Déjame revisar la relación $t^2 + 2r_2^2 = R^2$.

Repasemos la derivación. Para un semicírculo de radio $r$ inscrito en un semicírculo de radio $R$:

El centro del menor está a distancia $r$ del diámetro del mayor (medida perpendicular al diámetro del mayor), en el punto de tangencia $T$. En coordenadas con el diámetro del mayor en el eje $x$ y el centro en el origen: $T = (t, 0)$, centro del menor en $(t, r)$.

El diámetro del menor es una cuerda del mayor, con punto medio $(t, r)$ y longitud $2r$, con ángulo $\theta$ respecto a la horizontal. Los extremos: $(t \pm r\cos\theta, r \pm r\sin\theta)$.

Ambos extremos sobre el círculo mayor $x^2 + y^2 = R^2$:
$$(t + r\cos\theta)^2 + (r + r\sin\theta)^2 = R^2$$
$$(t - r\cos\theta)^2 + (r - r\sin\theta)^2 = R^2$$

Restando:
$$4tr\cos\theta + 4r^2\sin\theta = 0$$
$$t\cos\theta + r\sin\theta = 0 \quad (*)$$

Sumando:
$$t^2 + r^2\cos^2\theta + r^2 + r^2\sin^2\theta = R^2$$
$$t^2 + 2r^2 = R^2 \quad (**)$$

Hmm, pero espera. La condición (*) dice que la cuerda (diámetro del menor) es perpendicular al radio del mayor en su punto medio. El punto medio de la cuerda es $(t, r)$. El radio del mayor a este punto tiene pendiente $r/t$. La cuerda tiene pendiente $\tan\theta$. Para perpendicularidad: $\tan\theta \cdot (r/t) = -1$, es decir, $t \tan\theta = -r$, es decir, $t\cos\theta + r\sin\theta = 0$ multiplicado por algo. Esto es correcto: en un círculo, el radio al punto medio de una cuerda es perpendicular a la cuerda.

Así que las relaciones (*) y (**) son correctas para un semicírculo inscrito en otro.

Ahora, para $\omega_2$ en $\omega_3$: $R = 12$, $r = r_2$, $t = t$ (coordenada x del punto de tangencia).
$$t^2 + 2r_2^2 = 144$$

Para $\omega_1$ en $\omega_2$: Necesito expresar esto en el marco de $\omega_2$.

El semicírculo $\omega_2$ tiene diámetro como cuerda de $\omega_3$ con ángulo $\theta$ (donde $t\cos\theta + r_2\sin\theta = 0$). En el marco de $\omega_2$, su diámetro es la "base", y el semicírculo es inferior.

El diámetro de $\omega_1$ es paralelo al diámetro de $\omega_3$ (eje $x$). En el marco de $\omega_2$, el diámetro de $\omega_3$ forma un ángulo $-\theta$ con el diámetro de $\omega_2$.

El punto de tangencia de $\omega_1$ con el diámetro de $\omega_2$ está a distancia $s$ del punto medio del diámetro de $\omega_2$, medida a lo largo del diámetro de $\omega_2$.

En el marco de $\omega_2$, aplicando la relación (**) (con $R = r_2$, $r = r_1 = 3$, $t$ reemplazado por $s$ donde $s$ es la distancia desde el punto de tangencia al centro del semicírculo mayor $\omega_2$, medida a lo largo del diámetro de $\omega_2$... espera, necesito ser cuidadoso con la definición de $t$).

En la derivación, $t$ es la coordenada del punto de tangencia a lo largo del diámetro del semicírculo mayor (desde el centro), y la perpendicular desde el centro del menor al diámetro del mayor tiene longitud $r$ (el radio del menor).

En el marco de $\omega_2$: el diámetro de $\omega_2$ es la base horizontal, el centro de $\omega_2$ está en el origen del marco de $\omega_2$, el semicírculo $\omega_2$ es inferior.

El centro de $\omega_1$ está en $(s, -r_1) = (s, -3)$ en el marco de $\omega_2$ (donde $s$ es la coordenada a lo largo del diámetro de $\omega_2$).

Aplicando la relación (**) con $R = r_2$, $r = r_1 = 3$:
$$s^2 + 2(3)^2 = r_2^2$$
$$s^2 + 18 = r_2^2$$

También, la condición (*) en el marco de $\omega_2$: si el diámetro de $\omega_1$ tiene ángulo $\phi$ respecto al diámetro de $\omega_2$, entonces:
$$s\cos\phi + r_1\sin\phi = 0$$
$$\tan\phi = -s/r_1 = -s/3$$

Ahora, el diámetro de $\omega_1$ es paralelo al diámetro de $\omega_3$. El diámetro de $\omega_3$ (eje $x$) forma un ángulo $-\theta$ con el diámetro de $\omega_2$ (cuerda en ángulo $\theta$). Así que:
$$\phi = -\theta$$

Por tanto:
$$\tan\phi = \tan(-\theta) = -\tan\theta$$

Usando $\tan\theta = -t/r_2$ (de la condición (*) para $\omega_2$ en $\omega_3$):
$$\tan\phi = -\tan\theta = -(-t/r_2) = t/r_2$$

Pero $\tan\phi = -s/3$, así que:
$$-s/3 = t/r_2$$
$$s = -3t/r_2$$

## 19. Resolver el sistema

Tenemos:
1. $t^2 + 2r_2^2 = 144$ (de $\omega_2$ en $\omega_3$)
2. $s^2 + 18 = r_2^2$ (de $\omega_1$ en $\omega_2$)
3. $s = -3t/r_2$ (paralelismo de diámetros de $\omega_1$ y $\omega_3$)

Sustituyendo (3) en (2):
$$(9t^2/r_2^2) + 18 = r_2^2$$
$$9t^2 + 18r_2^2 = r_2^4$$
$$t^2 = (r_2^4 - 18r_2^2)/9 = r_2^2(r_2^2 - 18)/9$$

Sustituyendo en (1):
$$r_2^2(r_2^2 - 18)/9 + 2r_2^2 = 144$$
$$r_2^2(r_2^2 - 18) + 18r_2^2 = 1296$$
$$r_2^4 - 18r_2^2 + 18r_2^2 = 1296$$
$$r_2^4 = 1296$$
$$r_2^2 = 36$$
$$r_2 = 6$$

¡Excelente! Entonces $r_2 = 6$.

Ahora:
$$t^2 = 144 - 2r_2^2 = 144 - 72 = 72$$
$$|t| = 6\sqrt{2}$$

Y:
$$s = -3t/r_2 = -3(\pm 6\sqrt{2})/6 = \mp 3\sqrt{2}$$

$$s^2 + 18 = 18 + 18 = 36 = r_2^2. \checkmark$$

## 20. Calcular $PT \cdot TQ$

$$T = (t, 0) = (\pm 6\sqrt{2}, 0)$$

$$PT \cdot TQ = |t + 12| \cdot |12 - t| = (12 + t)(12 - t) = 144 - t^2$$

(con $t$ positivo; con $t$ negativo, $PT = 12 - |t|$ y $TQ = 12 + |t|$, lo que da el mismo producto $144 - t^2$)

$$PT \cdot TQ = 144 - 72 = 72$$

## 21. Verificación de la configuración completa

Verifiquemos todo:

**$\omega_3$:** centro $(0,0)$, radio $12$, semicírculo superior, diámetro $[-12, 12]$ en el eje $x$.

**$\omega_2$:** radio $r_2 = 6$, centro en $(t, r_2) = (6\sqrt{2}, 6)$, semicírculo inferior.

- Punto de tangencia: $T = (6\sqrt{2}, 0)$. 

  La distancia desde el centro $(6\sqrt{2}, 6)$ al eje $x$ es 6, que es el radio. ✓

- Diámetro de $\omega_2$: cuerda de $\omega_3$ con punto medio $(6\sqrt{2}, 6)$ y longitud 12.

  De la condición (*): $t\cos\theta + r_2\sin\theta = 0$, así que $6\sqrt{2}\cos\theta + 6\sin\theta = 0$, $\tan\theta = -\sqrt{2}$.

  La cuerda tiene pendiente $-\sqrt{2}$ y pasa por $(6\sqrt{2}, 6)$. Extremos: $(6\sqrt{2} \pm 6\cos\theta, 6 \pm 6\sin\theta)$.

  $\cos\theta = 1/\sqrt{1 + 2} = 1/\sqrt{3}$, $\sin\theta = -\sqrt{2}/\sqrt{3}$.

  Extremos: $(6\sqrt{2} \pm 2\sqrt{3}, 6 \mp 2\sqrt{6})$.

  Verificar que están sobre $x^2 + y^2 = 144$:

  Extremo 1: $x = 6\sqrt{2} + 2\sqrt{3}$, $y = 6 - 2\sqrt{6}$
  $$x^2 = 72 + 24\sqrt{6} + 12 = 84 + 24\sqrt{6}$$
  $$y^2 = 36 - 24\sqrt{6} + 24 = 60 - 24\sqrt{6}$$
  $$x^2 + y^2 = 144. \checkmark$$

  Extremo 2: $x = 6\sqrt{2} - 2\sqrt{3}$, $y = 6 + 2\sqrt{6}$
  $$x^2 = 72 - 24\sqrt{6} + 12 = 84 - 24\sqrt{6}$$
  $$y^2 = 36 + 24\sqrt{6} + 24 = 60 + 24\sqrt{6}$$
  $$x^2 + y^2 = 144. \checkmark$$

**$\omega_1$:** radio $r_1 = 3$, centro en el marco de $\omega_2$ en $(s, -3) = (-3\sqrt{2}, -3)$.

En coordenadas globales, el centro de $\omega_1$ es el centro de $\omega_2$ más $(s\cos\theta - (-3)\sin\theta, s\sin\theta + (-3)\cos\theta)$... espera, necesito calcular esto cuidadosamente.

El marco de $\omega_2$ tiene su origen en el centro $(6\sqrt{2}, 6)$, su eje $x$ a lo largo del diámetro de $\omega_2$ (con vector unitario $(\cos\theta, \sin\theta)$), y su eje $y$ perpendicular en dirección al interior del semicírculo inferior.

El interior del semicírculo $\omega_2$ está "abajo". El diámetro de $\omega_2$ es la cuerda con vector unitario $(\cos\theta, \sin\theta)$. El vector perpendicular apuntando al interior (hacia abajo, hacia $T$) es $(\sin\theta, -\cos\theta)$ o $(-\sin\theta, \cos\theta)$.

El punto de tangencia $T = (6\sqrt{2}, 0)$ está debajo del centro. El vector desde el centro $(6\sqrt{2}, 6)$ a $T$ es $(0, -6)$, que tiene longitud 6 = $r_2$.

En el marco de $\omega_2$, $T$ está en $(0, -6)$ (directamente debajo del centro, a lo largo del eje perpendicular). Y el vector unitario del eje perpendicular hacia el interior es $(0, -1)$ en coordenadas locales.

En coordenadas globales, este vector local $(0, -1)$ debe ser $(0, -6)/6 = (0, -1)$. Así que la perpendicular local apunta directamente hacia abajo en coordenadas globales. Esto significa que el vector local $(\cos\theta, \sin\theta)$ a lo largo del diámetro tiene que ser tal que $(\sin\theta, -\cos\theta) = (0, -1)$ o $(-\sin\theta, \cos\theta) = (0, -1)$.

De $(\sin\theta, -\cos\theta) = (0, -1)$: $\sin\theta = 0$, $\cos\theta = 1$. Pero eso da $\theta = 0$, no $\tan\theta = -\sqrt{2}$. Contradicción.

De $(-\sin\theta, \cos\theta) = (0, -1)$: $\sin\theta = 0$, $\cos\theta = -1$. También $\theta = \pi$, no $\tan\theta = -\sqrt{2}$. Contradicción.

Hmm, hay un problema. El vector desde el centro de $\omega_2$ a $T$ es $(0, -6)$, pero en un semicírculo inferior, el arco toca el diámetro del mayor en un punto que no necesariamente está directamente debajo del centro del semicírculo menor.

Espera, $T$ es el punto de tangencia del arco de $\omega_2$ con $PQ$. El arco de $\omega_2$ es tangente a $PQ$ en $T$. La tangente al arco en $T$ es horizontal (paralela a $PQ$), así que el radio desde el centro de $\omega_2$ a $T$ es vertical. Por tanto, $T$ está directamente debajo del centro de $\omega_2$. Esto es correcto: centro en $(t, r_2)$, $T$ en $(t, 0)$.

Ahora, el diámetro de $\omega_2$ es una cuerda de $\omega_3$, perpendicular al radio desde el centro de $\omega_3$ hasta el punto medio de la cuerda. El punto medio de la cuerda es $(t, r_2)$. El radio desde $(0,0)$ a $(t, r_2)$ tiene pendiente $r_2/t$. La cuerda tiene pendiente $\tan\theta = -t/r_2$ (perpendicular).

En el marco de $\omega_2$, su diámetro es la cuerda (línea con pendiente $\tan\theta$). El interior del semicírculo inferior está en el lado del diámetro opuesto a $T$... no, $T$ está sobre el arco, no sobre el diámetro. El semicírculo inferior incluye el arco que pasa por $T$ y todo el interior entre el arco y el diámetro.

El diámetro de $\omega_2$ es la cuerda con punto medio $(t, r_2)$. El arco de $\omega_2$ es el semicírculo inferior, que pasa por $T = (t, 0)$.

El vector desde el centro $(t, r_2)$ al punto de tangencia $T = (t, 0)$ es $(0, -r_2) = (0, -6)$, de longitud 6 (el radio). Este es un radio del semicírculo inferior, perpendicular a la tangente horizontal.

El diámetro de $\omega_2$ es perpendicular a este radio. Así que el diámetro es horizontal... ¡pero eso contradice $\tan\theta = -\sqrt{2}$!

¡Espera! Hay un error fundamental. He asumido que el diámetro de $\omega_2$ es perpendicular al radio desde el centro de $\omega_3$ hasta el punto medio de la cuerda. Pero en realidad, el diámetro de $\omega_2$ es una cuerda de $\omega_3$, y en un círculo, el radio perpendicular a una cuerda biseca la cuerda. Así que el radio desde $(0,0)$ hasta el punto medio de la cuerda es perpendicular a la cuerda. Esto es correcto.

Pero también, el diámetro de $\omega_2$ es perpendicular al radio desde el centro de $\omega_2$ hasta el punto de tangencia de su arco... no, eso no es correcto. El diámetro de $\omega_2$ es el segmento entre los extremos del semicírculo. El radio desde el centro de $\omega_2$ al punto de tangencia $T$ es perpendicular a la tangente en $T$. La tangente es $PQ$ (horizontal), así que este radio es vertical (apuntando hacia abajo o hacia arriba).

El diámetro de $\omega_2$ no tiene por qué ser perpendicular a este radio en particular. De hecho, el diámetro es simplemente el segmento entre los dos extremos, y es perpendicular al radio desde el centro al punto medio del diámetro (que pasa por el centro $(t, r_2)$).

Espera, el centro de $\omega_2$ es $(t, r_2)$, y el radio al punto $T$ es $(0, -r_2)$ (vertical). El diámetro de $\omega_2$ es una línea a través de $(t, r_2)$ (el centro), que es perpendicular al radio desde el centro al punto medio... pero el punto medio del diámetro es el propio centro $(t, r_2)$.

¡Creo que el problema es que estoy confundiendo dos cosas! Déjame aclarar.

El diámetro de $\omega_2$ es un segmento entre dos puntos $A$ y $B$ sobre el arco de $\omega_3$. El punto medio de este segmento es el centro del círculo $\omega_2$ (ya que el diámetro de $\omega_2$ pasa por su centro). Y el círculo $\omega_2$ tiene radio $r_2$ con centro en el punto medio de su diámetro.

El semicírculo $\omega_2$ es la mitad del círculo $\omega_2$ en un lado del diámetro. El arco es la mitad inferior, que contiene $T$.

El radio desde el centro de $\omega_2$ a $T$ es perpendicular a la tangente en $T$. La tangente es $PQ$ (horizontal), así que el radio es vertical: de $(t, r_2)$ a $(t, 0)$. Esto es correcto.

Ahora, el centro de $\omega_3$ es $(0, 0)$. El diámetro de $\omega_2$ es el segmento $AB$ donde $A, B$ están sobre el círculo de $\omega_3$. El punto medio de $AB$ es el centro de $\omega_2$ en $(t, r_2)$.

En un círculo, el radio desde el centro hasta el punto medio de una cuerda es perpendicular a la cuerda. Así que el segmento desde $(0,0)$ a $(t, r_2)$ es perpendicular al diámetro de $\omega_2$. 

Pero también, el segmento desde $(t, r_2)$ a $(t, 0)$ es perpendicular a $PQ$, no al diámetro de $\omega_2$. El diámetro de $\omega_2$ no es perpendicular al radio $(t, r_2) \to (t, 0)$.

Así que no hay contradicción: el diámetro de $\omega_2$ es perpendicular al radio del círculo $\omega_3$ en el punto medio del diámetro, no al radio del círculo $\omega_2$ en $T$.

El diámetro de $\omega_2$ (cuerda) es perpendicular al radio de $\omega_3$ que va de $(0,0)$ a $(t, r_2)$. La pendiente del radio de $\omega_3$ es $r_2/t = 6/(6\sqrt{2}) = 1/\sqrt{2}$. La pendiente de la cuerda sería $-t/r_2 = -6\sqrt{2}/6 = -\sqrt{2}$. Estas son perpendiculares: $(1/\sqrt{2})(-\sqrt{2}) = -1$. ✓

El radio de $\omega_2$ a $T$ es vertical (pendiente infinita). Su ángulo con la cuerda (pendiente $-\sqrt{2}$) es $\arctan(\sqrt{2}) \neq 90°$. Así que la cuerda y el radio vertical no son perpendiculares. ✓ Esto es consistente: la cuerda necesita ser perpendicular al radio del CÍRCULO MAYOR en su punto medio, no al radio del círculo menor.

Todo es consistente. Mi error fue pensar que el diámetro de $\omega_2$ debe ser perpendicular al radio de $\omega_2$ en $T$, lo cual no es cierto.

## 22. Verificar la tangencia de $\omega_1$ con el diámetro de $\omega_2$

El centro de $\omega_1$ en el marco de $\omega_2$ está en $(s, -3) = (-3\sqrt{2}, -3)$, donde el marco de $\omega_2$ tiene:
- Origen: centro de $\omega_2$ en $(6\sqrt{2}, 6)$
- Eje $x$ local: a lo largo del diámetro de $\omega_2$, vector unitario $(\cos\theta, \sin\theta) = (1/\sqrt{3}, -\sqrt{2}/\sqrt{3})$
- Eje $y$ local: perpendicular hacia el interior (hacia $T$), vector unitario $(\sin\theta, -\cos\theta)$ o $(-\sin\theta, \cos\theta)$

¿Cuál es el eje $y$ correcto? El vector desde el centro $(6\sqrt{2}, 6)$ a $T = (6\sqrt{2}, 0)$ es $(0, -6)$. En el marco local, $T$ debe estar en $(0, -6)$ (o $(0, -r_2)$). Así que el eje $y$ local apunta en la dirección $(0, -1)$.

El vector local $(0, -1)$ debe corresponder al vector global $(0, -1)$. Esto significa que el eje $y$ local es $(0, -1)$ (directamente hacia abajo).

El eje $x$ local es perpendicular al eje $y$ local, así que es $(\pm 1, 0)$ (horizontal). Pero espera, el diámetro de $\omega_2$ tiene pendiente $-\sqrt{2}$, no es horizontal. 

¡Contradicción de nuevo! Si el eje $y$ local (perpendicular al diámetro, hacia el interior) es $(0, -1)$ (hacia abajo), entonces el diámetro (eje $x$ local) sería horizontal, pero sabemos que tiene pendiente $-\sqrt{2}$.

Hmm, parece que hay un problema con mi comprensión del marco local. Déjame aclarar.

En el marco local de $\omega_2$:
- El eje $x$ local es a lo largo del diámetro de $\omega_2$.
- El eje $y$ local es perpendicular al diámetro, hacia el interior (hacia el arco, donde está $T$).

El diámetro de $\omega_2$ tiene vector unitario $(\cos\theta, \sin\theta)$, donde $\theta$ satisface $\tan\theta = -\sqrt{2}$. El vector perpendicular apuntando "hacia abajo" (hacia $T$) es el que tiene componente $y$ negativa.

El vector desde el centro $(6\sqrt{2}, 6)$ a $T = (6\sqrt{2}, 0)$ es $(0, -6)$. Este vector NO es perpendicular al diámetro (que tiene pendiente $-\sqrt{2}$). Espera, ¿es eso correcto?

El punto $T$ está sobre el arco de $\omega_2$, no sobre el diámetro. El radio desde el centro de $\omega_2$ a $T$ NO tiene que ser perpendicular al diámetro. De hecho, el radio al "punto más bajo" del semicírculo es perpendicular al diámetro solo si el diámetro es horizontal.

En un semicírculo con diámetro en ángulo $\theta$, el "punto más bajo" a lo largo de la perpendicular es donde la perpendicular al diámetro intersecta el arco. El radio a este punto es perpendicular al diámetro. Pero $T$ es el punto de tangencia con $PQ$ (el diámetro de $\omega_3$, que es horizontal). $T$ no es necesariamente el punto más bajo del semicírculo $\omega_2$; es el punto donde la tangente es horizontal.

La tangente a un círculo en un punto es perpendicular al radio en ese punto. Si la tangente en $T$ es horizontal (paralela a $PQ$), entonces el radio $CT$ es vertical. Esto es correcto: $C = (6\sqrt{2}, 6)$ y $T = (6\sqrt{2}, 0)$, radio vertical.

El diámetro de $\omega_2$ (cuerda) NO pasa por $T$; pasa por $C$ con pendiente $-\sqrt{2}$. El punto $T$ está sobre el arco, no sobre el diámetro.

El semiplano interior del semicírculo $\omega_2$ es el lado del diámetro que contiene $T$.

Ahora, el centro de $\omega_1$ está en $(s, -3)$ en el marco local, lo que significa:
- Componente $s$ a lo largo del diámetro: $s(\cos\theta, \sin\theta) = -3\sqrt{2}(1/\sqrt{3}, -\sqrt{2}/\sqrt{3}) = (-3\sqrt{6}/3, 6/\sqrt{3})$... espera, déjame calcular.

$\cos\theta = 1/\sqrt{3}$, $\sin\theta = -\sqrt{2/3} = -\sqrt{2}/\sqrt{3}$

$s\cos\theta = -3\sqrt{2} \cdot 1/\sqrt{3} = -3\sqrt{2/3}$
$s\sin\theta = -3\sqrt{2} \cdot (-\sqrt{2}/\sqrt{3}) = 6/\sqrt{3} = 2\sqrt{3}$

- Componente $-3$ a lo largo de la perpendicular hacia el interior: necesitamos el vector unitario perpendicular al diámetro apuntando hacia $T$.

El vector $CT = T - C = (0, -6) = (0, -r_2)$. La perpendicular al diámetro apuntando hacia $T$ es... necesitamos encontrar el vector unitario perpendicular al diámetro que tenga producto escalar positivo con $CT$.

El diámetro tiene dirección $(\cos\theta, \sin\theta) = (1/\sqrt{3}, -\sqrt{2}/\sqrt{3})$.

Los vectores perpendiculares son $(\sin\theta, -\cos\theta)$ y $(-\sin\theta, \cos\theta)$:
$(\sin\theta, -\cos\theta) = (-\sqrt{2}/\sqrt{3}, -1/\sqrt{3})$
$(-\sin\theta, \cos\theta) = (\sqrt{2}/\sqrt{3}, 1/\sqrt{3})$

¿Cuál apunta hacia $T$? $CT = (0, -6)$. El producto escalar con $(-\sqrt{2}/\sqrt{3}, -1/\sqrt{3})$ es $6/\sqrt{3} > 0$. Así que la perpendicular hacia $T$ es $(-\sqrt{2}/\sqrt{3}, -1/\sqrt{3})$.

Así que el centro de $\omega_1$ en coordenadas globales es:
$$C_1 = C + s(\cos\theta, \sin\theta) - 3(-\sqrt{2}/\sqrt{3}, -1/\sqrt{3})$$
$$= (6\sqrt{2}, 6) + (-3\sqrt{2/3}, 2\sqrt{3}) + (3\sqrt{2}/\sqrt{3}, 3/\sqrt{3})$$
$$= (6\sqrt{2} - 3\sqrt{2/3} + 3\sqrt{2}/\sqrt{3}, 6 + 2\sqrt{3} + 3/\sqrt{3})$$
$$= (6\sqrt{2} - 3\sqrt{2/3} + \sqrt{6}, 6 + 2\sqrt{3} + \sqrt{3})$$

$3\sqrt{2/3} = 3\sqrt{2}/\sqrt{3} = \sqrt{6}$, y $3/\sqrt{3} = \sqrt{3}$

$$C_1 = (6\sqrt{2} - \sqrt{6} + \sqrt{6}, 6 + 2\sqrt{3} + \sqrt{3}) = (6\sqrt{2}, 6 + 3\sqrt{3})$$

Hmm, el centro de $\omega_1$ está en $(6\sqrt{2}, 6 + 3\sqrt{3}) \approx (8.49, 11.20)$.

El diámetro de $\omega_1$ es horizontal (paralelo a $PQ$), con extremos en $(6\sqrt{2} \pm 3, 6 + 3\sqrt{3})$.

Verifiquemos que estos extremos están sobre el círculo de $\omega_2$ (círculo centrado en $(6\sqrt{2}, 6)$ con radio 6):
$$(6\sqrt{2} \pm 3 - 6\sqrt{2})^2 + (6 + 3\sqrt{3} - 6)^2 = 9 + 27 = 36 = 6^2. \checkmark$$

Verifiquemos que el arco de $\omega_1$ es tangente al diámetro de $\omega_2$:

El diámetro de $\omega_2$ es la línea con pendiente $-\sqrt{2}$ a través de $(6\sqrt{2}, 6)$.

El centro de $\omega_1$ está en $(6\sqrt{2}, 6 + 3\sqrt{3})$. La distancia desde este punto al diámetro de $\omega_2$ debe ser 3 (el radio de $\omega_1$).

La línea del diámetro de $\omega_2$: $y - 6 = -\sqrt{2}(x - 6\sqrt{2})$, es decir, $\sqrt{2}x + y - 6\sqrt{2}\cdot\sqrt{2} - 6 = 0$, es decir, $\sqrt{2}x + y - 12 - 6 = 0$, es decir, $\sqrt{2}x + y - 18 = 0$.

Distancia desde $(6\sqrt{2}, 6 + 3\sqrt{3})$:
$$d = \frac{|\sqrt{2} \cdot 6\sqrt{2} + (6 + 3\sqrt{3}) - 18|}{\sqrt{2 + 1}} = \frac{|12 + 6 + 3\sqrt{3} - 18|}{\sqrt{3}} = \frac{|3\sqrt{3}|}{\sqrt{3}} = 3. \checkmark$$

¡La tangencia se verifica!

Además, el diámetro de $\omega_1$ es horizontal (paralelo al de $\omega_3$). ✓

Y los extremos del diámetro de $\omega_1$ están sobre el arco de $\omega_2$ (círculo de $\omega_2$): calculado arriba, $9 + 27 = 36 = r_2^2$. ✓

Pero espera, ¿están esos extremos sobre el arco (el semicírculo inferior) o sobre la parte no-arco del círculo? El semicírculo inferior $\omega_2$ incluye los puntos del círculo con $y \leq 6$ (debajo del diámetro) y también los del arco... En realidad, el semicírculo inferior incluye el diámetro (la cuerda) y el arco inferior.

El diámetro de $\omega_2$ está en la línea $\sqrt{2}x + y - 18 = 0$, y el interior es el lado que contiene $T = (6\sqrt{2}, 0)$: $\sqrt{2}\cdot 6\sqrt{2} + 0 - 18 = 12 - 18 = -6 < 0$. Así que el interior es $\sqrt{2}x + y - 18 < 0$.

Los extremos del diámetro de $\omega_1$: en $(6\sqrt{2} + 3, 6 + 3\sqrt{3})$ y $(6\sqrt{2} - 3, 6 + 3\sqrt{3})$.

Evaluemos $\sqrt{2}x + y - 18$ para $(6\sqrt{2} + 3, 6 + 3\sqrt{3})$:
$$\sqrt{2}(6\sqrt{2} + 3) + 6 + 3\sqrt{3} - 18 = 12 + 3\sqrt{2} + 6 + 3\sqrt{3} - 18 = 3\sqrt{2} + 3\sqrt{3} > 0$$

¡Esto es positivo! Lo que significa que los extremos están en el lado exterior, no en el interior.

Hmm, esto sugiere que el diámetro de $\omega_1$ no está dentro del semicírculo $\omega_2$, sino fuera de él (en el lado equivocado).

Esto significa que hay un error en mi elección del signo. Déjame reconsiderar.

El semicírculo $\omega_2$ es el semicírculo inferior, con el arco por debajo del diámetro. El diámetro de $\omega_2$ separa el círculo en dos mitades: la mitad inferior (el arco que contiene a $T$) y la mitad superior.

El diámetro de $\omega_1$ debe estar en la mitad inferior (la que contiene a $T$), ya que $\omega_1$ está inscrito en $\omega_2$.

Pero calculé que el centro de $\omega_1$ está en $(6\sqrt{2}, 6 + 3\sqrt{3})$, que está por ENCIMA del centro de $\omega_2$ (en $y = 6$). Esto significa que $\omega_1$ está en el lado equivocado.

El problema es el signo del desplazamiento perpendicular. Debería ser +3 (no -3), o el signo de $s$ está mal.

Déjame reconsiderar. En el marco local, el centro de $\omega_1$ está en $(s, \pm 3)$, donde el segundo componente es perpendicular al diámetro, hacia el interior.

En mi derivación de la relación $s^2 + 2r_1^2 = r_2^2$, usé $s^2 + 2(3)^2 = r_2^2$, que viene de la condición de que los extremos del diámetro del menor estén sobre el mayor. Esta relación no depende del signo.

El centro de $\omega_1$ debe estar a distancia 3 del diámetro de $\omega_2$, en el lado interior (hacia $T$). El lado interior es donde está $T$: $\sqrt{2}x + y - 18 < 0$.

El centro de $\omega_1$ en $(6\sqrt{2}, 6 + 3\sqrt{3})$ tiene $\sqrt{2} \cdot 6\sqrt{2} + 6 + 3\sqrt{3} - 18 = 3\sqrt{3} > 0$, que está en el lado exterior.

El punto opuesto sería $(6\sqrt{2}, 6 - 3\sqrt{3})$, con $\sqrt{2}\cdot 6\sqrt{2} + 6 - 3\sqrt{3} - 18 = -3\sqrt{3} < 0$, en el lado interior. ✓

Así que el centro correcto de $\omega_1$ está en $(6\sqrt{2}, 6 - 3\sqrt{3})$.

Esto significa que en el marco local, el desplazamiento perpendicular es $-3$ (hacia el interior), pero mi cálculo anterior tenía un error de signo.

Recalculemos. El vector perpendicular hacia el interior es $(\sin\theta, -\cos\theta)$ o $(-\sin\theta, \cos\theta)$:

Con $\sin\theta = -\sqrt{2}/\sqrt{3}$ y $\cos\theta = 1/\sqrt{3}$:

Opción 1: $(\sin\theta, -\cos\theta) = (-\sqrt{2}/\sqrt{3}, -1/\sqrt{3})$ — componente $y$ negativa, apunta hacia abajo
Opción 2: $(-\sin\theta, \cos\theta) = (\sqrt{2}/\sqrt{3}, 1/\sqrt{3})$ — componente $y$ positiva, apunta hacia arriba

El interior contiene $T = (6\sqrt{2}, 0)$, que tiene $y < 6$. El vector hacia $T$ desde $C$ es $(0, -6)$, que tiene componente $y$ negativa. Así que el interior está "abajo", y el vector perpendicular hacia el interior es el de componente $y$ negativa: Opción 1.

Así que el centro de $\omega_1$ es:
$$C_1 = C + s(\cos\theta, \sin\theta) + (-3)(\sin\theta, -\cos\theta)$$

Donde el término $-3(\sin\theta, -\cos\theta)$ es el desplazamiento de 3 unidades en la dirección perpendicular hacia el interior.

$s = -3\sqrt{2}$ (de antes).

$s(\cos\theta, \sin\theta) = -3\sqrt{2}(1/\sqrt{3}, -\sqrt{2}/\sqrt{3}) = (-3\sqrt{2/3}, 6/\sqrt{3}) = (-\sqrt{6}, 2\sqrt{3})$

$-3(\sin\theta, -\cos\theta) = -3(-\sqrt{2}/\sqrt{3}, -1/\sqrt{3}) = (3\sqrt{2}/\sqrt{3}, 3/\sqrt{3}) = (\sqrt{6}, \sqrt{3})$

Sumando:
$$C_1 = (6\sqrt{2}, 6) + (-\sqrt{6}, 2\sqrt{3}) + (\sqrt{6}, \sqrt{3}) = (6\sqrt{2}, 6 + 3\sqrt{3})$$

Hmm, aún obtengo $(6\sqrt{2}, 6 + 3\sqrt{3})$. Pero vimos que este punto está en el lado exterior. 

Espera, creo que el problema es el signo de $s$. Si tomo $s = +3\sqrt{2}$ en lugar de $-3\sqrt{2}$, entonces:

$s(\cos\theta, \sin\theta) = 3\sqrt{2}(1/\sqrt{3}, -\sqrt{2}/\sqrt{3}) = (\sqrt{6}, -2\sqrt{3})$

$-3(\sin\theta, -\cos\theta) = -3(-\sqrt{2}/\sqrt{3}, -1/\sqrt{3}) = (\sqrt{6}, \sqrt{3})$

Sumando:
$$C_1 = (6\sqrt{2}, 6) + (\sqrt{6}, -2\sqrt{3}) + (\sqrt{6}, \sqrt{3}) = (6\sqrt{2} + 2\sqrt{6}, 6 - \sqrt{3})$$

Verifiquemos si este centro está en el lado interior:
$\sqrt{2}(6\sqrt{2} + 2\sqrt{6}) + (6 - \sqrt{3}) - 18 = 12 + 2\sqrt{12} + 6 - \sqrt{3} - 18 = 2\sqrt{12} - \sqrt{3} = 4\sqrt{3} - \sqrt{3} = 3\sqrt{3} > 0$. 

Todavía positivo. Hmm.

Espera, déjame verificar la ecuación del diámetro de $\omega_2$: $\sqrt{2}x + y - 18 = 0$.

El centro de $\omega_2$ es $(6\sqrt{2}, 6)$. Verifiquemos: $\sqrt{2} \cdot 6\sqrt{2} + 6 - 18 = 12 + 6 - 18 = 0$. ✓

El punto $T = (6\sqrt{2}, 0)$: $\sqrt{2}\cdot 6\sqrt{2} + 0 - 18 = 12 - 18 = -6 < 0$. ✓ Así que el interior es $\sqrt{2}x + y - 18 < 0$.

Para que el centro de $\omega_1$ esté en el interior, necesitamos $\sqrt{2}x_1 + y_1 - 18 < 0$.

En mi última expresión, $x_1 = 6\sqrt{2} + 2\sqrt{6}$, $y_1 = 6 - \sqrt{3}$:
$$\sqrt{2}x_1 + y_1 - 18 = 12 + 2\sqrt{12} + 6 - \sqrt{3} - 18 = 0 + 2\sqrt{12} - \sqrt{3} = 4\sqrt{3} - \sqrt{3} = 3\sqrt{3} > 0$$

Sigue siendo positivo. 

Déjame probar sistemáticamente las cuatro combinaciones de signos (±s, ±perpendicular):

Combinación A: $s = -3\sqrt{2}$, perpendicular $-3$ (hacia abajo):
$C_1 = (6\sqrt{2}, 6) + (-\sqrt{6}, 2\sqrt{3}) + (\sqrt{6}, \sqrt{3}) = (6\sqrt{2}, 6 + 3\sqrt{3})$
Valor: $12 + 6 + 3\sqrt{3} - 18 = 3\sqrt{3} > 0$ (exterior)

Combinación B: $s = -3\sqrt{2}$, perpendicular $+3$ (hacia arriba):
$C_1 = (6\sqrt{2}, 6) + (-\sqrt{6}, 2\sqrt{3}) + (-\sqrt{6}, -\sqrt{3}) = (6\sqrt{2} - 2\sqrt{6}, 6 + \sqrt{3})$
Valor: $12 - 2\sqrt{12} + 6 + \sqrt{3} - 18 = -4\sqrt{3} + \sqrt{3} = -3\sqrt{3} < 0$ (interior) ✓

Combinación C: $s = +3\sqrt{2}$, perpendicular $-3$:
$C_1 = (6\sqrt{2}, 6) + (\sqrt{6}, -2\sqrt{3}) + (\sqrt{6}, \sqrt{3}) = (6\sqrt{2} + 2\sqrt{6}, 6 - \sqrt{3})$
Valor: $12 + 2\sqrt{12} + 6 - \sqrt{3} - 18 = 4\sqrt{3} - \sqrt{3} = 3\sqrt{3} > 0$ (exterior)

Combinación D: $s = +3\sqrt{2}$, perpendicular $+3$ (hacia arriba):
$C_1 = (6\sqrt{2}, 6) + (\sqrt{6}, -2\sqrt{3}) + (-\sqrt{6}, -\sqrt{3}) = (6\sqrt{2}, 6 - 3\sqrt{3})$
Valor: $12 + 6 - 3\sqrt{3} - 18 = -3\sqrt{3} < 0$ (interior) ✓

Así que las combinaciones B y D ponen el centro en el interior. Verifiquemos cuál es la correcta.

Para la combinación B: $C_1 = (6\sqrt{2} - 2\sqrt{6}, 6 + \sqrt{3})$

El diámetro de $\omega_1$ es horizontal con extremos en $(6\sqrt{2} - 2\sqrt{6} \pm 3, 6 + \sqrt{3})$.

Verificar que los extremos están sobre el círculo de $\omega_2$:
$(6\sqrt{2} - 2\sqrt{6} \pm 3 - 6\sqrt{2})^2 + (6 + \sqrt{3} - 6)^2 = (-2\sqrt{6} \pm 3)^2 + 3$

Para $(-2\sqrt{6} + 3)^2 + 3 = 24 - 12\sqrt{6} + 9 + 3 = 36 - 12\sqrt{6} \neq 36$. ✗

Para $(-2\sqrt{6} - 3)^2 + 3 = 24 + 12\sqrt{6} + 9 + 3 = 36 + 12\sqrt{6} \neq 36$. ✗

Así que la combinación B NO funciona: los extremos no están sobre el círculo de $\omega_2$.

Para la combinación D: $C_1 = (6\sqrt{2}, 6 - 3\sqrt{3})$

El diámetro de $\omega_1$ tiene extremos $(6\sqrt{2} \pm 3, 6 - 3\sqrt{3})$.

Verificar:
$(6\sqrt{2} \pm 3 - 6\sqrt{2})^2 + (6 - 3\sqrt{3} - 6)^2 = 9 + 27 = 36$. ✓

Así que la combinación D es correcta: $C_1 = (6\sqrt{2}, 6 - 3\sqrt{3})$.

Esto corresponde a $s = +3\sqrt{2}$ y perpendicular hacia ARRIBA ($+3$ con la perpendicular que apunta hacia el interior, que es hacia arriba... espera, ¿hacia arriba?).

Déjame interpretar. El "interior" que encontramos es $\sqrt{2}x + y - 18 < 0$, y $T$ está en este lado. El punto $(6\sqrt{2}, 6 - 3\sqrt{3})$ tiene valor $-3\sqrt{3} < 0$, así que está en el interior. ✓

El vector desde $C = (6\sqrt{2}, 6)$ a $C_1 = (6\sqrt{2}, 6 - 3\sqrt{3})$ es $(0, -3\sqrt{3})$, que apunta hacia abajo.

La perpendicular al diámetro de $\omega_2$ que apunta hacia $T$ (hacia abajo-izquierda) es $(\sin\theta, -\cos\theta) = (-\sqrt{2}/\sqrt{3}, -1/\sqrt{3})$. El producto escalar de $(0, -3\sqrt{3})$ con $(-\sqrt{2}/\sqrt{3}, -1/\sqrt{3})$ es $3\sqrt{3}/\sqrt{3} = 3 > 0$, así que están en la misma dirección. ✓

Ahora, ¿el arco de $\omega_1$ es tangente al diámetro de $\omega_2$?

El centro de $\omega_1$ está en $(6\sqrt{2}, 6 - 3\sqrt{3})$, radio 3. El arco de $\omega_1$ debe ser tangente al diámetro de $\omega_2$.

La distancia desde $C_1$ al diámetro de $\omega_2$ debe ser 3. Verifiquemos:

$$\frac{|\sqrt{2}\cdot 6\sqrt{2} + (6 - 3\sqrt{3}) - 18|}{\sqrt{3}} = \frac{|12 + 6 - 3\sqrt{3} - 18|}{\sqrt{3}} = \frac{|-3\sqrt{3}|}{\sqrt{3}} = 3. \checkmark$$

La tangencia se verifica.

¿El diámetro de $\omega_1$ es horizontal? Sí, los extremos están en $(6\sqrt{2} \pm 3, 6 - 3\sqrt{3})$, misma altura. ✓

¿Los extremos están sobre el arco de $\omega_2$? Están sobre el círculo ($9 + 27 = 36$). ¿Están en el arco (semicírculo inferior)?

El arco de $\omega_2$ es el semicírculo inferior, que incluye todos los puntos del círculo con $\sqrt{2}x + y - 18 \leq 0$.

Para $(6\sqrt{2} + 3, 6 - 3\sqrt{3})$: $\sqrt{2}(6\sqrt{2} + 3) + 6 - 3\sqrt{3} - 18 = 12 + 3\sqrt{2} + 6 - 3\sqrt{3} - 18 = 3\sqrt{2} - 3\sqrt{3}$

$\sqrt{2} \approx 1.414$, $\sqrt{3} \approx 1.732$, así que $3(\sqrt{2} - \sqrt{3}) < 0$. ✓

Para $(6\sqrt{2} - 3, 6 - 3\sqrt{3})$: $\sqrt{2}(6\sqrt{2} - 3) + 6 - 3\sqrt{3} - 18 = 12 - 3\sqrt{2} + 6 - 3\sqrt{3} - 18 = -3\sqrt{2} - 3\sqrt{3} < 0$. ✓

Ambos extremos están sobre el arco. ✓

¿El arco de $\omega_1$ es tangente al diámetro de $\omega_2$ y está dentro de $\omega_2$?

El punto de tangencia es el punto del arco de $\omega_1$ más cercano al diámetro de $\omega_2$, que está en la perpendicular desde $C_1$ al diámetro, en el lado interior.

El diámetro de $\omega_2$ está en la línea $\sqrt{2}x + y - 18 = 0$. El punto de tangencia es $C_1$ más (o menos) 3 veces la perpendicular unitaria.

La perpendicular unitaria al diámetro apuntando desde $C_1$ hacia el diámetro: la perpendicular que va del interior al diámetro apunta en dirección opuesta a la perpendicular interior.

La normal a la línea $\sqrt{2}x + y - 18 = 0$ es $(\sqrt{2}, 1)$. El punto $C_1$ tiene valor $-3\sqrt{3}$, y el diámetro tiene valor 0. Para ir de $C_1$ al diámetro, nos movemos en la dirección de la normal: $(\sqrt{2}, 1)/\sqrt{3}$.

El punto de tangencia es $C_1 + 3(\sqrt{2}, 1)/\sqrt{3} = (6\sqrt{2} + \sqrt{6}, 6 - 3\sqrt{3} + \sqrt{3}) = (6\sqrt{2} + \sqrt{6}, 6 - 2\sqrt{3})$.

Este punto está sobre el diámetro de $\omega_2$ (verificable) y a distancia 3 de $C_1$. ✓

El arco de $\omega_1$ es el semicírculo en el lado del diámetro de $\omega_1$ opuesto... espera, el arco de $\omega_1$ es tangente al diámetro de $\omega_2$. El semicírculo $\omega_1$ tiene su diámetro horizontal (en $y = 6 - 3\sqrt{3}$) y su arco es el semicírculo superior o inferior.

Para que el arco de $\omega_1$ sea tangente al diámetro de $\omega_2$, necesitamos que el arco esté en el lado del diámetro de $\omega_1$ que está más cerca del diámetro de $\omega_2$.

El centro de $\omega_1$ está en $(6\sqrt{2}, 6 - 3\sqrt{3})$. El diámetro de $\omega_2$ pasa por $(6\sqrt{2}, 6)$, que está por ENCIMA del centro de $\omega_1$. Así que el arco de $\omega_1$ debe ser el semicírculo superior.

El punto de tangencia sería el punto más alto del semicírculo superior: $(6\sqrt{2} + 3\cos\alpha, 6 - 3\sqrt{3} + 3\sin\alpha)$ donde $\alpha$ es el ángulo de la perpendicular al diámetro. La perpendicular al diámetro de $\omega_2$ (pendiente $-\sqrt{2}$) tiene pendiente $1/\sqrt{2}$, así que el vector unitario a lo largo de la perpendicular es $\pm(1/\sqrt{1 + 1/2}, (1/\sqrt{2})/\sqrt{1 + 1/2}) = \pm(\sqrt{2/3}, 1/\sqrt{3})$.

El punto más alto del arco (en la dirección perpendicular hacia el diámetro de $\omega_2$) es:
$$C_1 + 3(\sqrt{2/3}, 1/\sqrt{3}) = (6\sqrt{2} + 3\sqrt{2/3}, 6 - 3\sqrt{3} + 3/\sqrt{3}) = (6\sqrt{2} + \sqrt{6}, 6 - 3\sqrt{3} + \sqrt{3}) = (6\sqrt{2} + \sqrt{6}, 6 - 2\sqrt{3})$$

Esto coincide con el punto de tangencia calculado. ✓

Así que el arco de $\omega_1$ (semicírculo superior) es tangente al diámetro de $\omega_2$ en $(6\sqrt{2} + \sqrt{6}, 6 - 2\sqrt{3})$. ✓

¡La configuración es completamente válida!

## 23. Calcular $PT \cdot TQ$ final

$T = (t, 0) = (6\sqrt{2}, 0)$ (o $(-6\sqrt{2}, 0)$ por simetría).

$$PT \cdot TQ = |t + 12| \cdot |12 - t|$$

Para $t = 6\sqrt{2} \approx 8.49$:
$$PT = 12 + 6\sqrt{2}$$
$$TQ = 12 - 6\sqrt{2}$$
$$PT \cdot TQ = (12 + 6\sqrt{2})(12 - 6\sqrt{2}) = 144 - 72 = 72$$

Para $t = -6\sqrt{2}$, da el mismo resultado.

## Respuesta

$$PT \cdot TQ = 72$$

\boxed{72}