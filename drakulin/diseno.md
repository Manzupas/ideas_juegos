# Drakulin (título provisional)

| Ficha | |
|-------|---|
| Estado | semilla |
| Plataforma candidata | Por decidir (estaba en el repo gameboy) |
| Origen | Port de *Drakulin*, juego para móviles Symbian |
| Año | 2023 o antes: el primer prototipo, en PICO-8, es de abril de 2023 |

## Concepto

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
