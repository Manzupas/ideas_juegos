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
- **El jugador**: eres un oficinista haciendo trabajo burocrático; te llega un correo electrónico con un enlace y ya no puedes parar de resolver *Murdokus*.
- **Quién es en realidad el oficinista**: una persona que también está en el purgatorio. Su papel allí es torturar a los demás, sin saberlo.
- **Estética**: la oficina es solo estilo, no se juega. La interfaz recuerda a un programa de facturación o algo parecido.
- **Posible título**: *Office Work*.

## Prototipo web

[prototipo/index.html](prototipo/index.html), publicado como artefacto para probarlo también en el móvil: https://claude.ai/artifact/QgHxcBtNP4yLWGyQ3VYhcJ

Es el ordenador del oficinista, con estética de Windows 98 (sistema «Lindero 98»):

- **Escritorio**: iconos (Mi PC, Mis documentos, Facturas, GESTA 2000, Correo, Navegador, Bloc de notas, Papelera de reciclaje), ventanas que se arrastran, minimizan, maximizan y cierran, barra de tareas con reloj y menú Inicio. En el móvil todas las ventanas se abren maximizadas y los iconos se abren con un toque.
- **GESTA 2000** (facturación de la Gestoría Lindero): lista de facturas, cabecera, líneas que se añaden y se borran, totales con el IVA desglosado; Nueva, Guardar, Añadir línea y Duplicar. Las facturas se guardan en el navegador. En pantallas grandes está abierto al empezar.
- **Explorador de carpetas**: Mi PC, Disco local (C:), Mis documentos, Archivos de programa y **Facturas**, donde cada factura es un archivo `.fac` que se abre en GESTA. Disquete y carpeta Windows dan sus avisos clásicos.
- **Correo**: carpetas (entrada, enviados, borradores, eliminados), lista, vista previa, Crear correo, Responder, Eliminar y Enviar y recibir.
- **El enganche**: la primera vez que se guarda una factura (o con «Enviar y recibir») llega un correo de Rosario Montes, una compañera: «esto engancha, ya verás». Sale un globo de aviso en la bandeja; al pulsarlo se abre el correo, y su enlace abre el caso en el **Navegador**.
- **Bloc de notas**: notas de la oficina en Mis documentos (`pendientes.txt`, `claves.txt`) y un borrador de carta en la Papelera; se pueden escribir y guardar notas nuevas.
- **Murdoku**: un caso de 6×6 con 6 personajes (Leopoldo, la víctima, y Amparo, Bruno, Carmela, Dámaso y Elvira) y 7 pistas. Se elige a una persona y se toca una casilla; tocarla otra vez la quita. Hay un modo para tachar casillas, las pistas se tachan al tocarlas y «Comprobar» dice qué pistas o reglas fallan. Al acertar se acusa al culpable.
- **Pistas del purgatorio**, muy discretas: los clientes y los correos tienen los nombres de los personajes (Leopoldo debe la factura 0141 y contestó «No pienso pagar esto»; Bruno «juraría» que ya le mandaron la factura), las notas dicen «Tercera vez», al cerrar el caso aparece «Fallecimientos registrados: 3» y **el equipo no se puede apagar**: «Todavía tiene tareas pendientes».
- **El caso** se generó con [prototipo/scripts/humano.py](prototipo/scripts/humano.py) (usa `caso.py`; se ejecutan desde esa carpeta): tiene una única solución y se resuelve solo con deducciones (las pistas de cada persona más una persona por fila y columna), sin probar a ciegas.

## Referencia

En un *Murdoku* hay un plano de una casa dividido en cuadrícula y unos sospechosos. Hay que colocar a cada uno en su casilla siguiendo pistas, con un solo personaje por fila y por columna. El asesino es quien queda solo en una habitación con la víctima.

## Preguntas abiertas

- Título definitivo: ¿*Office Work*?
- ¿10 o 12 personajes? ¿Quiénes son y qué relación tienen entre ellos?
- ¿Qué barbaridad hizo cada uno? ¿Están relacionadas entre ellas?
- ¿Cómo se cuenta la vida de cada personaje? ¿En las pistas, en textos entre casos, en objetos de los planos?
- ¿Cómo se va notando el giro? ¿Detalles raros en las pistas o en los planos, víctimas que reaparecen, personajes que recuerdan casos anteriores?
- ¿Qué hizo el oficinista en vida para estar en el purgatorio? ¿Se descubre al final?
- ¿Quién manda el correo? ¿Es otra persona del purgatorio, el propio purgatorio, alguien de la oficina?
- ¿Cómo y cuándo descubre el oficinista que los está torturando, y que él también está allí?
- ¿Qué pasa cuando el jugador lo descubre? ¿Puede seguir o parar? ¿Cambia algo según lo que decida?
- ¿Cuántos casos? ¿Hay un final o varios?
- ¿Los puzles se diseñan a mano o se generan? Hay que comprobar que cada uno tiene una única solución.
- ¿Se cambia algo de las reglas del *Murdoku* (por ejemplo, cuando se revela el purgatorio)?
