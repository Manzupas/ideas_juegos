# Tower defense: mecánicas

Bloques 1 (núcleo) y 3 (riesgo y recompensa). Ver el índice en [diseno.md](diseno.md).

## Bloque 1: núcleo

### Tablero

Decidido:

- Se juega **siempre en apaisado** (horizontal), en cualquier dispositivo. Al principio se planteó que el tablero fuese vertical u horizontal según el dispositivo, pero se descartó.
- **El tablero es fijo**: cabe entero en la pantalla y no se hace scroll.
- **La forma del recorrido es mixta y cambia según el nivel**: unos niveles tienen carriles rectos, otros son laberínticos y alguno puede modificarse durante la partida.
- **Por dónde entran los enemigos y dónde están las chuches depende de cada nivel.**
- **Una sola defensa por casilla.**
- **Casillas especiales**: hay casillas donde no se puede construir y obstáculos fijos. Algunos obstáculos se pueden destruir.

Por decidir:

- Número de carriles y de casillas en los niveles de carriles; tamaño de la cuadrícula en los laberínticos.
- Si el tamaño del tablero cambia entre niveles.
- Quién puede destruir los obstáculos destructibles (enemigos, jugador o ambos).

### Cambios de recorrido

Decidido:

- **Se introducen poco a poco**: al principio el recorrido no cambia; más adelante lo cambia el propio nivel en momentos marcados, y más adelante aún el jugador también puede cambiarlo.
- **El jugador cambia el recorrido con las piezas de construcción**, colocándolas para bloquear el paso. Es un segundo uso de esa defensa que aparece cuando se desbloquea la mecánica.
- **Se puede cerrar el camino del todo**, pero entonces los enemigos **empiezan a dañar mucho** tanto a las torres como a los obstáculos. (Sustituye a la propuesta anterior de dejar siempre una salida.)

Por decidir:

- Cómo cambia exactamente el recorrido en los niveles en que lo cambia el propio nivel.
- Cuánto más dañan los enemigos con el camino cerrado y a qué atacan primero.
- Si algún enemigo especial también puede modificar el recorrido (propuesta, sin decidir).

### Recursos

Decidido:

- Las torres **no se pagan con las chuches** que se defienden.
- El recurso principal se consigue de **dos fuentes**: un **goteo** pequeño y constante con el tiempo, más el **botín** que sueltan los enemigos al derrotarlos.
- **Se empieza cada nivel con algo de recurso** para colocar las primeras defensas.
- **Se puede retirar una defensa** y se recupera **la mitad** de lo que costó. Si estaba madurando, pierde lo acumulado.
- **Pilas** (aceptado «de momento»):
  - Son un segundo recurso, solo para algunos juguetes.
  - **Consumo**: los juguetes a pilas son potentes, pero gastan pila mientras funcionan; si se quedan sin pila, se paran. Contrastan con los de cuerda, que no gastan nada.
  - **Las usan los dos bandos**: hay juguetes a pilas entre los defensores y entre los enemigos.
  - **No gotean**: solo las sueltan algunos enemigos concretos (encaja con juguetes enemigos a pilas).
  - Descartadas por ahora: pila como potenciador temporal y pila como coste de construcción.

Propuesta (al usuario le parece bien, sin cerrar):

- **Canicas** como recurso principal: ruedan desde un bote volcado (goteo) y los enemigos las sueltan al derrotarlos (botín). Se eligieron frente a migas, pilas y botones.

Por decidir:

- Confirmar las canicas.
- Cuánto da el goteo, cuánto el botín de cada enemigo y con cuánto se empieza (valores iniciales).
- Pilas: cuánta gasta cada juguete, cómo se recarga un juguete parado y qué enemigos las sueltan.

### Ciclo de juego

Decidido:

- **Se puede pausar en cualquier momento** para hacer gestiones (colocar, retirar, revisar).
- **Las oleadas se llaman a mano**: la siguiente oleada no empieza hasta que el jugador la lanza.

Por decidir:

- Qué gestiones se pueden hacer con el juego en pausa (¿todas, o solo algunas?).
- Si el goteo de recurso sigue mientras no hay oleada en marcha (si sigue, esperar sin lanzar oleadas daría recurso gratis).
- Un **modo automático** de oleadas, para más adelante.

### Victoria y derrota

Decidido:

- **Se defienden chuches** (antes azúcar).
- **Los enemigos roban chuches y se pueden recuperar**: un enemigo que llega a las chuches coge una parte y huye; si se le derrota durante la huida, las chuches se recuperan.
- **Se gana** al superar la última oleada del nivel.
- **Se pierde** si se quedan sin chuches.
- **No hay estrellas** (demasiado de juego de móvil). De momento **se guardan los resultados** de cada nivel.

Por decidir:

- Si las chuches son un solo montón o hay varios (propuesta: un montón único).
- Cuántas chuches coge cada enemigo y por dónde huye.
- Qué resultados se guardan (chuches que quedan, tiempo, defensas usadas…) y para qué sirven.

## Bloque 3: riesgo y recompensa

### Mecánicas propias (propuestas, falta concretarlas)

- **El cebo**: se coloca un cebo que atrae a los enemigos de los carriles vecinos hacia uno solo. Así se concentra el botín en ese carril, pero también el peligro.
  - Por decidir: alcance (cuántos carriles), duración, coste, si se gasta, si los enemigos lo destruyen, cómo funciona en los niveles laberínticos.
- **Defensas que maduran**: una defensa que aguanta varias oleadas sin recibir daño evoluciona en una versión mucho mejor. Mientras madura es un punto débil que hay que proteger.
  - Cada tipo de torre madura a su manera; ver [defensas.md](defensas.md).

### Otras ideas de riesgo y recompensa (válidas como punto de partida, sin decidir)

- Dejar pasar enemigos: cuanto más se acercan a las chuches, más botín sueltan.
- Defensas que se sobrecargan: disparan más, pero pueden romperse.
- Descartada por ahora: llamar a la siguiente oleada antes de tiempo a cambio de más recursos (las oleadas se llaman a mano).

Por decidir: cuáles de estas entran en el juego.
