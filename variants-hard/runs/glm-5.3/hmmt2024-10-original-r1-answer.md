**Planteamiento.** Un polinomio mónico de grado 4 es *splitty* si y solo si $\bar f \in \mathbb{F}_p[x]$ es reducible para todo primo $p$ (la factorización trivial está excluida porque el coeficiente de $x^4$ es $1 \not\equiv 0 \bmod p$).

**Reductibilidad sobre $\mathbb{Q}$.** Para $f = x^4 + 16x^2 + n$, toda factorización tiene la forma $(x^2+bx+c)(x^2-bx+c')$, con $c'^2... $; analizando coeficientes: o bien $b=0$, $c+c'=16$, $cc'=n$ (posible $\iff 64-n$ es cuadrado), o bien $c=c'=\sqrt n$ y $2\sqrt n - b^2 = 16$ (posible $\iff n=k^2$ con $2k-16$ cuadrado). No hay raíces racionales. Luego $f$ es reducible sobre $\mathbb{Q}$ exactamente para
$$n \in \{64-m^2 : 0\le m\le 7\} = \{64,63,60,55,48,39,28,15\} \cup \{100\},$$
y todos estos son splitty (los grados de los factores se preservan mod $p$).

**Caso irreducible.** Para $f$ par irreducible, $G \subseteq D_4$, y $G$ es transitive: $G \in \{D_4, C_4, V_4\}$. Además $\operatorname{disc}(x^4+bx^2+c) = 16c(b^2-4c)^2$, así que
$$\operatorname{disc}(f) = 256\,n\,(64-n)^2.$$
- Si $G$ contiene un 4-ciclo ($C_4, D_4$), por Chebotarev hay infinitos primos con $\bar f$ irreducible → **no** splitty.
- Si $G = V_4$ (sin 4-ciclos), todo primo $p \nmid \operatorname{disc}$ da Frobenius de tipo $(1,1,1,1)$ o $(2,2)$ → reducible; y para $p \mid \operatorname{disc}$ (incluido $p=2$, donde $\bar f = x^4+\bar n$ es reducible) también lo es. → **splitty**.

Como $G \subseteq A_4 \iff \operatorname{disc}$ cuadrado $\iff n$ cuadrado, los irreducibles splitty son exactamente los $n = k^2$ irreducibles: $k \in \{1,\dots,7,9\}$, es decir $n \in \{1,4,9,16,25,36,49,81\}$ (verificado p. ej. $n=16$: $(x^2+2x+3)(x^2-2x+3)$ mod 7).

**Conclusión.** Splitty $\iff n$ cuadrado o $n = 64 - m^2$:
$$\{1,4,9,15,16,25,28,36,39,48,49,55,60,63,64,81,100\}.$$
Suma: $385 + 308 = 693$.

$\boxed{693}$