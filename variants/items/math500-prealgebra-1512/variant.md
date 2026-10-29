# math500-prealgebra-1512 — variant

In the diagram, three concentric circles have radii of $5,$ $8,$ and $9.$ The three regions they form are labeled $P,$ $Q,$ and $R$ as shown. Among these three regions, what is the difference between the area of the region with the largest area and the area of the region with the smallest area? Express your answer in exact form.

[asy]
import graph;
filldraw(circle((0,0),9), lightgray, black+linewidth(1));
filldraw(circle((0,0),8), gray, black+linewidth(1));
filldraw(circle((0,0),5), white, black+linewidth(1));
dot((0,0));
label("$P$",(2.5,0));
label("$Q$",(6.5,0));
label("$R$",(8.5,0));
[/asy]

**Answer:** $22\pi$  (areas $25\pi$, $39\pi$, $17\pi$; $39\pi - 17\pi$)
