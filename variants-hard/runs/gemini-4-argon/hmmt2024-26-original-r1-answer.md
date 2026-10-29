Para hallar la longitud de $AO$, analicemos la configuración geométrica paso a paso:

1. **Potencia del punto $A$ y eje radical:**
   Denotemos por $\omega_B$ y $\omega_C$ las circunferencias de diámetros $BB'$ y $CC'$, y sean $M_B$ y $M_C$ sus respectivos centros (que son los puntos medios de las cuerdas $BB'$ y $CC'$).
   
   Como los puntos $B, B', C', C$ pertenecen a la circunferencia $\omega$, por la potencia del punto $A$ respecto a $\omega$ se cumple que:
   $$P(A, \omega) = AB' \cdot AB = AC' \cdot AC$$
   
   Por otro lado, la recta $AB$ corta a $\omega_B$ en $B'$ y $B$, por lo que la potencia de $A$ respecto a $\omega_B$ es $P(A, \omega_B) = AB' \cdot AB$. Análogamente, la potencia de $A$ respecto a $\omega_C$ es $P(A, \omega_C) = AC' \cdot AC$. Así, el punto $A$ tiene la misma potencia respecto a $\omega_B$ y $\omega_C$:
   $$P(A, \omega_B) = P(A, \omega_C)$$
   
   Esto implica que $A$ pertenece al eje radical de $\omega_B$ y $\omega_C$. Dado que $\omega_B$ y $\omega_C$ son tangentes exteriormente en $T$, su eje radical es la recta tangente común en $T$. Por lo tanto, $AT$ es tangente a ambas circunferencias en $T$, lo que significa que $AT \perp M_B M_C$ (con $T$ sobre el segmento $M_B M_C$) y además:
   $$AB' \cdot AB = AC' \cdot AC = AT^2 = 12^2 = 144$$

2. **Cálculo de los radios y distancias desde $A$ a los centros $M_B$ y $M_C$:**
   - Para $\omega_B$, sabiendo que $AB = 18$:
     $$AB' = \frac{144}{18} = 8$$
     Como $B'$ está en el segmento $AB$, el diámetro es $BB' = AB - AB' = 18 - 8 = 10$, luego el radio de $\omega_B$ es $r_B = 5$ y la distancia de $A$ a su centro es:
     $$AM_B = AB' + r_B = 8 + 5 = 13$$

   - Para $\omega_C$, sabiendo que $AC = 36$:
     $$AC' = \frac{144}{36} = 4$$
     Como $C'$ está en el segmento $AC$, el diámetro es $CC' = AC - AC' = 36 - 4 = 32$, luego el radio de $\omega_C$ es $r_C = 16$ y la distancia de $A$ a su centro es:
     $$AM_C = AC' + r_C = 4 + 16 = 20$$

3. **Relación con $AO$:**
   Dado que $O$ es el centro de $\omega$ y $M_B, M_C$ son los puntos medios de las cuerdas $BB'$ y $CC'$, se tiene que $OM_B \perp AB$ y $OM_C \perp AC$. Por ende, $\angle AM_B O = \angle AM_C O = 90^\circ$, lo cual implica que los puntos $A, M_B, O, M_C$ son concíclicos y la circunferencia circunscrita al triángulo $\triangle A M_B M_C$ tiene diámetro $AO$.

   En el triángulo $\triangle A M_B M_C$, la altura trazada desde $A$ hacia el lado $M_B M_C$ es precisamente $AT = 12$. Recordando que el diámetro $D$ de la circunferencia circunscrita a un triángulo es igual al producto de dos lados dividido entre la altura correspondiente al tercer lado, obtenemos:
   $$AO = \frac{AM_B \cdot AM_C}{AT} = \frac{13 \cdot 20}{12} = \frac{65}{3}$$

\boxed{\frac{65}{3}}