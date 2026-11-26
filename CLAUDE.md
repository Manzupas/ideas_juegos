# Ideas de juegos: cómo se organiza este repo

Aquí viven las ideas de juegos que todavía no se están desarrollando: conceptos nuevos y prototipos antiguos que se quieren terminar o reimplementar. Cuando una idea empieza a desarrollarse, se mueve al repositorio de su plataforma (por ejemplo, [gameboy](https://github.com/Manzupas/gameboy)).

## Estructura

- **Una carpeta por idea** en la raíz, con un nombre corto en minúsculas y guiones: `mediador-de-monstruos/`. La carpeta no cambia de sitio cuando cambia el estado o la plataforma.
- Dentro de cada carpeta:
  - `diseno.md`: la especificación de la idea. Empieza con la **ficha** (ver abajo), y después el concepto, lo decidido y las preguntas abiertas.
  - `material/` (opcional, se crea cuando haga falta): material antiguo o de referencia, como código de prototipos viejos, bocetos, capturas o notas. Se guarda tal cual; lo que se decida a partir de él se apunta en `diseno.md`.
- Las ideas nuevas se crean copiando [_plantilla/diseno.md](_plantilla/diseno.md).
- `_entrada/` es una bandeja local que no se commitea (está en `.gitignore`): ahí se deja material sin organizar, como prototipos viejos o notas sueltas. Al organizarlo, lo que sirva se mueve a `material/` de su idea y se apunta en su `diseno.md`.
- El [README.md](README.md) es el índice: una fila por idea, agrupadas por estado. Hay que actualizarlo al crear una idea o al cambiarle el estado.

## Ficha

Tabla al principio de cada `diseno.md`:

| Campo | Qué va |
|-------|--------|
| Estado | Uno de los estados de abajo |
| Plataforma candidata | Game Boy, Godot, otra, o "Por decidir" |
| Origen | Idea nueva, prototipo antiguo (de qué y dónde está) o port de otro juego (cuál) |
| Año | Año de la idea o del prototipo original, si se sabe; si no, "Por apuntar" |

No se inventan datos: lo que no haya dicho el usuario queda como "Por decidir" o "Por apuntar".

## Estados

| Estado | Significa |
|--------|-----------|
| semilla | Solo el concepto, sin especificar. |
| definiendo | Se están cerrando reglas, mecánicas y alcance. |
| lista para prototipo | Hay suficiente definido para empezar a programar. |
| movida | Ya se desarrolla en otro repositorio. Se deja la carpeta solo con un `diseno.md` mínimo que enlaza al nuevo sitio. |
| fusionada | Se ha unido a otra idea. Su `diseno.md` enlaza a la idea con la que se fusionó, donde sigue el diseño; su `material/` se queda en su carpeta. No aparece en el índice salvo como origen de la otra. |

## Plan de desarrollo

Desde **lista para prototipo**, la idea sigue el [plan de desarrollo](plan-desarrollo.md): Plan A (prototipo, empezando por la fase 0 «Rescate» si es un prototipo antiguo) y, si el prototipo funciona, Plan B (juego completo). Al mover una idea a su repositorio se copia allí la [ficha de seguimiento](_plantilla/seguimiento.md) y se actualiza al cerrar cada fase. Publicación: Game Boy solo en itch.io; Playdate en itch.io y opcionalmente Catalog; Godot en itch.io y opcionalmente Steam. Marketing y Steam son opcionales.

## Conversaciones

El usuario trabaja desde varias conversaciones y quiere que todo lo que se habla de una idea esté disponible en las demás. **GitHub (`Manzupas/ideas_juegos`) es la fuente de verdad**:

- **Al empezar**: `git pull` antes de leer o tocar nada.
- **Durante**: cada decisión o propuesta se apunta en el `diseno.md` de la idea (o en otro `.md` de su carpeta, como `personajes.md`), marcando qué está decidido y qué es propuesta.
- **Al terminar cada cambio**: commit y `git push`. Lo que no está subido no existe para las demás conversaciones.
- **Excepción: Murdoku del purgatorio** está movida (se desarrolla en [murdokus](https://github.com/Manzupas/murdokus)), pero su diseño (todos los `.md` de su carpeta: `diseno.md`, `historia.md`, `escaleta.md`, `personajes.md`, `mecanicas.md`, `ambientacion.md`) sigue viviendo y actualizándose aquí, desde varias conversaciones, hasta que se escriba el GDD. No se reduce a un `diseno.md` mínimo.
- Los `.md` de **Murdoku del purgatorio** también se copian en los documentos del proyecto de claude.ai «Ideas De Juegos»; si cambian, se vuelven a subir allí.

## Commits

- Se trabaja directamente en `main`: aquí solo hay documentos.
- Los mensajes de commit van en castellano.
