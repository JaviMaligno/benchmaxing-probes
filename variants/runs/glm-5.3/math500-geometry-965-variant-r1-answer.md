## Planteamiento

Coloco coordenadas: sea $P$ el origen y $\overline{PS}$ sobre el eje $x$. Escribo $\angle QPS = 2\theta$, de modo que la bisectriz $\overline{PR}$ forma ángulo $\theta$ con $\overline{PS}$. Sea $PR = r$.

**Punto $R$:** 
$$R = (r\cos\theta,\; r\sin\theta)$$

**Condición $PR \perp RS$:** Como $S = (s, 0)$, la perpendicularidad da
$$(s - r\cos\theta)\cos\theta - r\sin^2\theta = 0 \;\Rightarrow\; s\cos\theta = r \;\Rightarrow\; PS = s = \frac{r}{\cos\theta}.$$

**Punto $Q$:** Como $\overline{QR}\parallel\overline{PS}$, $Q$ está en la horizontal por $R$. Como $\overline{PQ}$ forma ángulo $2\theta$ con el eje $x$, escribiendo $Q = t(\cos 2\theta, \sin 2\theta)$ e igualando alturas:
$$t\sin 2\theta = r\sin\theta \;\Rightarrow\; Q_x = \frac{r\sin\theta\cos 2\theta}{\sin 2\theta} = r\cos\theta - \frac{r}{2\cos\theta}.$$

Por lo tanto:
$$QR = R_x - Q_x = \frac{r}{2\cos\theta} = \frac{PS}{2}.$$

## Área del trapecio

La altura del trapecio es $h = r\sin\theta$, así que
$$[PQRS] = \frac{1}{2}\bigl(PS + QR\bigr)h = \frac{1}{2}\left(\frac{r}{\cos\theta} + \frac{r}{2\cos\theta}\right) r\sin\theta = \frac{3r^2\tan\theta}{4} = 45,$$
de donde
$$r^2 \tan\theta = 60.$$

## Área del triángulo

$$[\triangle PRS] = \frac{1}{2}\cdot PS \cdot h = \frac{1}{2}\cdot\frac{r}{\cos\theta}\cdot r\sin\theta = \frac{1}{2}r^2\tan\theta = \frac{60}{2} = 30.$$

**Verificación** (ejemplo numérico con $\tan\theta = \tfrac{3}{4}$, $r = 4\sqrt5$): se obtiene $PS = 5\sqrt5$, $QR = \tfrac{5\sqrt5}{2}$, $h = \tfrac{12\sqrt5}{5}$, y en efecto $[PQRS] = 45$ y $[\triangle PRS] = 30$. ✓

$$\boxed{30}$$