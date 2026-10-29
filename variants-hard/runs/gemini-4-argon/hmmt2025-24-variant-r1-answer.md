Para resolver el problema paso a paso, analicemos primero la condición geométrica general para que un semicírculo $\omega_a$ (con centro $O_a$ y radio $r_a$) esté inscrito en otro semicírculo $\omega_b$ (con centro $O_b$ y radio $r_b$).

### 1. Relación general entre dos semicírculos inscritos
1. **El diámetro de $\omega_a$ es una cuerda de $\omega_b$:**
   Como $O_a$ es el punto medio del diámetro de $\omega_a$ y sus extremos pertenecen al arco de $\omega_b$, el segmento $O_b O_a$ es perpendicular al diámetro de $\omega_a$. Por el teorema de Pitágoras, la distancia entre los centros cumple:
   $$O_b O_a^2 + r_a^2 = r_b^2 \implies O_b O_a = \sqrt{r_b^2 - r_a^2}$$

2. **El arco de $\omega_a$ es tangente al diámetro de $\omega_b$:**
   Sea $T_{ab}$ el punto de tangencia del arco de $\omega_a$ con el diámetro de $\omega_b$. Entonces $O_a T_{ab}$ es perpendicular al diámetro de $\omega_b$ y tiene longitud $r_a$.

3. **Ángulo entre los diámetros:**
   El ángulo agudo $\alpha_{ab}$ entre los diámetros de $\omega_a$ y $\omega_b$ es igual al ángulo entre sus respectivas rectas perpendiculares: la recta $O_b O_a$ (perpendicular al diámetro de $\omega_a$) y la recta $O_a T_{ab}$ (perpendicular al diámetro de $\omega_b$).
   En el triángulo rectángulo $\triangle O_b T_{ab} O_a$ (recto en $T_{ab}$), tenemos:
   $$\cos \alpha_{ab} = \frac{O_a T_{ab}}{O_b O_a} = \frac{r_a}{\sqrt{r_b^2 - r_a^2}}$$

---

### 2. Cálculo de $r_2^2$
Consideremos los tres semicírculos $\omega_1, \omega_2, \omega_3$ con radios $r_1 = 3$, $r_2$ y $r_3 = 12$.
- El ángulo $\alpha_{12}$ entre los diámetros de $\omega_1$ y $\omega_2$ satisface:
  $$\cos \alpha_{12} = \frac{r_1}{\sqrt{r_2^2 - r_1^2}}$$
- El ángulo $\alpha_{23}$ entre los diámetros de $\omega_2$ y $\omega_3$ satisface:
  $$\cos \alpha_{23} = \frac{r_2}{\sqrt{r_3^2 - r_2^2}}$$

Dado que los diámetros de $\omega_1$ y $\omega_3$ son paralelos y $\alpha_{12}, \alpha_{23} \in [0, \pi/2)$, el diámetro de $\omega_2$ debe formar el mismo ángulo agudo con ambos diámetros, es decir, $\alpha_{12} = \alpha_{23}$. Por lo tanto:
$$\frac{r_1}{\sqrt{r_2^2 - r_1^2}} = \frac{r_2}{\sqrt{r_3^2 - r_2^2}}$$

Elevando ambos lados al cuadrado e invirtiendo las fracciones:
$$\frac{r_2^2 - r_1^2}{r_1^2} = \frac{r_3^2 - r_2^2}{r_2^2} \implies \frac{r_2^2}{r_1^2} - 1 = \frac{r_3^2}{r_2^2} - 1 \implies r_2^4 = r_1^2 r_3^2$$

Como los radios son positivos, obtenemos que $r_2^2 = r_1 r_3$. Sustituyendo $r_1 = 3$ y $r_3 = 12$:
$$r_2^2 = 3 \cdot 12 = 36$$

---

### 3. Cálculo de $PT \cdot TQ$
En el semicírculo $\omega_3$, su centro $O_3$ es el punto medio del diámetro $PQ$, donde $O_3 P = O_3 Q = r_3$. Como $T$ es la proyección ortogonal de $O_2$ sobre $PQ$, en el triángulo rectángulo $\triangle O_3 T O_2$ se cumple:
$$O_3 T^2 = O_3 O_2^2 - O_2 T^2 = (r_3^2 - r_2^2) - r_2^2 = r_3^2 - 2r_2^2$$

Finalmente, expresamos el producto $PT \cdot TQ$ en función de $O_3 T$:
$$PT \cdot TQ = (r_3 + O_3 T)(r_3 - O_3 T) = r_3^2 - O_3 T^2 = r_3^2 - (r_3^2 - 2r_2^2) = 2r_2^2$$

Sustituyendo $r_2^2 = 36$:
$$PT \cdot TQ = 2 \cdot 36 = 72$$

\boxed{72}