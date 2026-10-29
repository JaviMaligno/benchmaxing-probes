Como 2027 es primo y $z \neq 1$, $z$ es una raíz primitiva 2027-ésima de la unidad, así que $z, z^2, \dots, z^{2026}$ recorren todas las raíces no triviales, y $z^{2027} = 1$.

**Último término:** $\dfrac{1}{1+z^{2027}} = \dfrac{1}{1+1} = \dfrac{1}{2}$.

**Los otros 2026 términos, por emparejamiento:** agrupo el término $k$ con el término $2027-k$. Como $z^{2027-k} = z^{-k}$:

$$\frac{1}{1+z^k} + \frac{1}{1+z^{-k}} = \frac{1}{1+z^k} + \frac{z^k}{z^k+1} = \frac{1+z^k}{1+z^k} = 1.$$

(Los denominadores nunca se anulan: $z^k = -1$ exigiría $z^{2k} = 1$, imposible porque el orden de $z$ es 2027, impar.)

Hay $\frac{2026}{2} = 1013$ parejas, que aportan $1013$ en total.

**Suma total:**
$$1013 + \frac{1}{2} = \frac{2027}{2}.$$

$$\boxed{\dfrac{2027}{2}}$$