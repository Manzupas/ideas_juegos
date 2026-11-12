"""Genera un caso de Murdoku 6x6 a partir de una definición en JSON y comprueba que:
  1. tiene una única solución, y
  2. se resuelve solo con deducciones sencillas: las pistas de cada persona (habitación,
     mueble en el que está, mueble junto al que está) más "una persona por fila y columna".

Uso:  python3 -I generar_caso.py caso2.json > caso2.salida.json

La definición lleva: rooms (6 cadenas), objs (6 cadenas), room_names (letra -> [nombre, "en el ..."]),
people (lista de {id, name, fem}), victim (id) y seeds (número de intentos).

Reglas del juego:
- Una persona por fila y por columna.
- Nadie en mesa (M), estantería (E) ni planta (P). Sí en silla (s), alfombra (a), cama (c) o suelo (.).
- El asesino es la única persona en la misma habitación que la víctima.
"""
import itertools, json, random, sys

D = json.load(open(sys.argv[1]))
ROOMS, OBJS, N = D["rooms"], D["objs"], 6
RN = {k: v for k, v in D["room_names"].items()}
PEOPLE = [p["id"] for p in D["people"]]
NAME = {p["id"]: p["name"] for p in D["people"]}
FEM = {p["id"]: p.get("fem", False) for p in D["people"]}
V = D["victim"]
BLOCK = set("MEP")
OBJ = {"M": "una mesa", "E": "una estantería", "P": "una planta", "s": "una silla", "a": "una alfombra", "c": "la cama"}
free = [[OBJS[r][c] not in BLOCK for c in range(N)] for r in range(N)]

def adj(r, c, o):
    return any(0 <= r + dr < N and 0 <= c + dc < N and OBJS[r + dr][c + dc] == o for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)))

def murderer(sol):
    room = ROOMS[sol[V][0]][sol[V][1]]
    o = [p for p in PEOPLE if p != V and ROOMS[sol[p][0]][sol[p][1]] == room]
    return o[0] if len(o) == 1 else None

cols = [p for p in itertools.permutations(range(N)) if all(free[r][p[r]] for r in range(N))]
ALL = []
for cp in cols:
    for pp in itertools.permutations(PEOPLE):
        s = {pp[r]: (r, cp[r]) for r in range(N)}
        if murderer(s):
            ALL.append(s)
print("soluciones posibles con las reglas:", len(ALL), file=sys.stderr)

def pool(sol):
    out = []
    for p in PEOPLE:
        r, c = sol[p]; n = NAME[p]; rm = ROOMS[r][c]; a = "a" if FEM[p] else "o"
        out.append((f"{n} estaba {RN[rm][1]}.", ("room", p, rm)))
        for o2 in RN:
            if o2 != rm:
                out.append((f"{n} no estaba {RN[o2][1]}.", ("noroom", p, o2)))
        o = OBJS[r][c]
        if o == "s": out.append((f"{n} estaba sentad{a} en una silla.", ("on", p, "s")))
        if o == "a": out.append((f"{n} estaba de pie sobre una alfombra.", ("on", p, "a")))
        if o == "c": out.append((f"{n} estaba tumbad{a} en la cama.", ("on", p, "c")))
        for ob in "MEPsac":
            if adj(r, c, ob):
                out.append((f"{n} estaba junto a {OBJ[ob]}.", ("adj", p, ob)))
    return out

def holds1(cl, r, c):
    k = cl[0]
    if k == "room": return ROOMS[r][c] == cl[2]
    if k == "noroom": return ROOMS[r][c] != cl[2]
    if k == "on": return OBJS[r][c] == cl[2]
    if k == "adj": return adj(r, c, cl[2])

def unique(clues):
    return [s for s in ALL if all(holds1(c, *s[c[1]]) for _, c in clues)]

def deduce(clues):
    cand = {p: {(r, c) for r in range(N) for c in range(N) if free[r][c]} for p in PEOPLE}
    for _, cl in clues:
        cand[cl[1]] = {x for x in cand[cl[1]] if holds1(cl, *x)}
    placed, changed = {}, True
    while changed:
        changed = False
        for p in PEOPLE:
            if p not in placed and len(cand[p]) == 1:
                (r, c), = cand[p]; placed[p] = (r, c); changed = True
                for q in PEOPLE:
                    if q != p:
                        cand[q] = {x for x in cand[q] if x[0] != r and x[1] != c}
                        if not cand[q]: return None
        for ax in (0, 1):
            for k in range(N):
                who = [p for p in PEOPLE if any(x[ax] == k for x in cand[p])]
                if not who: return None
                if len(who) == 1:
                    new = {x for x in cand[who[0]] if x[ax] == k}
                    if new != cand[who[0]]: cand[who[0]] = new; changed = True
    return placed if len(placed) == N else None

ORDER = {"noroom": 0, "room": 1, "adj": 2, "on": 3}
best = None
for seed in range(D.get("seeds", 300)):
    rnd = random.Random(seed)
    target = rnd.choice(ALL)
    if D.get("murderer") and murderer(target) != D["murderer"]:
        continue
    pl = pool(target)
    if deduce(pl) != target:
        continue
    rnd.shuffle(pl); pl.sort(key=lambda x: ORDER[x[1][0]])
    clues = list(pl)
    for cl in list(pl):
        trial = [x for x in clues if x is not cl]
        if min(sum(1 for _, c in trial if c[1] == p) for p in PEOPLE) < 1:
            continue
        if deduce(trial) == target:
            clues = trial
    kinds = [c[1][0] for c in clues]
    score = len(clues) + 3 * kinds.count("noroom") - (1 if "room" in kinds else 0)
    if best is None or score < best[0]:
        best = (score, seed, target, clues)

score, seed, target, clues = best
assert len(unique(clues)) == 1 and unique(clues)[0] == target
order = [V] + [p for p in PEOPLE if p != V]
clues.sort(key=lambda x: (order.index(x[1][1]), x[0]))
print("semilla", seed, "pistas", len(clues), "asesino", NAME[murderer(target)], file=sys.stderr)
for t, _ in clues: print(" -", t, file=sys.stderr)
at = {v: p for p, v in target.items()}
for r in range(N): print(" ".join(at.get((r, c)) or OBJS[r][c] for c in range(N)), "  ", ROOMS[r], file=sys.stderr)
print(json.dumps({"solution": {p: list(v) for p, v in target.items()}, "murderer": murderer(target),
                  "clues": [{"t": t, "k": c[0], "p": c[1], "o": c[2]} for t, c in clues]}, ensure_ascii=False))
