## Razonamiento

**1. La condición es puramente por pares.**

La restricción solo involucra dos letras a la vez, así que la palabra es válida si y solo si, para cada par $\{x,y\}$, la subpalabra inducida (de longitud 6, con tres $x$ y tres $y$) es válida en ambos sentidos.

Enumerando las $\binom{6}{3}=20$ subpalabras posibles, las que cumplen la condición en ambas direcciones son exactamente cuatro:
$$xxxyyy,\quad yyyxxx,\quad xyxyxy,\quad yxyxyx.$$

Es decir, cada par de letras está **separado** (todas las copias de una antes que las de la otra) o **entrelazado** (alternan perfectamente).

**2. "Estar entrelazado" es una relación de equivalencia.**

Supongamos $x\sim y$ y $y\sim z$ entrelazadas, pero $x,z$ separadas. Las $x$ y las $y$ alternan: $xyxyxy$. Si todas las $z$ van antes de las $x$, entonces también van antes de todas las $y$, luego $y,z$ estarían separadas: contradicción. Si todas las $z$ van después de las $x$, quedan después de la segunda $y$, así que la subpalabra de $\{y,z\}$ empieza con $yy$ y no alterna: contradicción. Por tanto el entrelazado es transitivo y parte el alfabeto en clases $C_1,\dots,C_k$.

**3. Estructura dentro de una clase.**

Sea una clase de tamaño $m$ con todas sus letras mutuamente entrelazadas. Entre dos apariciones consecutivas de cualquier letra hay exactamente una copia de cada una de las otras $m-1$ letras de la clase. Tomando la primera letra $a$ de la clase: su segunda copia está en la posición $m+1$ y la tercera en $2m+1$, de modo que la palabra restringida a la clase se corta en tres bloques de longitud $m$, cada uno con todas las letras una vez. Si $b$ ocupa la posición $i$ del primer bloque y la posición $j$ del segundo, entre ambas hay $m+j-1-i$ letras, que debe valer $m-1$, luego $j=i$. Igual con el tercer bloque. Así la clase aparece como $\sigma\sigma\sigma$ con $\sigma$ una permutación de la clase: $m!$ opciones.

**4. Entre clases.**

Como dentro de una clase las letras alternan, ninguna letra externa puede meterse en medio: cada clase ocupa un bloque contiguo, y las clases se ordenan linealmente.

**5. Conteo.**

Una configuración válida equivale a: concatenar las clases ordenadas con su permutación interna, lo que da una permutación de las 26 letras, junto con el corte de esa permutación en bloques consecutivos (una composición de 26).

$$26!\cdot 2^{25}$$

*(Comprobación con 2 letras: $2!\cdot 2^1=4$, y en efecto las válidas son $aaabbb,\ bbbaaa,\ ababab,\ bababa$.)*

\boxed{2^{25}\cdot 26!}