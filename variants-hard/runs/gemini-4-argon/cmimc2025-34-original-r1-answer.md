Para hallar $a_{\text{max}} - a_{\text{min}}$, analicemos la geometría de los seis puntos dados:
- Los cuatro puntos $A=(0,0)$, $B=(10,0)$, $C=(10,10)$ y $D=(0,10)$ forman un cuadrado de lado $10$, cuya área es $100$. Este cuadrado es la envolvente convexa de los $6$ puntos.
- Los otros dos puntos, $E=(3,4)$ y $F=(6,2)$, se encuentran estrictamente en el interior del cuadrado $ABCD$.

---

### 1. Estructura de los hexágonos simples

Como $A, B, C, D$ están en el borde de la envolvente convexa y el hexágono no se autointerseca, el recorrido de los vértices del hexágono debe visitar $A, B, C, D$ en su orden cíclico natural (de lo contrario, dos caminos diagonales dentro del cuadrado tendrían que cruzarse).

Por lo tanto, cualquier hexágono simple $RANDOM$ se obtiene a partir del cuadrado $ABCD$ reemplazando uno o dos lados del cuadrado por caminos que pasen por los puntos interiores $E$ y $F$. En consecuencia, el área del hexágono es siempre:
$$\text{Área}(RANDOM) = 100 - R,$$
donde $R$ es el área de la región (un cuadrilátero o dos triángulos) que se le quita al cuadrado. Así, maximizar y minimizar el área del hexágono equivale a minimizar y maximizar el área removida $R$, y se cumple que:
$$a_{\text{max}} - a_{\text{min}} = R_{\text{max}} - R_{\text{min}}.$$

---

### 2. Áreas de los triángulos básicos

Calculamos primero las áreas de los triángulos formados por $E=(3,4)$ y $F=(6,2)$ con cada uno de los cuatro lados del cuadrado (todos de base $10$):

- **Con el lado inferior $AB$ ($y=0$):**
  - $\text{Área}(\triangle AEB) = \frac{1}{2} \times 10 \times 4 = 20$
  - $\text{Área}(\triangle AFB) = \frac{1}{2} \times 10 \times 2 = 10$
- **Con el lado derecho $BC$ ($x=10$):**
  - $\text{Área}(\triangle BEC) = \frac{1}{2} \times 10 \times (10-3) = 35$
  - $\text{Área}(\triangle BFC) = \frac{1}{2} \times 10 \times (10-6) = 20$
- **Con el lado superior $CD$ ($y=10$):**
  - $\text{Área}(\triangle CED) = \frac{1}{2} \times 10 \times (10-4) = 30$
  - $\text{Área}(\triangle CFD) = \frac{1}{2} \times 10 \times (10-2) = 40$
- **Con el lado izquierdo $DA$ ($x=0$):**
  - $\text{Área}(\triangle DEA) = \frac{1}{2} \times 10 \times 3 = 15$
  - $\text{Área}(\triangle DFA) = \frac{1}{2} \times 10 \times 6 = 30$

Además, la recta que pasa por $E(3,4)$ y $F(6,2)$ tiene ecuación $2x + 3y = 18$. El área del triángulo formado por un vértice $(x_0, y_0)$ con el segmento $EF$ es $\frac{1}{2}|2x_0 + 3y_0 - 18|$:
- $\text{Área}(\triangle AEF) = \frac{1}{2}|0 + 0 - 18| = 9$
- $\text{Área}(\triangle BEF) = \frac{1}{2}|20 + 0 - 18| = 1$
- $\text{Área}(\triangle CEF) = \frac{1}{2}|20 + 30 - 18| = 16$
- $\text{Área}(\triangle DEF) = \frac{1}{2}|0 + 30 - 18| = 6$

---

### 3. Análisis de los dos casos posibles

#### Caso 1: $E$ y $F$ se insertan en el mismo lado del cuadrado
En este caso, se quita un cuadrilátero simple con base en un lado del cuadrado:
1. **En el lado $AB$:** El punto $F(6,2)$ está estrictamente en el interior de $\triangle AEB$ (pues la recta $EB$ es $4x+7y=40$ y para $F$ se tiene $4(6)+7(2)=38 < 40$). Por tanto, ambos órdenes son válidos y no se autointersecan:
   - Orden $A - F - E - B$: se quita el cuadrilátero $AFEB$ de área $\text{Área}(\triangle AEB) - \text{Área}(\triangle AEF) = 20 - 9 = 11$.
   - Orden $A - E - F - B$: se quita el cuadrilátero $AEFB$ de área $\text{Área}(\triangle AEB) - \text{Área}(\triangle BEF) = 20 - 1 = 19$.
2. **En el lado $BC$:** Solo el orden $B - F - E - C$ evita que los segmentos se crucen, quitando un área de $\text{Área}(\triangle BEC) + \text{Área}(\triangle BEF) = 35 + 1 = 36$.
3. **En el lado $CD$:** Solo el orden $C - F - E - D$ es simple, quitando un área de $\text{Área}(\triangle CED) + \text{Área}(\triangle CEF) = 30 + 16 = 46$.
4. **En el lado $DA$:** El punto $E(3,4)$ está estrictamente dentro de $\triangle DFA$ (pues la recta $DF$ es $4x+3y=30$ y para $E$ se tiene $4(3)+3(4)=24 < 30$). Ambos órdenes son válidos:
   - Orden $D - F - E - A$: se quita un área de $\text{Área}(\triangle DFA) - \text{Área}(\triangle AEF) = 30 - 9 = 21$.
   - Orden $D - E - F - A$: se quita un área de $\text{Área}(\triangle DFA) - \text{Área}(\triangle DEF) = 30 - 6 = 24$.

#### Caso 2: $E$ y $F$ se insertan en lados distintos del cuadrado
Aquí se quitan dos triángulos (uno con vértice $E$ y otro con vértice $F$) que no deben intersectarse en el interior del cuadrado.
- Como $F$ está dentro de $\triangle AEB$, $E$ no puede ir en $AB$.
- Como $E$ está dentro de $\triangle DFA$, $F$ no puede ir en $DA$.
- Entre las demás combinaciones posibles:
  - Si $E$ va en $DA$ (área $15$, con segmentos en $x \in [0,3]$) y $F$ va en $CD$ (área $40$, con segmentos $CF$ en $x \in [6,10]$ y $DF$ en la recta $4x+3y=30$), como $E(3,4)$ y $A(0,0)$ cumplen $4x+3y < 30$, los triángulos $\triangle DEA$ y $\triangle CFD$ no se cruzan. Esto produce el área removida máxima:
    $$R = 15 + 40 = 55.$$
  - Otras combinaciones válidas en este caso dan áreas removidas menores ($15+10=25$, $15+20=35$, $30+10=40$, $35+10=45$, $30+20=50$).

---

### 4. Conclusión

- El área removida mínima es $R_{\text{min}} = 11$ (con el hexágono $A - F - E - B - C - D$), por lo que el área máxima del hexágono es:
  $$a_{\text{max}} = 100 - 11 = 89.$$
- El área removida máxima es $R_{\text{max}} = 55$ (con el hexágono $A - B - C - F - D - E$), por lo que el área mínima del hexágono es:
  $$a_{\text{min}} = 100 - 55 = 45.$$

Por lo tanto, la diferencia buscada es:
$$a_{\text{max}} - a_{\text{min}} = 89 - 45 = 44.$$

\boxed{44}