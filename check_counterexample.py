"""Deterministic counterexamples to the retry policies described in D2/D2b.
This is our abstract model of their prose, NOT code executed by either LLM.
Run offline: python check_counterexample.py
"""
import json

def schedule(window_hours, resumed_at, allow_takeover):
    # A has already passed its last local deadline/state check at t=0 and pauses.
    # B may take over at t=1. A emits at resumed_at without another local check.
    remote_first_accept=None; effects=0; trace=[]
    for worker,t in [('B',1),('A',resumed_at)]:
        if worker=='B' and not allow_takeover:
            trace.append({'worker':worker,'time_h':t,'action':'blocked: non-transferable emission permit'})
            continue
        if remote_first_accept is None or t-remote_first_accept>=window_hours:
            effects+=1;remote_first_accept=t;action='new external effect'
        else:action='deduplicated'
        trace.append({'worker':worker,'time_h':t,'action':action})
    return {'effects':effects,'trace':trace}

out={}
for name,window,resume in [('D2',36,50),('D2b',6,10)]:
    retry=schedule(window,resume,True); exclusive=schedule(window,resume,False)
    assert retry['effects']==2
    assert exclusive['effects']==1
    out[name]={'retry_with_local_check':retry,'single_nontransferable_permit':exclusive}
# Exact arithmetic oracle for D4. Fractions prevent a formatting choice becoming a failure.
from fractions import Fraction as F
alfa=F(270,1000);beta=F(730,1000)
proj_a=F(1,10)*F(9,10)+F(9,10)*F(2,10)
proj_b=F(1,10)*F(8,10)+F(9,10)*F(1,10)
assert proj_a==F(27,100) and proj_b==F(17,100)
assert alfa*10+(1-alfa)*25==F(2095,100)
assert beta*8+(1-beta)*32==F(1448,100)
assert proj_b*8+(1-proj_b)*32==F(2792,100)
out['D4']={'observed_success':[float(alfa),float(beta)],'projected_success':[float(proj_a),float(proj_b)],'observed_minutes':[20.95,14.48],'projected_minutes':[20.95,27.92]}
print(json.dumps(out,indent=2))
