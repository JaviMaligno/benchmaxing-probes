## Planteamiento

"Breakable" significa que $f$ es reducible módulo todo primo $p$ (si $f\bmod p$ fuera irreducible, no habría factorización en grados menores; y recíprocamente).

Sea $f = x^4 + 20x^2 + n$, con $a=20$, $b=n$.

**Criterio.** Para una bicuadrática irreducible $x^4+ax^2+b$, el grupo de Galois es:
- $V_4$ si $b$ es cuadrado racional,
- $C_4$ si $b(a^2-4b)$ es cuadrado,
- $D_4$ en otro caso.

Por Chebotarev, $f$ es irreducible módulo algún primo exactamente cuando el grupo contiene un $4$-ciclo (los primos ramificados no pueden dar irreducibilidad, pues un irreducible sobre $\mathbb{F}_p$ es separable). $C_4$ y $D_4$ contienen $4$-ciclos; $V_4$ no. Por tanto:

$$f \text{ breakable} \iff f \text{ reducible sobre } \mathbb{Z} \ \text{ o } \ n \text{ es cuadrado perfecto.}$$

**Verificación directa del caso $n=s^2$:** $x^4+ax^2+s^2=(x^2+cx\pm s)(x^2-cx\pm s)$ con $c^2=\mp 2s-a$. Si ni $2s-a$ ni $-2s-a$ son cuadrados mod $p$, su producto $a^2-4b$ sí lo es, y entonces $f\equiv(x^2+u)(x^2+v)$. Siempre reducible, para todo $p$ (incluido $p=2$).

## Casos reducibles sobre $\mathbb{Z}$

No hay raíces racionales ($n=-(m^4+20m^2)\le 0$), así que solo factorización en dos cuadráticas $(x^2+px+q)(x^2-px+r)$: se necesita $p(r-q)=0$.

- $p=0$: $q+r=20$, $qr=n$ $\Rightarrow$ $100-n$ cuadrado, es decir $n=100-k^2$:
$$100,\,99,\,96,\,91,\,84,\,75,\,64,\,51,\,36,\,19$$
- $r=q$: entonces $n=q^2$, ya cubierto por los cuadrados.

## Unión y suma

- Cuadrados $\le 100$: $1,4,9,16,25,36,49,64,81,100$ → suma $385$.
- Nuevos de la forma $100-k^2$: $99,96,91,84,75,51,19$ → suma $515$.

Total: $385+515=900$.

\boxed{900}