Voy a resolver usando variables:

Sea:
- \(C\) = estudiantes de cálculo
- \(F\) = estudiantes de física
- \(Q\) = estudiantes de química

Datos:
- Total: \(360\)
- Todas tres: \(15\)
- Ninguna: \(15\)
- \(C = 180\)
- \(Q = 2F\)
- \(C \cap Q = 75\)
- \(F \cap Q = 75\)
- \(F \cap C = 30\)
- Se busca \(F\).

Por inclusión-exclusión, los que toman al menos una materia son:

\[
360 - 15 = 345
\]

Y:

\[
|C \cup F \cup Q| = C + F + Q - |C\cap F| - |C\cap Q| - |F\cap Q| + |C\cap F\cap Q|
\]

Sustituyendo:

\[
345 = 180 + F + 2F - 30 - 75 - 75 + 15
\]

\[
345 = 180 + 3F - 165
\]

Simplificando:

\[
345 = 3F + 15
\]

\[
330 = 3F
\]

\[
F = 110
\]

Así que **110 estudiantes toman física**.

\[
\boxed{110}
\]