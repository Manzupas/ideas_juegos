# Tower defense: mecánicas

Bloques 1 (núcleo) y 3 (riesgo y recompensa). Ver el índice en [diseno.md](diseno.md).

## Bloque 1: núcleo

### Tablero

Decidido:

- Se juega **siempre en apaisado** (horizontal), en cualquier dispositivo. Al principio se planteó que el tablero fuese vertical u horizontal según el dispositivo, pero se descartó.
- **El tablero es fijo**: cabe entero en la pantalla y no se hace scroll.
Por decidir:

- **Carriles o mapa generado por nivel.** El usuario aún no lo tiene claro: puede ser un tablero por carriles (como *Plantas contra zombis*) o un mapa distinto que se genere en cada nivel. Afecta al cebo (que se pensó para atraer bichos de carriles vecinos) y a dónde está el azúcar.
- Si son carriles: número de carriles y de casillas por carril.
- Si el tamaño del tablero cambia entre niveles.
- Desde qué lado entran los bichos y dónde está el azúcar.
- Si hay casillas especiales (obstáculos, casillas donde no se puede construir…).
- Si una casilla admite una sola defensa.

### Recurso

Decidido:

- Las torres **no se pagan con el azúcar** que se defiende: hay otro recurso.

- El recurso se consigue de **dos fuentes**: un **goteo** pequeño y constante con el tiempo, más el **botín** que sueltan los bichos al eliminarlos.

Propuestas (al usuario le parecen bien, sin cerrar):

- **Canicas** como recurso principal: ruedan desde un bote volcado (goteo) y los bichos las empujan como escarabajos peloteros con su bola (botín). Se eligieron frente a migas (se confunden con el azúcar), pilas y botones.
- **Pilas** como segundo recurso, solo para algunas torres o juguetes.

Por decidir:

- Confirmar las canicas.
- Pilas (aceptado «de momento»):
  - **Consumo**: los juguetes a pilas son potentes, pero gastan pila mientras funcionan; si se quedan sin pila, se paran. Contrastan con los de cuerda, que no gastan nada.
  - **No gotean**: solo las sueltan algunos bichos concretos.
  - Descartadas por ahora: pila como potenciador temporal y pila como coste de construcción.
  - Por decidir: cuánta pila gasta cada juguete, cómo se recarga un juguete parado y qué bichos sueltan pilas.
- Cuánto da el goteo y cuánto el botín de cada bicho (valores iniciales).
- Con qué recurso se empieza cada nivel.
- Si se puede vender o retirar una defensa y qué se recupera.

### Ciclo de juego

Por decidir:

- Qué pasa en una partida, paso a paso (preparación, oleadas, pausas entre oleadas).
- Si hay tiempo de preparación antes de la primera oleada.

### Victoria y derrota

Decidido:

- **Los bichos roban el azúcar y se puede recuperar**: un bicho que llega al azúcar coge una parte y huye; si se le aplasta durante la huida, el azúcar se recupera.

Por decidir:

- Si el azúcar es un solo montón o hay varios (propuesta: un montón único).
- Cuánto azúcar coge cada bicho y por dónde huye.
- Cuándo se pierde.
- Cuándo se gana el nivel.
- Si el azúcar que queda al final cuenta para algo (puntuación, estrellas…).

## Bloque 3: riesgo y recompensa

### Mecánicas propias (propuestas, falta concretarlas)

- **El cebo**: se coloca un cebo que atrae a los enemigos de los carriles vecinos hacia uno solo. Así se concentra el botín en ese carril, pero también el peligro.
  - Por decidir: alcance (cuántos carriles), duración, coste, si se gasta, si los bichos se lo comen.
- **Defensas que maduran**: una defensa que aguanta varias oleadas sin recibir daño evoluciona en una versión mucho mejor. Mientras madura es un punto débil que hay que proteger.
  - Cada tipo de torre madura a su manera; ver [defensas.md](defensas.md).

### Otras ideas de riesgo y recompensa (válidas como punto de partida, sin decidir)

- Dejar pasar enemigos: cuanto más se acercan a la base, más botín sueltan.
- Llamar a la siguiente oleada antes de tiempo, a cambio de más recursos.
- Defensas que se sobrecargan: disparan más, pero pueden romperse.

Por decidir: cuáles de estas entran en el juego.
