# Murdoku del purgatorio: ambientación y estética

## Lugar y época

**Decidido**:

- **Posible título**: *Office Work*.
- **El jugador es «el contable»**: trabaja en una gestoría haciendo trabajo burocrático; le llega un correo electrónico con un enlace y ya no puede parar de resolver Murdokus.
- **La oficina se juega**: la interfaz recuerda a un programa de facturación (GESTA).
- **Ambientación: España.** **Época: el contable empieza a trabajar en 1996.**
- **Los personajes tienen nombres españoles clásicos** (ver [personajes.md](personajes.md)).
- **La gestoría está en Logroño.** El periódico local es *El Diario del Ebro*, que se lee en su edición digital (ver [historia.md](historia.md)).
- **La gestoría es española.** No todos los personajes son clientes suyos, pero en cada círculo al menos uno sí lo es. Propuesta: Gestoría Lindero, fundada por Julián Lindero.
- **Temática de los casos**: en general, **la historia de España**. Los primeros casos, en la España de los 90.
- **Estética: Windows 95.** Un ordenador viejo en una gestoría de finales de los 90, que encaja con que vaya lento. (Se descartaron Windows 98 y Windows 7.)
- **El efecto 2000**: el reloj del ordenador nunca llega al 1 de enero de 2000; el tiempo del purgatorio está atascado en el final del milenio. Tomás, el informático, puede usar el efecto 2000 como excusa para cosas raras del ordenador.
- **La aplicación del hacker**: un cliente de **IRC** de la época (canales, apodos, la ventana de texto con la lista de usuarios a un lado), que aparece instalado sin que nadie lo haya instalado. En la España de finales de los 90 el IRC era muy popular (IRC-Hispano).
- **«Vender secretos» en los 90**: sacar disquetes, fotocopias o faxes de la gestoría y pasárselos a un periódico. Puede dar pistas y objetos para los Murdokus.

**Preguntas abiertas**:

- Título definitivo: ¿*Office Work*?

## La oficina por dentro (propuesta)

La Gestoría Lindero, en Logroño. **El mismo plano sirve para tres cosas**: como referencia del diseño, para dibujar la oficina en el juego y como plano de un Murdoku (por ejemplo, **un caso del arquitecto en la oficina**). Está en el juego en `game/office/office_map.json`, con el formato de los planos de los casos (8×8, con puertas), y se edita en la pestaña «Oficina» del editor.

```
 ┌──────────────┬──────────────┬─────────┐
 │ Despacho de  │ Despacho de  │ Archivo │
 │ Julián       │ Luis         │         │
 └──────────▯───┴▯─────────────┴──────▯──┘
   Pasillo (de lado a lado y baja junto a la oficina)
 ┌────────▯─────────────┐   ┌─────────┐
 │ Oficina              │   ▯ Cocina  │
 │ cuatro puestos:      │   ├─────────┤
 │ el tuyo y el de      │   ▯ Baño    │
 │ Rosario, uno junto   │   │         │
 │ al otro, y dos más   │ ┌─▯─────────┤
 │                      │ │ Recepción │
 │                      │ │ (Maruja)  │
 └──────────────────────┘ └────▯──────┘
                            entrada (▯ = puerta)
```

- **La oficina** (sala común): cuatro puestos de trabajo. El del contable y, al lado, el de Rosario, «la de las plantas», rodeada de ellas. Los otros dos, por decidir quién los ocupa.
- **Despacho de Luis**, el jefe; **despacho de Julián**, el fundador, que aún pasa por allí (y es donde muere: «en su despacho de la gestoría, a última hora, solo»). Tiene alfombra.
- **Archivo**: archivadores y la fotocopiadora. Es por donde saldrían los papeles al «vender secretos» (fotocopias, disquetes, fax).
- **Cocina**: la máquina de café («el café de la máquina es malo»).
- **Baño**: lavabo y váter.
- **Recepción**: el mostrador de Maruja y una silla de espera. Es la entrada desde la calle.
- **Pasillo**: une todas las habitaciones; cada una tiene una puerta.
- **Tomás no tiene mesa**: viene cuando se le llama.

Preguntas abiertas:

- ¿Quién se sienta en los otros dos puestos de la oficina?
- ¿Qué hace el mapa dentro del juego (moverse por la oficina, ir a hablar con alguien, ver quién está)? ¿Cómo encaja con que todo pase en la pantalla del ordenador?
- ¿Qué caso del arquitecto pasa en la oficina? ¿Y el del asesinato del contable o el de Tomás? El generador de casos llega de momento a 6×6; un caso en la oficina entera (8×8) necesita otro método, o usar solo una parte del plano.
- ¿Las puertas cambian las reglas del Murdoku (pistas como «estaba junto a la puerta», o habitaciones que solo se comunican por una puerta)?

## El Diario del Ebro: cómo se ve

Qué cuenta y cuándo llega: [historia.md](historia.md). Maqueta (diciembre de 1997): https://claude.ai/artifact/KgkBG1Jx4S8bP9fK9AqT2p

**Decidido** (18/11/2026):

- **La edición digital se inspira en la web de la CBC de finales de 1997** ([diciembre de 1997](https://web.archive.org/web/19971210160952/http://www.cbc.ca/)): ancho fijo y centrada, maquetada con tablas. Pero **más sencilla y menos profesional**: es la web de un periódico de provincias hecha en casa.
- **La portada lleva tres noticias, con bastante texto cada una**: titular, entradilla con el lugar y la fecha, y dos párrafos; alguna, con foto y pie de foto. Sin menú lateral, reloj ni noticia destacada.
- **La cabecera es sencilla, con un degradado mal hecho**: el nombre del periódico sobre un degradado con los escalones de color bien visibles, como hecho a mano. Las secciones van en una línea de enlaces debajo.
- **Un rótulo que va pasando**, como el de la versión de [noviembre de 1997](https://web.archive.org/web/19971121225751/http://www.cbc.ca/): un campo de texto de formulario en el que una frase corre de derecha a izquierda (allí lo hacía un JavaScript cada 200 ms).
- **El pie, como el de noviembre de 1997**: una raya, los enlaces a las secciones entre corchetes y separados por barras, otra raya, y el logo pequeño con «Copyright © 1997…».
- **Abajo del todo, la cartelera de cine** de esa semana, con los **cines que había abiertos en Logroño** en cada semestre y sus películas. Tiene la forma de la parrilla de programación de la CBC: una tabla con borde, las sesiones en filas y los cines en columnas.

**Propuesta** (por revisar), la de la maqueta:

- Cabecera: el nombre en amarillo, con una sombra negra demasiado separada, sobre un degradado de azul marino a verde en nueve franjas.
- Secciones: Portada, Logroño, La Rioja, España, Deportes, Cultura, El tiempo y Cartelera.
- El rótulo lleva la última hora; ahí puede colarse también la noticia que importa.
- La noticia que importa no va la primera, para que no se note: en la maqueta, la del medio (el embargo de los Domínguez por un préstamo de Créditos Altamira), entre la del euro y la del efecto 2000.

**Preguntas abiertas**:

- **Investigar qué cines había abiertos en Logroño** en cada semestre de 1996 a 1999, y qué películas se estrenaban en España en cada uno.
- ¿Cuál es la dirección de la web? En la maqueta, una provisional.

## Moneda

**Decidido**:

- **Primero pesetas, y más adelante se va metiendo el euro.**
- Facturas en pesetas, con el IVA español de la época (**16 %**) y el **NIF/CIF** de cada empresa.
- **Solo algunas empresas mandan sus facturas en euros**: las grandes o con negocios en el extranjero (por ejemplo, Promociones Torres, o quien mueve dinero a Suiza y Andorra). Que una empresa pague en euros es también una pista.
- **Las escrituras notariales vienen todas en las dos monedas.**

**Propuesta** (por revisar): el euro entra el **1 de enero de 1999** (como en la realidad, para la contabilidad).

**Preguntas abiertas**:

- ¿Qué empresas concretas facturan en euros, y desde cuándo?
