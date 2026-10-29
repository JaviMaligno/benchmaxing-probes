Voy a razonar con álgebra y además verificarlo por fuerza bruta.

**Reformulación.** Escribiendo la composición como producto ($fg$ significa $f\circ g$), las seis condiciones son:

$$fgh=g,\quad hgf=g,\quad ghf=h,\quad fhg=h,\quad hfg=f,\quad gfh=f.$$

De $fgh=g$ sale $h=g^{-1}f^{-1}g$, y de $gfh=f$ sale $h=f^{-1}g^{-1}f$; de $hgf=g$ sale $h=gf^{-1}g^{-1}$ y de $hfg=f$ sale $h=fg^{-1}f^{-1}$. Comparándolas: $g^2$ conmuta con $f$ y $f^2$ conmuta con $g$, y $f,g,h$ son todos conjugados entre sí. Esto recorta mucho el espacio, pero conviene confirmar el conteo exacto.