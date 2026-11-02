# Caperucita (título provisional)

| Ficha | |
|-------|---|
| Estado | semilla |
| Plataforma candidata | Playdate (por la manivela) |
| Origen | Prototipo antiguo para Playdate, guardado en [material/](material/) |
| Año | 2023 (según las fechas de los archivos, octubre de 2023) |

## Concepto

Un juego de tablero parecido a [Drakulin](../drakulin/diseno.md), con Caperucita y el lobo. La manivela de la Playdate mueve el tiempo hacia delante o hacia atrás.

## Prototipo

Es solo el arranque. En [material/playdate/](material/playdate/) están `main.lua`, `map.lua` y el sprite del árbol:

- Un mapa de 4×4 con Caperucita en una esquina y la casa y un árbol en otra. Los dos van en la misma casilla, así que uno pisa al otro.
- Dibuja el árbol en pantalla y escribe el mapa por consola. Todavía no hay juego.

No se guarda `extra.lua`, que era el ejemplo de la documentación de Playdate.

## Preguntas abiertas

- Título definitivo.
- ¿Cómo se parece a Drakulin? ¿Se colocan flechas o caminos y luego Caperucita anda sola?
- ¿Qué hace el lobo? ¿Se mueve por su cuenta y hay que evitar que se cruce con Caperucita, o que llegue antes a casa de la abuela?
- La manivela: ¿el jugador puede cambiar cosas en mitad del tiempo, o solo mirar hacia delante y hacia atrás para planificar?
- ¿Cuándo se gana y cuándo se pierde?
- Tamaño del tablero y número de niveles.
