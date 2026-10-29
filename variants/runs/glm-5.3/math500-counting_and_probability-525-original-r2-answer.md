# Resolución

**Paso 1: Sentar a las otras 4 personas.**

Primero siento a las 4 personas restantes alrededor de la mesa circular. Como las rotaciones se consideran iguales, el número de formas de sentar a \(n\) personas en círculo es \((n-1)!\):

\[
(4-1)! = 3! = 6
\]

**Paso 2: Identificar los espacios.**

Con las 4 personas sentadas, se crean \(4\) espacios entre ellas. Como todas las personas sentadas están separadas por al menos un espacio, **ninguno** de estos espacios es adyacente a otro.

**Paso 3: Colocar a Pierre, Rosa y Thomas.**

Coloco a las 3 personas restringidas en \(3\) de los \(4\) espacios. Como los espacios no son adyacentes entre sí, automáticamente ninguno de los tres quedará junto a otro.

- Elegir \(3\) espacios de los \(4\): \(\binom{4}{3} = 4\)
- Permutar a Pierre, Rosa y Thomas en los espacios elegidos: \(3! = 6\)

\[
4 \times 6 = 24
\]

**Paso 4: Total.**

\[
6 \times 24 = 144
\]

\boxed{144}