Para encontrar el número de subconjuntos de 8 sillas de un total de 16 en una fila, de modo que ninguna persona se siente junto a otras dos personas, podemos representar las sillas ocupadas con un $1$ y las sillas vacías con un $0$. 

El problema equivale a contar el número de cadenas binarias de longitud 16 formadas por ocho $1$s y ocho $0$s que no contienen tres $1$s consecutivos (es decir, no aparece la subcadena $111$).

### Paso 1: Planteamiento mediante espacios entre sillas vacías
Si colocamos primero los ocho $0$s en una fila, se determinan $9$ espacios posibles (uno antes del primer $0$, siete entre $0$s consecutivos y uno después del último $0$) donde podemos insertar los $1$s:
$$\_ \ 0 \ \_ \ 0 \ \_ \ 0 \ \_ \ 0 \ \_ \ 0 \ \_ \ 0 \ \_ \ 0 \ \_ \ 0 \ \_$$

Sea $x_i$ la cantidad de $1$s ubicados en el $i$-ésimo espacio (para $i = 1, 2, \dots, 9$). Para que ninguna persona tenga a otras dos personas a ambos lados, no puede haber 3 o más sillas ocupadas seguidas, lo que significa que en cada espacio puede haber a lo sumo dos $1$s ($x_i \in \{0, 1, 2\}$).

Buscamos el número de soluciones enteras de la ecuación:
$$x_1 + x_2 + \dots + x_9 = 8, \quad \text{con } x_i \in \{0, 1, 2\}$$

### Paso 2: Conteo por casos (o funciones generadoras)
El número de soluciones corresponde al coeficiente de $x^8$ en el polinomio:
$$(1 + x + x^2)^9$$

Podemos calcularlo dividiendo en casos según la cantidad $k$ de espacios que contienen exactamente un par de unos ($x_i = 2$). Si hay $k$ espacios con el valor $2$, entonces debe haber $m = 8 - 2k$ espacios con el valor $1$, y $z = 9 - k - m$ espacios con el valor $0$. El número de formas para un $k$ dado es el coeficiente multinomial $\frac{9!}{k! \, m! \, z!}$:

1. **Caso $k = 0$** ($0$ doses, $8$ unos, $1$ cero):
   $$\frac{9!}{0! \, 8! \, 1!} = 9$$

2. **Caso $k = 1$** ($1$ dos, $6$ unos, $2$ ceros):
   $$\frac{9!}{1! \, 6! \, 2!} = 9 \times \binom{8}{2} = 9 \times 28 = 252$$

3. **Caso $k = 2$** ($2$ doses, $4$ unos, $3$ ceros):
   $$\frac{9!}{2! \, 4! \, 3!} = \binom{9}{2} \times \binom{7}{3} = 36 \times 35 = 1260$$

4. **Caso $k = 3$** ($3$ doses, $2$ unos, $4$ ceros):
   $$\frac{9!}{3! \, 2! \, 4!} = \binom{9}{3} \times \binom{6}{2} = 84 \times 15 = 1260$$

5. **Caso $k = 4$** ($4$ doses, $0$ unos, $5$ ceros):
   $$\frac{9!}{4! \, 0! \, 5!} = \binom{9}{4} = 126$$

### Paso 3: Suma total y cálculo del residuo
Sumando todos los casos posibles obtenemos $N$:
$$N = 9 + 252 + 1260 + 1260 + 126 = 2907$$

Finalmente, calculamos el residuo al dividir $N$ entre $1000$:
$$2907 \equiv 907 \pmod{1000}$$

\boxed{907}