# Tower defense: mecánicas

Bloques 1 (núcleo) y 3 (riesgo y recompensa). Ver el índice en [diseno.md](diseno.md).

## Bloque 1: núcleo

### Tablero

Decidido:

- Se juega **siempre en apaisado** (horizontal), en cualquier dispositivo. Al principio se planteó que el tablero fuese vertical u horizontal según el dispositivo, pero se descartó.
- **El tablero es fijo**: cabe entero en la pantalla y no se hace scroll.
- Hay **carriles** por los que avanzan los bichos hacia el azúcar.

Por decidir:

- Número de carriles y de casillas por carril.
- Si el tamaño del tablero cambia entre niveles.
- Desde qué lado entran los bichos y dónde está el azúcar.
- Si hay casillas especiales (obstáculos, casillas donde no se puede construir…).
- Si una casilla admite una sola defensa.

### Recurso

Decidido:

- Las torres **no se pagan con el azúcar** que se defiende: hay otro recurso.

Por decidir:

- Qué es el recurso y cómo se llama.
- Cómo se consigue (botín de los bichos, generación con el tiempo, defensas que lo producen…).
- Con qué recurso se empieza cada nivel.
- Si se puede vender o retirar una defensa y qué se recupera.

### Ciclo de juego

Por decidir:

- Qué pasa en una partida, paso a paso (preparación, oleadas, pausas entre oleadas).
- Si hay tiempo de preparación antes de la primera oleada.

### Victoria y derrota

Por decidir:

- Cómo funciona el azúcar: si es una cantidad que los bichos van robando o comiendo, una por carril o una común.
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
