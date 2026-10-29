# Resolución paso a paso

## 1. Identificar las parábolas

Los vértices de las parábolas $y=(x-a)^2$ están en $a = 0, 5, 10, \ldots, 45$, es decir, hay **10 parábolas**, con los vértices separados por 5 unidades.

## 2. Contar intersecciones sin superposiciones

Para $k > 0$, cada parábola corta a la recta $y = k$ en dos puntos:
$$x = a \pm \sqrt{k}$$

En total habría $10 \times 2 = 20$ puntos, salvo que algunos coincidan. Como queremos **19 puntos distintos**, debe haber exactamente **una coincidencia** (dos intersecciones que caen en el mismo punto).

## 3. ¿Cuándo coinciden dos intersecciones?

Un punto de la recta $y=k$ pertenece a la parábola de vértice $a$ solo si $a = x \pm \sqrt{k}$; por tanto, como máximo **dos** parábolas pasan por un mismo punto de la recta.

Dos intersecciones de parábolas con vértices $a_i < a_j$ coinciden cuando:
$$a_i + \sqrt{k} = a_j - \sqrt{k} \implies 2\sqrt{k} = a_j - a_i = 5m$$
donde $m = j - i \in \{1, \ldots, 9\}$. Luego $\sqrt{k} = \frac{5m}{2}$.

Para un $m$ dado, el número de pares de parábolas separadas por $m$ posiciones es $10 - m$, y cada par produce exactamente una coincidencia. Así:
$$\text{puntos distintos} = 20 - (10 - m)$$

## 4. Imponer que haya 19 puntos

$$20 - (10 - m) = 19 \implies m = 9$$

Este es el único valor posible (con $m=9$ solo el par de parábolas extremas, $a=0$ y $a=45$, produce una coincidencia).

## 5. Calcular $k$

$$\sqrt{k} = \frac{5 \cdot 9}{2} = \frac{45}{2} \implies k = \left(\frac{45}{2}\right)^2 = \frac{2025}{4}$$

**Verificación:** con $\sqrt{k}=22{,}5$, los puntos son $a \pm 22{,}5$. El punto $0 + 22{,}5 = 22{,}5$ coincide con $45 - 22{,}5 = 22{,}5$, y todos los demás son distintos: 9 puntos negativos/fraccionarios a la izquierda, el punto doble $22{,}5$ y 9 puntos a la derecha, en total $9+1+9=19$. ✔

$$\boxed{\dfrac{2025}{4}}$$