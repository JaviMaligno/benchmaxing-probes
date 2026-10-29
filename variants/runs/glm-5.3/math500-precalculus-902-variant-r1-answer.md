## Solución

**1. Colocación del octaedro.** Pongo los seis vértices del octaedro regular en
$$(\pm a,0,0),\quad (0,\pm a,0),\quad (0,0,\pm a),$$
y sea $Q=(x,y,z)$, con $u=x^2+y^2+z^2$.

**2. Propiedad clave.** Las distancias al cuadrado a un vértice y a su opuesto son
$$x^2+y^2+z^2+a^2\pm 2ax,\qquad \text{etc.},$$
de modo que **cada par de vértices opuestos da dos distancias al cuadrado que suman lo mismo**: $2(u+a^2)$.

**3. Emparejamiento.** Las cinco distancias dadas al cuadrado son
$$16,\;64,\;100,\;121,\;169,$$
y sea $d^2$ la sexta. Las seis cifras deben repartirse en tres pares (opuestos) con **suma común** $S$. Busco entre los valores conocidos dos pares disjuntos de suma igual; repasando los cinco subconjuntos de cuatro elementos, la única que funciona es
$$16+169 \;=\; 64+121 \;=\; 185.$$
(Con cualquiera de los otros cuatro, las sumas de los dos pares difieren.)

Por tanto $d^2$ debe emparejarse con el valor sobrante, $100$:
$$d^2+100=185\;\Longrightarrow\; d^2=85\;\Longrightarrow\; d=\sqrt{85}.$$

**4. Verificación de que existe tal punto.** Con emparejas $(16,169),(64,121),(85,100)$ se obtiene $a|x|=38{,}25$, $a|y|=14{,}25$, $a|z|=3{,}75$ y $u+a^2=92{,}5$, lo que lleva a $16a^4-1480a^2+26883=0$, que tiene raíces positivas ($a^2\approx 24{,}8$ y $67{,}7$). Así que la configuración es realizable y no hay otra.

$$\boxed{\sqrt{85}}$$