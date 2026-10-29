Para encontrar el número total de coloraciones válidas, podemos dividir los $12$ segmentos unitarios de la cuadrícula de $2 \times 2$ en dos grupos:
1. **Los $4$ segmentos internos**, que se unen en el vértice central y son compartidos cada uno por dos cuadrados unitarios adyacentes.
2. **Los $8$ segmentos externos**, que forman el borde exterior de la cuadrícula. Cada uno de los $4$ cuadrados unitarios posee exactamente $2$ de estos segmentos externos, los cuales no comparte con ningún otro cuadrado.

### Paso 1: Opciones para los segmentos externos según los internos
Fijemos primero la coloración de los $4$ segmentos internos. Para que un cuadrado unitario tenga exactamente $2$ lados rojos y $2$ azules, el color de sus $2$ segmentos externos queda restringido por los colores de sus $2$ segmentos internos:
- **Si sus $2$ segmentos internos son del mismo color** (ambos rojos o ambos azules), entonces sus $2$ segmentos externos deben ser ambos del color opuesto. Hay $\binom{2}{2} = 1$ sola forma de colorearlos.
- **Si sus $2$ segmentos internos son de diferente color** (uno rojo y uno azul), entonces necesita exactamente un segmento externo rojo y uno azul. Hay $\binom{2}{1} = 2$ formas de colorearlos.

Por lo tanto, para una configuración dada de los $4$ segmentos internos, el número de formas de completar los $8$ segmentos externos es $2^m$, donde $m$ es la cantidad de cuadrados unitarios cuyos dos lados internos tienen colores distintos.

---

### Paso 2: Análisis por casos de los $4$ segmentos internos
Existen $2^4 = 16$ formas de colorear los $4$ segmentos internos (Norte, Sur, Este y Oeste respecto al centro). Las clasificamos según el número $r$ de segmentos internos rojos:

1. **$r = 0$ o $r = 4$ (todos los segmentos internos del mismo color):**
   - Hay $\binom{4}{0} + \binom{4}{4} = 1 + 1 = 2$ configuraciones internas.
   - En cada cuadrado, los dos lados internos tienen el mismo color ($m = 0$).
   - Número de coloraciones completas: $2 \times 2^0 = 2 \times 1 = 2$.

2. **$r = 1$ o $r = 3$ (tres segmentos de un color y uno del otro):**
   - Hay $\binom{4}{1} + \binom{4}{3} = 4 + 4 = 8$ configuraciones internas.
   - El único segmento de color distinto pertenece a $2$ cuadrados adyacentes, por lo que exactamente $m = 2$ cuadrados tienen lados internos de distinto color, mientras que los otros $2$ tienen lados internos del mismo color.
   - Número de coloraciones completas: $8 \times 2^2 = 8 \times 4 = 32$.

3. **$r = 2$ (dos segmentos internos rojos y dos azules):**
   Hay $\binom{4}{2} = 6$ configuraciones internas, que se dividen en dos subcasos según la posición de los segmentos del mismo color:
   - **Subcaso 3a (segmentos del mismo color opuestos, ej. Norte y Sur rojos, Este y Oeste azules):**
     - Hay $2$ configuraciones de este tipo.
     - Los colores alternan alrededor del centro, por lo que los $4$ cuadrados tienen un lado interno rojo y uno azul ($m = 4$).
     - Número de coloraciones completas: $2 \times 2^4 = 2 \times 16 = 32$.
   - **Subcaso 3b (segmentos del mismo color adyacentes, ej. Norte y Este rojos, Sur y Oeste azules):**
     - Hay $4$ configuraciones de este tipo.
     - Un cuadrado tiene dos lados internos rojos, su opuesto tiene dos lados internos azules, y los otros $m = 2$ cuadrados tienen lados internos de distinto color.
     - Número de coloraciones completas: $4 \times 2^2 = 4 \times 4 = 16$.

---

### Paso 3: Suma total
Sumando las posibilidades de todos los casos disjuntos obtenemos:
$$\text{Total} = 2 + 32 + 32 + 16 = 82$$

\boxed{82}