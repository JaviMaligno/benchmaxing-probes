Para encontrar el número total de coloraciones válidas, podemos dividir los $12$ segmentos unitarios en dos grupos:
1. Los **$4$ segmentos internos**, que son compartidos por dos cuadrados adyacentes (los que se unen en el vértice central de la cuadrícula).
2. Los **$8$ segmentos externos** (en el borde exterior de la cuadrícula $2 \times 2$), a razón de $2$ segmentos externos por cada uno de los $4$ cuadrados unitarios.

Observemos que, una vez fijados los colores de los $4$ segmentos internos, las elecciones de colores para los $2$ segmentos externos de cada cuadrado unitario son independientes entre sí:
- Si los $2$ segmentos internos de un cuadrado tienen el **mismo color** (ambos rojos o ambos azules), entonces sus $2$ segmentos externos están obligados a ser del color opuesto. En este caso hay $\binom{2}{0} = 1$ forma de colorear sus segmentos externos.
- Si los $2$ segmentos internos de un cuadrado tienen **colores diferentes** (uno rojo y uno azul), entonces entre sus $2$ segmentos externos debe haber uno rojo y uno azul. En este caso hay $\binom{2}{1} = 2$ formas de colorear sus segmentos externos.

Denotemos los $4$ segmentos internos en orden cíclico alrededor del centro como $(e_1, e_2, e_3, e_4)$. Hay $2^4 = 16$ formas de colorear estos $4$ segmentos. Cada cuadrado unitario contiene un par de segmentos internos consecutivos en este ciclo: $(e_1, e_2)$, $(e_2, e_3)$, $(e_3, e_4)$ y $(e_4, e_1)$.

Si $k$ es el número de cuadrados cuyos dos segmentos internos tienen colores distintos (es decir, el número de cambios de color en el ciclo $(e_1, e_2, e_3, e_4, e_1)$), entonces hay $2^k$ formas de colorear los $8$ segmentos externos. Clasificamos las $16$ configuraciones de los segmentos internos según el valor de $k$:

1. **$k = 0$ (ningún cambio de color):** Todos los segmentos internos tienen el mismo color: $(R,R,R,R)$ o $(A,A,A,A)$.
   - Hay $2$ configuraciones de este tipo.
   - Cada una permite $2^0 = 1$ forma de colorear los segmentos externos.
   - Total en este caso: $2 \times 1 = 2$.

2. **$k = 4$ (los colores alternan):** Los segmentos internos alternan de color alrededor del centro: $(R,A,R,A)$ o $(A,R,A,R)$.
   - Hay $2$ configuraciones de este tipo.
   - Cada una permite $2^4 = 16$ formas de colorear los segmentos externos.
   - Total en este caso: $2 \times 16 = 32$.

3. **$k = 2$ (dos cambios de color):** Como el número de cambios de color en un ciclo siempre es par, las $16 - 2 - 2 = 12$ configuraciones restantes (aquellas con $3$ segmentos de un color y $1$ del otro, o con $2$ adyacentes de cada color) tienen exactamente $k = 2$.
   - Hay $12$ configuraciones de este tipo.
   - Cada una permite $2^2 = 4$ formas de colorear los segmentos externos.
   - Total en este caso: $12 \times 4 = 48$.

Sumando todos los casos posibles, obtenemos el número total de coloraciones:
$$2 + 32 + 48 = 82$$

\boxed{82}