## Planteamiento

Si el mínimo $L$ se alcanza en exactamente dos puntos $p,q>0$, entonces para todo $x>0$:

$$g(x)-L=\frac{(x-8)(x-50)(x-72)(x-k)-Lx}{x}\ge 0$$

con igualdad en $x=p,q$. Luego el numerador es un polinomio mónico de grado 4, no negativo en $x>0$, con raíces dobles en $p$ y $q$:

$$(x-8)(x-50)(x-72)(x-k)-Lx=(x-p)^2(x-q)^2$$

## Comparación de coeficientes

Con $s=p+q$, $t=pq$, el lado derecho más $Lx$ es
$$x^4-2s\,x^3+(s^2+2t)x^2+(L-2st)x+t^2.$$

Igualando con $x^4-e_1x^3+e_2x^2-e_3x+e_4$ (donde $e_i$ son las simétricas de $8,50,72,k$), las condiciones **independientes de $L$** son:

$$e_1=2s,\qquad e_2=s^2+2t,\qquad e_4=t^2.$$

Como $e_1=130+k$, $e_2=4576+130k$, $e_4=28800k$:

$$s=\frac{130+k}{2},\qquad t=\frac{e_2-s^2}{2}=\frac{-k^2+260k+1404}{8}.$$

La condición $e_4=t^2$ da:

$$(k^2-260k-1404)^2=1843200\,k$$
$$k^4-520k^3+64792k^2-1113120k+1971216=0$$

## Raíces

Factorizando: $(k-2)(k-18)(k^2-500k+54756)=0$, y $k^2-500k+54756=0$ da $k=\frac{500\pm176}{2}$, es decir $162$ y $338$.

Candidatos: $k=2,\,18,\,162,\,338$ (suma $520$).

**Descarte:** se requiere $t=pq>0$, o sea $-k^2+260k+1404>0$, válido solo para $k<\tfrac{260+\sqrt{73216}}{2}\approx265.3$. Para $k=338$ resulta $t=-3120<0$ (una de las raíces dobles es negativa, así que el mínimo en $x>0$ se alcanza en un solo punto): **espurio**.

**Verificación de los otros tres:**

| $k$ | $s$ | $t$ | discriminante $s^2-4t$ | $p,q$ |
|---|---|---|---|---|
| $2$ | $66$ | $240$ | $3396>0$ | positivos ✓ |
| $18$ | $74$ | $720$ | $2596>0$ | positivos ✓ |
| $162$ | $146$ | $2160$ | $12676>0$ | positivos ✓ |

En cada caso $g(x)-L=\dfrac{(x-p)^2(x-q)^2}{x}\ge0$, confirmando que $L$ es el mínimo alcanzado exactamente en dos puntos positivos.

Suma: $2+18+162=182$.

\boxed{182}