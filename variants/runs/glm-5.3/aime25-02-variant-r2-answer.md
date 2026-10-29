## Planteamiento

Coloco $P$ en el origen. Sea $e_1$ el vector unitario a lo largo de $\overline{PQ}$ y $e_2$ el unitario a lo largo de $\overline{PR}$, con $e_1\times e_2 = \sin\theta = s$, donde $\theta = \angle QPR$. Todo punto a distancia $x$ sobre $\overline{PQ}$ es $x\,e_1$, y a distancia $y$ sobre $\overline{PR}$ es $y\,e_2$.

**Posiciones** (con $PQ = 3+9+6 = 18$ y $PR = 5+15+10 = 30$):

$$D = 3e_1,\quad E = 12e_1,\quad Q = 18e_1,\qquad F = 5e_2,\quad G = 20e_2,\quad R = 30e_2.$$

**Reflexiones:** $M = 2F - D = -3e_1 + 10e_2$ y $N = 2E - G = 24e_1 - 20e_2$.

## Área del cuadrilátero $DEGF$

Con la fórmula del shoelace (los productos cruz $\times$ llevan el factor $s$):

$$[DEGF] = \tfrac12\big|D\times E + E\times G + G\times F + F\times D\big| = \tfrac12\big|0 + 240s + 0 - 15s\big| = 112{,}5\,s.$$

## Área del heptágono $PFNQREM$

Vértices en orden: $P,\ F,\ N,\ Q,\ R,\ E,\ M$:

$$P\times F = 0,\quad F\times N = -120s,\quad N\times Q = 360s,\quad Q\times R = 540s,$$
$$R\times E = -360s,\quad E\times M = 120s,\quad M\times P = 0.$$

Suma $= 540s$, de modo que:

$$[PFNQREM] = \tfrac12\cdot 540s = 270\,s.$$

(Verificado numéricamente con $\cos\theta = 0.8$: ambos lados dan $162$, y el heptágono resulta simple, sin auto-intersecciones.)

## Conclusión

Ambas áreas son proporcionales a $s$, así que su cociente es constante para todo triángulo:

$$\frac{[PFNQREM]}{[DEGF]} = \frac{270}{112{,}5} = \frac{12}{5}.$$

Por lo tanto:

$$[PFNQREM] = \frac{12}{5}\cdot 300 = 720.$$

*Nota:* los datos fuerzan formalmente $s = \tfrac{300}{112.5} = \tfrac83 > 1$, es decir, ningún triángulo real realiza exactamente essas cifras; pero como el área pedida es siempre exactamente $\tfrac{12}{5}$ del área dada (identidad válida para cualquier $\triangle PQR$ con esa configuración), el valor determinado es único.

$$\boxed{720}$$