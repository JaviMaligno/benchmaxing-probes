Para encontrar el número de *peacocks* (enteros positivos de 10 dígitos que usan cada dígito del $0$ al $9$ exactamente una vez) que son el doble de otro *peacock*, contaremos de manera equivalente cuántos *peacocks* $A$ cumplen que $B = 2A$ también es un *peacock*.

### Paso 1: Descomposición de los dígitos y acarreos
Sea $A = \overline{a_9 a_8 a_7 a_6 a_5 a_4 a_3 a_2 a_1 a_0}$ un *peacock*, donde $\{a_0, a_1, \dots, a_9\} = \{0, 1, \dots, 9\}$ y $a_9 \neq 0$.
Cada dígito $a_i$ puede escribirse de manera única como:
$$a_i = 5t_i + r_i$$
donde $t_i \in \{0, 1\}$ indica si el dígito es pequeño ($a_i \in \{0, 1, 2, 3, 4\} \iff t_i = 0$) o grande ($a_i \in \{5, 6, 7, 8, 9\} \iff t_i = 1$), y $r_i = a_i \bmod 5 \in \{0, 1, 2, 3, 4\}$ es su residuo módulo $5$.

Al calcular $B = 2A = \overline{b_9 b_8 b_7 b_6 b_5 b_4 b_3 b_2 b_1 b_0}$, sea $c_i \in \{0, 1\}$ el acarreo que entra en la posición $i$ (con $c_0 = 0$). En cada posición $i$ tenemos:
$$2a_i + c_i = 10t_i + (2r_i + c_i)$$
Como $r_i \in \{0, 1, 2, 3, 4\}$ y $c_i \in \{0, 1\}$, se cumple que $0 \le 2r_i + c_i \le 9$. Por lo tanto, para cada $i \in \{0, 1, \dots, 9\}$:
- El dígito de $B$ en la posición $i$ es $b_i = 2r_i + c_i$.
- El acarreo hacia la siguiente posición es $c_{i+1} = t_i$.

Para que $B$ sea un número de 10 dígitos, no debe haber acarreo de salida en la última posición, es decir, $c_{10} = t_9 = 0$. Como además $a_9 \neq 0$, esto equivale a $t_9 = 0$ y $r_9 \neq 0$ (es decir, $a_9 \in \{1, 2, 3, 4\}$). Esto garantiza automáticamente que $b_9 = 2r_9 + c_9 \ge 2 > 0$.

---

### Paso 2: Condiciones para que $A$ y $B$ sean *peacocks*
1. **$A$ contiene todos los dígitos del $0$ al $9$:**
   Entre los diez pares $(t_i, r_i)$, debe haber exactamente cinco posiciones con $t_i = 0$ (cuyos residuos $r_i$ formen una permutación de $\{0, 1, 2, 3, 4\}$) y cinco posiciones con $t_i = 1$ (cuyos residuos $r_i$ también formen una permutación de $\{0, 1, 2, 3, 4\}$).

2. **$B$ contiene todos los dígitos del $0$ al $9$:**
   Como $c_0 = 0$, $c_i = t_{i-1}$ para $1 \le i \le 9$, y $t_9 = 0$, la secuencia de acarreos $(c_0, c_1, \dots, c_9) = (0, t_0, t_1, \dots, t_8)$ también tiene exactamente cinco $0$'s y cinco $1$'s.
   Dado que $b_i = 2r_i + c_i$, los diez dígitos $b_i$ son todos distintos si y solo si las cinco posiciones con $c_i = 0$ tienen residuos $r_i$ que forman una permutación de $\{0, 1, 2, 3, 4\}$ (generando los dígitos pares $\{0, 2, 4, 6, 8\}$), y las cinco posiciones con $c_i = 1$ tienen residuos $r_i$ que forman una permutación de $\{0, 1, 2, 3, 4\}$ (generando los dígitos impares $\{1, 3, 5, 7, 9\}$).

---

### Paso 3: Conteo de asignaciones de residuos para una secuencia $(t_0, \dots, t_9)$ fija
Fijemos una secuencia $(t_0, t_1, \dots, t_9) \in \{0, 1\}^{10}$ con cinco $0$'s, cinco $1$'s y $t_9 = 0$. Particionamos el conjunto de índices $\{0, 1, \dots, 9\}$ en cuatro subconjuntos según el par $(t_i, c_i)$:
$$P_{ab} = \{i \in \{0, \dots, 9\} : t_i = a, \, c_i = b\} \quad \text{para } a, b \in \{0, 1\}.$$

Como $|P_{00}| + |P_{01}| = 5$ y $|P_{00}| + |P_{10}| = 5$, si llamamos $k = |P_{10}|$, entonces:
$$|P_{10}| = |P_{01}| = k \quad \text{y} \quad |P_{00}| = |P_{11}| = 5 - k.$$

Sea $R(P_{ab})$ el conjunto de residuos asignados a las posiciones de $P_{ab}$. Las condiciones del Paso 2 exigen que:
- $R(P_{00})$ y $R(P_{01})$ sean subconjuntos complementarios en $\{0, 1, 2, 3, 4\}$.
- $R(P_{00})$ y $R(P_{10})$ sean subconjuntos complementarios en $\{0, 1, 2, 3, 4\}$.
- $R(P_{10})$ y $R(P_{11})$ sean subconjuntos complementarios en $\{0, 1, 2, 3, 4\}$.

Por lo tanto, una vez elegido el subconjunto $U = R(P_{00}) \subseteq \{0, 1, 2, 3, 4\}$ de tamaño $5-k$, queda determinado que $R(P_{11}) = U$ y $R(P_{01}) = R(P_{10}) = \{0, 1, 2, 3, 4\} \setminus U$.
- Hay $\binom{5}{5-k} = \binom{5}{k}$ formas de elegir el subconjunto $U$.
- Hay $((5-k)!)^2$ formas de permutar los elementos de $U$ en $P_{00}$ y $P_{11}$.
- Hay $(k!)^2$ formas de permutar los elementos de $\{0, 1, 2, 3, 4\} \setminus U$ en $P_{01}$ y $P_{10}$.

Por simetría entre los $5$ residuos $\{0, 1, 2, 3, 4\}$, exactamente $\frac{4}{5}$ de estas asignaciones cumplen que $r_9 \neq 0$. Así, para una secuencia $(t_0, \dots, t_9)$ fija con parámetro $k$, el número de formas válidas de asignar los residuos es:
$$\frac{4}{5} \binom{5}{k} ((5-k)!)^2 (k!)^2 = \frac{4}{5} \cdot 5! \, k! (5-k)! = 96 \, k! (5-k)!.$$

---

### Paso 4: Conteo de secuencias $(t_0, \dots, t_9)$ según el valor de $k$
Un índice $i$ pertenece a $P_{10}$ si $c_i = 0$ y $t_i = 1$. En la secuencia extendida $(c_0, t_0, t_1, \dots, t_8, t_9) = (0, t_0, t_1, \dots, t_8, 0)$, esto ocurre exactamente cuando hay una transición de $0$ a $1$. Por lo tanto, $k = |P_{10}|$ es el número de bloques (rachas) de $1$'s en la subsecuencia $(t_0, t_1, \dots, t_8)$, la cual está formada por cinco $1$'s y cuatro $0$'s.

Para cada $k \in \{1, 2, 3, 4, 5\}$:
- Hay $\binom{5-1}{k-1} = \binom{4}{k-1}$ formas de dividir los cinco $1$'s en $k$ bloques no vacíos.
- Hay $\binom{4+1}{k} = \binom{5}{k}$ formas de intercalar estos $k$ bloques entre los cuatro $0$'s.

Multiplicando por el número de asignaciones de residuos y sumando sobre todos los valores posibles de $k$:
$$\text{Total} = \sum_{k=1}^{5} \binom{4}{k-1} \binom{5}{k} \cdot 96 \, k! (5-k)!$$

Dado que $\binom{5}{k} k! (5-k)! = 5! = 120$ para todo $k$, obtenemos:
$$\text{Total} = 96 \cdot 120 \sum_{k=1}^{5} \binom{4}{k-1} = 11520 \cdot 2^4 = 11520 \cdot 16 = 184320.$$

\boxed{184320}