# Drakulin + Caperucita (título provisional)

| Ficha | |
|-------|---|
| Estado | definiendo |
| Plataforma candidata | **Playdate** |
| Origen | Port de *Drakulin* (Symbian), fusionado con [Caperucita](../caperucita/diseno.md) (prototipo para Playdate de 2023) |
| Año | 2023 o antes: el primer prototipo, en PICO-8, es de abril de 2023 |

## Fusión con Caperucita (26/11/2026)

**Decidido**:

- Drakulin y [Caperucita](../caperucita/diseno.md) pasan a ser **un solo juego**, para **Playdate**. Es el siguiente juego pequeño que se quiere **publicar para vender** (itch.io y, opcionalmente, el Catalog de Playdate).
- De Drakulin se toma la mecánica: un tablero con flechas que se colocan y un personaje que camina solo y gira al pisarlas.
- De Caperucita se toma la **manivela**, que mueve el tiempo de la simulación hacia delante y hacia atrás.
- Entra en el [plan de desarrollo](../plan-desarrollo.md) como **prototipo (Plan A)**. Según el plan, puede ir en paralelo al juego completo activo (Top Hat) y pasaría a juego completo cuando ese termine.

**Propuesta para la fase 1 del Plan A («Pregunta y límites»)** (por revisar):

- **En una frase**: colocas flechas en un tablero y, con la manivela, adelantas y rebobinas el tiempo para ver si el personaje llega a su destino.
- **Pregunta del prototipo**: ¿es divertido planificar el camino y comprobarlo moviendo el tiempo con la manivela, o la manivela estorba?
- **Criterio de éxito**: que 3 de 4 personas que lo prueben quieran jugar otro nivel, y que usen la manivela para rebobinar sin que se lo expliquen.
- **Herramienta**: Playdate SDK, en Lua (los dos prototipos antiguos ya están en Lua: PICO-8 y Playdate).
- **Fase 0 «Rescate»**: los prototipos ya están guardados en `material/` de cada idea. Propuesta: reimplementar desde cero en el SDK de Playdate, aprovechando la lógica del de PICO-8 (colocar y simular).
- **Contenido del prototipo**: un tablero, flechas en las cuatro direcciones, el personaje, el destino y 5 niveles de prueba.
- **Lo que no se hará en el prototipo**: menús, música, guardado, gráficos finales, más de 5 niveles, enemigos.
- **Fecha límite**: por decidir (el plan da de 1 a 4 semanas para un prototipo).
- **Limitación a tener en cuenta**: desde las sesiones en la nube se puede compilar con el SDK de Playdate, pero no hay simulador gráfico; las pruebas de verdad (y las de la manivela) se hacen en el PC del usuario o en la consola.

**Preguntas abiertas de la fusión**:

- **Temática**: ¿Caperucita y el lobo (cuento de dominio público, sin problemas para vender), un vampiro como Drakulin pero con nombre y personaje propios, u otra?
- **¿Qué papel tiene el lobo** (o el peligro equivalente)? ¿Un segundo personaje que también sigue las flechas, uno que se mueve por su cuenta, o nada en el prototipo?
- **¿Se puede cambiar el tablero en mitad del tiempo**, o la manivela solo sirve para mirar adelante y atrás y luego se recoloca?
- Fecha límite del prototipo.

## Concepto (Drakulin original)

Versión de *Drakulin*, un juego que salió para móviles Symbian. Hay un tablero con flechas y los personajes tienen que llegar de un lado al otro.

## Prototipos

### PICO-8 (abril de 2023)

Guardado tal cual en [material/pico8/](material/pico8/): `game.p8` (el cartucho, con los gráficos) incluye los `.lua`. Es un primer nivel que funciona entero:

- **Objetivo**: guiar a Drakulin hasta su ataúd «antes de que sea demasiado tarde».
- **Tablero** de 10×10 casillas de 12 px, con el suelo a cuadros. Drakulin empieza en una esquina (9,9) y el ataúd está en (4,5).
- **Dos fases** que se alternan con 🅾️:
  - *Colocar*: el jugador mueve un cursor por el tablero y pone con ❎ las flechas de su inventario. Si pone una flecha sobre otra, la de antes vuelve al inventario.
  - *Simular*: Drakulin camina solo, hacia arriba al principio, y gira al pisar el centro de una flecha. Si llega al ataúd, aparece «DRAKULIN HAS ARRIVED! YOU WIN!».
- Hay dos pantallas de instrucciones al empezar.
- El nivel 1 solo da una flecha hacia la izquierda, y en pantalla pone «1/10: to the left», así que se pensaba en **10 niveles**. Hay sprites para flechas en las cuatro direcciones, pero el código solo usa la de la izquierda.
- Aún no hay forma de perder: no hay límite de tiempo y Drakulin no se choca con nada.
- Textos en inglés.

### Godot (abril de 2025)

Un proyecto vacío llamado `drakulin`, sin código.

## Preguntas abiertas

- Título definitivo: ¿se mantiene el nombre del original o se le da uno propio?
- Plataforma: el prototipo es de PICO-8 y la idea pasó por el repo gameboy. En Game Boy, un tablero de 10×10 casillas de 12 px no cabe tal cual (160×144 px); con casillas de 8 o 16 px habría que rehacerlo.
- ¿Cuándo se pierde? ¿Amanecer (límite de tiempo), salirse del tablero, chocar con obstáculos?
- ¿Hay obstáculos, enemigos u otros personajes además de Drakulin?
- Los 10 niveles: ¿qué introduce cada uno?
- ¿Se puede repetir la simulación cambiando flechas, o solo hay un intento?
- Conviene describir el original de Symbian con más detalle (o buscar capturas o vídeos) para saber qué se conserva y qué se cambia.
