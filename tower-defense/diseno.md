# Tower defense (título provisional)

| Ficha | |
|-------|---|
| Estado | definiendo |
| Plataforma candidata | Godot |
| Origen | Idea nueva: tower defense al estilo de *Plantas contra zombis* |
| Año | 2026 |

## Concepto

Un tower defense al estilo de *Plantas contra zombis*: defensas colocadas en un tablero por carriles frente a oleadas de enemigos que avanzan.

## Decidido

- **Plataforma: Godot.** El proyecto tiene su repo privado, `Manzupas/tower-defense`, con la ficha de seguimiento del plan de desarrollo (Plan A, fase 1 sin empezar). El diseño sigue aquí.
- Se juega **siempre en apaisado** (horizontal), en cualquier dispositivo. Al principio se planteó que el tablero fuese vertical u horizontal según el dispositivo, pero se descartó.
- **El tablero es fijo**: cabe entero en la pantalla y no se hace scroll.
- El juego se basa en **mecánicas de riesgo y recompensa**.
- **Los enemigos son bichos** y **lo que se defiende es azúcar**.
- Estética **sencilla**.
- **Los niveles no son puzles**: no hay una solución concreta que encontrar.

## Preguntas abiertas

- Título definitivo y ambientación: dónde está el azúcar (por ejemplo, una mesa o una cocina), quiénes lo defienden y qué bichos atacan.
  - Defensores: el usuario se inclina por **juguetes**, sin decidir todavía.
- En qué dispositivos se juega: PC, web o móvil (Godot exporta a todos).
- Recursos (equivalente a los soles), tipos de defensas y de enemigos. Las torres **no se pagan con el azúcar** que se defiende: hay que buscar otro recurso.
- Estructura: niveles, oleadas, modos de juego.
- Qué mecánicas concretas de riesgo y recompensa tiene. El usuario quiere **mecánicas propias**. Le parecen ideas válidas como punto de partida, sin decidir todavía:
  - Dejar pasar enemigos: cuanto más se acercan a la base, más botín sueltan.
  - Llamar a la siguiente oleada antes de tiempo, a cambio de más recursos.
  - Defensas que se sobrecargan: disparan más, pero pueden romperse.
- Mecánicas propias que le gustan al usuario (propuestas, falta concretarlas):
  - **El cebo**: se coloca un cebo que atrae a los enemigos de los carriles vecinos hacia uno solo. Así se concentra el botín en ese carril, pero también el peligro.
  - **Defensas que maduran**: una defensa que aguanta varias oleadas sin recibir daño evoluciona en una versión mucho mejor. Mientras madura es un punto débil que hay que proteger.
    - Con juguetes, cada tipo de torre madura a su manera (el usuario quiere las tres formas propuestas, como tipos de torre distintos):
      - **Juguetes de cuerda**: acumulan cuerda mientras nadie los toca y atacan más fuerte; si un bicho los golpea, pierden la cuerda y vuelven a empezar. Papel: **atacante frágil**; le conviene estar lejos de los bichos, por eso se combina con el cebo.
      - **Piezas de construcción**: por cada oleada que aguantan se les añade un bloque, hasta convertirse en una torre o un castillo. Basta con que aguanten la oleada, aunque reciban golpes. Papel: **muro**.
      - **Soldaditos**: suben de rango (cabo, sargento, general…) por cada oleada que sobreviven. Pueden recibir daño, pero si los destruyen pierden el rango. Papel: **torre equilibrada**.
