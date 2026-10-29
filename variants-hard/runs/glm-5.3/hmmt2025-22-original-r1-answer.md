# Planteamiento

Sea $h$ la altura de la cueva. Coloco el suelo en $y=0$ y el techo en $y=h$.

Como las estructuras son perpendiculares al suelo/techo, cada punta está justo debajo (o encima) de su punto de anclaje, así que las coordenadas de las puntas son:

- Estalactitas (cuelgan del techo): alturas $h-16$ y $h-36$
- Estalagmites (crecen del suelo): alturas $25$ y $49$

# Condición clave: el centro del cuadrado

En un cuadrado, las diagonales se cortan en su punto medio, así que las dos parejas de vértices opuestos deben tener la **misma suma de alturas** (ambas iguales al doble de la ordenada del centro).

Debo repartir $\{h-16,\; h-36,\; 25,\; 49\}$ en dos parejas con sumas iguales. Hay tres formas:

1. $(h-16)+(h-36) = 25+49 \;\Rightarrow\; 2h-52 = 74 \;\Rightarrow\; h = 63$ ✓
2. $(h-16)+25 = (h-36)+49 \;\Rightarrow\; h+9 = h+13$ — imposible
3. $(h-16)+49 = (h-36)+25 \;\Rightarrow\; h+33 = h-11$ — imposible

La única posibilidad es la primera: las estalactitas son vértices opuestos entre sí (y las estalagmites también), con $h = 63$.

# Verificación de que el cuadrado existe

Con $h=63$, las puntas de las estalactitas están a alturas $47$ y $27$ (diferencia vertical $20$), y las de las estalagmites a $25$ y $49$ (diferencia vertical $24$). Las diagonales del cuadrado son:

$$\vec d_1 = (a,\,-20), \qquad \vec d_2 = (b,\,24)$$

donde $a$ y $b$ son las separaciones horizontales entre anclajes de cada pareja. Exigimos diagonales iguales y perpendiculares:

$$a\,b = 480 \qquad a^2 + 400 = b^2 + 576$$

De la segunda: $a^2 - b^2 = 176$. Sustituyendo $b = 480/a$ y con $u=a^2$:

$$u^2 - 176u - 230400 = 0 \;\Rightarrow\; u = \frac{176 + \sqrt{30976+921600}}{2} = \frac{176+976}{2} = 576$$

Así $a=24$, $b=20$, y en efecto $ab = 480$ y $24^2+400 = 20^2+576 = 976$. El cuadrado existe. Además, todas las puntas quedan dentro de la cueva: $27, 47 \in (0,63)$ y $25, 49 \in (0,63)$. ✓

# Conclusión

$$\boxed{63}$$