## Planteamiento

Clasifico cada variable por $a=v_3(x)$, ya que $x^3 \bmod 3^8$ sólo depende de $x \bmod 3^7$.

**Hecho clave:** en $(\mathbb{Z}/3^k)^*$ (cíclico), los cubos forman el subgrupo de índice 3, que coincide con $\{c \equiv \pm 1 \pmod 9\}$. Por tanto el cubo de una unidad es $\equiv \pm1 \pmod 9$.

Tipos de $x\in[1,3^7]$ y residuos que aportan módulo $3^8$:

| Tipo | $x$ | aporte | residuos posibles | peso (nº de $x$) |
|---|---|---|---|---|
| $T_0$ | $3\nmid x$ | $c$ | $1458$ unidades $\equiv\pm1\ (9)$ | $1$ |
| $T_1$ | $a=1$ | $27d$, $d=u^3\bmod 3^5$ | $54$ valores | $9$ |
| $T_2$ | $a=2$ | $3^6e$, $e=u^3\bmod 9$ | $e\in\{1,8\}$ | $81$ |
| $D$ | $a\ge3$ | $0$ | — | $81$ |

Total $1458+486+162+81=2187=3^7$ ✓

**Imposibilidades (vía mód 9):** tres cubos de unidades de un mismo nivel dan suma $\equiv \pm1,\pm3 \pmod 9$, nunca $0$. Luego $n_0=3$, $n_1=3$, $n_2=3$ fallan; y un único término del nivel mínimo también falla (unidad $\not\equiv 0$).

## Casos válidos

- **Todos $D$:** $81^3 = 531441$
- **$n_2=2$ + $D$:** $e_1+e_2\equiv0\ (9)$: $2\cdot81^2\cdot81\cdot3 = 3188646$
- **$n_1=2$ + $D$:** $d_2=-d_1$: $54\cdot9^2\cdot81\cdot3 = 1062882$
- **$n_1=2$ + $T_2$:** $d_1+d_2+27e\equiv0\ (3^5)$, siempre soluble: $54\cdot2\cdot9^2\cdot81\cdot3 = 2125764$
- **$n_0=2$ + $D$:** $1458\cdot81\cdot3 = 354294$
- **$n_0=2$ + $T_1$:** $1458\cdot54\cdot9\cdot3 = 2125764$
- **$n_0=2$ + $T_2$:** $1458\cdot2\cdot81\cdot3 = 708588$

(En todos, el tercer residuo queda determinado y automáticamente es $\equiv\mp1\bmod 9$, por lo que es válido.)

## Suma

$$M = 531441+3188646+1062882+2125764+354294+2125764+708588 = 10\,097\,379 = 19\cdot3^{12}$$

*Verificación del método:* aplicado al caso análogo $x,y,z\le 3^6$ con $3^7$, da $885735$, cuyo resto mód 1000 es $735$ (valor conocido), lo que confirma el procedimiento.

$10\,097\,379 \equiv 379 \pmod{1000}$

\boxed{379}