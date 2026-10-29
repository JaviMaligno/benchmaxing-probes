## razonamiento

**observación clave.** las seis letras iniciales (las menores de cada par) son todas distintas, ya que los pares reparten las 12 letras sin repetirla. por tanto el orden alfabético de las palabras coincide exactamente con el orden de sus primeras letras. es decir, la última palabra es el par cuya letra menor es la mayor de todas.

numerando a=1, ..., l=12, el problema es: probabilidad de que el par con máximo mínimo contenga a h=8.

**caso b: h es la primera letra**, par (8,y), y ∈ {9,10,11,12}. se requiere que todos los otros pares tengan mínimo < 8. las otras 3 letras de {9,...,12} deben emparejarse con letras de {1,...,7} (entre ellas tendrían mínimo ≥ 9). número de emparejamientos: elegir pareja distinta para cada una (7·6·5 = 210) y emparejar las 4 letras bajas restantes de 3!! = 3 formas: 630 por cada y. total: **4·630 = 2520**.

**caso a: h es la segunda letra**, par (x,8), x < 8. se requiere que todo otro par tenga mínimo < x. las letras mayores que x (salvo la 8) son {x+1,...,7} ∪ {9,...,12}, en total 11−x, y cada una debe emparejarse con una letra menor que x, que son x−1. se necesita 11−x ≤ x−1, o sea x ≥ 6:

- x=6, par (f,h): 5 altas {g,i,j,k,l} con 5 bajas {a,...,e}: biyección, 5! = **120**.
- x=7, par (g,h): 4 altas {i,j,k,l} con 6 bajas: 6·5·4·3 = 360, y las 2 bajas restantes se emparejan: **360**.

total caso a: **480**.

**total favorable:** 2520 + 480 = 3000, de un total de (12−1)!! = 11!! = 10395 emparejamientos.

**verificación de consistencia.** sumando las cuentas análogas para las letras 12, 11, 10, 9, 7, 6 (3840, 3840, 3840, 3630, 1920, 720) y 0 para las letras 1–5 se obtiene 20790 = 2·10395, como debe ser, pues cada emparejamiento contribuye dos letras al par final.

la probabilidad es
$$\frac{3000}{10395}=\frac{200}{693},$$
con 200 = 2³·5² y 693 = 3²·7·11 coprimos. así, m = 200 y n = 693.

## resultado

$$m+n = 200+693 = \boxed{893}$$