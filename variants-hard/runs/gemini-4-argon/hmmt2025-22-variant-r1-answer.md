Para hallar la altura de la caverna, situemos un sistema de coordenadas cartesianas donde el suelo de la caverna esté en la recta $y = 0$ y el techo en la recta $y = H$, siendo $H$ la altura de la caverna.

Las coordenadas verticales ($y$) de las puntas de las cuatro formaciones son:
- Para las dos estalactitas (que cuelgan del techo):
  $$y_1 = H - 18, \quad y_2 = H - 34$$
- Para las dos estalagmitas (que suben desde el suelo):
  $$y_3 = 25, \quad y_4 = 47$$

En cualquier cuadrado en el plano, las diagonales se bisecan mutuamente, lo que significa que el punto medio de una diagonal coincide con el punto medio de la otra. Por lo tanto, la suma de las coordenadas $y$ de dos vértices opuestos debe ser igual a la suma de las coordenadas $y$ de los otros dos vértices opuestos.

Consideremos las tres formas posibles de emparejar los cuatro vértices en pares opuestos:

1. **Si una estalactita es opuesta a una estalagmita en ambas diagonales:**
   - Emparejando $(y_1, y_3)$ y $(y_2, y_4)$:
     $$(H - 18) + 25 = (H - 34) + 47 \implies H + 7 = H + 13$$
     Esta ecuación no tiene solución.
   - Emparejando $(y_1, y_4)$ y $(y_2, y_3)$:
     $$(H - 18) + 47 = (H - 34) + 25 \implies H + 29 = H - 9$$
     Esta ecuación tampoco tiene solución.

2. **Si las dos estalactitas son vértices opuestos y las dos estalagmitas son vértices opuestos:**
   - Emparejando $(y_1, y_2)$ y $(y_3, y_4)$:
     $$(H - 18) + (H - 34) = 25 + 47$$
     $$2H - 52 = 72$$
     $$2H = 124$$
     $$H = 62$$

Para $H = 62$, las alturas de las puntas son $44$, $28$, $25$ y $47$, las cuales permiten construir un cuadrado válido eligiendo adecuadamente las posiciones horizontales de las formaciones.

\boxed{62}