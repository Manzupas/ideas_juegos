# Murdoku del purgatorio: mecánicas

Cómo se juega: los Murdokus, las facturas y escrituras, y los correos. La trama está en [historia.md](historia.md).

## Los Murdokus

### Las reglas

En un *Murdoku* hay un plano de una casa dividido en cuadrícula y unos sospechosos. Hay que colocar a cada uno en su casilla siguiendo pistas, con un solo personaje por fila y por columna. El asesino es quien queda solo en una habitación con la víctima.

**Decidido**:

- **Los casos son fijos**: se preparan todos los que va a haber en el juego. El generador es una herramienta de diseño, no se usa mientras se juega.
- Cada caso tiene una única solución y se resuelve solo con deducciones, sin probar a ciegas (así se hizo en el prototipo).
- **Se van metiendo mecánicas nuevas poco a poco.**

**Propuesta** (por revisar): las mecánicas se aprenden en la primera parte, como pasatiempo, y la segunda las usa todas. Ideas guardadas:

- Pistas en negativo: «X no estaba en la cocina».
- Pistas entre personas: «X estaba en la misma fila que Y», «X estaba a la izquierda de Y».
- Puertas y ventanas: «X estaba junto a una puerta».
- Planos más grandes (7×7, 8×8) y más sospechosos.
- Un arma en el plano: el asesino tiene que estar junto a ella.
- **Ideas del arma del crimen**:
  - **Cada arma tiene su alcance**: el abrecartas, al lado de la víctima; el cable del teléfono, en la misma habitación; el pisapapeles lanzado, en la misma fila o columna sin paredes en medio. La regla de quién pudo matar cambia con el arma.
  - **Varias armas, una usada**: varios objetos que pudieron servir (grapadora, cenicero, perforadora); además del asesino hay que deducir el arma, como en el *Cluedo*.
  - **Veneno en el café**: el asesino no tuvo que estar con la víctima; es quien pasó junto a la cafetera.
  - **El arma se movió**: el asesino se la llevó y la dejó en otra habitación, en un sitio por el que pudo pasar.
  - **El arma tiene dueño** (el abrecartas de Luis, la pluma de Ramón): el dueño no tiene por qué ser el asesino, pero cuenta dónde la dejó.
  - **El arma desaparecida**: no está en el plano porque el asesino aún la lleva encima («quien la tenga no pudo pasar por el detector del vestíbulo»).
  - **El sello de la gestoría**: en la muerte del contable, el arma sale de su propia mesa (el sello, la calculadora, un archivador de sus facturas). Cierra el tema de la complicidad.
- Una habitación cerrada o una casilla que solo se sabe que está vacía.
- En la segunda parte, mecánicas que solo tienen sentido en el purgatorio (por ejemplo, un personaje que aparece dos veces).
- **El cuerpo tumbado**: la víctima ocupa dos casillas seguidas, así que su fila o su columna cuenta doble y nadie más puede usarla.
- **Al revés**: se sabe quién es el asesino, pero no quién murió; hay que deducir cuál de los presentes era la víctima.
- **Preguntas de sí o no**: además de las pistas, tres preguntas al purgatorio («¿Estaba Elena en la cocina?»); elegir qué preguntar es parte del puzle.
- **Retrato robot**: cada sospechoso tiene rasgos (gafas, sombrero, bastón) y las pistas solo hablan de rasgos («alguien con gafas estaba en la cocina»).
- **Cómplices**: en la habitación de la víctima hay dos personas y las dos son culpables; hay que acusar a la pareja.
- **La habitación cerrada**: una habitación tiene llave y solo puede estar dentro quien la tenía; hay que deducir quién la llevaba.
- **El pasillo no cuenta**: quien está en el pasillo va de paso y no comparte habitación con nadie.
- **Fichas boca abajo**: primero se colocan fichas sin nombre (las posiciones) y después se descubre quién es cada una.
- **Ventanas**: algunas paredes tienen ventanas que dejan ver la habitación de al lado («Elena vio a Diego por la ventana»).
- **Las extensiones**: cada habitación tiene un teléfono con su extensión y las pistas son llamadas («Isabel llamó a la extensión 3»). Enlaza con la centralita de las facturas.
- **El frío**: hay radiadores en el plano; quien tenía frío estaba lejos de todos y quien tenía calor, junto a uno.
- **El gato de la oficina**: el gato siempre se pone al lado de quien le da de comer; su casilla es una pista que cambia de un caso a otro.
- **El plano de la vuelta anterior**: se ve en transparencia dónde estaba cada uno en la vuelta anterior, y algunas pistas hablan de quién se ha movido y quién no.
- **Los pecados capitales**: cada sospechoso tiene un pecado y cada habitación atrae a uno (la gula, a la cocina; la avaricia, al archivo). Todos acaban en su habitación menos uno.
- **La balanza**: el plano es una balanza; el peso de las almas de la mitad izquierda tiene que igualar el de la derecha.
- **El inspector de Hacienda**: una ficha de inspector; nadie comparte fila, columna ni habitación con él (como la dama del ajedrez), y deja casillas prohibidas.
- **Cada alma se mueve a su manera** (gusta, pero pide cambiar las reglas del Murdoku enteras en esos niveles): las almas empiezan en un sitio conocido y se mueven como piezas de ajedrez (una en línea recta, otra en diagonal, otra saltando); hay que deducir adónde llegaron.

**Preguntas abiertas**:

- ¿Qué mecánicas nuevas y en qué orden?
- ¿Se cambia algo de las reglas del Murdoku (por ejemplo, cuando se revela el purgatorio)?

### Cómo se ven los casos: tres estilos

Maquetas de los tres estilos (el caso 0001 a 1280×720): https://claude.ai/artifact/KgkBG1Jx4S8bP9fK9AqT2p

**Decidido**: el aspecto de los Murdokus cambia a lo largo del juego, y cada cambio llega por algo que pasa en la historia. La mecánica es la misma; cambia cómo se presenta. **El orden es: web (1996) → programa del hacker, GESTA 2000 modificado (final de 1996) → arquitecto (entra como cliente en 1997).**

1. **Página web de 1997** (al principio): el caso se abre en el Navegador como una página web de la época: Times, título granate, rayas horizontales, los sospechosos como enlaces, el plano como un GIF con su pie de foto y un contador de visitas. Encaja con el correo con enlace y con la carga lenta, como con módem.
2. **El programa del hacker**: el hacker le instala al contable **un programa con más funciones**, y los casos salen del Navegador. **Decidido** (17/11/2026): llega al final de 1996, con un **.bat** que instala el IRC y **modifica GESTA 2000 para que muestre los Murdokus**. Por revisar: la maqueta lo muestra en una ventana propia con los controles de Windows 95 (botones biselados, grupos con marco, la lista de pistas en un cuadro hundido). Al no estar dentro del Navegador, el plano tiene más sitio.
3. **Versión de arquitecto**: **un cliente arquitecto** le manda al contable su versión: el plano dibujado en azul, como un plano de arquitecto, y las pistas («Declaraciones») a máquina sobre una carpeta de cartón con un sello («PENDIENTE»).

**Propuesta** (por revisar): **cada fuente trae su dificultad**. Los casos de la web son los fáciles, de tutorial: enseñan las reglas y las mecánicas nuevas. Los del cliente arquitecto son los difíciles. Así la dificultad tiene una razón dentro de la historia, y el jugador sabe qué le espera por dónde le llega el caso.

**Preguntas abiertas**:

- Si la dificultad va por fuentes: ¿se siguen recibiendo casos de la web cuando ya llegan los del arquitecto (dos ritmos a la vez) o la web deja de mandar? ¿Y los casos del programa del hacker, de qué dificultad son?
- ¿Por qué tiene el arquitecto una versión de los casos? (Quién es: [personajes.md](personajes.md).)
- La versión de arquitecto, ¿llega por correo (un adjunto o un enlace) y se sigue abriendo en el Navegador?
- ¿Qué funciones de más tiene el programa del hacker? Por ejemplo: notas por casilla, deshacer, ver el historial de casos y expedientes, o algo que solo tenga sentido con el hacker (marcar secretos en el expediente para vendérselos).
- ¿Cómo se ven los Murdokus dentro de GESTA 2000: una pestaña más, como si fueran documentos, o la ventana propia de la maqueta?
- ¿Qué pasa en la segunda parte? ¿Se queda el programa del hacker o vuelve todo a empezar?

## Facturas y escrituras

**Decidido**:

- El trabajo del contable es **aceptarlas o no**. De momento **no se modifican**: ni se editan cabeceras ni líneas.
- Llegan a una bandeja de **«Pendientes de revisar»** en GESTA. Cada una se abre, se mira y se pulsa **Aceptar** o **Rechazar**.
- **Es una mezcla**:
  - **Reglas con respuesta correcta**, como en *Papers, Please*: reglas de la gestoría que llegan por correo de Luis y que se van acumulando.
  - **Decisiones morales**: algunas facturas no se resuelven con las reglas, y **a veces no hay una opción buena o mala**.
- **Los secretos están en las facturas**: algunas son de los personajes y sus conceptos delatan sus barbaridades. El hacker pide copias justo de esas.
- **El contable revisa también las escrituras notariales**, con sus propias normas.
- **De momento, sin botones nuevos**: el camino sale de aceptar o rechazar, de lo que se vende al hacker (fuera de GESTA) y de lo que se sube a Hacienda. Se descartó por ahora añadir acciones como «hacer una copia» o «apartar como prueba».
- **Las decisiones afectan: el juego lleva la cuenta.** En el prototipo, una cuenta oculta con tres contadores: **errores** (según las normas), **complicidad** (aceptar algo que tapa una barbaridad) y **dureza** (rechazar algo que perjudica a un inocente). Qué cambia con ellos está por decidir.

**Propuesta** (por revisar):

- Ejemplos de reglas: el total tiene que cuadrar con las líneas y el IVA; el emisor tiene que tener NIF o CIF; nada con fecha del ejercicio siguiente; nada duplicado (mismo número o mismo concepto e importe). En 1999, la del efecto 2000 y la del contravalor en euros.
- Normas de las escrituras: las dos cifras (pesetas y euros) tienen que cuadrar al cambio (1 € = 166,386 pesetas, redondeando al céntimo) y tienen que llevar la firma del notario.
- Las escrituras dan juego con los personajes: los embargos de Ramón, la compra del terreno de Bernardo, las ventas de los cuarenta pisos.
- Tres tipos de factura:
  1. **Corrientes**: solo cuentan las reglas. Son la mayoría y dan el ritmo de trabajo.
  2. **Las reglas contra la conciencia**: la factura es correcta pero ayuda a hacer daño (los honorarios de Diego por un embargo de Ramón: aceptarla es lo correcto para la gestoría), o es incorrecta pero rechazarla perjudica a alguien inocente (la factura de una viuda que se ha olvidado del número de IVA y no cobrará a tiempo).
  3. **Sin opción buena**: las dos salidas hacen daño o ninguna arregla nada (pagos de Amparo a Isabel como «asesoría sanitaria»: aceptarla tapa la residencia; rechazarla retrasa el sueldo de las cuidadoras, que tampoco cobran si la residencia cierra).
- Las aceptadas pasan a la carpeta Facturas; las rechazadas, a «Rechazadas».
- **Fallos sin castigo inmediato**: equivocarse con las reglas no se castiga en el momento, pero se nota: un correo seco de Luis o una línea más en una «hoja de errores».
- **Ritmo**: las facturas llegan en tandas; al terminar una tanda llega un correo de un compañero o el siguiente caso.

**Preguntas abiertas**:

- ¿Cuántas facturas por tanda y cada cuánto?
- ¿Cuándo empiezan a llegar las escrituras?

### La gravedad: cómo se decide el camino

**Decidido**: cada documento tiene una gravedad oculta, según lo que destapa:

- **0, corrientes** (la papelería, el bar): no sirven ni para vender ni para denunciar; el hacker las desprecia y Hacienda no hace nada con ellas.
- **1, sin opción buena** (las de las notas de Maruja y Tomás): destapan algo, pero también hacen daño a inocentes.
- **2, contra la conciencia** (el embargo de los Domínguez, el informe del suelo sin anexo C, la recalificación).
- **3, escrituras clave** de cada círculo (los embargos de Ramón, la compra del terreno, las ventas de los pisos).

Se suma la gravedad de lo vendido y la de lo denunciado. Gana el camino con más puntos; si los dos se quedan por debajo de un mínimo, el camino es **callar**. En caso de empate, cuenta lo último que hizo. Así, vender veinte facturas de papelería no es vender: lo que pesa es qué secretos salen y por dónde.

### Ejemplo: la tanda 1 del prototipo (20 facturas, diciembre de 1997)

Facturas en pesetas, con el IVA de 1997 (16 %) y el NIF o CIF de cada empresa, de proveedores y clientes de Logroño y Benidorm. Las normas llegan en el correo de Luis Lindero «Normas para revisar facturas»; la quinta (más de 1.000.000 de pesetas necesita su firma) llega por correo al revisar 10 facturas.

| Nº | Factura | Tipo | Qué dicen las normas | Coste moral |
|----|---------|------|----------------------|-------------|
| 1 | Papelería Brenes → Panadería Olivares, papelería | Corriente | Aceptar | — |
| 2 | Electricidad Quintana → Bar El León Rojo, reparación | Corriente | Rechazar (el total no cuadra) | — |
| 3 | Panadería Olivares → Parroquia de Santa María, canapés de un bautizo | Corriente | Aceptar | — |
| 4 | Cuervo Abogados (Diego) → Créditos Altamira (Ramón), embargo de la familia Domínguez | Conciencia | Aceptar | Aceptar: complicidad |
| 5 | Mudanzas Dávila → Sra. Domínguez, mudanza de la casa embargada al Residencial Ebro (los pisos de Bernardo) | Conciencia | Rechazar (sin NIF/CIF) | Rechazar: dureza |
| 6 | Limpiezas La Glorieta → Gestoría Lindero, fechada el 05/01/1998 | Corriente | Rechazar (fecha) | — |
| 7 | Duplicado de la 1 | Corriente | Rechazar (duplicada) | — |
| 8 | Talleres Picazo → Promociones Torres, revisión de furgoneta | Corriente | Aceptar | — |
| 9 | Consultoría Sanitaria Losada (Isabel) → Residencia Pombo, «asesoría sanitaria» | Sin opción buena (nota de Maruja) | No cuentan | Aceptar: complicidad; rechazar: dureza |
| 10 | Catering El Sequero → Residencia Pombo, menús a 210 pesetas por residente y día | Corriente | Rechazar (el total no cuadra) | — |
| 11 | Construcciones Arteaga → Promociones Torres, cimentación del Residencial Ebro, firmada | Corriente | Aceptar | — |
| 12 | Cobros Bellido (Francisco) → Créditos Altamira, cobros a domicilio, sin firma | Corriente | Rechazar (norma 5) | — |
| 13 | Laboratorio Geotécnico Asensio → Promociones Torres, informe de suelo «sin anexo C» | Conciencia | Aceptar | Aceptar: complicidad |
| 14 | Electricidad Quintana → Bar El León Rojo, factura rectificada | Corriente | Aceptar | — |
| 15 | Residencia Pombo → Sra. Ocaña, cuidados de noche que no se hicieron | Sin opción buena (nota de Maruja) | No cuentan | Aceptar: complicidad; rechazar: dureza |
| 16 | Mercedes Sáez → Residencia Pombo, «medicación de refuerzo» | Corriente | Rechazar (sin NIF/CIF) | — |
| 17 | Arcos y Asociados (Nicolás) → Promociones Torres, recalificación de la antigua Química del Ebro, justo por debajo de 1.000.000 | Conciencia | Aceptar | Aceptar: complicidad |
| 18 | Limpiezas La Glorieta → Gestoría Lindero, fechada el 31/12/1997 | Corriente | Aceptar (justo en el límite) | — |
| 19 | Cobros Bellido → Créditos Altamira, daños en su coche durante un cobro a los Domínguez | Sin opción buena (nota de Tomás) | No cuentan | Aceptar: complicidad; rechazar: dureza |
| 20 | Papelería Brenes → Gestoría Lindero, agendas para 1998 | Corriente | Aceptar | — |

Los correos de los Murdokus llegan al revisar 4, 11 y 17 facturas (cada uno, una vez resuelto el caso anterior). Al terminar la tanda, Luis manda un resumen con los errores; en el prototipo, ese correo enseña también la cuenta oculta.

### Que revisar facturas sea divertido

**Propuesta** (por revisar): la revisión tal cual, abrir y aceptar en GESTA, es demasiado real. Se hicieron maquetas jugables de varias ideas (noviembre de 2026); estas gustaron y pueden combinarse:

- **La cinta de sellos** (la que más gustó): arcade. Las facturas pasan de una en una con el tiempo justo y se sellan ACEPTADA o RECHAZADA con dos sellos grandes (o deslizando la factura). Por rondas, Luis añade normas y al final una excepción que contradice las anteriores («las de Promociones Torres, siempre aceptadas»). Rachas que multiplican y tres vidas: la paciencia de Luis. Encaja con las reglas que se acumulan y con la complicidad: la excepción de Luis es justo lo que tapa algo.
- **Busca las diferencias** (la que más gustó): el original del archivo al lado de la copia que ha llegado, retocada con Tipp-Ex; se tocan en la copia las líneas cambiadas (importe, fecha, cubiertos, firma) y cada fallo cuesta tiempo. Sirve para que el contable descubra por sí mismo quién infla las cuentas.
- **La mesa del contable**: la factura sobre la mesa y herramientas de verdad: sello, Tipp-Ex, el cajón (guardar sin decidir) y la trituradora.
- **A escondidas del jefe**: copiar para el hacker las facturas comprometedoras mientras Luis pasa por detrás; si te ve, hay que disimular. Sería la forma de jugar la venta al hacker.
- **Leer entre líneas** (podría valer): de un grupo de facturas se eligen las que dan las pistas de un Murdoku; con las buenas, el caso tiene solución única. Une las facturas con los Murdokus.
- **Cuadrar las cuentas** (podría valer): un puzle sobre el libro de cuentas: cada factura se coloca en su casilla (cuenta por mes) para que cada fila y cada columna sumen su total y se cumplan las notas de Luis. Podría ser el momento de cerrar cada tanda o cada mes.

- **Esa factura miente**: un proveedor llama para defender su factura rechazada; se pasan sus frases y, al oír la mentira, se toca la línea de la factura que la desmiente (una fecha que no cuadra, un IVA mal calculado, una reforma que no era «solo la planta segunda»). Tocar una línea cuando dice la verdad cuesta credibilidad. Daría voz a los rechazos.
- **El archivador**: Luis pide facturas con pistas vagas («la de la luz del bar, la rectificada») y hay que encontrarlas en los cajones, ordenados por emisor, antes de que se le acabe la paciencia. Lo que pide Luis también cuenta la historia: ¿para qué quiere justo esas?

- **Seguir el dinero**: de un pago de Torres se sigue el dinero de factura en factura (la paga quien cobró la anterior, es posterior y se lleva casi todo, menos una comisión) entre facturas trampa, a través de empresas pantalla, hasta quien se lo queda. Una forma de jugar los círculos de corrupción con facturas.
- **El cheque en letras**: el importe en letras se escribe con fichas de palabras; las trampas son las de la escuela («trescientos» con pesetas, «ciento mil», «veinte y cuatro»). Luis puede pedir que no se cierre la línea con rayas, y luego aparece algo añadido.
- **La factura triturada**: recomponer las tiras de lo que Luis ha pasado por la trituradora, guiándose por lo que cruza de una tira a otra. Lo reconstruido es lo que quería esconder.

- **La centralita** (puede estar bien): suenan varias líneas a la vez y cada llamada se pasa a su extensión según la nota de Luis («si llama Hacienda, no estoy»; «Torres, siempre conmigo»), con trampas como el «amigo de la delegación». Las llamadas que van a Luis se pueden escuchar a escondidas, a riesgo de que se oiga el clic: así se entera el contable de lo que no está en los papeles.
Descartadas: las cuatro barras al estilo *Reigns*, el ordenador que se cuelga, el tablón de corcho, la firma de Luis (calcarla con el dedo), la caja (dar el cambio en pesetas), de memoria (recordar una factura antes de que la trituren), la tesorería (repartir los pagos de la semana), la inspección de Hacienda (elegir qué documento se enseña) y conciliar el banco (emparejar cargos con facturas).

**Preguntas abiertas**:

- La mesa (Tipp-Ex, trituradora) choca con «no se modifican» y con «sin botones nuevos»; *A escondidas del jefe* añade «hacer una copia». ¿Se reabre esa decisión?
- ¿La cinta es el modo normal de revisar o un momento puntual (el cierre del ejercicio, una tanda con prisas)?
- ¿Busca las diferencias va con todas las facturas o solo con las que Luis ha retocado?

## Correos

**Decidido**:

- El jugador **contesta con respuestas predefinidas** (elige una entre varias; no escribe). **Las respuestas podrían cambiar algo** (qué, por decidir).
- **Cuándo llegan**: a medida que se resuelven Murdokus y que se procesan facturas.
- Al hacker se le contesta igual (por ejemplo, «Te la mando» / «No puedo» / no contestar), o por IRC.

**Propuesta** (por revisar): cada correo de trabajo trae dos o tres respuestas. Ejemplo, de Luis: «Necesito las facturas de octubre cerradas para el viernes.» Respuestas: «Ya están hechas» / «Las tendrás el jueves» / «Voy con retraso, lo siento». Unos minutos después: «¿Qué facturas? No te he pedido nada. ¿Estás bien?»

**Preguntas abiertas**:

- ¿Qué pueden cambiar las respuestas? Sin pensar todavía.
- ¿Qué se puede hacer en el IRC, además de vender?
