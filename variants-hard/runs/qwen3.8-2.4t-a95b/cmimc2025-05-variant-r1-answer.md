

Sea \(x\) un múltiplo de \(91\) menor que \(1{,}000{,}000\). Incluimos temporalmente a \(0\), pues no aporta ningún dígito impar.

Escribimos cada número como un bloque de seis cifras:

\[
x=1000a+b,\qquad 0\le a,b\le 999.
\]

Como

\[
1000=91\cdot 11-1 \equiv -1 \pmod{91},
\]

tenemos

\[
x\equiv 0 \pmod{91}
\iff -a+b\equiv 0 \pmod{91}
\iff b\equiv a \pmod{91}.
\]

Ahora contamos los números de \(0\) a \(999\) según su residuo módulo \(91\). Como

\[
1000=91\cdot 10+90,
\]

los residuos \(0,1,\dots,89\) aparecen \(11\) veces, y el residuo \(90\) aparece \(10\) veces.

Sea \(S_r\) la suma de los dígitos impares de todos los números de \(0\) a \(999\), escritos con tres cifras, que tienen residuo \(r\) módulo \(91\).

La suma total buscada es

\[
2\sum_{r=0}^{90} c_r S_r,
\]

donde \(c_r=11\) para \(r=0,\dots,89\) y \(c_{90}=10\). El factor \(2\) aparece porque cada número de seis cifras tiene dos bloques de tres cifras, \(a\) y \(b\).

Primero calculamos la suma total de dígitos impares en todos los bloques de tres cifras \(000\) a \(999\). En cada posición, cada dígito aparece \(100\) veces. Los dígitos impares suman

\[
1+3+5+7+9=25.
\]

Por posición:

\[
100\cdot 25=2500.
\]

Con tres posiciones:

\[
\sum_{r=0}^{90} S_r=3\cdot 2500=7500.
\]

Entonces

\[
\sum_{r=0}^{90} c_rS_r
=11\cdot 7500-S_{90}.
\]

Falta calcular \(S_{90}\). Los números de \(0\) a \(999\) congruentes con \(90\) módulo \(91\) son

\[
090,\ 181,\ 272,\ 363,\ 454,\ 545,\ 636,\ 727,\ 818,\ 909.
\]

Sus sumas de dígitos impares son:

\[
9,\ 2,\ 7,\ 6,\ 5,\ 10,\ 3,\ 14,\ 1,\ 18.
\]

Por tanto,

\[
S_{90}=9+2+7+6+5+10+3+14+1+18=75.
\]

Así,

\[
\sum_{r=0}^{90} c_rS_r
=11\cdot 7500-75
=82500-75
=82425.
\]

La suma total para los seis dígitos es

\[
2\cdot 82425=164850.
\]

El \(0\) no aporta nada, así que esta es también la suma para los múltiplos positivos.

\[
\boxed{164850}
\]