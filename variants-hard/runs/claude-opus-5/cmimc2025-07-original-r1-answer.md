**Enfoque:** $a_n$ tiene $n$ dígitos, siendo el $k$-ésimo dígito igual a $k \bmod 10$. Calcular $\nu_3$ de números de hasta 810 dígitos a mano es inviable, así que lo computo directamente.

`a_n = 10*a_{n-1} + (n mod 10)`, y acumulo `ν₃`.