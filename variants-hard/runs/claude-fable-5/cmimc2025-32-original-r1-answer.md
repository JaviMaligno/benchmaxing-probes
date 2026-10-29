Voy a resolver el problema analíticamente y luego verificarlo con una simulación rápida.

**Planteamiento:** Como el 4 está en la raíz al inicio, $p(4)=1$, y para $a \neq 4,7$, $p(a)$ es la probabilidad de que la etiqueta $a$ llegue a la raíz **antes** que la etiqueta 7 (porque al llegar el 7 el proceso termina). Basta seguir la cadena de Markov del par (posición de $a$, posición de 7).

Sea $h(x,y)$ la probabilidad de que una etiqueta en la posición $x$ llegue a la raíz antes que otra en la posición $y$. Por simetrías del árbol (intercambiar hojas hermanas, intercambiar subárboles) y porque $h(x,y)+h(y,x)=1$:

- Hojas hermanas, hojas opuestas, o los dos nodos internos: $h = 1/2$.

Esto da $p(1)=p(3)=p(5)=1/2$ de inmediato. Quedan dos incógnitas:

- $u = h(A, A_1)$: interno vs. su hija (caso de $p(6)$, el 6 es padre del 7).
- $v = h(A, B_1)$: interno vs. hoja del otro lado (caso de $p(2)$).

Con 6 aristas equiprobables, desde $(A, A_1)$: la arista $R\!-\!A$ gana ($1/6$), la arista $A\!-\!A_1$ intercambia y da $1-u$, la arista $A\!-\!A_2$ lleva a hojas hermanas ($1/2$), y 3 aristas no cambian nada:

$$6u = 1 + (1-u) + \tfrac12 + 3u \implies u = \tfrac58.$$

Desde $(A, B_1)$: $R\!-\!A$ gana ($1/6$), $A\!-\!A_1$ y $A\!-\!A_2$ dan hojas opuestas ($1/2$ cada una), $B\!-\!B_1$ da los dos internos ($1/2$), y 2 aristas no cambian nada:

$$6v = 1 + \tfrac12+\tfrac12+\tfrac12 + 2v \implies v = \tfrac58.$$

Verifico con una simulación Monte Carlo:


{
  "command": "python3 -I -c \"\nimport random\n# posiciones: 0=R, 1=A, 2=B, 3=A1, 4=A2, 5=B1, 6=B2\nedges=[(0,1),(0,2),(1,3),(1,4),(2,5),(2,6)]\nN=400000\ncounts={a:0 for a in [1,2,3,5,6]}\nfor _ in range(N):\n    arr=[4,2,6,1,3,5,7]\n    seen=set()\n    while True:\n        seen.add(arr[0])\n        if arr[0]==7: break\n        i,j=random.choice(edges)\n        arr[i],arr[j]=arr[j],arr[i]\n    for a in counts:\n        if a in seen: counts[a]+=1\nfor a in sorted(counts): print(a, counts[a]/N)\nprint('suma', sum(counts.values())/N)\n\"",
  "description": "Simulación Monte Carlo del proceso"
}


{
  "command": null,
  "description": null
}