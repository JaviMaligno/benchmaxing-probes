Los ceros al final de un factorial provienen de los factores de 10, es decir, de pares de factores 2 y 5. Como hay más factores 2 que factores 5 en 42!, basta contar cuántos factores 5 hay.

**Paso 1:** Múltiplos de 5 hasta 42: ⌊42/5⌋ = 8 (números 5, 10, 15, 20, 25, 30, 35, 40).

**Paso 2:** Múltiplos de 25 hasta 42: ⌊42/25⌋ = 1 (el número 25 contribuye un factor 5 adicional).

**Paso 3:** Múltiplos de 125: ⌊42/125⌋ = 0, así que ya no hay más aportes.

Total de factores de 5: 8 + 1 = 9. Como sobran factores de 2, cada 5 forma un 10, dando 9 ceros al final.

\boxed{9}