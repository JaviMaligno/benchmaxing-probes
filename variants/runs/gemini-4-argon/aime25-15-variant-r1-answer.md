Para hallar el número $M$ de ternas ordenadas de enteros positivos $(x, y, z)$ con $x, y, z \le 3^7$ tales que $x^3 + y^3 + z^3$ sea divisible por $3^8$, analizamos el comportamiento de $x^3 \pmod{3^8}$.

### Paso 1: Periodicidad y estructura de los cubos módulo $3^8$
Observamos primero que para cualquier entero $x$ y cualquier entero $k$:
$$(x + k \cdot 3^7)^3 = x^3 + 3 x^2 k \cdot 3^7 + 3 x k^2 \cdot 3^{14} + k^3 \cdot 3^{21} \equiv x^3 \pmod{3^8}.$$
Por lo tanto, el valor de $x^3 \pmod{3^8}$ depende únicamente de $x \pmod{3^7}$.

Sea $F(n)$ el número de ternas $(x, y, z) \in \{1, 2, \dots, 3^n\}^3$ tales que
$$x^3 + y^3 + z^3 \equiv 0 \pmod{3^{n+1}}.$$
Queremos calcular $M = F(7)$.

### Paso 2: Análisis según la divisibilidad por $3$
Para un $n \ge 1$ dado, dividimos el conjunto $\{1, 2, \dots, 3^n\}$ en dos subconjuntos:
1. $S_0 = \{x \in \{1, \dots, 3^n\} : 3 \nmid x\}$, que tiene $2 \cdot 3^{n-1}$ elementos.
2. $S_{\ge 1} = \{x \in \{1, \dots, 3^n\} : 3 \mid x\}$, que tiene $3^{n-1}$ elementos.

Notemos que:
- Si $x \in S_0$, entonces $x \equiv \pm 1 \pmod 3$, lo que implica $x^3 \equiv \pm 1 \pmod 9$.
- Si $x \in S_{\ge 1}$, entonces $3 \mid x$, por lo que $27 \mid x^3$ y en particular $x^3 \equiv 0 \pmod 9$.

Para que $x^3 + y^3 + z^3 \equiv 0 \pmod{3^{n+1}}$, es necesario que $x^3 + y^3 + z^3 \equiv 0 \pmod 9$. Considerando los posibles residuos en $\{0, 1, -1\} \pmod 9$, existen únicamente dos configuraciones posibles para $(x, y, z)$:
- **Caso A:** Exactamente dos elementos pertenecen a $S_0$ y uno pertenece a $S_{\ge 1}$.
- **Caso B:** Los tres elementos pertenecen a $S_{\ge 1}$.

#### Conteo del Caso A
El grupo de unidades $(\mathbb{Z}/3^{n+1}\mathbb{Z})^\times$ es cíclico de orden $2 \cdot 3^n$. El morfismo $u \mapsto u^3 \pmod{3^{n+1}}$ tiene núcleo $\{1 + k \cdot 3^n : k \in \{0, 1, 2\}\}$, por lo que al restringir el dominio a $S_0$ (representantes módulo $3^n$), la aplicación $x \mapsto x^3 \pmod{3^{n+1}}$ es una **biyección** entre $S_0$ y el conjunto:
$$U_n = \{u \in \mathbb{Z}/3^{n+1}\mathbb{Z} : u \equiv \pm 1 \pmod 9\},$$
ambos de tamaño $2 \cdot 3^{n-1}$.

Si elegimos cuál de las tres variables está en $S_{\ge 1}$ (hay $3$ opciones, digamos $z \in S_{\ge 1}$) y fijamos cualquier $z \in S_{\ge 1}$ ($3^{n-1}$ opciones) y cualquier $x \in S_0$ ($2 \cdot 3^{n-1}$ opciones), entonces como $z^3 \equiv 0 \pmod 9$ y $x^3 \equiv \pm 1 \pmod 9$, el valor requerido para $y^3$:
$$v \equiv -z^3 - x^3 \pmod{3^{n+1}}$$
satisface $v \equiv \mp 1 \pmod 9$, es decir, $v \in U_n$. Por la biyectividad, existe un único $y \in S_0$ tal que $y^3 \equiv v \pmod{3^{n+1}}$. Así, el número de ternas en el Caso A es:
$$3 \times 3^{n-1} \times (2 \cdot 3^{n-1}) \times 1 = 2 \cdot 3^{2n-1}.$$

#### Conteo del Caso B (Reducción recursiva)
Si $x, y, z \in S_{\ge 1}$, escribimos $x = 3x_1, y = 3y_1, z = 3z_1$ con $x_1, y_1, z_1 \in \{1, \dots, 3^{n-1}\}$. La condición para $n \ge 4$ se convierte en:
$$27(x_1^3 + y_1^3 + z_1^3) \equiv 0 \pmod{3^{n+1}} \iff x_1^3 + y_1^3 + z_1^3 \equiv 0 \pmod{3^{n-2}}.$$
Como $x_1^3 \pmod{3^{n-2}}$ solo depende de $x_1 \pmod{3^{n-3}}$, cada variable en $\{1, \dots, 3^{n-1}\}$ recorre un sistema completo de residuos módulo $3^{n-3}$ exactamente $3^2 = 9$ veces. Por tanto, para las tres variables obtenemos $(3^2)^3 F(n-3) = 3^6 F(n-3)$ soluciones.

### Paso 3: Cálculo de $M = F(7)$
Aplicando la relación $F(n) = 2 \cdot 3^{2n-1} + 3^6 F(n-3)$ sucesivamente:
1. Para $n = 7$:
   $$F(7) = 2 \cdot 3^{13} + 3^6 F(4).$$
2. Para $n = 4$:
   $$F(4) = 2 \cdot 3^7 + 3^6 F(1).$$
3. Para $n = 1$, contamos las ternas $(x, y, z) \in \{1, 2, 3\}^3$ tales que $x^3 + y^3 + z^3 \equiv 0 \pmod 9$. Como $1^3 \equiv 1$, $2^3 \equiv -1$ y $3^3 \equiv 0 \pmod 9$, las soluciones son las $3! = 6$ permutaciones de $(1, 2, 3)$ más la terna $(3, 3, 3)$, lo que da:
   $$F(1) = 6 + 1 = 7.$$

Sustituyendo hacia atrás:
$$M = F(7) = 2 \cdot 3^{13} + 3^6 \left(2 \cdot 3^7 + 3^6 \cdot 7\right) = 2 \cdot 3^{13} + 2 \cdot 3^{13} + 7 \cdot 3^{12} = (6 + 6 + 7) \cdot 3^{12} = 19 \cdot 3^{12}.$$

### Paso 4: Cálculo módulo $1000$
Calculamos $3^{12} \pmod{1000}$:
$$3^{12} = (3^6)^2 = 729^2 = 531441 \equiv 441 \pmod{1000}.$$
Finalmente, multiplicamos por $19$:
$$M \equiv 19 \times 441 = 8379 \equiv 379 \pmod{1000}.$$

\boxed{379}