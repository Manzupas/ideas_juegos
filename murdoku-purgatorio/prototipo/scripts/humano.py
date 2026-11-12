"""Busca un caso que se resuelva con deducciones sencillas (sin probar casos a ciegas):
pistas de una persona (habitación, mueble, junto a) + una por fila/columna."""
import sys, random, json, itertools
sys.argv=[sys.argv[0],"0"]
exec(open("caso.py").read().split("best = None")[0])

UNARY = {"room","noroom","on","adj"}
def propagate(clues):
    cand = {p:{(r,c) for r in range(N) for c in range(N) if free[r][c]} for p in PEOPLE}
    for _,cl in clues:
        if cl[0] in UNARY:
            p=cl[1]; cand[p]={(r,c) for (r,c) in cand[p] if holds(cl,{**{q:(0,0) for q in PEOPLE},p:(r,c)})}
    placed={}
    changed=True
    while changed:
        changed=False
        for p in PEOPLE:
            if p not in placed and len(cand[p])==1:
                (r,c),=cand[p]; placed[p]=(r,c); changed=True
                for q in PEOPLE:
                    if q!=p: 
                        n0=len(cand[q]); cand[q]={x for x in cand[q] if x[0]!=r and x[1]!=c}
                    if q!=p and not cand[q]: return None
        for axis in (0,1):
            for k in range(N):
                who=[p for p in PEOPLE if any(x[axis]==k for x in cand[p])]
                if len(who)==1:
                    p=who[0]; new={x for x in cand[p] if x[axis]==k}
                    if new!=cand[p]: cand[p]=new; changed=True
                if not who: return None
    return placed if len(placed)==N else None

best=None
for seed in range(400):
    rnd=random.Random(seed); target=rnd.choice(ALL)
    pool=[x for x in clue_pool(target) if x[1][0] in UNARY]
    if propagate(pool)!=target: continue
    rnd.shuffle(pool); pool.sort(key=lambda x:{"noroom":0,"room":1,"adj":2,"on":3}[x[1][0]])
    clues=list(pool)
    for cl in list(pool):
        trial=[x for x in clues if x is not cl]
        per={p:sum(1 for _,c in trial if c[1]==p) for p in PEOPLE}
        if min(per.values())<1: continue
        if propagate(trial)==target: clues=trial
    kinds=[c[1][0] for c in clues]
    score=len(clues)+3*kinds.count("noroom")
    if best is None or score<best[0]: best=(score,seed,target,clues)
score,seed,target,clues=best
# añadir una pista de la víctima con sabor si no la hay ya, y comprobar unicidad global con reglas completas
assert len(count(clues,ALL))==1
order="VABCDE"; clues.sort(key=lambda x:(order.index(x[1][1]),x[0]))
print("semilla",seed,len(clues),file=sys.stderr)
for t,_ in clues: print(" -",t,file=sys.stderr)
at={v:p for p,v in target.items()}
for r in range(N): print(" ".join(at.get((r,c)) or OBJS[r][c] for c in range(N)),"  ",ROOMS[r],file=sys.stderr)
print(json.dumps({"rooms":ROOMS,"objs":OBJS,"solution":{p:list(v) for p,v in target.items()},"murderer":murderer(target),"clues":[t for t,_ in clues]},ensure_ascii=False))
