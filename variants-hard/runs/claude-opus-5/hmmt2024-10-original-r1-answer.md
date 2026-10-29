## Planteamiento

Un polinomio es *splitty* exactamente cuando es reducible módulo todo primo $p$.

**Caso 1: $f$ reducible sobre $\mathbb{Z}$.** Entonces es trivialmente splitty.

Como $x^4+16x^2+n>0$ para $n>0$, no hay raíces reales, así que la factorización debe ser en dos cuadráticos:
$$(x^2+ax+b)(x^2-ax+c),\qquad b+c-a^2=16,\quad a(c-b)=0,\quad bc=n.$$

- Si $a=0$: $b+c=16$, $bc=n$, es decir $n=64-t^2$ con $t=8-b$. Esto da
$$n\in\{64,63,60,55,48,39,28,15\}.$$
- Si $a\neq0$: $b=c$, $2b=16+a^2$, luego $a=2s$, $b=8+2s^2$ y $n=b^2$ (un cuadrado perfecto). Con $n\le100$: $s=0\Rightarrow n=64$, $s=1\Rightarrow n=100$ (en efecto $x^4+16x^2+100=(x^2+2x+10)(x^2-2x+10)$).

**Caso 2: $f$ irreducible.** Por Chebotarev, $f$ es reducible módulo todo primo si y solo si su grupo de Galois no contiene un ciclo de longitud 4. Para un polinomio bicuadrático $x^4+px^2+q$ irreducible, el grupo es $C_4$, $D_4$ o $V_4$, y es $V_4$ (sin 4-ciclos) exactamente cuando $q$ es un cuadrado perfecto. Si $q$ no es cuadrado, el grupo es $C_4$ o $D_4$, ambos con un 4-ciclo, luego $f$ es irreducible módulo algún primo.

Por tanto, $f$ es splitty $\iff$ $n$ es un cuadrado perfecto **o** $64-n$ es un cuadrado perfecto.

## Suma

Cuadrados perfectos $\le 100$:
$$1+4+9+16+25+36+49+64+81+100=385.$$

Valores $n=64-t^2$ no cuadrados: $15,28,39,48,55,60,63$ (el $64$ ya está contado):
$$15+28+39+48+55+60+63=308.$$

Total: $385+308=693$.

\boxed{693}