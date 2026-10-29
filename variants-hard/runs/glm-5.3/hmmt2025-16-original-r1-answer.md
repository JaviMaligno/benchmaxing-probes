Contemos primero pares ordenados de rectángulos y después dividamos por \(2\).

En una cuadrícula \(5\times 5\) hay \(6\) líneas verticales y \(6\) horizontales. Un rectángulo queda determinado por dos líneas en cada dirección, así que hay
\[
\binom{6}{2}=15
\]
intervalos posibles en cada dirección.

Dos rectángulos no pueden compartir interior, lados ni vértices; es decir, sus rectángulos cerrados deben ser disjuntos. Esto ocurre exactamente cuando sus intervalos horizontales son disjuntos o sus intervalos verticales son disjuntos.

En una dirección, el número de pares ordenados de intervalos disjuntos es
\[
2\binom{6}{4}=30.
\]
Elegimos cuatro líneas \(p_1<p_2<p_3<p_4\); un intervalo es \([p_1,p_2]\), el otro es \([p_3,p_4]\), y hay \(2\) maneras de asignarlos al primer y segundo rectángulo.

Para pares ordenados de rectángulos:

- Separación horizontal: \(30\cdot 15\cdot 15=6750\).
- Separación vertical: \(6750\).
- Ambas separaciones: \(30\cdot 30=900\).

Por inclusión-exclusión, los pares ordenados válidos son
\[
6750+6750-900=12600.
\]

Como el orden no importa, cada par válido se contó dos veces, así que
\[
\frac{12600}{2}=6300.
\]

\[
\boxed{6300}
\]