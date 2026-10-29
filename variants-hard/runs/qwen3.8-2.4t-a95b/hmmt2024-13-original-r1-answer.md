

Clasifiquemos los cubitos según cuántas caras del cubo grande muestran:

- Esquinas: \(8\), visibles en \(3\) caras.
- Centros de arista: \(12\), visibles en \(2\) caras.
- Centros de cara: \(6\), visibles en \(1\) cara.
- Centro interior: \(1\), visible en \(0\) caras.

Debemos elegir 2 posiciones para los cubitos rojos de modo que la unión de las caras donde se ve rojo tenga tamaño exactamente \(4\).

Casos posibles:

1. **Esquina + esquina**: deben compartir exactamente 2 caras, es decir, ser extremos de una misma arista del cubo grande. Hay \(12\) aristas, así que hay \(12\) pares.

2. **Esquina + centro de arista**: para cubrir \(4\) caras, deben compartir exactamente 1 cara. Para cada centro de arista, hay \(4\) esquinas que cumplen esto. Total:
\[
12\cdot 4=48.
\]

3. **Esquina + centro de cara**: deben ser disjuntos en caras visibles. Para cada esquina, los centros de cara disjuntos son los de las \(3\) caras opuestas. Total:
\[
8\cdot 3=24.
\]

4. **Centro de arista + centro de arista**: sus dos caras visibles deben ser disjuntas. Para cada centro de arista, hay \(5\) centros de arista disjuntos. Como cada par se cuenta dos veces:
\[
\frac{12\cdot 5}{2}=30.
\]

Sumando:
\[
12+48+24+30=114.
\]

\[
\boxed{114}
\]