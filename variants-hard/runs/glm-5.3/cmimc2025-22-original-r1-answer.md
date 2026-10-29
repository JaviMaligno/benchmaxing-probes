## Razonamiento

**Colocación de las esferas unitarias:** Coloco el cubo como $[0,4]^3$. La configuración natural es poner cada esfera de radio 1 en una esquina del cubo, tangente a las tres caras que se encuentran ahí. Así, los centros quedan en todos los puntos $(x,y,z)$ donde cada coordenada vale $1$ o $3$:

$$(1,1,1),\ (3,1,1),\ (1,3,1),\ (1,1,3),\ (3,3,1),\ (3,1,3),\ (1,3,3),\ (3,3,3)$$

**Verificación de la tangencia entre pares:** Tomo una esfera, por ejemplo la de centro $(1,1,1)$:
- Con las tres esferas "adyacentes" que difieren en una coordenada, como $(3,1,1)$: distancia entre centros $= 2 = 1+1$. ✓ Tangentes.
- Con las que difieren en dos coordenadas (diagonales de cara): distancia $= 2\sqrt{2}$; y con la opuesta por el cuerpo: $2\sqrt{3}$. No son tangentes.

Por tanto cada esfera es tangente exterior a exactamente **tres** otras. ✓

**Esfera central:** Por simetría, la esfera más grande tangente a las ocho está centrada en el centro del cubo, $(2,2,2)$.

Distancia del centro del cubo al centro de cualquier esfera unitaria:

$$d = \sqrt{(2-1)^2+(2-1)^2+(2-1)^2} = \sqrt{3}$$

**Condición de tangencia:** Si $R$ es el radio buscado:

$$R + 1 = \sqrt{3} \implies R = \sqrt{3} - 1$$

**Comprobación de que cabe en el cubo:** La distancia del centro $(2,2,2)$ a cualquier cara es $2$, y $\sqrt{3}-1 \approx 0.732 < 2$. ✓

$$\boxed{\sqrt{3}-1}$$