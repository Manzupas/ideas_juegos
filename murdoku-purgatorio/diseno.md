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

[prototipo/index.html](prototipo/index.html), publicado como artefacto para probarlo en el móvil: https://claude.ai/artifact/QgHxcBtNP4yLWGyQ3VYhcJ

- **Facturación** (*GESTA 2000*, de la Gestoría Lindero): lista de facturas, cabecera (serie, número, fecha, cliente, NIF, dirección, forma de pago), líneas que se añaden y se borran (código, concepto, cantidad, precio, descuento, IVA) y totales con el IVA desglosado. Botones Nueva, Guardar, Añadir línea y Duplicar. Las facturas se guardan en el navegador.
- **Notificación**: la primera vez que se guarda una factura llega un correo («esto engancha, ya verás»); también con el botón de correo de la barra de estado. Al pulsarlo se abre el caso en una ventana de navegador.
- **Murdoku**: un caso de 6×6 con 6 personajes (Leopoldo, la víctima, y Amparo, Bruno, Carmela, Dámaso y Elvira) y 7 pistas. Se elige a una persona y se toca una casilla; tocarla otra vez la quita. Hay un modo para tachar casillas, las pistas se pueden tachar al tocarlas y «Comprobar» dice qué pistas o reglas fallan. Al acertar se acusa al culpable.
- **Pistas del purgatorio**: casi ninguna. Los clientes de las facturas tienen los nombres de los personajes (Leopoldo tiene una factura de «Gestión de testamento» sin respuesta) y al cerrar el caso aparece «Fallecimientos registrados: 3».
- **El caso** se generó con [prototipo/scripts/humano.py](prototipo/scripts/humano.py) (usa `caso.py`): tiene una única solución y se resuelve solo con deducciones (las pistas de cada persona más una persona por fila y columna), sin probar a ciegas.

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
