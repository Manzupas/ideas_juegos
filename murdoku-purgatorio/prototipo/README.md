# Prototipo de Office Work (HTML y JavaScript)

Prototipo jugable del Murdoku del purgatorio: el ordenador del contable, con estética de Windows 95, en el que llegan los casos por correo. Todo está en un solo archivo, sin dependencias ni conexión a internet.

## Jugar en local

Abre **[office-work.html](office-work.html)** con doble clic (o arrástralo al navegador).

- Para que llegue el primer caso: abre GESTA 2000 y pulsa **Guardar** (o «Enviar y recibir» en el Correo).
- Cada caso siguiente llega por correo al resolver el anterior.
- Las facturas guardadas se conservan en el navegador; los casos resueltos y los correos, no (se empieza de cero al recargar).

También está publicado como artefacto para jugarlo desde el móvil: https://claude.ai/artifact/QgHxcBtNP4yLWGyQ3VYhcJ

## Qué hay en el prototipo

**Decidido**: el prototipo no se actualiza más; se queda como está. Es de antes de la estructura en dos partes: todo pasa en un solo día, los Murdokus ya son los del purgatorio y usa los nombres anteriores al 17/11/2026 (Rogelio, Águeda, Bernardo…; la tabla de cambios está en [personajes.md](../personajes.md)).

Es el ordenador del contable de la Gestoría Lindero, con estética de Windows 95 (sistema «Lindero 95»: barras de título lisas, sin degradado). El día es el miércoles 31 de diciembre de 1997, cierre del ejercicio.

- **Escritorio**: iconos (Mi PC, Mis documentos, Facturas, GESTA 2000, Correo, Navegador, Bloc de notas, Papelera de reciclaje), ventanas que se arrastran, se redimensionan con el ratón (bordes y esquinas), minimizan, maximizan y cierran, barra de tareas con reloj y menú Inicio. En el móvil todas las ventanas se abren maximizadas y los iconos se abren con un toque.
- **GESTA 2000** (Gestoría Lindero): revisión de una tanda de 20 facturas (la tabla está en [mecanicas.md](../mecanicas.md)). Pestañas Pendientes, Aceptadas y Rechazadas; cada factura se ve como un papel (emisor, cliente, líneas, base, IVA, total, firma) con su sello y, si la lleva, una nota pegada. Botones Aceptar, Rechazar y Normas. No se puede modificar nada. En pantallas grandes está abierto al empezar.
- **Explorador de carpetas**: Mi PC, Disco local (C:), Mis documentos, Archivos de programa, **Facturas** y **Facturas rechazadas**, donde cada factura revisada es un archivo `.fac` que se abre en GESTA. Disquete y carpeta Windows dan sus avisos clásicos.
- **Correo**: carpetas (entrada, enviados, borradores, eliminados), lista, vista previa, Crear correo, Responder, Eliminar y Enviar y recibir.
- **El ordenador va lento**, y cuánto depende de lo que se hace. Mientras tanto sale el reloj de arena y se ignoran los clics. Dentro del Murdoku, colocar fichas es instantáneo. Tiempos (constante `DELAY` en `index.html`):

  | Acción | Espera |
  |--------|--------|
  | Cambiar de factura, abrir un `.fac`, factura nueva o duplicada | 0,15–0,35 s |
  | Guardar factura | 0,3–0,6 s |
  | Avisos, menú Inicio | 0,1–0,3 s |
  | Bloc de notas, mensaje nuevo, entrar en una carpeta | 0,2–0,6 s |
  | Abrir una ventana del explorador | 0,5–0,9 s |
  | Abrir GESTA 2000 | 0,7–1,2 s |
  | Abrir el Correo | 0,9–1,5 s |
  | Enviar y recibir | 1,5–2,5 s |
  | Abrir el Navegador | 1,8–2,8 s |
  | Cargar un caso por primera vez | unos 9 s (con barra de progreso) |
- **Las páginas cargan como con módem**: la primera vez que se abre cada caso, la barra de estado va diciendo «Buscando…», «Conectando…», «Transfiriendo datos…», con barra de progreso; primero llega el texto, luego las pistas una a una y el plano baja poco a poco de arriba abajo, como una imagen antigua. Las veces siguientes sale al momento. Mientras carga, el puntero es la flecha con reloj de arena y no se puede jugar.
- **La ventana del caso se ajusta** para que el Murdoku se vea entero (si cabe en la pantalla). Las pistas y las reglas van pegadas al tablero con anchos fijos: al agrandar la ventana, el hueco queda a la derecha.
- **El enganche**: al revisar 4 facturas llega un correo de Rosario Valle, una compañera: «esto engancha, ya verás». Sale un globo de aviso en la bandeja; al pulsarlo se abre el correo, y su enlace abre el caso en el **Navegador**.
- **Bloc de notas**: notas de la oficina en Mis documentos (`pendientes.txt`, `claves.txt`) y un borrador de carta en la Papelera; se pueden escribir y guardar notas nuevas.
- **Personajes**: Ramón Altamira, Amparo Pombo, Bernardo Torres, Carmen, Diego, Elena, Francisco y Gloria (en el prototipo salen con los nombres anteriores). Cada caso usa seis.
- **Tres Murdokus de 6×6**, cada uno con otra casa, otra víctima y otro asesino:

  | Caso | Escenario | Víctima | Asesino | Expediente | Llega |
  |------|-----------|---------|---------|------------|-------|
  | 0001 | Un chalé en Puerta de Hierro, Madrid | Ramón | Diego | Prestamista; se quedó con las casas de tres familias. Fallecimientos: 3 | Correo de Rosario al revisar 4 facturas |
  | 0002 | La Residencia Pombo, Benidorm | Amparo | Carmen | Dueña de una residencia de ancianos; cobraba cuidados que nunca se daban. Fallecimientos: 5 | Correo de Rosario («¿Ya? Hay otro») al revisar 11 facturas, con el 0001 resuelto |
  | 0003 | Un chalé en las afueras de Zaragoza | Bernardo | Elena | Promotor; vendió cuarenta pisos sobre un terreno que sabía contaminado. Fallecimientos: 2 | Correo «(sin remitente)» al revisar 17 facturas, con el 0002 resuelto |

  En el caso 0003 vuelve a aparecer Ramón, vivo, aunque murió en el 0001.
- **Cómo se juega**: se elige a una persona y se toca una casilla; tocarla otra vez la quita. Hay un modo para tachar casillas, las pistas se tachan al tocarlas y «Comprobar» dice qué pistas o reglas fallan. Al acertar se acusa al culpable y se abre el expediente de la víctima.
- **Los casos** tienen una única solución y se resuelven solo con deducciones (las pistas de cada persona más una persona por fila y columna), sin probar a ciegas.

## Archivos

| Archivo | Qué es |
|---------|--------|
| [index.html](index.html) | La fuente. Es lo que se edita y lo que se publica como artefacto (sin `<!doctype>` ni `<head>`, que los pone la plataforma). |
| [office-work.html](office-work.html) | La versión para jugar en local. Se genera a partir de `index.html`; no se edita a mano. |
| [scripts/empaquetar.py](scripts/empaquetar.py) | Genera `office-work.html`: `python3 -I scripts/empaquetar.py` desde esta carpeta. Hay que ejecutarlo después de cada cambio en `index.html`. |
| [scripts/caso.py](scripts/caso.py), [scripts/humano.py](scripts/humano.py) | Generaron el caso 0001. |
| [scripts/generar_caso.py](scripts/generar_caso.py) | Genera y comprueba un caso a partir de un JSON (`caso2.json`, `caso3.json`): solución única y resoluble solo con deducciones. Se ejecuta desde `scripts/`: `python3 -I generar_caso.py caso2.json`. |
| `scripts/casoN.salida.json` | Resultado del generador (solución, asesino y pistas) que se copió a `index.html`. |
