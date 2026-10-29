Herramienta: functions.bash({"command":"python3 -I - <<'PY'
import mpmath as mp
mp.mp.dps=50
f=lambda y: 169*mp.sqrt(1-y*y)*y**4+120*y**3-144*mp.sqrt(1-y*y)
y=mp.findroot(f, (mp.mpf('0.76'),mp.mpf('0.78')))
x=mp.sqrt(1-y*y)
print('x,y=',x,y)
print('poly=',169*x*y**4+120*y**3-144*x)
# solve for j using P on circle
D=5*x+12*y
E=y-12*x/5

def F(j):
    s=(60-5*j)/D
    v=s*E
    return j*j+v*v-12*j-5*v
for guess in [0.1,2,4,6,8,10,11.9]:
    try:
        j=mp.findroot(F, guess)
        s=(60-5*j)/D; v=s*E
        print('root',j,'s',s,'v',v,'Q',(j+s*x,s*y),'F',F(j))
    except: pass
PY","description":"Resuelve numéricamente los datos geométricos"})