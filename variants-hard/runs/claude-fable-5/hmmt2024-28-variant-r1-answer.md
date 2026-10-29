Voy a resolver este problema de geometría. Primero plantearé las ecuaciones (usando que la tangencia interna ocurre en X, lo que permite modelar ambas circunferencias tangentes a una recta común en X) y luego usaré Python para resolver el sistema con alta precisión e identificar la forma cerrada.

**Planteamiento:** Las dos circunferencias pasan por X y son tangentes, así que son tangentes en X con una recta tangente común ℓ. Coloco X en el origen con ℓ como eje x y ambos círculos arriba (tangencia interna). Un punto en dirección θ sobre un círculo de radio R tangente en el origen está a distancia 2R·sin θ. Con el orden angular Q, P, S, R desde ℓ:

- θ_Q = t, θ_P = t+α, θ_S = t+α+90°, θ_R = t+120°, donde α = ∠QXP y β = 30°−α = ∠SXR
- XQ = 2R₁·sin t = 3, XR = 2R₂·sin(t+120°) = 6
- PQ = RS ⟹ R₁·sin α = R₂·sin(30°−α)
- Área total = [XPQ] + [XPS] + [XRS] = 27

Resuelvo numéricamente:

**Tool Call: Bash** (call_1)
```json
{
  "command": "cd /tmp && python3 -I -c \"\nfrom mpmath import mp, mpf, sin, cos, tan, pi, findroot, radians, mpmath\nimport mpmath\nmp.dps = 50\n\ndeg = pi/180\n\ndef eqs(t, a):\n    # t = theta_Q, a = alpha (radianes)\n    R1 = 3/(2*sin(t))\n    R2 = 3/sin(t + 120*deg)\n    u = t + a\n    # condicion PQ = RS\n    e1 = R1*sin(a) - R2*sin(30*deg - a)\n    # areas\n    XP = 2*R1*sin(u)\n    XS = 2*R2*cos(u)   # sin(u+90) = cos u\n    XQ = mpf(3); XR = mpf(6)\n    A_xpq = XQ*XP*sin(a)/2\n    A_xrs = XR*XS*sin(30*deg - a)/2\n    A_xps = XP*XS/2\n    e2 = A_xpq + A_xrs + A_xps - 27\n    return e1, e2, A_xps, A_xpq, A_xrs, R1, R2, XP, XS\n\ndef F(t, a):\n    r = eqs(t, a)\n    return r[0], r[1]\n\n# buscar raices con varios puntos iniciales\nsols = []\nfor t0 in [5,10,15,20,25,30,35,40,45,50,55]:\n    for a0 in [2,5,10,15,20,25,28]:\n        try:\n            t, a = findroot(F, (t0*deg, a0*deg))\n            t, a = mpf(t), mpf(a)\n            # validez: 0<t, t+120<180, 0<a<30\n            if 0 < t < 60*deg and 0 < a < 30*deg:\n                if not any(abs(t-s[0])<1e-20 and abs(a-s[1])<1e-20 for s in sols):\n                    sols.append((t,a))\n        except Exception:\n            pass\n\nfor t,a in sols:\n    r = eqs(t,a)\n    print('t(deg)=', mpmath.nstr(t/deg, 25), ' alpha(deg)=', mpmath.nstr(a/deg, 25))\n    print('  [XPS]=', mpmath.nstr(r[2], 30), ' [XPQ]=', mpmath.nstr(r[3],15), ' [XRS]=', mpmath.nstr(r[4],15))\n    print('  R1=', mpmath.nstr(r[5],15), ' R2=', mpmath.nstr(r[6],15), ' XP=', mpmath.nstr(r[7],15), ' XS=', mpmath.nstr(r[8],15))\n\"\n"
}
```