## Planteamiento

Sea $h = HO$ la altura del globo, $c = OC$ y $d = OD$. Como $A$, $B$, $C$, $D$ están al norte, oeste, sur y este de $O$, el ángulo $\angle COD = 90^\circ$ (sur y este son direcciones perpendiculares).

**Paso 1: Encontrar $h$, $c$ y $d$.**

Como $HO$ es vertical, los triángulos $HOC$ y $HOD$ son rectángulos en $O$:
$$h^2 + c^2 = 150^2 = 22500, \qquad h^2 + d^2 = 130^2 = 16900.$$

Y por el ángulo recto en $O$ dentro del campo:
$$c^2 + d^2 = 140^2 = 19600.$$

Restando las dos primeras: $c^2 - d^2 = 5600$. Combinando con $c^2 + d^2 = 19600$:
$$c^2 = 12600, \qquad d^2 = 7000, \qquad h^2 = 22500 - 12600 = 9900.$$

**Paso 2: Minimizar $HP$ con $P$ en el segmento $CD$.**

Como $HO$ es perpendicular al suelo, para cualquier punto $P$ del campo:
$$HP^2 = h^2 + OP^2.$$

Entonces $HP$ es mínimo cuando $OP$ es mínimo, es decir, cuando $P$ es el pie de la perpendicular desde $O$ a la recta $CD$ (que cae dentro del segmento, pues es la altura sobre la hipotenusa del triángulo rectángulo $COD$).

La altura sobre la hipotenusa cumple $OP = \dfrac{c \cdot d}{CD}$:
$$OP^2 = \frac{c^2 d^2}{140^2} = \frac{12600 \cdot 7000}{19600} = 4500.$$

Por lo tanto:
$$HP^2 = 9900 + 4500 = 14400 \implies HP = 120.$$

**Paso 3: Ahorro máximo.**

La cuerda usada antes era $HC + HD = 150 + 130 = 280$ m; la mínima cuerda nueva es $120$ m:
$$280 - 120 = 160 \text{ m}.$$

$$\boxed{160 \text{ m}}$$