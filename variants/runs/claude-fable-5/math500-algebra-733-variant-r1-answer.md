Los términos complicados —la exponencial, el coeficiente binomial y la función $\phi$— son **idénticos** en $p(x)$ y $q(x)$ (ambos dependen solo de $\lfloor x \rfloor$ y $x$ de la misma forma, al igual que el término $51x^4$), así que al igualar $p(x) = q(x)$ se cancelan por completo:

$$3x^3 - 4x^2 + 5x + 2 = 4x^3 - 7x^2 - 8x + 17$$

Pasando todo a un lado:

$$0 = x^3 - 3x^2 - 13x + 15$$

Busco raíces racionales: con $x = 1$ obtengo $1 - 3 - 13 + 15 = 0$. Dividiendo entre $(x-1)$:

$$x^3 - 3x^2 - 13x + 15 = (x - 1)(x^2 - 2x - 15) = (x - 1)(x - 5)(x + 3)$$

Las intersecciones ocurren en $x = -3,\ 1,\ 5$. Verifico que en $x = 5$ todos los términos comunes están bien definidos ($\lfloor 5 \rfloor = 5$, así que $|{\lfloor x \rfloor}|! = 120$, el binomio y $\phi(6)$ existen), y como son iguales en ambas funciones, la intersección es válida.

La mayor de las tres raíces es:

$$\boxed{5}$$