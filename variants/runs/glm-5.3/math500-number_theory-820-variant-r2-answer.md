**Paso 1.** Sea $g=\gcd(m,n)=2310$. Escribimos $m=g\cdot a$ y $n=g\cdot b$ con $\gcd(a,b)=1$.

**Paso 2.** Entonces
$$\mathop{\text{lcm}}[m,n]=g\cdot a\cdot b=2310^3 \implies a\cdot b=\frac{2310^3}{2310}=2310^2.$$

**Paso 3.** Factorizamos $2310=2\cdot 3\cdot 5\cdot 7\cdot 11$, así que
$$ab=2^2\cdot 3^2\cdot 5^2\cdot 7^2\cdot 11^2.$$

**Paso 4.** Como $\gcd(a,b)=1$, cada primo $p\in\{2,3,5,7,11\}$ (con exponente $2$ en el producto) debe repartirse completamente entre $a$ y $b$: exponentes $(2,0)$ o $(0,2)$. Son $2$ opciones por cada uno de los $5$ primos, lo que da $2^5=32$ pares ordenados $(a,b)$.

(Notemos que nunca ocurre $a=b$: eso exigiría $a=b=2310$, contradictorio con $\gcd(a,b)=1$.)

**Paso 5.** La condición $m<n$ equivale a $a<b$, que selecciona exactamente la mitad de los pares, ya que $(a,b)$ y $(b,a)$ están emparejados:

$$\frac{32}{2}=16.$$

**Verificación.** Cada valor de $m$ queda determinado por el subconjunto de primos asignados a $a$; hay $2^5$ asignaturas y la simetría $a\leftrightarrow b$ reduce a la mitad, dando $16$ valores distintos de $m$.

$$\boxed{16}$$