# Murdoku del purgatorio (título provisional)

| Ficha | |
|-------|---|
| Estado | movida |
| Plataforma candidata | Godot, para PC |
| Origen | Idea nueva, basada en los puzles *Murdoku* |
| Año | 2026 |

Ya se desarrolla en el repo [murdokus](https://github.com/Manzupas/murdokus) (Godot 4.7, desde el 17/11/2026). Aun así, **el diseño se sigue actualizando aquí** hasta que exista el GDD (que se hará en Markdown, en este repo, cuando se haya hablado más): es una excepción a la regla de las ideas movidas (ver [CLAUDE.md](../CLAUDE.md)).

> **En pausa desde el 25/11/2026**: el desarrollo se para de momento porque el proyecto es demasiado grande por ahora. Todo lo decidido hasta aquí se conserva; el GDD (en Markdown, en este repo) queda pendiente para cuando se retome.

## Concepto

Un juego de puzles tipo *Murdoku* metido en la vida de un contable de una gestoría española de finales de los 90. En la primera parte revisa facturas, y lo que decide tiene consecuencias; al final lo asesinan. En la segunda, en el purgatorio, resolviendo Murdokus tortura a sus antiguos clientes.

## Documentos

| Archivo | Qué hay |
|---------|---------|
| [historia.md](historia.md) | La trama: las dos partes, los tres caminos, el hacker, los compañeros y el purgatorio. |
| [escaleta.md](escaleta.md) | Lo que pasa en cada semestre y en cada vuelta del purgatorio: casos, historia, hacker, documentos y mecánicas. |
| [personajes.md](personajes.md) | Los doce personajes en tres círculos, la gestoría y los compañeros. |
| [mecanicas.md](mecanicas.md) | Los Murdokus y sus tres estilos, las facturas y escrituras, la gravedad y los correos. |
| [ambientacion.md](ambientacion.md) | España desde 1996, Windows 95, el efecto 2000, el IRC y la moneda. |
| [herramientas/escaleta_html.py](herramientas/escaleta_html.py) | Genera una página para ver la escaleta: `python3 -I escaleta_html.py` desde `herramientas/`. Publicada como artefacto: https://claude.ai/artifact/Q33tFmM5NWKU1LDyKhNKUM (se vuelve a publicar cuando cambia la escaleta). |
| [prototipo/README.md](prototipo/README.md) | El prototipo web (*Office Work*): qué tiene y cómo se juega. No se actualiza más. |

## Cómo se apunta

- Cada sección tiene, en este orden, **Decidido**, **Propuesta** (por revisar) y **Preguntas abiertas**.
- Cada cosa se apunta en un solo sitio; los demás enlazan a él.
- No se guarda el historial de cambios («antes era…»): eso ya está en git. Solo se apunta lo que hay ahora.
- Cuando una pregunta se contesta, se quita de las preguntas abiertas y se apunta la respuesta.
