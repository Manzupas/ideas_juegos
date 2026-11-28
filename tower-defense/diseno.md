# Tower defense (título provisional)

| Ficha | |
|-------|---|
| Estado | definiendo |
| Plataforma candidata | Godot |
| Origen | Idea nueva: tower defense al estilo de *Plantas contra zombis* |
| Año | 2026 |

## Concepto

Un tower defense al estilo de *Plantas contra zombis*: defensas colocadas en un tablero (de carriles rectos o laberíntico, según el nivel) frente a oleadas de enemigos que avanzan. Los enemigos son bichos y lo que se defiende es azúcar. Se basa en mecánicas de riesgo y recompensa.

## Cómo se organiza el diseño

La implementación se hará en el PC, así que antes hay que definirlo **todo**. El diseño se reparte en varios archivos y se cierra por bloques, en este orden (cada bloque depende de los anteriores):

| # | Bloque | Archivo | Estado |
|---|--------|---------|--------|
| 1 | Núcleo: recurso, tablero, victoria y derrota | [mecanicas.md](mecanicas.md) | abierto |
| 2 | Defensas y enemigos (se equilibran juntos) | [defensas.md](defensas.md), [enemigos.md](enemigos.md) | abierto |
| 3 | Riesgo y recompensa: cebo y maduración | [mecanicas.md](mecanicas.md) | abierto |
| 4 | Niveles y oleadas | [niveles.md](niveles.md) | abierto |
| 5 | Ambientación (puede adelantarse: casi no condiciona las reglas) | [ambientacion.md](ambientacion.md) | abierto |
| 6 | Interfaz | [interfaz.md](interfaz.md) | abierto |
| 6 | Técnico | [tecnico.md](tecnico.md) | abierto |

Reglas:

- Cada conversación trabaja un bloque. Se apunta en su archivo qué está **decidido** y qué es **propuesta**, y se hace commit y push.
- Un bloque está **cerrado** cuando no le queda nada «por decidir».
- Los números (vida, daño, costes…) se apuntan como **valor inicial**: se ajustarán al jugar.
- Cuando todos los bloques estén cerrados, la idea pasa a «lista para prototipo» y se copia al repo privado `Manzupas/tower-defense` para implementarla.

## Decidido (general)

- **Plataforma: Godot.** El proyecto tiene su repo privado, `Manzupas/tower-defense`, con la ficha de seguimiento del plan de desarrollo (Plan A, fase 1 sin empezar). El diseño sigue aquí.
- El juego se basa en **mecánicas de riesgo y recompensa**, y el usuario quiere **mecánicas propias**.
- **Los niveles no son puzles**: no hay una solución concreta que encontrar.
