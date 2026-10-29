Para calcular la longitud de $MD$, podemos resolver el problema paso a paso utilizando las propiedades del trapecio isósceles, la potencia de un punto y la fórmula de la mediana.

### Paso 1: Relación métrica en el trapecio mediante proyecciones
Sea $A'$ la proyección ortogonal del vértice $A$ sobre la recta $CD$, y sea $h = AA'$ la altura del trapecio $ABCD$.
Como $ABCD$ es un trapecio isósceles con bases paralelas $AB$ y $CD$ tales que $CD > AB = 4$, la distancia desde $D$ hasta $A'$ viene dada por:
$$DA' = \frac{CD - AB}{2} = \frac{CD - 4}{2} = \frac{CD}{2} - 2$$

Dado que $D$ se encuentra entre $E$ y $C$ (y $A'$ está entre $D$ y $C$), el punto $D$ se ubica entre $E$ y $A'$. Sabiendo que $DE = 2$, la distancia desde $E$ hasta $A'$ es:
$$EA' = ED + DA' = 2 + \left(\frac{CD}{2} - 2\right) = \frac{CD}{2}$$

Aplicando el teorema de Pitágoras en los triángulos rectángulos $\triangle AA'D$ y $\triangle AA'E$:
$$AD^2 = h^2 + DA'^2 = h^2 + \left(\frac{CD}{2} - 2\right)^2 = h^2 + \left(\frac{CD}{2}\right)^2 - 2CD + 4$$
$$AE^2 = h^2 + EA'^2 = h^2 + \left(\frac{CD}{2}\right)^2$$

Restando ambas expresiones, obtenemos una relación directa entre $AD$, $AE$ y $CD$:
$$AD^2 = AE^2 - 2CD + 4 \quad \text{(Ecuación 1)}$$

---

### Paso 2: Potencia del punto $E$ respecto a la circunferencia
Los puntos $A, B, C, D$ y $M$ pertenecen a una misma circunferencia (de radio $R = 5$, lo cual garantiza la existencia de la configuración con $CD < 2R = 10$). 
Como la recta $EC$ corta a la circunferencia en $D$ y $C$, y la recta $EA$ la corta en $M$ y $A$, por la potencia del punto exterior $E$ respecto a la circunferencia tenemos:
$$EM \cdot EA = ED \cdot EC$$

Dado que $M$ es el punto medio de $\overline{AE}$, se cumple que $EM = \frac{1}{2}AE$. Además, $ED = 2$ y $EC = ED + DC = 2 + CD$. Sustituyendo estos valores:
$$\left(\frac{1}{2}AE\right) \cdot AE = 2(2 + CD) \implies AE^2 = 8 + 4CD \quad \text{(Ecuación 2)}$$

Sustituyendo la Ecuación 2 en la Ecuación 1:
$$AD^2 = (8 + 4CD) - 2CD + 4 = 12 + 2CD \quad \text{(Ecuación 3)}$$

---

### Paso 3: Cálculo de $MD$ mediante el teorema de la mediana
En el triángulo $\triangle ADE$, el segmento $\overline{MD}$ es la mediana relativa al lado $\overline{AE}$. Por la fórmula de la longitud de la mediana (teorema de Apolonio):
$$MD^2 = \frac{2AD^2 + 2ED^2 - AE^2}{4}$$

Sustituimos $ED = 2$, $AE^2 = 8 + 4CD$ y $AD^2 = 12 + 2CD$:
$$MD^2 = \frac{2(12 + 2CD) + 2(2^2) - (8 + 4CD)}{4}$$
$$MD^2 = \frac{24 + 4CD + 8 - 8 - 4CD}{4} = \frac{24}{4} = 6$$

Por lo tanto, tomando la raíz cuadrada obtenemos la longitud de $MD$:
$$MD = \sqrt{6}$$

\boxed{\sqrt{6}}