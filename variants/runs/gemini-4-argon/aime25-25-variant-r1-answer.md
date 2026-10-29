Para resolver este problema, podemos representar los 17 asientos como una cadena binaria de longitud 17, donde un `1` representa un asiento ocupado (hay 9 en total) y un `0` representa un asiento vacío (hay $17 - 9 = 8$ en total).

La condición de que ningún invitado esté sentado junto a otros dos invitados significa que ningún invitado puede tener un invitado inmediatamente a su izquierda y otro inmediatamente a su derecha. En otras palabras, no puede haber tres o más asientos consecutivos ocupados (la subcadena `111` está prohibida).

Los 8 asientos vacíos (`0`) dividen la fila en $8 + 1 = 9$ espacios donde pueden ubicarse los bloques de asientos ocupados (`1`):
$$x_1 \ 0 \ x_2 \ 0 \ x_3 \ 0 \ x_4 \ 0 \ x_5 \ 0 \ x_6 \ 0 \ x_7 \ 0 \ x_8 \ 0 \ x_9$$

Donde $x_i$ representa la cantidad de `1`s en el $i$-ésimo espacio. Como no puede haber tres `1`s consecutivos, cada espacio puede contener a lo sumo dos `1`s, es decir, $x_i \in \{0, 1, 2\}$ para todo $i \in \{1, 2, \dots, 9\}$. Además, como hay 9 invitados en total, debemos tener:
$$x_1 + x_2 + \dots + x_9 = 9$$

Sea $a$ la cantidad de espacios que tienen dos `1`s ($x_i = 2$), $b$ la cantidad de espacios que tienen un `1` ($x_i = 1$), y $c$ la cantidad de espacios vacíos ($x_i = 0$). Entonces se cumplen las siguientes relaciones:
1. $a + b + c = 9$
2. $2a + b = 9 \implies b = 9 - 2a$

Sustituyendo la segunda ecuación en la primera, obtenemos que $c = a$. Como $b \ge 0$, los posibles valores enteros para $a$ son $0, 1, 2, 3, 4$.

Para cada valor de $a$, el número de formas de elegir qué espacios toman los valores $2, 1$ y $0$ está dado por el coeficiente multinomial:
$$\frac{9!}{a! \, b! \, c!} = \frac{9!}{a! \, (9-2a)! \, a!} = \binom{9}{2a}\binom{2a}{a}$$

Calculamos el número de configuraciones para cada valor posible de $a$:

* **Para $a = 0$** ($b = 9, c = 0$):
  $$\binom{9}{0}\binom{0}{0} = 1 \times 1 = 1$$

* **Para $a = 1$** ($b = 7, c = 1$):
  $$\binom{9}{2}\binom{2}{1} = 36 \times 2 = 72$$

* **Para $a = 2$** ($b = 5, c = 2$):
  $$\binom{9}{4}\binom{4}{2} = 126 \times 6 = 756$$

* **Para $a = 3$** ($b = 3, c = 3$):
  $$\binom{9}{6}\binom{6}{3} = 84 \times 20 = 1680$$

* **Para $a = 4$** ($b = 1, c = 4$):
  $$\binom{9}{8}\binom{8}{4} = 9 \times 70 = 630$$

Sumando todos los casos posibles obtenemos el valor total de $N$:
$$N = 1 + 72 + 756 + 1680 + 630 = 3139$$

Finalmente, hallamos el residuo cuando $N$ se divide por $1000$:
$$3139 \equiv 139 \pmod{1000}$$

\boxed{139}