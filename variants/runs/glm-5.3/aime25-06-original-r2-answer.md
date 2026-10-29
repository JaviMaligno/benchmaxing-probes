## Razonamiento paso a paso

**Paso 1: Usar la fórmula del área de un cuadrilátero tangencial.**
Para cualquier cuadrilátero con círculo inscrito de radio $\rho$, el área es $A = \rho \cdot p$, donde $p$ es el semiperímetro. Aquí:
$$72 = 3 \cdot p \implies p = 24 \implies \text{perímetro} = 48$$

**Paso 2: Condición de tangencia.**
En un cuadrilátero tangencial, las sumas de lados opuestos son iguales:
$$r + s = \ell_1 + \ell_2$$
Como el trapecio es isósceles, $\ell_1 = \ell_2 = \ell$, entonces:
$$r + s = 2\ell$$
El perímetro es $2(r+s) = 48$, de donde:
$$r + s = 24, \qquad \ell = 12$$

**Paso 3: Hallar la altura.**
$$A = \frac{r+s}{2}\cdot h = 12h = 72 \implies h = 6$$
(Consistente: $h = 2\rho = 6$, el diámetro del círculo.)

**Paso 4: Diferencia de las bases.**
En un trapecio isósceles, cada pata, la altura y la semidiferencia de las bases forman un triángulo rectángulo:
$$\left(\frac{s-r}{2}\right)^2 = \ell^2 - h^2 = 144 - 36 = 108 \implies \frac{s-r}{2} = 6\sqrt{3}$$
$$s - r = 12\sqrt{3}$$

**Paso 5: Calcular $r^2 + s^2$.**
De $r+s = 24$ y $s-r = 12\sqrt{3}$:
$$r = 12 - 6\sqrt{3}, \qquad s = 12 + 6\sqrt{3}$$
$$r^2+s^2 = (12-6\sqrt{3})^2 + (12+6\sqrt{3})^2 = 2(144) + 2(108) = 288 + 216 = 504$$

**Verificación:** bases $12\pm 6\sqrt{3}$ suman $24$, área $= 12\cdot 6 = 72$ ✓, suma de bases $=$ suma de patas $= 24$ ✓.

$$\boxed{504}$$