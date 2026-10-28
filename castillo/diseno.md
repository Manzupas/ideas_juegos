# Castle (título provisional)

| Ficha | |
|-------|---|
| Estado | semilla |
| Plataforma candidata | Por decidir (el prototipo está en Unity 6) |
| Origen | Prototipo antiguo en Unity: `Castle`, guardado en [material/](material/) |
| Año | 2025 (según las fechas de los archivos, mayo de 2025) |

## Concepto

Un juego de puzles sencillo: hay que recorrer un castillo abriendo y cerrando puertas y consiguiendo los objetos que hacen falta para ello.

## Lo que hace el prototipo

- El jugador es una cápsula con el controlador de los *Starter Assets* de Unity.
- Al tocar un objeto coleccionable, este desaparece y se abre la puerta que le corresponde: diamante verde, azul o rosa, y un relámpago. Cada uno abre su puerta.
- Las puertas solo se abren (giran 90°); todavía no se cierran.

## Material

- [material/scripts/](material/scripts/): los dos scripts propios (`PlayerCapsule`, `Puerta`). El resto del proyecto (unos 2 GB) son assets de terceros (*Starter Assets*, gemas BTM) y archivos generados por Unity, y no se guarda.

## Preguntas abiertas

- Título definitivo.
- ¿Primera persona, tercera persona o vista desde arriba?
- ¿Qué hace que sea un puzle? ¿Puertas que, al abrirse, cierran otras, llaves que se gastan, un orden que hay que descubrir?
- ¿Qué objetos hay además de los diamantes y el relámpago?
- ¿Un solo castillo grande o varios niveles?
- Plataforma: ¿seguir en Unity o pasar a otra?
