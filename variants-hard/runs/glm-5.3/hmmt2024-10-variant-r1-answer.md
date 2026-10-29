## Planteamiento

Como $f(x) = x^4+20x^2+n$ es mónico, $f \bmod p$ siempre tiene grado $4$. Como $\mathbb{F}_p[x]$ es dominio íntegro, de $f \equiv g_p h_p \pmod p$ con $\deg g_p, \deg h_p \le 3$ se sigue que $f \bmod p$ es **reducible** (ambos factores de grado $\ge 1$). Además, si $p \mid \operatorname{disc}(f)$, entonces $f \bmod p$ no es separable, y sobre $\mathbb{F}_p$ un polinomio irreducible es separable; luego $f \bmod p$ es reducible automáticamente.

**Conclusión:** $f$ es *breakable* $\iff$ $f \bmod p$ es reducible para todo primo $p$ $\iff$ (para primos $p \nmid \operatorname{disc}$) el grupo de Galois $G$ no contiene 4-ciclos (por Chebotarev, cada clase de conjugación ocurre como Frobenius, y $f \bmod p$ es irreducible $\iff$ Frobenius es 4-ciclo).

## Análisis

**Caso 1: $f$ reducible sobre $\mathbb{Z}$.** Entonces $f = gh$ exactamente, con $\deg g, \deg h \le 3$ (no hay raíces racionales, pues $f > 0$ en reales para $n \ge 1$). Buscamos $(x^2+ax+b)(x^2-ax+d)$: la condición es $b+d=20$, $bd=n$ (caso $a=0$) o $b=d$, $2b-a^2=20$ (caso $a\neq 0$, que exige $n$ cuadrado y $2\sqrt{n}-20$ cuadrado: solo $n=100$).

Con $a=0$: $b,d = 10\pm\sqrt{100-n}$ racionales $\iff 100-n$ es cuadrado perfecto. Para $k=0,\dots,9$: $n = 100-k^2 \in \{100, 99, 96, 91, 84, 75, 64, 51, 36, 19\}$, con $f=(x^2+(10-k))(x^2+(10+k))$.

**Caso 2: $f$ irreducible sobre $\mathbb{Q}$.** Aquí $G$ es transitive y $G \subseteq D_4$ (polinomio bicuadrático), así que $G \in \{V_4, C_4, D_4\}$, y $C_4, D_4$ contienen 4-ciclos. Entonces:

$$\text{breakable} \iff G \subseteq A_4 \iff \operatorname{disc}(f) \text{ es cuadrado}.$$

Para $x^4+bx^2+c$ se tiene $\operatorname{disc} = 16c(b^2-4c)^2$. Aquí:

$$\operatorname{disc}(f) = 16n(400-4n)^2 = 256\,n\,(100-n)^2,$$

que es cuadrado $\iff$ $n$ es cuadrado perfecto. (Verificación estructural: si $n=s^2$, las raíces $\pm\alpha, \pm\beta$ con $\alpha\beta = s \in \mathbb{Q}$ dan $G \cong V_4$ sin 4-ciclos; si $n$ no es cuadrado, $G \in \{C_4, D_4\}$ — comprobado con $n=2, 50, 3, 5, 6$, todos irreducibles mod algún primo; y $n=1,4,49$ reducibles mod todos los primos probados, p. ej. $x^4+1 \equiv (x^2+2)(x^2+3) \pmod 5$.)

## Enumeración

Breakable $\iff$ $n$ cuadrado perfecto, o $100-n$ cuadrado perfecto:

- Cuadrados $\le 100$: $1,4,9,16,25,36,49,64,81,100$ — suma $385$.
- $\{100-k^2\}$ nuevos: $19, 51, 75, 84, 91, 96, 99$ — suma $515$.

Total: $385 + 515 = 900$.

$$\boxed{900}$$