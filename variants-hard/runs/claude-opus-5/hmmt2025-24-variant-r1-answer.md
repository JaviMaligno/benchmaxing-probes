## Planteamiento

Caracterizo primero la relación de inscripción. Si una semicircunferencia de radio $\rho$ está inscrita en una de centro $C$, radio $R$, dirección del diámetro $u$ y normal interior $n$:

- Su centro $C'$ cumple $C' = C + a\,u + \rho\,n$,
- Como los extremos de su diámetro están en la circunferencia grande: $|C'-C|^2+\rho^2=R^2$, luego $|C'-C|=\sqrt{R^2-\rho^2}$ y $a^2 = R^2-2\rho^2$,
- Su diámetro es perpendicular a $C'-C$, y su arco se curva **hacia** $C$, es decir $n' = -\frac{C'-C}{|C'-C|}$,
- El punto de tangencia con el diámetro grande es el pie de la perpendicular: $C' - \rho\, n$.

## Aplicación

Tomo $\omega_3$ con centro $O_3=(0,0)$, $u_3=(1,0)$, $n_3=(0,1)$, $R=12$.

Para $\omega_2$ (radio $r$): $C_2=(a,r)$ con
$$a^2 = 144-2r^2,\qquad s:=|C_2|=\sqrt{144-r^2}.$$
Entonces $n_2=-\frac{(a,r)}{s}$ y $u_2=\frac{(-r,a)}{s}$.

Para $\omega_1$ (radio $3$): $C_1 = C_2 + a_1u_2 + 3n_2$ con $a_1^2 = r^2-18$, y
$$C_1-C_2=\frac{1}{s}\big(-a_1r-3a,\; a_1a-3r\big).$$

El diámetro de $\omega_1$ es perpendicular a $C_1-C_2$; que sea paralelo al de $\omega_3$ exige que $C_1-C_2$ sea vertical:
$$-a_1r-3a=0\ \Longrightarrow\ a_1=-\frac{3a}{r}.$$

Sustituyendo en $a_1^2=r^2-18$ y usando $a^2=144-2r^2$:
$$\frac{9(144-2r^2)}{r^2}=r^2-18\ \Longrightarrow\ 1296-18r^2=r^4-18r^2\ \Longrightarrow\ r^4=1296,$$
luego $r=6$ (y $a^2=72$, $a_1^2=18$: configuración válida).

## Cálculo final

El punto de tangencia es $T=C_2-(0,r)=(a,0)$, con $P=(-12,0)$, $Q=(12,0)$:
$$PT\cdot TQ=(12+a)(12-a)=144-a^2=144-72=72.$$

(De hecho, en general $PT\cdot TQ = 144-a^2 = 2r^2$.)

\boxed{72}