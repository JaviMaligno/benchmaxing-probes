Para resolver el problema paso a paso, podemos utilizar álgebra vectorial.

**Paso 1: Planteamiento vectorial**
Consideremos los puntos $P, Q, T, R$ en el plano. Sabemos que la suma de los vectores a lo largo de un camino cerrado es cero, o equivalentemente:
$$\overrightarrow{PQ} + \overrightarrow{QT} + \overrightarrow{TR} = \overrightarrow{PR}$$

Reordenando los términos para agrupar aquellos cuyos ángulos mutuos conocemos, obtenemos:
$$\overrightarrow{PQ} + \overrightarrow{TR} = \overrightarrow{PR} - \overrightarrow{QT}$$

**Paso 2: Análisis de longitudes y ángulos entre vectores**
1. Sabemos que $PQ = 6$, $PR = 8$ y $QT = 3$.
2. Dado que $QT \perp PR$, los vectores $\overrightarrow{PR}$ y $\overrightarrow{QT}$ son perpendiculares, por lo que su producto escalar es $\overrightarrow{PR} \cdot \overrightarrow{QT} = 0$.
3. Como el punto $Y$ pertenece al segmento $\overline{PQ}$, el vector $\overrightarrow{PQ}$ tiene la misma dirección y sentido que el vector $\overrightarrow{YQ}$.
4. Como el punto $T$ pertenece al segmento $\overline{RY}$, el vector $\overrightarrow{TR}$ tiene la misma dirección y sentido que el vector $\overrightarrow{YR}$.
5. Por lo tanto, el ángulo entre los vectores $\overrightarrow{PQ}$ y $\overrightarrow{TR}$ es igual al ángulo entre las semirrectas $YQ$ y $YR$, que es $\angle QYR = 60^{\circ}$.

**Paso 3: Cálculo de $RT$**
Tomando la norma al cuadrado en ambos lados de la igualdad vectorial $\overrightarrow{PQ} + \overrightarrow{TR} = \overrightarrow{PR} - \overrightarrow{QT}$:
$$|\overrightarrow{PQ} + \overrightarrow{TR}|^2 = |\overrightarrow{PR} - \overrightarrow{QT}|^2$$

Desarrollando ambos miembros mediante el producto escalar:
$$|\overrightarrow{PQ}|^2 + |\overrightarrow{TR}|^2 + 2|\overrightarrow{PQ}||\overrightarrow{TR}|\cos(60^{\circ}) = |\overrightarrow{PR}|^2 + |\overrightarrow{QT}|^2 - 2\overrightarrow{PR}\cdot\overrightarrow{QT}$$

Sustituyendo los valores conocidos ($|\overrightarrow{PQ}| = 6$, $|\overrightarrow{PR}| = 8$, $|\overrightarrow{QT}| = 3$, $\cos(60^{\circ}) = \frac{1}{2}$ y $\overrightarrow{PR} \cdot \overrightarrow{QT} = 0$):
$$6^2 + RT^2 + 2(6)(RT)\left(\frac{1}{2}\right) = 8^2 + 3^2$$
$$36 + RT^2 + 6RT = 64 + 9$$
$$RT^2 + 6RT + 36 = 73$$

Completando el cuadrado en el miembro izquierdo:
$$(RT + 3)^2 + 27 = 73$$
$$(RT + 3)^2 = 46$$

Dado que $RT > 0$, tomamos la raíz positiva:
$$RT + 3 = \sqrt{46} \implies RT = \sqrt{46} - 3$$

\boxed{\sqrt{46} - 3}