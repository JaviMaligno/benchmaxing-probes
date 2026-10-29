## Planteamiento

Lena ensarta 6 cuentas (L, E₁, T₁, T₂, E₂, R, donde las cuentas repetidas son objetos físicamente distintos) en orden aleatorio. Hay **6! = 720** ordenaciones igualmente probables, cada una fija una disposición circular en posiciones etiquetadas.

## Disposiciones favorables

El brazalete "funciona" si, leído tras alguna rotación o volteo, deletrea LETTER. Las disposiciones de letras equivalentes a LETTER bajo el grupo diédrico D₆ (12 simetrías: 6 rotaciones × 2 reflexiones) forman una órbita de tamaño 12/|estabilizador|.

**Estabilizador de LETTER:**
- *Rotaciones:* como solo hay una L, ninguna rotación no trivial fija la palabra.
- *Reflexiones:* la lectura en sentido contrario desde L es L-R-E-T-T-E, que no es rotación de L-E-T-T-E-R (tras la L viene R en vez de E). Tampoco hay reflexión que la fije.

El estabilizador es trivial, así que hay **12** secuencias de letras favorables sobre las posiciones fijas del brazalete.

## Conteo de ordenaciones

Cada secuencia de letras favorable se obtiene de **2! · 2! = 4** ordenaciones de cuentas (intercambiando las dos E y las dos T entre sí). Entonces:

$$P = \frac{12 \cdot 4}{720} = \frac{48}{720} = \frac{1}{15}$$

$$\boxed{\dfrac{1}{15}}$$