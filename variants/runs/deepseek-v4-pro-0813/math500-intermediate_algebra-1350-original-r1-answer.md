Voy a resolver el problema paso a paso.

Sea

\[
f(x)=a_nx^n+a_{n-1}x^{n-1}+\cdots+a_1x+a_0
\]

con coeficientes enteros, raíces enteras distintas, \(a_n=2\) y \(a_0=66\).

**Paso 1: relación entre coeficientes y raíces**

Como el coeficiente principal es \(2\), y las raíces son enteros distintos \(r_1,\dots,r_n\), podemos escribir:

\[
f(x)=2(x-r_1)(x-r_2)\cdots(x-r_n).
\]

Entonces el término constante es:

\[
a_0 = 2(-1)^n r_1r_2\cdots r_n.
\]

Dado que \(a_0=66\), tenemos

\[
2(-1)^n r_1r_2\cdots r_n = 66,
\]

por lo que

\[
r_1r_2\cdots r_n = \frac{66}{2(-1)^n} = (-1)^n \cdot 33.
\]

Así que el producto de las raíces es \(\pm 33\), según la paridad de \(n\).

**Paso 2: factorizar y encontrar posibles conjuntos de raíces**

Las raíces son enteros distintos, y su producto tiene valor absoluto \(33\). Factorizamos:

\[
33=1\cdot 33 = 1\cdot 3\cdot 11 = 1\cdot(-1)\cdot(-3)\cdot(-11),\quad\text{etc.}
\]

Más precisamente, los divisores de \(33\) son \(\pm1,\pm3,\pm11,\pm33\).

Buscamos conjuntos de enteros no nulos y distintos cuyo producto (con signo) sea \(\pm33\).

Posibilidades con pocas raíces:

1. Dos raíces con producto \(\pm33\):
   - \((1,33)\), \((1,-33)\), \((-1,33)\), \((-1,-33)\),
   - \((3,11)\), \((3,-11)\), \((-3,11)\), \((-3,-11)\).

2. Cuatro raíces:
   - \((1,3,11,-1)\), porque \(1\cdot 3\cdot 11\cdot(-1)=-33\).
   - \((1,3,-11,-1)\), etcétera, y sus variantes con signos.

3. Seis raíces o más, añadiendo pares \(r,-r\), pero eso solo cambia el signo del producto; sin embargo, para \(n=6\) necesitaríamos producto \(\pm33\) y raíces distintas, lo cual es posible añadiendo por ejemplo \(\pm 3\) y \(\pm 11\) al conjunto, pero hay que mantener el producto.

**Paso 3: minimizar \(a_{n-1}\)**

Relacionamos \(a_{n-1}\) con las raíces. Para

\[
f(x)=2(x-r_1)\cdots(x-r_n),
\]

el coeficiente de \(x^{n-1}\) es

\[
a_{n-1}=2\left(-(r_1+r_2+\cdots+r_n)\right)
= -2\sum_{i=1}^n r_i.
\]

Entonces minimizar \(|a_{n-1}|\) equivale a minimizar \(\left|\sum r_i\right|\).

**Paso 4: analizar los casos**

Caso \(n=2\):

\[
f(x)=2(x-r_1)(x-r_2),
\]
\[
a_1=-2(r_1+r_2).
\]

Las posibles parejas con producto \(\pm33\):

- \(1\) y \(-33\): suma \(-32\), \(|a_1|=64\).
- \(-1\) y \(33\): suma \(32\), \(|a_1|=64\).
- \(1\) y \(33\): suma \(34\), \(|a_1|=68\).
- \(-1\) y \(-33\): suma \(-34\), \(|a_1|=68\).
- \(3\) y \(-11\): suma \(-8\), \(|a_1|=16\).
- \(-3\) y \(11\): suma \(8\), \(|a_1|=16\).
- \(3\) y \(11\): suma \(14\), \(|a_1|=28\).
- \(-3\) y \(-11\): suma \(-14\), \(|a_1|=28\).

El mínimo aquí es \(16\).

Caso \(n=4\):

Necesitamos cuatro raíces distintas con producto \(\pm33\). Por ejemplo:

\[
1,\ -1,\ 3,\ -11
\]

tienen producto \(1\cdot(-1)\cdot3\cdot(-11)=33\). Su suma es

\[
1+(-1)+3+(-11)=-8.
\]

Entonces \(|a_{n-1}|=2|{-8}|=16\).

Intentemos conseguir suma \(0\). Buscamos cuatro enteros distintos con producto \(\pm33\) y suma \(0\).

Los únicos divisores con valor absoluto pequeño son \(\pm1,\pm3,\pm11,\pm33\). Con cuatro raíces, para tener producto \(\pm33\), necesitamos esencialmente los factores \(\pm1,\pm3,\pm11\) y un cuarto factor \(\pm1\) (pero deben ser distintos, así que no podemos repetir \(1\)).

Probemos combinaciones:

- \(1,-3,11,a\): producto \(1\cdot(-3)\cdot11\cdot a=-33a\). Para que sea \(\pm33\), \(a=1\) o \(a=-1\), pero \(1\) ya está usado; \(-1\) no está en el conjunto. Así \(1,-3,11,-1\) da producto \(33\), suma \(8\).
- \(1,3,-11,a\): producto \(1\cdot3\cdot(-11)\cdot a=-33a\). Para \(\pm33\), \(a=1\) o \(a=-1\). Con \(a=-1\): conjunto \((-1,1,3,-11)\), suma \(-8\).
- \(1,-3,-11,a\): producto \(1\cdot(-3)\cdot(-11)\cdot a=33a\). Para \(\pm33\), \(a=1\) o \(a=-1\). Ya \(1\) usado; con \(a=-1\): conjunto \((-1,1,-3,-11)\), producto \(33\), suma \(-14\).

No veo forma de que sumen \(0\), porque los valores absolutos son demasiado dispares. Pero hay que verificar si hay un caso con suma \(0\) para \(n=4\).

Realmente, con los conjuntos de cuatro raíces posibles, las sumas posibles en valor absoluto parecen \(8, 14, etc.\). El mínimo siguiente es \(8\), que da \(|a_{n-1}|=16\).

Caso \(n=6\):

Para \(n=6\), el producto debe ser \((-1)^6\cdot 33=33\). Podemos usar seis raíces distintas cuyo producto sea \(33\). Por ejemplo:

\[
1,\ -1,\ 3,\ -3,\ 11,\ -11
\]

tienen producto

\[
1\cdot(-1)\cdot3\cdot(-3)\cdot11\cdot(-11)=?
\]

Multipliquemos:

\[
1\cdot(-1)=-1,
\]
\[
-1\cdot3=-3,
\]
\[
-3\cdot(-3)=9,
\]
\[
9\cdot11=99,
\]
\[
99\cdot(-11)=-1089.
\]

Eso no es \(33\), porque en realidad agregamos pares \((r,-r)\), que multiplican por \(-(r^2)\), alterando el producto. Veamos con cuidado.

Para tener seis raíces distintas con producto \(33\), no podemos simplemente usar pares opuestos de \(1,3,11\), porque su producto sería

\[
(1\cdot(-1))(3\cdot(-3))(11\cdot(-11)) = (-1)(-9)(-121) = -1089.
\]

Necesitamos elegir signos para que el producto sea \(33\). Recordemos que solo disponemos de los divisores \(\pm1,\pm3,\pm11,\pm33\) y quizá otros divisores como \(\pm33\), y necesitamos seis valores distintos.

Los únicos divisores de \(33\) son \(\pm1,\pm3,\pm11,\pm33\). Eso son solo \(8\) valores posibles, y entre ellos, \(\pm33\) son divisores también. Para \(n=6\) necesitamos seis raíces distintas entre estos ocho, con producto \(33\).

Probemos seleccionar \(\pm1,\pm3,\pm11,\pm33\), pero solo seis. Como \(33\) y \(-33\) son divisores, podríamos combinar. Por ejemplo:

\[
1,\ -1,\ 3,\ -3,\ 11,\ 12?
\]

No, \(12\) no divide a \(33\). Solo los divisores son \(\pm1,\pm3,\pm11,\pm33\). Entonces con seis raíces, tenemos que elegir seis de estos ocho.

Probemos el conjunto \(1,-1,3,-3,11,33\). Producto:

\[
1\cdot(-1)\cdot3\cdot(-3)\cdot11\cdot33 = (-1)\cdot(-9)\cdot363 = 9\cdot363 = 3267,
\]

demasiado grande. Pero el producto debe ser \(33\) en valor absoluto, así que \(n=6\) no es posible porque el producto de seis divisores distintos de \(33\) tendrá valor absoluto mayor que \(33\), salvo que incluyamos \(\pm1,\pm3,\pm11\) y \(\pm33\), pero entonces el producto será enorme.

De hecho, el conjunto completo de los ocho divisores tendría producto:

\[
(1)(-1)(3)(-3)(11)(-11)(33)(-33).
\]

Calculemos:

\[
1\cdot(-1)=-1,
\]
\[
-1\cdot3=-3,
\]
\[
-3\cdot(-3)=9,
\]
\[
9\cdot11=99,
\]
\[
99\cdot(-11)=-1089,
\]
\[
-1089\cdot33=-35937,
\]
\[
-35937\cdot(-33)=1\,185\,921.
\]

Así que el producto solo de los divisores pequeños \(\pm1,\pm3,\pm11\) es \(-1089\), que ya es demasiado grande en valor absoluto comparado con \(33\). Por lo tanto, \(n\) no puede ser mayor que \(4\).

**Paso 5: conclusión**

El mínimo posible de \(|a_{n-1}|\) es \(16\), alcanzado por ejemplo con raíces \((3,-11)\) en el caso \(n=2\), o con \((1,-1,3,-11)\) en el caso \(n=4\).

Verifiquemos el caso \(n=2\) con raíces \(3\) y \(-11\):

\[
f(x)=2(x-3)(x+11)=2(x^2+8x-33)=2x^2+16x-66.
\]

Aquí \(a_2=2\), \(a_0=-66\). Pero necesitamos \(a_0=66\), no \(-66\).

Revisemos el signo. Con \(n=2\),

\[
a_0=2(-1)^2 r_1r_2 = 2r_1r_2.
\]

Para \(a_0=66\), necesitamos \(r_1r_2=33\). Entonces las raíces deben tener producto \(33\), no \(-33\).

Así que para \(n=2\), las parejas con producto \(33\):

- \(1\) y \(33\): suma \(34\), \(|a_1|=68\).
- \(-1\) y \(-33\): suma \(-34\), \(|a_1|=68\).
- \(3\) y \(11\): suma \(14\), \(|a_1|=28\).
- \(-3\) y \(-11\): suma \(-14\), \(|a_1|=28\).

El mínimo para \(n=2\) es \(28\).

Ahora \(n=4\). Como

\[
a_0 = 2(-1)^4 r_1r_2r_3r_4 = 2 r_1r_2r_3r_4,
\]

necesitamos \(r_1r_2r_3r_4=33\).

Buscamos cuatro enteros distintos con producto \(33\) y suma mínima en valor absoluto.

Divisores de \(33\): \(\pm1,\pm3,\pm11,\pm33\).

Posibles conjuntos de cuatro raíces distintas con producto \(33\):

Como el valor absoluto del producto es \(33\), los factores deben ser esencialmente \(\pm1,\pm3,\pm11\) y un cuarto factor. Para que cuatro números distintos tengan producto \(33\), consideremos los signos.

Trabajemos con los valores absolutos. Necesitamos cuatro enteros distintos cuyo producto (en valor absoluto) sea \(33\).

Las factorizaciones de \(33\) en cuatro factores enteros no nulos:

\[
33 = 1\cdot(-1)\cdot3\cdot(-11).
\]

Veamos las combinaciones con signos correctos para que el producto sea \(33\):

1. \(1\cdot(-1)\cdot3\cdot(-11)=33\). Suma:
\[
1-1+3-11=-8.
\]

2. \(1\cdot(-1)\cdot(-3)\cdot11=33\). Suma:
\[
1-1-3+11=8.
\]

3. ¿Podemos usar \(33\) y otros? Por ejemplo \(1\cdot(-1)\cdot 33 \cdot a\) con \(a\) un entero distinto: para producto \(33\), \(a\) tendría que ser \(1\) o \(-1\), repetidos, no válido.

Entonces las únicas sumas posibles son \(\pm8\).

Por lo tanto, para \(n=4\), el mínimo \(|a_{n-1}|\) es:

\[
|a_{n-1}| = \left|-2\sum r_i\right| = 2|-8| = 16.
\]

Verifiquemos con raíces \(1,-1,3,-11\):

\[
f(x)=2(x-1)(x+1)(x-3)(x+11).
\]

El término constante es:

\[
2(-1)^4(1)(-1)(3)(-11)=2\cdot33=66.
\]

El coeficiente de \(x^3\) viene de:

\[
f(x)=2(x-1)(x+1)(x-3)(x+11).
\]

Primero \((x-1)(x+1)=x^2-1\), y \((x-3)(x+11)=x^2+8x-33\). Multiplicando:

\[
(x^2-1)(x^2+8x-33)=x^4+8x^3-33x^2-x^2-8x+33
\]
\[
=x^4+8x^3-34x^2-8x+33.
\]

Multiplicando por \(2\):

\[
f(x)=2x^4+16x^3-68x^2-16x+66.
\]

Aquí \(a_4=2\), \(a_3=16\), \(a_0=66\). Entonces \(|a_{n-1}|=|a_3|=16\).

**Paso 6: ¿puede ser menor que 16?**

Para \(n=4\), ya vimos que el mínimo es \(16\). Para \(n=2\), el mínimo es \(28\). Para \(n=3\), veamos:

Con \(n=3\),

\[
a_0=2(-1)^3 r_1r_2r_3 = -2r_1r_2r_3.
\]

Para \(a_0=66\), necesitamos \(r_1r_2r_3=-33\).

Buscamos tres enteros distintos con producto \(-33\) y suma mínima en valor absoluto.

Divisores: \(\pm1,\pm3,\pm11,\pm33\).

Combinaciones de tres enteros distintos con producto \(-33\):

- \(1,3,-11\): producto \(1\cdot3\cdot(-11)=-33\). Suma \(1+3-11=-7\).
- \(-1,-3,-11\): producto \((-1)(-3)(-11)=-33\). Suma \(-1-3-11=-15\).
- \(1,-3,11\): producto \(1\cdot(-3)\cdot11=-33\). Suma \(1-3+11=9\).
- \(-1,3,11\): producto \((-1)\cdot3\cdot11=-33\). Suma \(-1+3+11=13\).
- \(1,-1,33\): producto \(1\cdot(-1)\cdot33=-33\). Suma \(1-1+33=33\).
- etcétera.

El mínimo valor absoluto de la suma es \(7\). Entonces

\[
|a_{n-1}| = \left|-2\sum r_i\right| = 2\cdot 7 = 14.
\]

¡Ah! Para \(n=3\), con raíces \(1,3,-11\), tenemos \(|a_{n-1}|=14\), que es menor que \(16\).

Verifiquemos:

\[
f(x)=2(x-1)(x-3)(x+11).
\]

El término constante:

\[
2(-1)^3(1)(3)(-11)=2(-1)(-33)=66.
\]

Calculemos el coeficiente de \(x^2\):

\[
(x-1)(x-3)=x^2-4x+3.
\]

Multiplicamos por \((x+11)\):

\[
(x^2-4x+3)(x+11)=x^3+11x^2-4x^2-44x+3x+33
\]
\[
=x^3+7x^2-41x+33.
\]

Multiplicando por \(2\):

\[
f(x)=2x^3+14x^2-82x+66.
\]

Aquí \(a_3=2\), \(a_2=14\), \(a_0=66\). Entonces \(|a_{n-1}|=|a_2|=14\).

**Paso 7: ¿puede ser aún menor?**

Para \(n=3\), el mínimo valor absoluto de la suma fue \(7\). ¿Puede ser menor? Buscamos tres enteros distintos con producto \(-33\) y suma con valor absoluto menor que \(7\).

Posibles sumas pequeñas: \(0,1,2,3,4,5,6\).

¿Existen tres enteros distintos cuyo producto sea \(-33\) y suma en valor absoluto menor que \(7\)?

Los factores deben ser divisores de \(33\). Los conjuntos de tres divisores distintos con producto \(-33\) son:

En valores absolutos, los factores deben ser \(1,3,11\) (pues \(33=1\cdot3\cdot11\)), o \(1,1,33\) (pero repetidos no válidos), etc.

Así que los valores absolutos son necesariamente \(\{1,3,11\}\), con algún signo elegido para que el producto sea \(-33\).

Los signos posibles:

- \((1,3,-11)\): suma \(-7\).
- \((-1,-3,-11)\): suma \(-15\).
- \((1,-3,11)\): suma \(9\).
- \((-1,3,11)\): suma \(13\).

El mínimo valor absoluto es \(7\). No hay forma de obtener suma menor, porque con valores absolutos \(1,3,11\), las sumas posibles en valor absoluto son solo \(7,9,13,15\).

Por lo tanto, \(|a_{n-1}|=14\) es el mínimo posible.

**Paso 8: verificar que no haya caso con \(n=5\) o más**

Para \(n=5\),

\[
a_0 = 2(-1)^5 r_1\cdots r_5 = -2 r_1\cdots r_5,
\]

así que \(r_1\cdots r_5 = -33\).

Necesitaríamos cinco enteros distintos cuyo producto sea \(-33\). Pero con divisores de \(33\), los valores absolutos deben multiplicarse para dar \(33\). Si usamos cinco enteros no nulos, el producto en valor absoluto será al menos \(1\cdot1\cdot1\cdot1\cdot1=1\), pero para que sea \(33\) necesitamos cinco factores cuyo producto en valor absoluto sea \(33\).

Como los divisores de \(33\) son solo \(\pm1,\pm3,\pm11,\pm33\), cualquier conjunto de cinco divisores distintos tendrá un producto con valor absoluto mucho mayor que \(33\), salvo que todos sean \(\pm1\), pero no hay cinco \(\pm1\) distintos.

De hecho, el conjunto de cinco divisores distintos con el menor valor absoluto del producto sería:

\[
1,\ -1,\ 3,\ -3,\ 11
\]

cuyo producto es

\[
1\cdot(-1)\cdot3\cdot(-3)\cdot11 = 99,
\]

que ya supera \(33\). Por lo tanto, no es posible para \(n\ge5\).

**Conclusión final**

El mínimo valor posible de \(|a_{n-1}|\) es \(14\), alcanzado con \(f(x)=2x^3+14x^2-82x+66\), cuyas raíces son \(1,3,-11\), todas enteras y distintas.

\[
\boxed{14}
\]