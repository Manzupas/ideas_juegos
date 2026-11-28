# Tower defense: mecánicas

Bloques 1 (núcleo) y 3 (riesgo y recompensa). Ver el índice en [diseno.md](diseno.md).

## Bloque 1: núcleo

### Tablero

Decidido:

- Se juega **siempre en apaisado** (horizontal), en cualquier dispositivo. Al principio se planteó que el tablero fuese vertical u horizontal según el dispositivo, pero se descartó.
- **El tablero es fijo**: cabe entero en la pantalla y no se hace scroll.
- **La forma del recorrido es mixta y cambia según el nivel**: unos niveles tienen carriles rectos, otros son laberínticos y alguno puede modificarse durante la partida.
- **Los cambios de recorrido durante la partida se introducen poco a poco**: al principio el recorrido no cambia; más adelante lo cambia el propio nivel en momentos marcados, y más adelante aún el jugador también puede cambiarlo.
Por decidir:

- Cómo cambia el recorrido exactamente en los niveles del nivel y qué herramienta usa el jugador para cambiarlo (¿las piezas de construcción?).
- Si el jugador puede bloquear del todo el camino o siempre tiene que quedar una salida.
- Si algún enemigo especial también puede modificar el recorrido (propuesta, sin decidir).
- Número de carriles y de casillas en los niveles de carriles; tamaño de la cuadrícula en los laberínticos.
- Cómo funciona el cebo en los niveles laberínticos (se pensó para atraer enemigos de carriles vecinos).
- Si el tamaño del tablero cambia entre niveles.
- Desde qué lado entran los enemigos y dónde están las chuches.
- Si hay casillas especiales (obstáculos, casillas donde no se puede construir…).
- Si una casilla admite una sola defensa.

### Recurso

Decidido:

- Las torres **no se pagan con las chuches** que se defienden: hay otro recurso.

- El recurso se consigue de **dos fuentes**: un **goteo** pequeño y constante con el tiempo, más el **botín** que sueltan los enemigos al eliminarlos.

Propuestas (al usuario le parecen bien, sin cerrar):

- **Canicas** como recurso principal: ruedan desde un bote volcado (goteo) y los enemigos las sueltan al derrotarlos (botín). Se eligieron frente a migas, pilas y botones.
- **Pilas** como segundo recurso, solo para algunas torres o juguetes.

Por decidir:

- Confirmar las canicas.
- Pilas (aceptado «de momento»):
  - **Consumo**: los juguetes a pilas son potentes, pero gastan pila mientras funcionan; si se quedan sin pila, se paran. Contrastan con los de cuerda, que no gastan nada.
  - **Las usan los dos bandos**: hay juguetes a pilas entre los defensores y entre los enemigos.
  - **No gotean**: solo las sueltan algunos enemigos concretos (encaja con juguetes enemigos a pilas).
  - Descartadas por ahora: pila como potenciador temporal y pila como coste de construcción.
  - Por decidir: cuánta pila gasta cada juguete, cómo se recarga un juguete parado y qué enemigos sueltan pilas.
- Cuánto da el goteo y cuánto el botín de cada enemigo (valores iniciales).
- Con qué recurso se empieza cada nivel.
- Si se puede vender o retirar una defensa y qué se recupera.

### Ciclo de juego

Por decidir:

- Qué pasa en una partida, paso a paso (preparación, oleadas, pausas entre oleadas).
- Si hay tiempo de preparación antes de la primera oleada.

### Victoria y derrota

Decidido:

- **Se defienden chuches** (antes azúcar).
- **Los enemigos roban chuches y se pueden recuperar**: un enemigo que llega a las chuches coge una parte y huye; si se le derrota durante la huida, las chuches se recuperan.

Por decidir:

- Si las chuches son un solo montón o hay varios (propuesta: un montón único).
- Cuántas chuches coge cada enemigo y por dónde huye.
- Cuándo se pierde.
- Cuándo se gana el nivel.
- Si las chuches que quedan al final cuenta para algo (puntuación, estrellas…).

## Bloque 3: riesgo y recompensa

### Mecánicas propias (propuestas, falta concretarlas)

- **El cebo**: se coloca un cebo que atrae a los enemigos de los carriles vecinos hacia uno solo. Así se concentra el botín en ese carril, pero también el peligro.
  - Por decidir: alcance (cuántos carriles), duración, coste, si se gasta, si los enemigos lo destruyen.
- **Defensas que maduran**: una defensa que aguanta varias oleadas sin recibir daño evoluciona en una versión mucho mejor. Mientras madura es un punto débil que hay que proteger.
  - Cada tipo de torre madura a su manera; ver [defensas.md](defensas.md).

### Otras ideas de riesgo y recompensa (válidas como punto de partida, sin decidir)

- Dejar pasar enemigos: cuanto más se acercan a la base, más botín sueltan.
- Llamar a la siguiente oleada antes de tiempo, a cambio de más recursos.
- Defensas que se sobrecargan: disparan más, pero pueden romperse.

Por decidir: cuáles de estas entran en el juego.
