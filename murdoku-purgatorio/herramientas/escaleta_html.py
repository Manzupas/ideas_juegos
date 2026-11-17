"""Genera una página HTML para ver la escaleta del Murdoku del purgatorio.

Lee ../escaleta.md y escribe escaleta.html al lado de este script.
Uso, desde esta carpeta:  python3 -I escaleta_html.py [commit]
"""
import html
import json
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
MD = AQUI.parent / "escaleta.md"
SALIDA = AQUI / "escaleta.html"
CAMPOS = ["Casos", "Historia", "Hacker", "Documentos", "Mecánica nueva"]


def inline(texto):
    t = html.escape(texto, quote=False)
    t = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", t)
    t = t.replace("*(esbozo)*", '<span class="tag esbozo">esbozo</span>')
    t = re.sub(r"\((propuesta[^)]*)\)", r'<span class="tag prop">\1</span>', t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"\*(.+?)\*", r"<i>\1</i>", t)
    t = re.sub(r"(?i)\bpor decidir\b", '<span class="tag nada">por decidir</span>', t)
    return t


def leer():
    lineas = MD.read_text(encoding="utf-8").splitlines()
    datos = {"colocado": [], "propuesta": [], "semestres": [], "vueltas": [], "por_colocar": []}
    seccion, sub, actual = None, None, None
    for l in lineas:
        if l.startswith("## "):
            seccion, sub = l[3:].strip(), None
            continue
        if l.startswith("### "):
            titulo = l[4:].strip()
            nombre, _, lema = titulo.partition(":")
            actual = {"nombre": nombre.strip(), "lema": lema.strip(), "campos": {}}
            datos["semestres"].append(actual)
            continue
        if seccion == "Lo que ya está colocado":
            if l.startswith("**Decidido**"):
                sub = "colocado"
            elif l.startswith("**Propuesta**"):
                sub = "propuesta"
            elif l.startswith("- ") and sub:
                datos[sub].append(inline(l[2:]))
        elif seccion and seccion.startswith("Primera parte") and actual:
            m = re.match(r"- \*\*(.+?)\*\*: (.*)", l)
            if m and m.group(1) in CAMPOS:
                actual["campos"][m.group(1)] = inline(m.group(2))
        elif seccion and seccion.startswith("Segunda parte"):
            celdas = [c.strip() for c in l.strip().strip("|").split("|")]
            if l.startswith("|") and len(celdas) == 3 and celdas[0].isdigit():
                datos["vueltas"].append({"n": celdas[0], "casos": celdas[1], "texto": inline(celdas[2])})
        elif seccion == "Por colocar" and l.startswith("- "):
            datos["por_colocar"].append(inline(l[2:]))
    return datos


def casos_num(texto):
    m = re.match(r"\s*(\d+)", re.sub(r"<[^>]+>", "", texto))
    return int(m.group(1)) if m else 0


PLANTILLA = r"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Murdoku del purgatorio: escaleta</title>
<style>
:root{--teal:#008080;--gris:#c0c0c0;--osc:#808080;--neg:#000;--bla:#fff;--azul:#000080;--azul2:#1084d0;
--esbozo:#fff3a8;--prop:#cfe3ff;--nada:#e4e4e4;
--c-casos:#7a1f1f;--c-historia:#000080;--c-hacker:#0a6b0a;--c-documentos:#6b4a00;--c-mecanica:#5b2a86}
*{box-sizing:border-box}
body{margin:0;background:var(--teal);font:14px/1.45 Tahoma,"MS Sans Serif",Verdana,sans-serif;color:var(--neg);padding:12px 10px 40px}
.win{background:var(--gris);border:2px solid;border-color:var(--bla) var(--neg) var(--neg) var(--bla);box-shadow:inset -1px -1px var(--osc),inset 1px 1px #dfdfdf;margin:0 auto 14px;max-width:760px}
.bar{background:linear-gradient(90deg,var(--azul),var(--azul2));color:var(--bla);font-weight:bold;padding:3px 6px;display:flex;justify-content:space-between;align-items:center;gap:8px}
.bar .x{background:var(--gris);color:var(--neg);border:2px solid;border-color:var(--bla) var(--neg) var(--neg) var(--bla);width:20px;height:18px;font-size:11px;line-height:12px;text-align:center;flex:none}
.body{padding:10px 12px}
h1{font-size:15px;margin:0}
.sub{color:#222;margin:0 0 6px}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin:4px 0 2px}
.chip{font:inherit;background:var(--gris);border:2px solid;border-color:var(--bla) var(--neg) var(--neg) var(--bla);padding:3px 9px;cursor:pointer}
.chip[aria-pressed=true]{border-color:var(--neg) var(--bla) var(--bla) var(--neg);background:#d8d8d8;font-weight:bold}
.chip i{display:inline-block;width:9px;height:9px;margin-right:5px;vertical-align:0}
.leyenda{margin-top:8px;font-size:12px;display:flex;flex-wrap:wrap;gap:6px;align-items:center}
.tag{font-size:11px;padding:0 5px;border:1px solid #0003;white-space:nowrap;font-style:normal;font-weight:normal}
.tag.esbozo{background:var(--esbozo)}.tag.prop{background:var(--prop)}.tag.nada{background:var(--nada);color:#555}
.linea{display:flex;align-items:flex-end;gap:2px;height:96px;padding:6px 3px 0;background:var(--bla);border:2px solid;border-color:var(--osc) var(--bla) var(--bla) var(--osc)}
.col{flex:1;min-width:0;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;height:100%;text-decoration:none;color:inherit}
.col .b{width:70%;background:var(--c-casos);min-height:2px}
.col.p .b{background:#4b4b4b}
.col span{font-size:9px;white-space:nowrap;letter-spacing:-.3px}
.col small{font-size:10px;color:#555}
.sep{width:2px;align-self:stretch;background:repeating-linear-gradient(#000 0 4px,transparent 4px 8px)}
.ejes{display:flex;justify-content:space-between;font-size:11px;color:#333;margin-top:4px}
.campo{display:grid;grid-template-columns:96px 1fr;gap:8px;padding:6px 0;border-top:1px solid var(--osc);box-shadow:0 1px 0 var(--bla) inset}
.campo:first-child{border-top:0;box-shadow:none}
.filtrado .campo{border-top:0;box-shadow:none}
.campo .v::first-letter,.vuelta div::first-letter{text-transform:uppercase}
.campo .k{font-weight:bold;font-size:12px;padding-left:7px;border-left:5px solid}
.campo.vacio .v{color:#555}
@media (max-width:520px){.campo{grid-template-columns:1fr;gap:2px}}
.lema{font-weight:normal;opacity:.9}
.parte{max-width:760px;margin:22px auto 8px;color:var(--bla);font-weight:bold;font-size:16px;text-shadow:1px 1px #000}
ul{margin:4px 0 0;padding-left:20px}li{margin:3px 0}
.vuelta{display:grid;grid-template-columns:70px 1fr;gap:10px;padding:7px 0;border-top:1px solid var(--osc)}
.vuelta:first-child{border-top:0}
.vuelta .n{font-weight:bold}
.oculto{display:none!important}
.pie{max-width:760px;margin:10px auto;color:#e8ffff;font-size:12px}
</style>
</head>
<body>
<div class="win"><div class="bar"><h1>Murdoku del purgatorio · escaleta</h1><span class="x">×</span></div>
<div class="body">
<p class="sub">Lo que pasa en cada semestre y en cada vuelta del purgatorio. Toca un campo para filtrar.</p>
<div class="chips" id="chips"></div>
<div class="leyenda"><span class="tag esbozo">esbozo</span> primer esbozo, para discutir <span class="tag prop">propuesta</span> por revisar <span class="tag nada">por decidir</span> sin hablar. Sin etiqueta: decidido.</div>
</div></div>

<div class="win"><div class="bar"><span>Casos por bloque (propuesta)</span><span class="x">×</span></div>
<div class="body"><div class="linea" id="linea"></div><div class="ejes"><span>Primera parte: la vida real</span><span>Segunda parte: el purgatorio</span></div></div></div>

<div class="parte">Primera parte: la vida real</div>
<div id="semestres"></div>

<div class="parte">Segunda parte: el purgatorio</div>
<div class="win"><div class="bar"><span>Cada vuelta es el segundo semestre de 1999 otra vez</span><span class="x">×</span></div>
<div class="body" id="vueltas"></div></div>

<div class="parte">Lo que ya está colocado</div>
<div class="win"><div class="bar"><span>Decidido</span><span class="x">×</span></div><div class="body"><ul id="colocado"></ul></div></div>
<div class="win"><div class="bar"><span>Propuesta (por revisar)</span><span class="x">×</span></div><div class="body"><ul id="propuesta"></ul></div></div>
<div class="win"><div class="bar"><span>Por colocar</span><span class="x">×</span></div><div class="body"><ul id="porcolocar"></ul></div></div>

<p class="pie">Generado a partir de <b>murdoku-purgatorio/escaleta.md</b> (repo ideas_juegos__COMMIT__). Para cambiar algo, se cambia el .md y se vuelve a generar.</p>

<script>
const D = __DATOS__;
const CAMPOS = [["Casos","casos"],["Historia","historia"],["Hacker","hacker"],["Documentos","documentos"],["Mecánica nueva","mecanica"]];
const $ = id => document.getElementById(id);
let filtro = null;

const chips = $("chips");
const todo = document.createElement("button");
todo.className = "chip"; todo.textContent = "Todo"; todo.setAttribute("aria-pressed","true");
todo.onclick = () => poner(null); chips.appendChild(todo);
for (const [nombre, clave] of CAMPOS) {
  const b = document.createElement("button");
  b.className = "chip"; b.dataset.k = clave; b.setAttribute("aria-pressed","false");
  b.innerHTML = `<i style="background:var(--c-${clave})"></i>${nombre}`;
  b.onclick = () => poner(filtro === clave ? null : clave);
  chips.appendChild(b);
}
function poner(k) {
  filtro = k;
  for (const b of chips.children) b.setAttribute("aria-pressed", String((b.dataset.k || null) === k));
  document.body.classList.toggle("filtrado", !!k);
  document.querySelectorAll(".campo").forEach(c => c.classList.toggle("oculto", !!k && c.dataset.k !== k));
  try { localStorage.setItem("escaleta-filtro", k || ""); } catch (e) {}
}

const sem = $("semestres");
D.semestres.forEach((s, i) => {
  const w = document.createElement("div");
  w.className = "win"; w.id = "s" + i;
  let h = `<div class="bar"><span>${s.nombre}${s.lema ? ` <span class="lema">· ${s.lema}</span>` : ""}</span><span class="x">×</span></div><div class="body">`;
  for (const [nombre, clave] of CAMPOS) {
    const v = s.campos[nombre] || '<span class="tag nada">por decidir</span>';
    const vacio = /^\s*<span class="tag nada">por decidir<\/span>\.?\s*$/i.test(v);
    h += `<div class="campo${vacio ? " vacio" : ""}" data-k="${clave}"><div class="k" style="border-color:var(--c-${clave})">${nombre}</div><div class="v">${v}</div></div>`;
  }
  w.innerHTML = h + "</div>";
  sem.appendChild(w);
});

const lin = $("linea");
const max = Math.max(...D.semestres.map(s => s.n), ...D.vueltas.map(v => +v.casos || 0), 1);
D.semestres.forEach((s, i) => {
  const a = document.createElement("a"); a.className = "col"; a.href = "#s" + i;
  a.innerHTML = `<small>${s.n}</small><div class="b" style="height:${s.n / max * 62}px"></div><span>${s.corto}</span>`;
  lin.appendChild(a);
});
const sep = document.createElement("div"); sep.className = "sep"; lin.appendChild(sep);
D.vueltas.forEach(v => {
  const a = document.createElement("a"); a.className = "col p"; a.href = "#vueltas";
  a.innerHTML = `<small>${v.casos}</small><div class="b" style="height:${(+v.casos || 0) / max * 62}px"></div><span>V${v.n}</span>`;
  lin.appendChild(a);
});

$("vueltas").innerHTML = D.vueltas.map(v => `<div class="vuelta"><div class="n">Vuelta ${v.n}<br><small>${v.casos} casos</small></div><div>${v.texto}</div></div>`).join("");
$("colocado").innerHTML = D.colocado.map(t => `<li>${t}</li>`).join("");
$("propuesta").innerHTML = D.propuesta.map(t => `<li>${t}</li>`).join("");
$("porcolocar").innerHTML = D.por_colocar.map(t => `<li>${t}</li>`).join("");

let guardado = null;
try { guardado = localStorage.getItem("escaleta-filtro"); } catch (e) {}
if (guardado) poner(guardado);
</script>
</body>
</html>
"""


def main():
    datos = leer()
    for s in datos["semestres"]:
        s["n"] = casos_num(s["campos"].get("Casos", ""))
        m = re.match(r"(\d{4}), (primer|segundo)", s["nombre"])
        s["corto"] = f"{m.group(1)[2:]}·{'1' if m.group(2) == 'primer' else '2'}" if m else s["nombre"][:6]
    commit = f", commit {sys.argv[1]}" if len(sys.argv) > 1 else ""
    pagina = PLANTILLA.replace("__DATOS__", json.dumps(datos, ensure_ascii=False)).replace("__COMMIT__", commit)
    SALIDA.write_text(pagina, encoding="utf-8")
    print(f"{SALIDA.name}: {len(datos['semestres'])} semestres, {len(datos['vueltas'])} vueltas")


if __name__ == "__main__":
    main()
