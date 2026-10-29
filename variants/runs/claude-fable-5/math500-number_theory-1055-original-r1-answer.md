Planteemos el problema paso a paso:

**Planteamiento.** Sea $n$ el número de monedas en cada una de las 7 bolsas originales. Antes del hallazgo tengo $7n$ monedas; después tengo $7n + 53$, que debe repartirse en partes iguales entre 8 bolsas.

**Condición de divisibilidad.** Necesito que $8 \mid 7n + 53$. Trabajando módulo 8:

$$7n + 53 \equiv -n + 5 \equiv 0 \pmod 8 \implies n \equiv 5 \pmod 8$$

**Condición de cantidad.** El total supera 200 monedas: $7n + 53 > 200$, es decir $7n > 147$, o sea $n > 21$.

**Búsqueda del mínimo.** Los valores posibles de $n$ son $5, 13, 21, 29, 37, \dots$ El primero que cumple $n > 21$ es $n = 29$ (nótese que $n = 21$ daría exactamente 200 monedas en total, lo cual no supera 200).

**Verificación.** Con $n = 29$: tenía $7 \times 29 = 203$ monedas; al sumar 53 obtengo $256$, y $256 / 8 = 32$ monedas por bolsa, un reparto exacto. Además $256 > 200$. ✓

$$\boxed{203}$$