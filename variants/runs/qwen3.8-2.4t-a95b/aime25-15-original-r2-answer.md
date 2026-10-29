Sea \(M=3^7=2187\). Clasificamos \(a\) según \(v_3(a)\).

**Tipos de cubos módulo \(3^7\):**

1. **Unidades** \(3\nmid a\): hay \(486\) valores.  
   Los cubos son exactamente los residuos módulo \(3^7\) congruentes a \(\pm1 \pmod 9\), cada uno una vez.  
   En efecto, todo cubo de unidad es \(\pm1 \pmod 9\), y hay \(2\cdot 3^5=486\) tales residuos; la inyectividad se sigue de que \(x^3\equiv1\pmod{3^7}\) fuerza \(x\equiv1\pmod{3^6}\).

2. **\(v_3(a)=1\)**: \(a=3u\), con \(u\) unidad. Hay \(162\) valores.  
   \(a^3=27u^3\). Módulo \(81\), \(u^3\) recorre los residuos \(\pm1\pmod 9\), y cada uno aparece \(9\) veces.

3. **\(v_3(a)=2\)**: \(a=9u\). Hay \(54\) valores.  
   \(a^3\equiv \pm 729 \pmod{3^7}\), con \(27\) valores para cada signo.

4. **\(v_3(a)\ge3\)**: hay \(27\) valores, y su cubo es \(0\pmod{3^7}\).

Llamemos \(U\) al primer tipo y \(N\) a la unión de los otros tres. Los elementos de \(N\) tienen cubos múltiplos de \(27\), en particular congruentes a \(0\pmod 9\).

**Lema de pares.** Si \(C_m\) es el conjunto de residuos módulo \(3^m\) congruentes a \(\pm1\pmod 9\), entonces para todo \(s\equiv0\pmod 9\),
\[
\#\{(x,y)\in C_m^2:x+y\equiv s\}=|C_m|,
\]
pues \(x\mapsto s-x\) biyecta \(C_m\). Así, para \(m=7\) hay \(486\) pares, y para \(m=4\) hay \(18\).

**Conteo por número de unidades:**

- **3 unidades:** imposible, porque la suma de tres números \(\pm1\pmod 9\) nunca es \(0\pmod 9\).
- **1 unidad:** imposible módulo \(9\).
- **2 unidades:** el tercer término es de tipo no unidad. Para cada uno de los \(162+54+27=243\) elementos no unidad, hay \(486\) pares de unidades. Con \(3\) posiciones:
  \[
  3\cdot 486\cdot 243=354294.
  \]

- **0 unidades:** dividimos todo entre \(27\) y trabajamos módulo \(81\).  
  Los tipo \(v_3=1\) dan residuos en \(C_4\) con peso \(9\); los tipos \(v_3\ge2\) dan \(0,\pm27\) con peso total \(81\).

  - Dos términos de \(C_4\) y uno de \(\{0,\pm27\}\):
    \[
    3\cdot 18\cdot 9^2\cdot 81=354294.
    \]
  - Solo términos de \(\{0,\pm27\}\): escribiendo \(27t\), \(t\in\mathbb F_3\), hay \(9\) ternas con suma \(0\pmod 3\), cada una con peso \(27^3\):
    \[
    9\cdot 27^3=177147.
    \]
  - Con una o tres unidades módulo \(81\), imposible módulo \(9\).

Por tanto,
\[
N=354294+354294+177147=885735.
\]

Finalmente,
\[
885735 \equiv 735 \pmod{1000}.
\]

\[
\boxed{735}
\]