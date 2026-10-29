# Solución

## Paso 1: El espacio muestral

Lena ensarta las 6 cuentas (L, E, T, T, E, R) en un orden aleatorio. Si tratamos las cuentas como objetos físicos distinguibles (aunque dos lleven la misma letra), hay:

$$6! = 720$$

ordenaciones igualmente probables.

## Paso 2: Identificar los órdenes favorables

El brazalete es circular y puede girarse o voltearse. Entonces el ensartado tiene éxito si, al leerlo desde algún punto y en alguna dirección, se lee L-E-T-T-E-R.

Esto significa que la secuencia lineal de letras debe ser una **rotación** de "LETTER" o una **rotación** de su inverso "RETTEL":

- Rotaciones de LETTER: LETTER, ETTERL, TTERLE, TERLET, ERLETT, RLETTE (6 cadenas)
- Rotaciones de RETTEL: RETTEL, ETTELR, TTELRE, TELRET, ELRETT, LRETTE (6 cadenas)

Ninguna de estas 12 cadenas coincide entre sí (LETTER no es un palíndromo y sus repeticiones de letras no permiten coincidencias). Así que hay **12 cadenas de letras** válidas.

## Paso 3: Contar los ensartados favorables

Cada cadena de letras corresponde a varias ordenaciones de las cuentas físicas: las dos E pueden intercambiarse ($2!$ formas) y las dos T pueden intercambiarse ($2!$ formas). Por lo tanto:

$$\text{favorables} = 12 \times 2! \times 2! = 12 \times 4 = 48$$

## Paso 4: Calcular la probabilidad

$$P = \frac{48}{720} = \frac{1}{15}$$

**Verificación rápida:** si contamos solo arreglos de letras distintos (sin etiquetar), hay $\frac{6!}{2!\,2!} = 180$ arreglos equiprobables, de los cuales 12 son favorables, y $\frac{12}{180} = \frac{1}{15}$. ✓

$$\boxed{\dfrac{1}{15}}$$