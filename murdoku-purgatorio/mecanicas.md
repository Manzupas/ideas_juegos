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
- Una habitación cerrada o una casilla que solo se sabe que está vacía.
- En la segunda parte, mecánicas que solo tienen sentido en el purgatorio (por ejemplo, un personaje que aparece dos veces).

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
- ¿Quién es el cliente arquitecto? ¿Uno de los doce (encajaría en el círculo del terreno, por los cuarenta pisos) o alguien nuevo? ¿Por qué tiene una versión de los casos?
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

## Correos

**Decidido**:

- El jugador **contesta con respuestas predefinidas** (elige una entre varias; no escribe). **Las respuestas podrían cambiar algo** (qué, por decidir).
- **Cuándo llegan**: a medida que se resuelven Murdokus y que se procesan facturas.
- Al hacker se le contesta igual (por ejemplo, «Te la mando» / «No puedo» / no contestar), o por IRC.

**Propuesta** (por revisar): cada correo de trabajo trae dos o tres respuestas. Ejemplo, de Luis: «Necesito las facturas de octubre cerradas para el viernes.» Respuestas: «Ya están hechas» / «Las tendrás el jueves» / «Voy con retraso, lo siento». Unos minutos después: «¿Qué facturas? No te he pedido nada. ¿Estás bien?»

**Preguntas abiertas**:

- ¿Qué pueden cambiar las respuestas? Sin pensar todavía.
- ¿Qué se puede hacer en el IRC, además de vender?
