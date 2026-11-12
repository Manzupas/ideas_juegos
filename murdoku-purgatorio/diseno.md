# Murdoku del purgatorio (título provisional)

| Ficha | |
|-------|---|
| Estado | semilla |
| Plataforma candidata | Godot, para PC |
| Origen | Idea nueva, basada en los puzles *Murdoku* |
| Año | 2026 |

## Concepto

Un juego de puzles tipo *Murdoku*, con un giro gordo:

- **Siempre son los mismos personajes**: una colección de 10 o 12 que se repiten en todos los casos.
- **En realidad están en el purgatorio.**
- **Empieza siendo un *Murdoku* "normal"**: al principio el jugador no sabe nada del purgatorio; el giro se descubre jugando.

## Decidido

- **Historia por entregas**: *Murdoku* a *Murdoku* se va descubriendo quién era cada personaje y las barbaridades que hizo en vida.
- **Por qué están en el purgatorio**: porque lo merecen por haber sido malas personas.
- **El papel del jugador**: sin saberlo, se dedica a torturarlos.
- **Cómo es la tortura**: en los casos, cada personaje va muriendo varias veces.
- **No pueden salir del purgatorio.**
- **El jugador es «el contable»**: trabajas en una gestoría haciendo trabajo burocrático; te llega un correo electrónico con un enlace y ya no puedes parar de resolver *Murdokus*.
- **Quién es en realidad el contable**: una persona que también está en el purgatorio. Su papel allí es torturar a los demás, sin saberlo.
- **Estética**: la oficina es solo estilo, no se juega. La interfaz recuerda a un programa de facturación o algo parecido.
- **Posible título**: *Office Work*.
- **Los personajes tienen nombres clásicos ingleses** (los torturados).
- **La gestoría del contable también es inglesa**: se llama Finch & Limbrick, y su socio fundador es Oswald Finch, uno de los personajes. No todos los personajes son clientes suyos, pero en cada «relación» (cada círculo de personajes que comparten una barbaridad) al menos uno sí lo es. Ver [personajes.md](personajes.md). La compañera de los correos se llama Rosemary Mount. El prototipo todavía usa la gestoría española (Gestoría Lindero, Rosario Montes, euros): está pendiente de cambiar.
- **Temática de los casos**: en general, relacionada con la historia inglesa. Los primeros casos (los del prototipo) son de la Inglaterra contemporánea.

## Personajes

Propuesta de historias de los doce personajes, agrupados en tres círculos (las deudas, la residencia, el terreno), la gestoría inglesa y el contable: [personajes.md](personajes.md). Pendiente de revisar.

## Prototipo web

Prototipo en HTML y JavaScript, en un solo archivo y sin dependencias. **Para jugar en local, abrir [prototipo/office-work.html](prototipo/office-work.html)**; cómo se genera y qué es cada archivo está en [prototipo/README.md](prototipo/README.md). También está publicado como artefacto para probarlo en el móvil: https://claude.ai/artifact/QgHxcBtNP4yLWGyQ3VYhcJ

Es el ordenador del contable, con estética de Windows 98 (sistema «Lindero 98»):

- **Escritorio**: iconos (Mi PC, Mis documentos, Facturas, GESTA 2000, Correo, Navegador, Bloc de notas, Papelera de reciclaje), ventanas que se arrastran, minimizan, maximizan y cierran, barra de tareas con reloj y menú Inicio. En el móvil todas las ventanas se abren maximizadas y los iconos se abren con un toque.
- **GESTA 2000** (facturación de la Gestoría Lindero): lista de facturas, cabecera, líneas que se añaden y se borran, totales con el IVA desglosado; Nueva, Guardar, Añadir línea y Duplicar. Las facturas se guardan en el navegador. En pantallas grandes está abierto al empezar.
- **Explorador de carpetas**: Mi PC, Disco local (C:), Mis documentos, Archivos de programa y **Facturas**, donde cada factura es un archivo `.fac` que se abre en GESTA. Disquete y carpeta Windows dan sus avisos clásicos.
- **Correo**: carpetas (entrada, enviados, borradores, eliminados), lista, vista previa, Crear correo, Responder, Eliminar y Enviar y recibir.
- **El enganche**: la primera vez que se guarda una factura (o con «Enviar y recibir») llega un correo de Rosario Montes, una compañera: «esto engancha, ya verás». Sale un globo de aviso en la bandeja; al pulsarlo se abre el correo, y su enlace abre el caso en el **Navegador**.
- **Bloc de notas**: notas de la oficina en Mis documentos (`pendientes.txt`, `claves.txt`) y un borrador de carta en la Papelera; se pueden escribir y guardar notas nuevas.
- **Personajes**: Reginald Ashcombe, Agatha Pembroke, Bernard Thorne, Cecily, Desmond, Edith, Frederick y Gertrude. Cada caso usa seis.
- **Tres Murdokus de 6×6**, cada uno con otra casa, otra víctima y otro asesino:

  | Caso | Escenario | Víctima | Asesino | Expediente | Llega |
  |------|-----------|---------|---------|------------|-------|
  | 0001 | Una casa en Hampstead, Londres | Reginald | Desmond | Dueño de una empresa de préstamos rápidos; se quedó con las casas de tres familias. Fallecimientos: 3 | Correo de Rosario al guardar una factura (o con «Enviar y recibir») |
  | 0002 | La residencia Pembroke, Brighton | Agatha | Cecily | Directora de una residencia de mayores; cobraba cuidados que nunca se daban. Fallecimientos: 5 (pendiente: Agatha pasa a ser la dueña y Cecily la directora, ver [personajes.md](personajes.md)) | Correo de Rosario («¿Ya? Hay otro») al resolver el 0001 |
  | 0003 | Una casa en las afueras de Manchester | Bernard | Edith | Promotor; vendió cuarenta pisos sobre un terreno que sabía contaminado. Fallecimientos: 2 | Correo «(sin remitente)» al resolver el 0002 |

  En el caso 0003 vuelve a aparecer Reginald, vivo, aunque murió en el 0001.
- **Cómo se juega**: se elige a una persona y se toca una casilla; tocarla otra vez la quita. Hay un modo para tachar casillas, las pistas se tachan al tocarlas y «Comprobar» dice qué pistas o reglas fallan. Al acertar se acusa al culpable y se abre el expediente de la víctima.
- **Los casos** se generan con los scripts de [prototipo/scripts/](prototipo/scripts/): el 0001 con `humano.py` (usa `caso.py`) y el 0002 y el 0003 con `generar_caso.py casoN.json`, que lee el plano, los personajes y la víctima de un JSON. Se ejecutan desde esa carpeta. Cada caso tiene una única solución y se resuelve solo con deducciones (las pistas de cada persona más una persona por fila y columna), sin probar a ciegas.

## Referencia

En un *Murdoku* hay un plano de una casa dividido en cuadrícula y unos sospechosos. Hay que colocar a cada uno en su casilla siguiendo pistas, con un solo personaje por fila y por columna. El asesino es quien queda solo en una habitación con la víctima.

## Preguntas abiertas

- Título definitivo: ¿*Office Work*?
- ¿10 o 12 personajes? ¿Quiénes son y qué relación tienen entre ellos?
- ¿Qué barbaridad hizo cada uno? ¿Están relacionadas entre ellas?
- ¿Cómo se cuenta la vida de cada personaje? ¿En las pistas, en textos entre casos, en objetos de los planos?
- ¿Cómo se va notando el giro? ¿Detalles raros en las pistas o en los planos, víctimas que reaparecen, personajes que recuerdan casos anteriores?
- ¿Qué hizo el contable en vida para estar en el purgatorio? ¿Se descubre al final?
- ¿Quién manda el correo? ¿Es otra persona del purgatorio, el propio purgatorio, alguien de la oficina?
- ¿Cómo y cuándo descubre el contable que los está torturando, y que él también está allí?
- ¿Qué pasa cuando el jugador lo descubre? ¿Puede seguir o parar? ¿Cambia algo según lo que decida?
- ¿Cuántos casos? ¿Hay un final o varios?
- ¿Los puzles se diseñan a mano o se generan? Hay que comprobar que cada uno tiene una única solución.
- ¿Se cambia algo de las reglas del *Murdoku* (por ejemplo, cuando se revela el purgatorio)?
