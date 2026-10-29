Para encontrar el número máximo de puertas (aristas) que Karthik puede atravesar, podemos modelar la cuadrícula de $11 \times 11$ como un grafo $G = (V, E)$, donde las celdas son los vértices y las puertas que conectan celdas adyacentes son las aristas.

### 1. Conteo del total de puertas (aristas)
En una cuadrícula de $n \times n$, hay $n(n-1)$ puertas horizontales y $n(n-1)$ puertas verticales. Para $n = 11$, el número total de puertas es:
$$|E| = 2 \times 11 \times (11 - 1) = 220$$

### 2. Condición de grado par (Teorema de Euler)
Un recorrido que comienza y termina en la misma celda sin repetir ninguna puerta equivale a un **circuito euleriano** en un subgrafo de $G$. Por el teorema de Euler, un subgrafo tiene un circuito euleriano si y solo si todas sus aristas pertenecen a una misma componente conexa y **todos los vértices tienen grado par**.

Analicemos los grados de los vértices en el grafo completo $G$:
- **4 celdas en las esquinas:** tienen grado $2$ (par).
- **$9 \times 9 = 81$ celdas interiores:** tienen grado $4$ (par).
- **$4 \times 9 = 36$ celdas en los bordes (sin contar las esquinas):** tienen grado $3$ (impar).

Para que todos los vértices tengan grado par en el subgrafo elegido, el conjunto de puertas que Karthik **no** utiliza debe formar un conjunto de caminos disjuntos en aristas que emparejen los $36$ vértices de grado impar.

### 3. Mínimo número de puertas a eliminar
Dividamos los $36$ vértices impares en $4$ grupos $T_1, T_2, T_3, T_4$ correspondientes a los $4$ bordes de la cuadrícula. Cada grupo $T_i$ contiene $9$ vértices consecutivos a lo largo de su borde:
- Dos vértices adyacentes dentro de un mismo borde $T_i$ están a distancia $1$ (conectados por una sola puerta).
- Sin embargo, como cada borde tiene $9$ vértices impares (un número impar), al emparejar vértices dentro de cada borde $T_i$ siempre quedará al menos $1$ vértice impar sin emparejar en cada uno de los $4$ bordes.
- Dos vértices impares pertenecientes a bordes distintos están separados al menos por una esquina, por lo que la distancia mínima entre ellos es de **$2$ puertas** (por ejemplo, pasando por la celda de la esquina que los separa).

Por lo tanto, de los $36 / 2 = 18$ emparejamientos necesarios entre vértices impares:
- A lo sumo $16$ parejas pueden formarse entre vértices adyacentes del mismo borde (costando $1$ puerta cada una, es decir, $4$ por borde).
- Al menos $2$ parejas deben conectar vértices de bordes distintos (costando al menos $2$ puertas cada una).

Así, el número mínimo de puertas que debemos eliminar es:
$$16 \times 1 + 2 \times 2 = 20$$

### 4. Construcción válida
Podemos lograr exactamente $20$ puertas eliminadas manteniendo el resto del grafo conexo:
1. En el borde superior, eliminamos las $4$ puertas entre las parejas $(1,2)-(1,3)$, $(1,4)-(1,5)$, $(1,6)-(1,7)$ y $(1,8)-(1,9)$, dejando libre $(1,10)$.
2. Conectamos $(1,10)$ con $(2,11)$ del borde derecho eliminando las $2$ puertas incidentes a la esquina $(1,11)$. Esto deja a la esquina $(1,11)$ con grado $0$ (aislada) y corrige la paridad de $(1,10)$ y $(2,11)$.
3. Emparejamos los $8$ vértices restantes del borde derecho $(3,11), \dots, (10,11)$ mediante $4$ puertas.
4. De manera simétrica, emparejamos los vértices del borde inferior y del borde izquierdo usando $4 + 2 + 4 = 10$ puertas (aislando la esquina opuesta $(11,1)$).

Como solo se han eliminado puertas del perímetro, todas las demás celdas siguen conectadas a través del interior de la cuadrícula y todos los vértices tienen grado par.

Por lo tanto, el número máximo de puertas que Karthik puede atravesar es:
$$220 - 20 = 200$$

\boxed{200}