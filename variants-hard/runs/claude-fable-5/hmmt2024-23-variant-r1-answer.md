## Solución

**Planteamiento con coordenadas.** Sea la cuerda de longitud $6t$, con segmentos $t$, $2t$, $3t$. Coloco la cuerda sobre el eje $x$: los extremos de la cuerda en $A=(0,0)$ y $B=(6t,0)$, y los puntos de corte con $\gamma$ en $P=(t,0)$ y $Q=(3t,0)$.

**Centros de los círculos.**
- El centro $O$ de $\Gamma$ está sobre la mediatriz de $AB$, es decir $O=(3t,\,k)$, y como $A\in\Gamma$: 
$$k^2 = 203^2 - 9t^2.$$
- El centro $C$ de $\gamma$ está sobre la mediatriz de $PQ$, es decir $C=(2t,\,h)$, y como $P\in\gamma$:
$$h^2 = 101^2 - t^2.$$

**Condición de que $O$ esté sobre $\gamma$:** $|OC| = 101$, o sea
$$(3t-2t)^2 + (k-h)^2 = 101^2.$$

Expandiendo:
$$t^2 + k^2 + h^2 - 2kh = 101^2$$
$$t^2 + (203^2 - 9t^2) + (101^2 - t^2) - 2kh = 101^2$$
$$203^2 - 9t^2 = 2kh.$$

**Elevando al cuadrado** y usando $k^2 h^2 = (203^2-9t^2)(101^2-t^2)$:
$$(203^2 - 9t^2)^2 = 4(203^2 - 9t^2)(101^2 - t^2).$$

Si $203^2 - 9t^2 = 0$ entonces $k=0$ y la cuerda pasaría por $O$, es decir sería un diámetro, lo cual está excluido. Dividiendo entre $203^2-9t^2$:
$$203^2 - 9t^2 = 4\cdot 101^2 - 4t^2 \;\Longrightarrow\; 5t^2 = 203^2 - 4\cdot101^2 = 41209 - 40804 = 405,$$
$$t^2 = 81 \;\Longrightarrow\; t = 9.$$

**Verificación:** $k^2 = 41209 - 729 = 40480$ y $h^2 = 10201 - 81 = 10120$; en efecto $4k^2h^2 = 4\cdot 40480\cdot 10120 = 40480^2 = (203^2-9t^2)^2$. ✓

La cuerda mide $6t = 54$.

$$\boxed{54}$$