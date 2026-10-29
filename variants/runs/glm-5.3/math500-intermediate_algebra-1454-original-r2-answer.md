## Razonamiento paso a paso

**Paso 1: Simplificar el tercer radical.**
Como $1600 + 2500 = 4100$, se completa la expresión en cuadrados:
$$x^2 + y^2 - 80x - 100y + 4100 = (x-40)^2 + (y-50)^2.$$
Entonces la función es
$$f(x,y) = \sqrt{x^2+400} + \sqrt{y^2+900} + \sqrt{(40-x)^2 + (50-y)^2}.$$

**Paso 2: Acotar cada término con $(a-b)^2 \ge 0$ (Cauchy–Schwarz).**

*Primer término:* como $2(x^2+400) - (x+20)^2 = (x-20)^2 \ge 0$, y $x+20>0$ en el dominio:
$$\sqrt{x^2+400} \ge \frac{x+20}{\sqrt2}, \qquad \text{igualdad } \iff x = 20.$$

*Segundo término:* como $2(y^2+900) - (y+30)^2 = (y-30)^2 \ge 0$:
$$\sqrt{y^2+900} \ge \frac{y+30}{\sqrt2}, \qquad \text{igualdad } \iff y = 30.$$

*Tercer término:* con $a = 40-x \ge 0$ y $b = 50-y \ge 0$, se usa $(a+b)^2 \le 2(a^2+b^2)$:
$$\sqrt{(40-x)^2+(50-y)^2} \ge \frac{(40-x)+(50-y)}{\sqrt2} = \frac{90-x-y}{\sqrt2}, \qquad \text{igualdad } \iff 40-x = 50-y.$$

**Paso 3: Sumar las tres cotas.**
$$f(x,y) \ge \frac{(x+20) + (y+30) + (90-x-y)}{\sqrt2} = \frac{140}{\sqrt2} = 70\sqrt2.$$

**Paso 4: Verificar que la igualdad es alcanzable.**
Se necesita $x = 20$, $y = 30$ y $40 - x = 50 - y$. En $(x,y) = (20,30)$ (que cumple $0\le x\le 40$, $0 \le y \le 50$) las tres condiciones se cumplen, y de hecho:
$$\sqrt{800} + \sqrt{1800} + \sqrt{800} = 20\sqrt2 + 30\sqrt2 + 20\sqrt2 = 70\sqrt2.$$

Por lo tanto, el valor mínimo es $\boxed{70\sqrt{2}}$.