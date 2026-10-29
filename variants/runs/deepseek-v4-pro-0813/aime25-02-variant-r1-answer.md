<system-reminder>
This is a math problem. You have access to a Python environment. Use Python for all computation where appropriate.
</system-reminder>

Voy a verificar los cálculos con Python.

<｜DSML｜tool_calls>
<｜DSML｜invoke name="exec_command">
<｜DSML｜parameter name="cmd" string="true">python3 -c "
import sympy as sp
# Use symbolic det = D (area of parallelogram for v=PQ, w=PR)
# Let v, w be vectors; we'll represent positions as coefficients.
# We'll compute determinant sums symbolically using a 2x2 determinant with det(v,w)=D.
# Represent each point as (a,b) meaning a*v + b*w.
# Cross product of (a1,b1) and (a2,b2) is (a1*b2 - a2*b1)*D.

def cross(p1, p2, D):
    a1,b1 = p1; a2,b2 = p2
    return (a1*b2 - a2*b1)*D

# Points
P = (0,0)
D = (sp.Rational(1,6), 0)
E = (sp.Rational(2,3), 0)
Q = (1, 0)
F = (0, sp.Rational(1,6))
G = (0, sp.Rational(2,3))
R = (0, 1)
M = (sp.Rational(-1,6), sp.Rational(1,3))   # 2F - D = 2*(0,1/6) - (1/6,0)
N = (sp.Rational(4,3), sp.Rational(-2,3))   # 2E - G = 2*(2/3,0) - (0,2/3)

Dv = sp.Symbol('D')
# Area DEGF (order D,E,G,F)
verts_deggf = [D,E,G,F]
S1 = sum(cross(verts_deggf[i], verts_deggf[(i+1)%4], Dv) for i in range(4))
print('DEGF sum/det =', sp.simplify(S1/Dv))
print('DEGF area = 1/2 * (', sp.simplify(S1/Dv), ') * det =', sp.simplify(sp.Rational(1,2)*S1))

# Area heptagon PFNQREM (order given)
verts_hept = [P,F,N,Q,R,E,M]
S2 = sum(cross(verts_hept[i], verts_hept[(i+1)%7], Dv) for i in range(7))
print('Heptagon sum/det =', sp.simplify(S2/Dv))
print('Heptagon area = 1/2 * (', sp.simplify(S2/Dv), ') * det =', sp.simplify(sp.Rational(1,2)*S2))

# Ratio
print('Ratio hept/DEGF =', sp.simplify(S2/S1))
"
</｜DSML｜parameter>
</｜DSML｜invoke>
</｜DSML｜tool_calls>## Razonamiento paso a paso

Analicemos la geometría del problema.

**Puntos sobre $\overline{PQ}$:** $P, D, E, Q$ en ese orden, con $PD = 3$, $DE = 9$, $EQ = 6$. Así que las coordenadas a lo largo de $PQ$ (tomando $P$ como origen y dirección hacia $Q$) son:
- $P$ en posición $0$
- $D$ en posición $3$
- $E$ en posición $12$
- $Q$ en posición $18$

Por tanto $DE = 9$ y $DQ = 6$, $PQ = 18$.

**Puntos sobre $\overline{PR}$:** $P, F, G, R$ en ese orden, con $PF = 5$, $FG = 15$, $GR = 10$. Coordenadas a lo largo de $PR$:
- $P$ en posición $0$
- $F$ en posición $5$
- $G$ en posición $20$
- $R$ en posición $30$

Por tanto $FG = 15$, $GR = 10$, $PR = 30$.

**Reflexiones:**
- $M$ es el reflejo de $D$ a través de $F$. Es decir, $F$ es el punto medio de $DM$.
- $N$ es el reflejo de $G$ a través de $E$. Es decir, $E$ es el punto medio de $GN$.

**Área dada:** $[DEGF] = 300$.

Necesito hallar el área del heptágono $PFNQREM$.

Voy a plantear un sistema de coordenadas robusto. Tomaré $P = (0,0)$, y colocaré $Q$ y $R$ en posiciones convenientes.

Sea el ángulo $\angle QPR = \theta$, sea $a = \sin\theta$.

---

Primero coloquemos coordenadas:

- $P = (0,0)$
- $Q = (18, 0)$ (a lo largo del eje $x$)
- $R = (30\cos\theta, 30\sin\theta)$

Entonces:
- $D = (3, 0)$
- $E = (12, 0)$
- $F = 5 \cdot \frac{R}{30} = (5\cos\theta, 5\sin\theta)$
- $G = 20 \cdot \frac{R}{30} = (20\cos\theta, 20\sin\theta)$

**Área de $DEGF$:**

Los vértices en orden alrededor del polígono $DEGF$: $D = (3,0)$, $E = (12,0)$, $G = (20\cos\theta, 20\sin\theta)$, $F = (5\cos\theta, 5\sin\theta)$.

Uso la fórmula del área por determinantes (shoelace). Calculemos:

$A = \frac{1}{2}\left| \sum (x_i y_{i+1} - x_{i+1} y_i) \right|$

- $D \to E$: $x_D y_E - x_E y_D = 3\cdot0 - 12\cdot0 = 0$
- $E \to G$: $x_E y_G - x_G y_E = 12 \cdot 20\sin\theta - 20\cos\theta \cdot 0 = 240\sin\theta$
- $G \to F$: $x_G y_F - x_F y_G = 20\cos\theta \cdot 5\sin\theta - 5\cos\theta \cdot 20\sin\theta = 0$
- $F \to D$: $x_F y_D - x_D y_F = 5\cos\theta\cdot0 - 3\cdot5\sin\theta = -15\sin\theta$

Suma $= 240\sin\theta - 15\sin\theta = 225\sin\theta$.

Área $= \frac{1}{2} \cdot 225 \sin\theta = \frac{225}{2}\sin\theta$.

Dado $[DEGF]=300$: $\frac{225}{2}\sin\theta = 300$, así que $\sin\theta = \frac{600}{225} = \frac{8}{3}$.

¡Espera! $\sin\theta = \frac{8}{3} > 1$ es imposible. Debo revisar la orientación o mis coordenadas.

Revisemos: Los puntos $D, E, G, F$. $D$ y $E$ están en $PQ$, $F$ y $G$ en $PR$. El cuadrilátero $DEGF$ tiene lados: $DE$ (sobre $PQ$), $EG$, $GF$ (sobre $PR$), $FD$.

Orden correcto de vértices del cuadrilátero: siguiendo el borde, sería $D \to E \to G \to F \to D$. Correcto como lo hice.

Entonces el área de $DEGF$ en función de $\sin\theta$:

$$[DEGF] = [PEG] - [PDF]$$

- $[PEG] = \frac{1}{2} \cdot PE \cdot PG \cdot \sin\theta = \frac{1}{2}\cdot 12 \cdot 20 \cdot \sin\theta = 120\sin\theta$
- $[PDF] = \frac{1}{2} \cdot PD \cdot PF \cdot \sin\theta = \frac{1}{2}\cdot 3 \cdot 5 \cdot \sin\theta = \frac{15}{2}\sin\theta$

Restando: $[DEGF] = 120\sin\theta - \frac{15}{2}\sin\theta = \frac{240-15}{2}\sin\theta = \frac{225}{2}\sin\theta$.

Lo mismo. Entonces $\sin\theta = \frac{600}{225} = \frac{8}{3}$, imposible.

Esto sugiere que la "área" de 300 es mucho más grande de lo que permite el ángulo. Hmm, espera... Quizá el problema no exige que $F$ esté entre $P$ y $R$ de forma que $PF=5$, $FG=15$, $GR=10$, $PR=30$. Eso ya lo consideré.

Reconsideremos: a lo mejor $D, E$ en $PQ$ y $F, G$ en $PR$, y el cuadrilátero $DEGF$ es un trapecio con $DE \parallel FG$? No, $DE$ está en $PQ$ y $FG$ en $PR$; no son paralelos en general.

Pero $[DEGF] = 300$ con $\sin\theta \le 1$ daría el máximo $[DEGF] = 112.5$. Así que 300 es imposible si mi lectura es correcta.

Oh, quizá la orientación del cuadrilátero es $D \to F \to G \to E \to D$ (es decir, un cuadrilátero cruzado o el otro orden), pero el área convexa sería la misma. En realidad la región $DEGF$ con vértices en ese orden forma un cuadrilátero convexo con lados $DE$, $EG$, $GF$, $FD$. No puede tener área mayor que $[PEG] \le 120$. Contradicción.

Quizá hay algo raro: perhaps $E$ y $D$ están al revés, o hay que interpretar $DE=9$ como distancia y $EQ=6$, correcto.

Hmm, déjame reconsiderar. Quizá la reflexión cambia: $M$ reflejo de $D$ a través de $F$ significa $F$ es punto medio de $DM$, pero $M$ puede no estar... no importa.

Espera, hay un problema: el área del **cuadrilátero $DEGF$** — si $D, E, G, F$ están en ese orden cíclico, pero ¿y si el cuadrilátero se llama $DEGF$ con vértices $D, E, G, F$ en orden, formando una figura cóncava o cruzada? Con $D$ y $E$ en el rayo $PQ$ y $F$ y $G$ en $PR$, el orden convexo alrededor es $D, E, G, F$ (si $E$ está "más allá" de $D$ y $G$ "más allá" de $F$). Es convexo.

No hay forma de alcanzar área 300. A menos que... los puntos no estén en un triángulo, sino que $PQ$ y $PR$ formen un ángulo obtuso, pero aún así $\sin\theta \le 1$ siempre. El área máxima de $DEGF$ es cuando $\sin\theta=1$: $112.5$.

Entonces 300 parece inconsistente... a menos que la interpretación de la reflexión u otra cosa afecte, o que el área dada sea de otra figura.

Releamos: "Quadrilateral $DEGF$ has area $300$." Tal cual.

Hmm, quizás cometí un error: $D$, $E$, $Q$ en orden, pero $E$ a 12 y $Q$ a 18. $DE = 9$, $EQ=6$: correcto.

$F$, $G$, $R$: $PF=5$, $FG=15$, $GR=10$: $PR = 30$. Correcto.

Calculo $[PEG] = \frac12 \cdot 12 \cdot 20 \sin\theta = 120 \sin\theta$. Máximo 120. $[DEGF] \le 120$. Contradicción con 300.

Por lo tanto, probablemente el problema tiene un dato diferente o hay un error de transcripción. Pero es un problema de competencia; tal vez los puntos no están en el mismo lado, o el cuadrilátero $DEGF$ se interpreta de otra manera.

Espera — quizá los puntos $D, E$ NO están sobre un lado sino que... no, dice "on side $\overline{PQ}$".

Déjame considerar la posibilidad: tal vez $P, D, E, Q$ y $P, F, G, R$ están sobre lados que NO comparten el vértice $P$ en común de la forma que asumo. Actually they do share $P$: both lists start with $P$.

Hmm, quizá hay un error y $FG = 15$ debería ser otro valor, o quizás el área de $DEGF$ no es la del cuadrilátero pequeño.

En realidad, revisemos el área de $DEGF$ de nuevo: podríamos estar confundiéndonos entre el cuadrilátero con vértices $D, E, G, F$ (que tiene $DE$ y $FG$ como lados no paralelos) y el cuadrilátero con vértices $D, E, G, F$ tomados en orden **D → E → G → F**.

Calculo vía shoelace correctamente:
- $D(3,0)$, $E(12,0)$, $G(20c,20s)$, $F(5c,5s)$, donde $c=\cos\theta$, $s=\sin\theta$.

- $D\to E$: $3\cdot0 - 12\cdot0 = 0$
- $E\to G$: $12 \cdot 20s - 20c\cdot0 = 240s$
- $G\to F$: $20c\cdot5s - 5c\cdot20s = 0$
- $F\to D$: $5c\cdot0 - 3\cdot5s = -15s$

Suma = $240s - 15s = 225s$. Área = $112.5 s$. Max $112.5$.

Así que realmente imposible.

Unless... the problem intends for $PQ$ and $PR$ to be perpendicular? Entonces $s=1$ y área sería $112.5$, no $300$.

Quizás los datos son: $PD=3$, $DE=9$, $EQ=6$ (total 18) y $PF=5$, $FG=15$, $GR=10$ (total 30). Si en cambio el cuadrilátero fuera $DEGF$ con $D$ y $G$ conectados por un lado y $E$ y $F$ conectados... no, el nombre prescribiría orden.

Wait — maybe I should double-check whether $D, E, F, G$ might be arranged such that $DEGF$ is a self-intersecting quadrilateral whose "area" is computed differently, but competitions use convex area. Still bounded by triangle $PEG$ area ≤ 120.

Por lo tanto hay un error en el enunciado tal como lo recibí. Sin embargo, tal vez la reflexión da pistas: $M$ reflejo de $D$ a través de $F$, $N$ reflejo de $G$ a través de $E$. Esto sugiere que el problema original puede tener un área dada diferente.

Déjame buscar: este problema se asemeja a un problema de AIME. Probablemente es AIME y el área del heptágono es un número entero específico. Si el cuadrilátero tuviera área $\frac{225}{2} \cdot \frac{4}{5} = 90$ (con $\sin\theta = 4/5$) u otro, podríamos proceder.

En realidad, observemos: si $[DEGF]=300$, y la fórmula es $\frac{225}{2}\sin\theta$, entonces $\sin\theta = \frac{600}{225} = \frac{8}{3}$, imposible. Esto confirma inconsistencia.

Sin embargo, quizá la "altura" no se restringe por $\sin\theta \le 1$ porque... no, siempre lo está.

Consideremos otra interpretación: quizás $D$ y $E$ están en $\overline{PQ}$ y $F$ y $G$ están en $\overline{PR}$, pero el cuadrilátero $DEGF$ no es convexo con esos cuatro puntos en orden; en su lugar, los puntos están en una configuración donde $E$ está entre $D$ y $Q$ (sí) y $G$ entre $F$ y $R$ (sí). La figura convexa $D$–$E$–$G$–$F$ tiene área $[PEG]-[PDF]$.

Máximo posible: $120 - 0 = 120$ cuando $\theta \to 90°$ y $D \to P$... no exactamente.

Dado que todo es inconsistente, probablemente hay un typo en el reporte. Aun así, debo dar una respuesta. Déjame pensar si hay una versión estándar.

Este problema se parece mucho a un problema AIME 2023 o similar que involucra heptágono. Busco en memoria: "In triangle PQR, points P, D, E, Q lie in that order..." con $PD=3$, $DE=9$, $EQ=6$ — estos números (3, 9, 6) y (5, 15, 10) son proporcionales (×5/3). La reflexión de $D$ por $F$ y $G$ por $E$. Área del cuadrilátero 300. Heptágono $PFNQREM$.

Probablemente la respuesta sea un número como 750 o similar. Déjame trabajar algebraicamente sin fijar $\sin\theta \le 1$, tratando $\sin\theta$ como variable $s$ (la relación área real puede ser $\frac{225}{2}s=300 \Rightarrow s=\frac{8}{3}$ — no es válido físicamente, pero quizá el problema usa áreas "con signo" o lados no necesariamente en el plano con ese ángulo).

Alternativamente, puede que el triángulo sea tal que $\angle QPR$ no es el ángulo entre $PQ$ y $PR$, sino que la figura es 3D. Improbable.

Déjame reconsiderar las longitudes. Quizá $EQ = 6$ y $DQ = 6$, total $PQ = 18$. Y $GR=10$, $FR=10$, $PR=30$. Es decir, $PR = 30$. Quizás en el problema real $FG=15$ pero $PF=5$ y $GR=10$, y la relación es que $PG=20$, $PE=12$.

Área $DEGF$ = $[PEG] - [PDF]$. Si hacemos $[PEG] = \frac12 \cdot PE \cdot PG \cdot \sin\theta$. Con $\sin\theta = 1$, $[PEG]=120$. No llega a 300.

Entonces hay que revisar si $E, G$ son los "puntos exteriores". Quizá la configuración es que $D$ y $E$ están sobre el segmento $PQ$ pero extendido, o que el cuadrilátero es $D$–$F$–$G$–$E$ con lados cruzados... No mejora.

Si en cambio el área del cuadrilátero fuera $[DEGF] = [PDF] + [PEG]$ en una configuración donde $D$ está en un lado y $F$ en el otro formando un cuadrilátero cóncavo... pero geométricamente $D, E$ en el mismo rayo y $F, G$ en el otro rayo, el polígono $DEGF$ es convexo.

Creo que hay un error tipográfico. A pesar de ello, intentemos asumir que el área dada es correcta con $\sin\theta = \frac{8}{3}$ (ignorando la restricción) y completar el álgebra para obtener una respuesta, porque quizá el problema real tiene otras longitudes pero estructura idéntica, y la respuesta sigue un patrón.

Voy a configurar coordenadas generales usando vectores y áreas con la convención de áreas orientadas (que permiten $\sin\theta > 1$ formalmente). Usaré un enfoque vectorial con $\vec{v} = \overrightarrow{PQ}$, $\vec{w} = \overrightarrow{PR}$, y usaré determinantes.

## Enfoque vectorial

Sea $\vec{v} = \overrightarrow{PQ}$ con $|\vec v| = 18$, y $\vec w = \overrightarrow{PR}$ con $|\vec w| = 30$. El área con signo del paralelogramo es $\det(\vec v, \vec w)$.

Posiciones desde $P$:
- $D = \frac{3}{18}\vec v = \frac{1}{6}\vec v$
- $E = \frac{12}{18}\vec v = \frac{2}{3}\vec v$
- $Q = \vec v$
- $F = \frac{5}{30}\vec w = \frac{1}{6}\vec w$
- $G = \frac{20}{30}\vec w = \frac{2}{3}\vec w$
- $R = \vec w$

Reflexiones:
- $M$: $F$ es punto medio de $DM$, entonces $M = 2F - D = 2\cdot\frac16\vec w - \frac16\vec v = \frac13\vec w - \frac16\vec v$.
- $N$: $E$ es punto medio de $GN$, entonces $N = 2E - G = 2\cdot\frac23\vec v - \frac23\vec w = \frac43\vec v - \frac23\vec w$.

Área $DEGF$: vértices $D, E, G, F$. Como calculamos, área orientada $\frac12[\det(D,E)+\det(E,G)+\det(G,F)+\det(F,D)]$.

Calculemos con determinantes:
- $\det(D,E) = \det(\frac16 v, \frac23 v) = 0$
- $\det(E,G) = \det(\frac23 v, \frac23 w) = \frac49 \det(v,w)$
- $\det(G,F) = \det(\frac23 w, \frac16 w) = 0$
- $\det(F,D) = \det(\frac16 w, \frac16 v) = \frac1{36}\det(w,v) = -\frac1{36}\det(v,w)$

Suma $= \frac49 - \frac1{36} = \frac{16-1}{36} = \frac{15}{36} = \frac{5}{12}$ veces $\det(v,w)$.

Área $= \frac12 \cdot \frac{5}{12}\det(v,w) = \frac{5}{24}\det(v,w)$.

Espera, verifiquemos con lo anterior: $\det(v,w) = |v||w|\sin\theta = 18\cdot30\sin\theta = 540\sin\theta$. Entonces área $= \frac{5}{24}\cdot540\sin\theta = \frac{2700}{24}\sin\theta = 112.5\sin\theta$. ✓. Coincide, $[DEGF]=112.5\sin\theta$.

Con $[DEGF]=300$: $\frac{5}{24}\det = 300$, así que $\det(v,w) = 300\cdot\frac{24}{5} = 1440$.

Entonces $\det(v,w) = 1440$. Nota: $\det(v,w) = 540\sin\theta$, daría $\sin\theta = \frac{1440}{540} = \frac{8}{3}$, confirmando la inconsistencia física. Pero formalmente usemos $\det = 1440$ para áreas con signo y continuemos. Es posible que la respuesta final sea un número limpio pese a la inconsistencia.

Ahora calculemos el área del heptágono $PFNQREM$. Los vértices en orden: $P, F, N, Q, R, E, M$.

Listemos los vectores posición:
- $P = 0$
- $F = \frac16 w$
- $N = \frac43 v - \frac23 w$
- $Q = v$
- $R = w$
- $E = \frac23 v$
- $M = \frac13 w - \frac16 v$

El área del heptágono (orientada) es $\frac12$ de la suma de determinantes de vértices consecutivos (cerrando con $P$).

Calculemos término a término:

1. $\det(P, F) = \det(0, \frac16 w) = 0$
2. $\det(F, N) = \det(\frac16 w, \frac43 v - \frac23 w)$
   $= \frac16 \cdot \frac43 \det(w, v) - \frac16\cdot\frac23\det(w,w)$
   $= \frac{4}{18}\det(w,v) = -\frac{2}{9}\det(v,w)$
3. $\det(N, Q) = \det(\frac43 v - \frac23 w, v)$
   $= \frac43\det(v,v) - \frac23\det(w,v) = 0 - \frac23(-\det(v,w)) = \frac23\det(v,w)$
4. $\det(Q, R) = \det(v, w)$
5. $\det(R, E) = \det(w, \frac23 v) = \frac23\det(w,v) = -\frac23\det(v,w)$
6. $\det(E, M) = \det(\frac23 v, \frac13 w - \frac16 v)$
   $= \frac23\cdot\frac13\det(v,w) - \frac23\cdot\frac16\det(v,v)$
   $= \frac29\det(v,w)$
7. $\det(M, P) = \det(\frac13 w - \frac16 v, 0) = 0$

Suma total $S$:
$S = -\frac29 + \frac23 + 1 - \frac23 + \frac29 = 1$ veces $\det(v,w)$.

Verifiquemos: $-\frac29 + \frac29 = 0$, $+\frac23 - \frac23 = 0$, queda $1$. Entonces $S = \det(v,w)$.

Área heptágono $= \frac12 \det(v,w) = \frac12 \cdot 1440 = 720$.

¡Excelente! Área $= 720$. Esto es un resultado limpio y probablemente la respuesta esperada.

Espera, pero verifiquemos la fórmula más cuidadosamente porque el área usa valor absoluto y hay que asegurar que el polígono no se auto-interseca. Asumimos que el orden $P, F, N, Q, R, E, M$ es correcto.

La suma de determinantes dio exactamente $\det(v,w)$, lo cual es elegante, sugiriendo que la respuesta 720 es intencional.

También notemos que la inconsistencia de $\sin\theta>1$ sugiere que quizás en el problema real el área del cuadrilátero fuera 112.5 y la respuesta 720 sea correcta en proporción. De hecho, la relación es: $[hept]/[DEGF] = 720/300 = 12/5 = 2.4$. Y $\frac{1/2 \det}{5/24 \det} = \frac{1/2}{5/24} = \frac{12}{5} = 2.4$. ✓. Así que independientemente del valor real de $\det$, el heptágono es $\frac{12}{5}$ veces el cuadrilátero. Si el área del cuadrilátero fuera 112.5, el heptágono sería 270. Pero con 300, es 720.

La respuesta es 720.

Déjame verificar todo con Python rápidamente para asegurar los