Voy a resolver el sistema paso a paso.

## Paso 1: Sustitución

De la primera ecuación, $y = x^2 - 7$. Sustituyo en la segunda:

$$(x^2-7)^2 = -9x + 45$$

$$x^4 - 14x^2 + 49 + 9x - 45 = 0$$

$$x^4 - 14x^2 + 9x + 4 = 0$$

## Paso 2: Factorización

Pruebo valores enteros:
- $x = 1$: $1 - 14 + 9 + 4 = 0$ ✓
- $x = -4$: $256 - 224 - 36 + 4 = 0$ ✓

Dividiendo entre $(x-1)(x+4) = x^2 + 3x - 4$:

$$x^4 - 14x^2 + 9x + 4 = (x^2+3x-4)(x^2 - 3x - 1) = 0$$

## Paso 3: Valores de $x$ y de $y$

Los cuatro valores de $x$ son distintos:

| $x$ | $y = x^2 - 7$ |
|---|---|
| $1$ | $-6$ |
| $-4$ | $9$ |
| $\dfrac{3+\sqrt{13}}{2}$ | $\dfrac{3(\sqrt{13}-1)}{2}$ |
| $\dfrac{3-\sqrt{13}}{2}$ | $-\dfrac{3(\sqrt{13}+1)}{2}$ |

(Verificación rápida: para $x=1$, $y^2 = 36 = -9+45$ ✓; para $x=-4$, $y^2 = 81 = 36+45$ ✓.)

## Paso 4: Producto de las coordenadas $y$

$$(-6)(9) \cdot \frac{3(\sqrt{13}-1)}{2} \cdot \left(-\frac{3(\sqrt{13}+1)}{2}\right)$$

Como $(\sqrt{13}-1)(\sqrt{13}+1) = 13 - 1 = 12$:

$$= (-54)\cdot \left(-\frac{9 \cdot 12}{4}\right) = (-54)(-27) = 1458$$

$$\boxed{1458}$$