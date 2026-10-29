Vamos a razonar paso a paso.

**Paso 1: Modelar el problema**

Tenemos una cuadrícula $2\times 2$ con 4 cuadrados unitarios. Hay 12 segmentos unitarios (lados). Cada cuadrado debe tener exactamente 2 lados rojos y 2 azules.

**Paso 2: Codificar los colores**

Asignemos a cada segmento una variable binaria. Por ejemplo, sea $x_i \in \{0,1\}$ donde $1$ = rojo y $0$ = azul (o viceversa). La condición de que cada cuadrado tenga 2 rojos y 2 azules significa que la suma de los 4 lados de cada cuadrado es exactamente 2.

**Paso 3: Plantear las ecuaciones**

Numeremos los segmentos. Hay 4 cuadrados, cada uno impone una ecuación lineal sobre $\mathbb{Z}$ (o módulo 2, pero aquí la condición es de suma exacta, no de paridad).

Las 4 ecuaciones son:
- Cuadrado superior izquierdo: suma de sus 4 lados = 2
- Cuadrado superior derecho: suma = 2
- Cuadrado inferior izquierdo: suma = 2
- Cuadrado inferior derecho: suma = 2

**Paso 4: Contar soluciones**

Hay 12 variables y 4 ecuaciones. Los segmentos interiores (compartidos entre dos cuadrados) aparecen en dos ecuaciones, mientras que los del borde exterior aparecen en una sola.

Contemos los segmentos:
- Borde exterior: 8 segmentos (perímetro del cuadrado grande $2\times 2$).
- Segmentos interiores: 4 segmentos (2 horizontales interiores + 2 verticales interiores).

Total: $8 + 4 = 12$. ✓

**Paso 5: Resolver el sistema**

Sea $a_1, a_2, a_3, a_4$ los 4 segmentos interiores, y $b_1, \dots, b_8$ los 8 segmentos del borde.

Las ecuaciones de los 4 cuadrados:

1. Cuadrado superior izquierdo: $b_1 + b_2 + a_1 + a_2 = 2$
2. Cuadrado superior derecho: $b_3 + b_4 + a_1 + a_3 = 2$
3. Cuadrado inferior izquierdo: $b_5 + b_6 + a_2 + a_4 = 2$
4. Cuadrado inferior derecho: $b_7 + b_8 + a_3 + a_4 = 2$

donde los $b_i$ son los lados del borde correspondientes a cada cuadrado.

**Paso 6: Contar por casos sobre los segmentos interiores**

Los 4 segmentos interiores $a_1, a_2, a_3, a_4$ pueden tomar $2^4 = 16$ configuraciones. Para cada una, los 8 segmentos del borde quedan determinados de forma independiente.

Para cada cuadrado, dado el valor de sus 2 segmentos interiores, los 2 segmentos del borde deben sumar $2 - (\text{suma de interiores})$.

- Si los 2 interiores suman 0: los 2 del borde deben sumar 2 → solo 1 forma (ambos rojos).
- Si los 2 interiores suman 1: los 2 del borde deben sumar 1 → 2 formas.
- Si los 2 interiores suman 2: los 2 del borde deben sumar 0 → solo 1 forma (ambos azules).

Cada cuadrado es independiente en cuanto a sus lados del borde (los lados del borde no se comparten entre cuadrados).

**Paso 7: Calcular el total**

Para una configuración fija de los 4 interiores, el número de formas de colorear los bordes es el producto sobre los 4 cuadrados del número de opciones para sus 2 lados del borde.

Sea $s_k$ la suma de los 2 lados interiores del cuadrado $k$. El número de opciones para el borde del cuadrado $k$ es:
- $1$ si $s_k = 0$ o $s_k = 2$
- $2$ si $s_k = 1$

Entonces el número total de coloraciones es:

$$\sum_{a_1,a_2,a_3,a_4 \in \{0,1\}} \prod_{k=1}^{4} f(s_k)$$

donde $f(0)=f(2)=1$, $f(1)=2$.

**Paso 8: Evaluar la suma**

Las sumas $s_k$ son:
- $s_1 = a_1 + a_2$
- $s_2 = a_1 + a_3$
- $s_3 = a_2 + a_4$
- $s_4 = a_3 + a_4$

Contemos por el número de $a_i$ iguales a 1. Sea $m$ = número de unos entre $a_1, a_2, a_3, a_4$.

- $m=0$: todos $s_k = 0$, producto $= 1^4 = 1$. Hay $\binom{4}{0}=1$ config.
- $m=4$: todos $s_k = 2$, producto $= 1^4 = 1$. Hay $\binom{4}{4}=1$ config.
- $m=1$: exactamente un $a_i=1$. Entonces dos cuadrados tienen $s=1$ y dos tienen $s=0$. Producto $= 2^2 \cdot 1^2 = 4$. Hay $\binom{4}{1}=4$ configs.
- $m=3$: exactamente un $a_i=0$. Entonces dos cuadrados tienen $s=1$ y dos tienen $s=2$. Producto $= 2^2 \cdot 1^2 = 4$. Hay $\binom{4}{3}=4$ configs.
- $m=2$: dos unos. Hay dos subcasos:
  - Los dos unos son adyacentes (comparten un cuadrado): hay 4 pares adyacentes en un ciclo de 4. Entonces un cuadrado tiene $s=2$, dos cuadrados tienen $s=1$, y un cuadrado tiene $s=0$. Producto $= 1 \cdot 2^2 \cdot 1 = 4$.
  - Los dos unos son opuestos (diagonal): hay 2 pares opuestos. Entonces los 4 cuadrados tienen $s=1$. Producto $= 2^4 = 16$.

Total de configuraciones de interiores con $m=2$: $4 + 2 = 6$.

**Paso 9: Sumar todo**

- $m=0$: $1 \cdot 1 = 1$
- $m=1$: $4 \cdot 4 = 16$
- $m=2$ (adyacentes): $4 \cdot 4 = 16$
- $m=2$ (opuestos): $2 \cdot 16 = 32$
- $m=3$: $4 \cdot 4 = 16$
- $m=4$: $1 \cdot 1 = 1$

Suma total: $1 + 16 + 16 + 32 + 16 + 1 = 82$.

**Paso 10: Verificación alternativa**

Podemos verificar con un enfoque de transferencia de matrices o simplemente confiar en el conteo sistemático. El resultado $82$ es consistente.

Por lo tanto, el número de coloraciones es:

$$\boxed{82}$$