## Planteamiento

Sea $\alpha=\arccos x$, $\beta=\arccos 2x$, $\gamma=\arccos 3x$, con $\alpha+\beta+\gamma=\pi$.

**Dominio:** necesitamos $x\in[-1,1]$, $2x\in[-1,1]$ y $3x\in[-1,1]$, así que $x\in\left[-\tfrac13,\tfrac13\right]$. Como $\arccos$ toma valores en $[0,\pi]$, todos los senos son no negativos.

## Desarrollo

De $\alpha+\beta=\pi-\gamma$, tomando coseno:

$$\cos\alpha\cos\beta-\sin\alpha\sin\beta=-\cos\gamma$$
$$2x^2-\sqrt{1-x^2}\sqrt{1-4x^2}=-3x$$

Despejando:
$$\sqrt{(1-x^2)(1-4x^2)}=2x^2+3x$$

El lado izquierdo es $\ge 0$, lo que fuerza $2x^2+3x\ge 0$; junto con el dominio, esto da $x\in\left[0,\tfrac13\right]$. En este rango ambos lados son no negativos, así que elevar al cuadrado es reversible:

$$(1-x^2)(1-4x^2)=(2x^2+3x)^2$$
$$1-5x^2+4x^4=4x^4+12x^3+9x^2$$
$$12x^3+14x^2-1=0$$

Efectivamente hay una raíz en $\left(0,\tfrac13\right)$: en $x=0$ la expresión vale $-1$ y en $x=\tfrac13$ vale $+1$.

## Minimización

Para saber qué polinomios cúbicos enteros puede satisfacer $x$, verifico si $12x^3+14x^2-1$ es irreducible sobre $\mathbb{Q}$. Sus únicas posibles raíces racionales son $\pm\tfrac1q$ con $q\mid 12$:

$$f\left(\pm\tfrac12\right)=4,\,1;\quad f\left(\pm\tfrac13\right)=1,\,\tfrac19;\quad f\left(\pm\tfrac14\right)=\tfrac1{16},-\tfrac5{16};\quad f\left(\pm\tfrac16\right)=-\tfrac59,-\tfrac23;\quad f\left(\pm\tfrac1{12}\right)\neq 0;\quad f(\pm1)\neq 0$$

Ninguna es raíz, así que el polinomio es irreducible: es el polinomio mínimo de $x$, y está ya en forma primitiva ($\gcd(12,14,1)=1$).

Por lo tanto, todo polinomio cúbico entero que satisfaga $x$ es un múltiplo $k\left(12x^3+14x^2-1\right)$ con $k\in\mathbb{Z}\setminus\{0\}$, y la suma de valores absolutos es $|k|\cdot 27$, mínima para $k=\pm1$:

$$|12|+|14|+|0|+|-1|=27$$

$$\boxed{27}$$