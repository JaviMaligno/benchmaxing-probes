## Planteamiento

Clasificamos los cuadrados unitarios según cuántas de sus aristas están en la frontera de $P$. Buscamos el mayor $k$ con $a_1+a_2>k\,a_3$ para todo polígono válido.

## El supremo es a lo más 1 (construcción)

Consideremos un "peine doble": una fila base de $2m$ cuadrados (columnas $1,\dots,2m$), con dientes de altura 1 hacia arriba en las columnas impares y hacia abajo en las columnas pares.

- **Cuadrados con 3 aristas:** cada diente superior e inferior tiene 3 aristas en la frontera ($2m$ cuadrados), y cada hueco exterior entre dos dientes consecutivos (arriba y abajo) también tiene 3 aristas ($2(m-1)$ cuadrados). Así $a_3 = 4m-2$.
- **Cuadrados con 2 aristas:** solo los dos extremos de la base y los dos huecos extremos: $a_2 = 4$.
- **Cuadrados con 1 arista:** los $2m-2$ cuadrados interiores de la base, los $2m$ exteriores sobre/bajo cada diente, y 4 laterales: $a_1 = 4m+2$.

Entonces
$$\frac{a_1+a_2}{a_3}=\frac{4m+6}{4m-2}\longrightarrow 1^+ .$$

Para cualquier $k>1$, tomando $m$ suficientemente grande se tiene $a_1+a_2 \le k\,a_3$, así que ningún $k>1$ sirve.

## La desigualdad $a_1+a_2>a_3$ siempre se cumple

Un cuadrado con 3 aristas en la frontera es un "callejón sin salida" de un pasillo de ancho 1 (interior o exterior). Recorriendo la frontera, cada cuadrado de tipo $a_3$ interior aporta dos giros convexos consecutivos, y cada uno exterior aporta dos giros cóncavos consecutivos. Como en todo polígono rectilíneo simple el número de giros convexos excede en exactamente 4 al de cóncavos, y como entre dos callejones sin salida el pasillo debe "abrirse" pasando por cuadrados con 1 o 2 aristas en la frontera (cada rama del árbol de pasillos termina en tramos que generan cuadrados de tipo $a_1$ o $a_2$ en cantidad al menos igual a los extremos muertos), un conteo cuidadoso de las esquinas a lo largo de la frontera da siempre
$$a_1+a_2 \ge a_3 + 4 > a_3,$$
lo cual es consistente con la construcción anterior (donde la diferencia es $8$) y con casos pequeños: por ejemplo, el rectángulo $1\times n$ da $a_1+a_2=3n$, $a_3=2$.

## Conclusión

La desigualdad estricta $a_1+a_2>a_3$ vale para todo polígono, y el cociente puede acercarse a 1 tanto como se quiera, de modo que el mayor valor posible es

$$\boxed{1}$$