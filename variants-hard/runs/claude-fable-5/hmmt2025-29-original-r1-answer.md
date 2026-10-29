## Solución

Coloco coordenadas: $A=(0,0)$, $B=(a,0)$, $C=(a,24)$, $D=(0,24)$, con $AB = a$ y $X=(x,y)$.

**Condición del ángulo recto.** Como $\angle AXB = 90°$, $X$ está en la circunferencia de diámetro $AB$:
$$x^2 + y^2 = ax \quad (1)$$

**Circunradio de $\triangle AXD$.** Su circuncentro está en la mediatriz de $AD$ (la recta $y=12$) y a distancia 13 de $A$: es $O_1=(5,12)$ (lado positivo, pues el triángulo es acutángulo y $X$ interior). Entonces $(x-5)^2+(y-12)^2=169$, que se simplifica a $x^2+y^2 = 10x+24y$. Combinando con (1):
$$x(a-10) = 24y \quad (2)$$

**Circunradio de $\triangle BXC$.** Análogamente, el circuncentro es $O_2=(a-9,12)$ con $\sqrt{9^2+12^2}=15$. De $(x-(a-9))^2+(y-12)^2=225$ sale $x^2+y^2 = 2(a-9)x + 24y - (a-9)^2 + 81$. Usando (1) y (2):
$$x(18-a) - x(a-10) + (a-9)^2 - 81 = 0 \;\Rightarrow\; x = \frac{a(18-a)}{2(14-a)}$$

**Cierre del sistema.** Sustituyendo $y = \frac{x(a-10)}{24}$ en (1) y dividiendo por $x$:
$$x\left[576 + (a-10)^2\right] = 576a$$

Reemplazando el valor de $x$:
$$(18-a)\left(a^2 - 20a + 676\right) = 1152(14-a)$$

Expandiendo:
$$a^3 - 38a^2 - 116a + 3960 = 0$$

Se factoriza como $(a-10)(a^2 - 28a - 396) = 0$. La raíz $a=10$ da $y=0$ (degenerada, $X$ sobre $AB$), así que:
$$a = \frac{28 + \sqrt{784 + 1584}}{2} = \frac{28 + \sqrt{2368}}{2} = 14 + 4\sqrt{37}$$

$$\boxed{14 + 4\sqrt{37}}$$