Para encontrar el radio de la bola más grande que cumple las condiciones, ubiquemos el cubo de arista $6$ centrado en el origen de coordenadas, de modo que ocupe la región $[-3, 3]^3$.

1. **Posición de las ocho bolas de radio $\frac{3}{2}$:**
   Para que una bola de radio $r = \frac{3}{2}$ esté completamente contenida dentro del cubo $[-3, 3]^3$, su centro debe encontrarse dentro del cubo más pequeño $[-3 + \frac{3}{2}, 3 - \frac{3}{2}]^3 = [-\frac{3}{2}, \frac{3}{2}]^3$, el cual tiene longitud de arista $3$.
   
   Dado que las bolas no se superponen y cada una tiene radio $\frac{3}{2}$, la distancia entre los centros de cualesquiera dos bolas debe ser al menos $2r = 3$. Al colocar $8$ puntos en un cubo de arista $3$ con distancia mutua mínima de $3$, los centros de las ocho bolas deben ubicarse en los ocho vértices de dicho cubo:
   $$\left(\pm \frac{3}{2}, \pm \frac{3}{2}, \pm \frac{3}{2}\right)$$
   En esta configuración, cada centro está a distancia $3 = 2r$ de los tres centros que difieren en exactamente una coordenada, por lo que cada bola es tangente exteriormente a exactamente tres de las otras.

2. **Cálculo del radio $R$ de la bola tangente a las ocho bolas:**
   Por simetría, la bola que es tangente exteriormente a las ocho bolas tiene su centro en el origen $(0, 0, 0)$. La distancia $d$ desde el origen hasta el centro de cualquiera de las ocho bolas es la mitad de la diagonal espacial del cubo de centros:
   $$d = \sqrt{\left(\frac{3}{2}\right)^2 + \left(\frac{3}{2}\right)^2 + \left(\frac{3}{2}\right)^2} = \frac{3\sqrt{3}}{2}$$

   Como la bola central de radio $R$ es tangente exteriormente a las bolas de radio $r = \frac{3}{2}$, la distancia entre sus centros cumple $d = R + r$:
   $$R + \frac{3}{2} = \frac{3\sqrt{3}}{2} \implies R = \frac{3\sqrt{3} - 3}{2}$$

   Dado que $R = \frac{3(\sqrt{3}-1)}{2} < 3$, esta bola queda completamente contenida dentro del cubo de arista $6$.

\boxed{\frac{3\sqrt{3}-3}{2}}