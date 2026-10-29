Los ceros finales de $n!$ provienen de los factores de $10 = 2 \times 5$. Como en $47!$ hay más factores 2 que factores 5, basta contar cuántas veces aparece el factor 5.

**Paso 1:** Múltiplos de 5 entre 1 y 47:
$$\left\lfloor \frac{47}{5} \right\rfloor = 9 \quad (5, 10, 15, 20, 25, 30, 35, 40, 45)$$

**Paso 2:** Múltiplos de 25, que aportan un factor 5 adicional:
$$\left\lfloor \frac{47}{25} \right\rfloor = 1 \quad (25)$$

**Total:** $9 + 1 = 10$ factores de 5 (y sobran factores de 2 para emparejarlos).

\boxed{10}