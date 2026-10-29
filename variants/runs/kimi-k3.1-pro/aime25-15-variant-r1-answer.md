Como \((a+3^7)^3\equiv a^3\pmod{3^8}\), podemos contar residuos módulo \(3^7\).

Para cada residuo, sea \(v_3(x)\) su valuación \(3\)-ádica. Si \(v_3(x)\ge3\), entonces \(x^3\equiv0\pmod{3^8}\). Hay \(3^4=81\) tales residuos, así que el caso en que los tres sean de este tipo aporta
\[
81^3=3^{12}.
\]

En los demás casos, la menor valuación \(m\in\{0,1,2\}\) debe aparecer exactamente dos veces: si aparece una sola vez no puede haber cancelación, y si aparece tres veces, la suma de los tres cubos tiene valuación exactamente \(3m+1\), insuficiente.

Fijemos la posición del tercer término, de valuación \(b>m\). Escribimos los dos términos mínimos como \(3^m u,3^m v\), con \(u,v\) unidades. Tras dividir por \(3^{3m}\), debemos resolver una congruencia módulo \(3^r\), donde \(r=8-3m\).

Las unidades \(u,v\) deben ser opuestas módulo \(3\). Además,
\[
v_3(u^3+v^3)=1+v_3(u+v),
\]
pues
\[
u^3+v^3=(u+v)\bigl((u+v)^2-3uv\bigr).
\]

- Si el tercer término tiene valuación al menos \(3\), necesitamos \(v_3(u+v)\ge r-1\). El número de soluciones es \(2\cdot3^{m+10}\).
- Los únicos casos restantes son \((m,b)=(0,1),(0,2),(1,2)\). En ellos debe cumplirse \(v_3(u+v)=3(b-m)-1\). Sustituyendo \(v=-u+3^q s\), con \(q=v_3(u+v)\), y contando las unidades y sus levantamientos, se obtienen los valores de la tabla siguiente.

\[
\begin{array}{c|c|c}
m&\text{tercer término}&\text{número de soluciones, con su posición fijada}\\ \hline
0&b\ge3&2\cdot3^{10}\\
0&b=1&4\cdot3^{11}\\
0&b=2&4\cdot3^{10}\\
1&b\ge3&2\cdot3^{11}\\
1&b=2&4\cdot3^{11}\\
2&b\ge3&2\cdot3^{12}
\end{array}
\]

Para cada \(m\), la suma de su fila correspondiente es \(2\cdot3^{12}\). Hay tres valores de \(m\) y tres posiciones para el tercer término, por lo que
\[
M=3^{12}+9\bigl(2\cdot3^{12}\bigr)
=19\cdot3^{12}
=10\,097\,379.
\]
Por tanto, el resto al dividir entre \(1000\) es

\[
\boxed{379}
\]