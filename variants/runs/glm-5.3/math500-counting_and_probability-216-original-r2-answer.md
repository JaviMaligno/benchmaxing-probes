# Solución

**Datos:** 8 republicanos y 6 demócratas, para un total de 14 miembros. Queremos subcomités de 5 personas con al menos un miembro de cada partido.

**Paso 1: Total de subcomités sin restricción.**

$$\binom{14}{5} = \frac{14!}{5!\,9!} = 2002$$

**Paso 2: Restar los subcomités inválidos** (aquellos formados por un solo partido):

- Solo republicanos: $\binom{8}{5} = 56$
- Solo demócratas: $\binom{6}{5} = 6$

**Paso 3: Aplicar complemento.**

$$2002 - 56 - 6 = 1940$$

**Verificación por casos:**
- (1R, 4D): $\binom{8}{1}\binom{6}{4} = 8 \cdot 15 = 120$
- (2R, 3D): $\binom{8}{2}\binom{6}{3} = 28 \cdot 20 = 560$
- (3R, 2D): $\binom{8}{3}\binom{6}{2} = 56 \cdot 15 = 840$
- (4R, 1D): $\binom{8}{4}\binom{6}{1} = 70 \cdot 6 = 420$

Suma: $120 + 560 + 840 + 420 = 1940$ ✓

\boxed{1940}