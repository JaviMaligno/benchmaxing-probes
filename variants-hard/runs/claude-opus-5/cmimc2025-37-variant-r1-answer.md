## Reducción módulo 3

Módulo 3 se cumple $x^3-1\equiv (x-1)^3$, y como $1+x+x^2=\dfrac{x^3-1}{x-1}$, resulta

$$1+x+x^2\equiv (x-1)^2 \pmod 3.$$

Por tanto

$$(1+x+x^2)^{2019}\equiv (x-1)^{4038}=(1-x)^{4038}\pmod 3,$$

y comparando coeficientes de $x^k$:

$$\binom{2019}{k}_3\equiv (-1)^k\binom{4038}{k}\pmod 3.$$

(Verificación con $n=1$: $(1-x)^2=1-2x+x^2\equiv 1+x+x^2$.)

## Lucas en base 3

$4038 = (1,2,1,1,2,1,2,0)_3$, es decir $d_7=1,\;d_6=2,\;d_5=1,\;d_4=1,\;d_3=2,\;d_2=1,\;d_1=2,\;d_0=0$.

Por Lucas, $\binom{4038}{k}\not\equiv 0$ exige $k_i\le d_i$ en cada dígito, y entonces

$$\binom{4038}{k}\equiv\prod_i\binom{d_i}{k_i}\equiv 2^{a}\pmod 3,\qquad a=\#\{i: d_i=2,\;k_i=1\},$$

ya que $\binom{1}{0}=\binom11=1$, $\binom20=\binom22=1$, $\binom21=2$.

Como $2\equiv -1$, la condición $(-1)^k\binom{4038}{k}\equiv 1$ se vuelve

$$(-1)^{a+k}\equiv 1\iff a+k\ \text{par},$$

y al ser $3^i$ impar, $k\equiv \sum_i k_i \pmod 2$. Luego la condición es $\sum_i k_i + a \equiv 0 \pmod 2$.

## Contribuciones por dígito

- Si $d_i=2$: $k_i=0\to 0$; $k_i=1\to 1+1=2\equiv 0$; $k_i=2\to 2\equiv 0$. **Siempre par**, sin restricción (3 opciones libres).
- Si $d_i=1$: contribuye $k_i$, así que importa la paridad del número de unos.
- Si $d_i=0$: contribuye $0$.

Hay **3** posiciones con $d_i=2$ (índices 6, 3, 1) y **4** posiciones con $d_i=1$ (índices 7, 5, 4, 2).

La condición final es: *un número par de unos entre las 4 posiciones con $d_i=1$*.

$$\underbrace{3^3}_{\text{dígitos }2}\times \underbrace{2^{4-1}}_{\text{subconjuntos pares}} = 27\times 8 = 216.$$

(Control: en total hay $\prod(d_i+1)=432$ coeficientes no nulos, y resultan repartidos mitad y mitad entre $1$ y $2$. Con $n=2$: $(1+x+x^2)^2\equiv 1+2x+0+2x^3+x^4$, dos coeficientes iguales a 1, y la fórmula da $2^{2-1}=2$.)

\boxed{216}