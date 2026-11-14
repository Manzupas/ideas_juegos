"""Genera y comprueba un caso de Murdoku 6x6 con solución única.

Reglas:
- Una persona por fila y por columna.
- No se puede estar en casillas con mueble que estorba (mesa M, estantería E, planta P).
  Sí en silla (s), alfombra (a), cama (c) y suelo (.).
- El asesino es la única persona que está sola con la víctima en su habitación.
"""
import itertools, random, json, sys

ROOMS = [
    "CCCBBB",
    "CCCBBB",
    "SSSSDD",
    "SSSSDD",
    "SSSSDD",
    "TTSSDD",
]
OBJS = [
    "E.Ms.E",
    "s.M..E",
    "P..a.c",
    ".a.M.c",
    "sM...P",
    "..as..",
]
ROOM_NAME = {"C": "la cocina", "B": "la biblioteca", "S": "el salón", "D": "el dormitorio", "T": "el baño"}
OBJ_NAME = {"M": "una mesa", "E": "una estantería", "P": "una planta", "s": "una silla", "a": "una alfombra", "c": "la cama"}
BLOCK = set("MEP")
N = 6
PEOPLE = ["A", "B", "C", "D", "E", "V"]  # V = víctima
NAMES = {"A": "Águeda", "B": "Bernardo", "C": "Cecilia", "D": "Damián", "E": "Elvira", "V": "Rogelio"}

free = [[OBJS[r][c] not in BLOCK for c in range(N)] for r in range(N)]

def neighbors(r, c):
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        rr, cc = r + dr, c + dc
        if 0 <= rr < N and 0 <= cc < N:
            yield rr, cc

def adj_obj(r, c, o):
    return any(OBJS[rr][cc] == o for rr, cc in neighbors(r, c))

# todas las colocaciones: perm de columnas por fila, casillas libres
col_perms = [p for p in itertools.permutations(range(N)) if all(free[r][p[r]] for r in range(N))]
person_perms = list(itertools.permutations(PEOPLE))

def solutions_iter():
    for cp in col_perms:
        for pp in person_perms:
            # pp[r] = persona en la fila r
            yield {pp[r]: (r, cp[r]) for r in range(N)}

def murderer(sol):
    vr, vc = sol["V"]
    room = ROOMS[vr][vc]
    others = [p for p in PEOPLE if p != "V" and ROOMS[sol[p][0]][sol[p][1]] == room]
    return others[0] if len(others) == 1 else None

ALL = [s for s in solutions_iter() if murderer(s)]
print("soluciones válidas por reglas:", len(ALL), file=sys.stderr)

def clue_pool(sol):
    pool = []
    room_of = {p: ROOMS[sol[p][0]][sol[p][1]] for p in PEOPLE}
    for p in PEOPLE:
        r, c = sol[p]
        n = NAMES[p]
        rm = room_of[p]
        pool.append((f"{n} estaba en {ROOM_NAME[rm]}.", ("room", p, rm)))
        for other in ROOM_NAME:
            if other != rm:
                pool.append((f"{n} no estaba en {ROOM_NAME[other]}.", ("noroom", p, other)))
        o = OBJS[r][c]
        if o in "sac":
            verb = {"s": "estaba sentado en una silla" if p in "BDV" else "estaba sentada en una silla",
                    "a": "estaba de pie sobre una alfombra", "c": "estaba tumbado en la cama" if p in "BDV" else "estaba tumbada en la cama"}[o]
            pool.append((f"{n} {verb}.", ("on", p, o)))
        for ob in "MEPsa":
            if adj_obj(r, c, ob):
                pool.append((f"{n} estaba junto a {OBJ_NAME[ob]}.", ("adj", p, ob)))
        same = [q for q in PEOPLE if q != p and room_of[q] == rm]
        if not same:
            pool.append((f"{n} estaba solo en su habitación." if p in "BDV" else f"{n} estaba sola en su habitación.", ("alone", p)))
    for p, q in itertools.combinations(PEOPLE, 2):
        if room_of[p] == room_of[q]:
            pool.append((f"{NAMES[p]} y {NAMES[q]} estaban en la misma habitación.", ("same", p, q)))
        if sol[p][0] < sol[q][0]:
            pool.append((f"{NAMES[p]} estaba más al norte que {NAMES[q]}.", ("north", p, q)))
        elif sol[q][0] < sol[p][0]:
            pool.append((f"{NAMES[q]} estaba más al norte que {NAMES[p]}.", ("north", q, p)))
        if sol[p][1] < sol[q][1]:
            pool.append((f"{NAMES[p]} estaba más al oeste que {NAMES[q]}.", ("west", p, q)))
        elif sol[q][1] < sol[p][1]:
            pool.append((f"{NAMES[q]} estaba más al oeste que {NAMES[p]}.", ("west", q, p)))
    return pool

def holds(clue, sol):
    k = clue[0]
    room_of = lambda p: ROOMS[sol[p][0]][sol[p][1]]
    if k == "room": return room_of(clue[1]) == clue[2]
    if k == "noroom": return room_of(clue[1]) != clue[2]
    if k == "on": r, c = sol[clue[1]]; return OBJS[r][c] == clue[2]
    if k == "adj": r, c = sol[clue[1]]; return adj_obj(r, c, clue[2])
    if k == "alone": return all(room_of(q) != room_of(clue[1]) for q in PEOPLE if q != clue[1])
    if k == "same": return room_of(clue[1]) == room_of(clue[2])
    if k == "north": return sol[clue[1]][0] < sol[clue[2]][0]
    if k == "west": return sol[clue[1]][1] < sol[clue[2]][1]
    raise ValueError(k)

WEIGHT = {"room": 3, "noroom": 1, "on": 3, "adj": 3, "alone": 2, "same": 2, "north": 1, "west": 1}

def count(clues, cands):
    return [s for s in cands if all(holds(c, s) for _, c in clues)]

best = None
for seed in range(int(sys.argv[1]) if len(sys.argv) > 1 else 40):
    rnd = random.Random(seed)
    target = rnd.choice(ALL)
    pool = clue_pool(target)
    # empezar por todas, quitar priorizando las de menos peso (quitar primero las feas)
    rnd.shuffle(pool)
    pool.sort(key=lambda x: WEIGHT[x[1][0]])
    clues = list(pool)
    cands = count(clues, ALL)
    assert len(cands) == 1
    for cl in list(pool):
        trial = [x for x in clues if x is not cl]
        if len(count(trial, ALL)) == 1:
            clues = trial
    kinds = [c[1][0] for c in clues]
    score = len(clues) + 2 * sum(k in ("north", "west", "noroom") for k in kinds)
    if best is None or score < best[0]:
        best = (score, seed, target, clues)
    print(seed, len(clues), kinds, file=sys.stderr)

score, seed, target, clues = best
print("mejor semilla", seed, "pistas", len(clues), file=sys.stderr)
order = "AVBCDE"
clues.sort(key=lambda x: (order.index(x[1][1]) if x[1][1] in order else 9))
for t, _ in clues: print(" -", t, file=sys.stderr)
at = {v: p for p, v in target.items()}
for r in range(N):
    print(" ".join(at.get((r, c)) or (OBJS[r][c] if OBJS[r][c] != "." else ROOMS[r][c].lower()) for c in range(N)), file=sys.stderr)
print(json.dumps({"rooms": ROOMS, "objs": OBJS, "solution": {p: list(v) for p, v in target.items()},
                  "murderer": murderer(target), "clues": [t for t, _ in clues]}, ensure_ascii=False))
