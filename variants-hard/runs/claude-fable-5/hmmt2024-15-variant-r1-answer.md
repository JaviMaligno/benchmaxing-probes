## Planteamiento

Buscamos grafos 3-regulares con 12 vértices etiquetados (las ciudades son distinguibles) donde cada par de vértices tiene exactamente 0 o 2 vecinos comunes.

## Clasificación de las componentes conexas

**Caso con triángulo.** Si $u,v,w$ forman un triángulo, la arista $uv$ tiene a $w$ como vecino común, así que debe tener exactamente 2: existe $x$ adyacente a $u$ y $v$. Ahora la arista $uw$ tiene a $v$ como vecino común y necesita otro; como los vecinos de $u$ son exactamente $v,w,x$, ese segundo vecino común debe ser $x$, luego $w \sim x$. Análogamente con $vw$. Entonces $\{u,v,w,x\}$ forman un $K_4$ y los cuatro vértices ya tienen grado 3, así que la componente es exactamente $K_4$.

**Caso sin triángulos.** Los pares adyacentes tienen 0 vecinos comunes, y todo par a distancia 2 debe tener exactamente 2. Tomemos $v$ con vecinos $a,b,c$. Cada par como $\{a,b\}$ tiene a $v$ y exactamente un vecino común más, llamémoslo $x_{ab}$ (y análogamente $x_{ac}, x_{bc}$). Estos tres son distintos: si $x_{ab}=x_{ac}$, ese vértice compartiría 3 vecinos con $v$. Además $x_{ab} \not\sim x_{ac}$ (formarían triángulo con $a$). El par $\{x_{ab}, x_{ac}\}$ comparte a $a$ y necesita un segundo vecino común, que debe ser el tercer vecino de ambos; iterando sobre los tres pares, los tres vértices $x_{\cdot\cdot}$ comparten un único vértice nuevo $z$. Resultan 8 vértices, todos de grado 3: la componente es exactamente el **cubo $Q_3$**.

Por tanto, cada componente es $K_4$ (4 vértices) o $Q_3$ (8 vértices). Con 12 vértices hay dos opciones:

- **Tres copias de $K_4$**, o
- **Un $Q_3$ y un $K_4$**.

## Conteo

**Tres $K_4$:** partimos los 12 vértices en 3 conjuntos no ordenados de 4:
$$\frac{12!}{(4!)^3 \cdot 3!} = \frac{479001600}{13824 \cdot 6} = 5775.$$

**$Q_3 + K_4$:** elegimos los 4 vértices del $K_4$ de $\binom{12}{4} = 495$ formas. Sobre los 8 vértices restantes, el número de copias etiquetadas de $Q_3$ es
$$\frac{8!}{|\mathrm{Aut}(Q_3)|} = \frac{40320}{48} = 840,$$
ya que $|\mathrm{Aut}(Q_3)| = 2^3 \cdot 3! = 48$. Esto da $495 \cdot 840 = 415800$.

**Total:** $5775 + 415800 = 421575$.

$$\boxed{421575}$$