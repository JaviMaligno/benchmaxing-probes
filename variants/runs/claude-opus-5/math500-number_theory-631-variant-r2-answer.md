## Razonamiento

**Período de cada rueda** (tiempo de una vuelta completa):

- Rueda 1: $37\frac{1}{2} = \frac{75}{2}$ vueltas por minuto, es decir en 60 s. Período:
$$T_1 = \frac{60}{75/2} = \frac{120}{75} = \frac{8}{5} = 1{,}6\ \text{s}$$

- Rueda 2: 54 vueltas en 60 s. Período:
$$T_2 = \frac{60}{54} = \frac{10}{9}\ \text{s}$$

**El punto vuelve a apuntar hacia arriba** en los múltiplos enteros de su período, así que buscamos el menor $t>0$ que sea múltiplo común de $\frac{8}{5}$ y $\frac{10}{9}$:

$$\text{mcm}\left(\frac{8}{5},\frac{10}{9}\right)=\frac{\text{mcm}(8,10)}{\text{mcd}(5,9)}=\frac{40}{1}=40$$

**Verificación:**
- Rueda 1: $40 \div 1{,}6 = 25$ vueltas exactas ✓
- Rueda 2: $40 \div \frac{10}{9} = 36$ vueltas exactas ✓

Y ningún valor menor funciona: los tiempos de la rueda 1 son $1{,}6;\ 3{,}2;\ \dots$ y hace falta que $\frac{8k}{5}$ sea múltiplo de $\frac{10}{9}$, o sea $\frac{72k}{50}=\frac{36k}{25}$ entero, lo que exige $k=25$.

\boxed{40}