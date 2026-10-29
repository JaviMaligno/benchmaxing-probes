Para determinar cuántas horas tarda Dave en terminar la carrera de $1$ milla, analicemos el movimiento por intervalos de tiempo según el momento en que cada participante cruza la meta.

### 1. Tiempos de llegada de Alice, Bob y Charlie
La distancia total de la carrera es de $1\text{ milla}$. Conociendo sus velocidades constantes, calculamos el tiempo que tarda cada quien en llegar a la meta ($t = \frac{\text{distancia}}{\text{velocidad}}$):
* **Alice** ($8\text{ mph}$): termina en $t_A = \frac{1}{8}\text{ horas}$.
* **Bob** ($4\text{ mph}$): termina en $t_B = \frac{1}{4}\text{ horas}$.
* **Charlie** ($2\text{ mph}$): termina en $t_C = \frac{1}{2}\text{ horas}$.

### 2. Progreso de Dave paso a paso
Inicialmente, Dave corre a la mitad de la velocidad de Charlie, es decir, a una velocidad inicial de $\frac{2}{2} = 1\text{ mph}$.

* **Primer intervalo ($0 \le t \le \frac{1}{8}\text{ horas}$):**
  Antes de que alguien termine la carrera, Dave corre a $1\text{ mph}$. Cuando Alice cruza la meta en $t = \frac{1}{8}\text{ horas}$, la distancia que ha recorrido Dave es:
  $$d_1 = 1\text{ mph} \times \frac{1}{8}\text{ h} = \frac{1}{8}\text{ millas}$$

* **Segundo intervalo ($\frac{1}{8} \le t \le \frac{1}{4}\text{ horas}$):**
  En $t = \frac{1}{8}\text{ horas}$, Alice termina la carrera y la velocidad de Dave se duplica a $2\text{ mph}$. Este intervalo hasta que Bob termina en $t = \frac{1}{4}\text{ horas}$ dura $\frac{1}{4} - \frac{1}{8} = \frac{1}{8}\text{ horas}$. La distancia que recorre Dave en este tramo es:
  $$d_2 = 2\text{ mph} \times \frac{1}{8}\text{ h} = \frac{2}{8}\text{ millas} = \frac{1}{4}\text{ millas}$$
  La distancia total acumulada por Dave hasta $t = \frac{1}{4}\text{ horas}$ es:
  $$d_{\text{total}} = \frac{1}{8} + \frac{2}{8} = \frac{3}{8}\text{ millas}$$

* **Tercer intervalo ($t \ge \frac{1}{4}\text{ horas}$):**
  En $t = \frac{1}{4}\text{ horas}$, Bob cruza la meta y la velocidad de Dave vuelve a duplicarse, pasando a ser de $4\text{ mph}$. En ese instante, a Dave le falta por recorrer:
  $$d_{\text{restante}} = 1 - \frac{3}{8} = \frac{5}{8}\text{ millas}$$
  Si mantiene la velocidad de $4\text{ mph}$, el tiempo adicional necesario para cubrir las $\frac{5}{8}\text{ millas}$ restantes es:
  $$\Delta t = \frac{5/8\text{ millas}}{4\text{ mph}} = \frac{5}{32}\text{ horas}$$

### 3. Tiempo total
Sumamos el tiempo transcurrido hasta la llegada de Bob y el tiempo adicional del último tramo:
$$t_{\text{Dave}} = \frac{1}{4} + \frac{5}{32} = \frac{8}{32} + \frac{5}{32} = \frac{13}{32}\text{ horas}$$

Como $\frac{13}{32} < \frac{16}{32} = \frac{1}{2}$, Dave cruza la meta antes de que Charlie termine la carrera, por lo que no ocurre ninguna otra duplicación de velocidad.

\boxed{\frac{13}{32}}