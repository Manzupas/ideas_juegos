# Prototipo de Office Work (HTML y JavaScript)

Prototipo jugable del Murdoku del purgatorio: el ordenador del contable, con estética de Windows 98, en el que llegan los casos por correo. Todo está en un solo archivo, sin dependencias ni conexión a internet.

## Jugar en local

Abre **[office-work.html](office-work.html)** con doble clic (o arrástralo al navegador).

- Para que llegue el primer caso: abre GESTA 2000 y pulsa **Guardar** (o «Enviar y recibir» en el Correo).
- Cada caso siguiente llega por correo al resolver el anterior.
- Las facturas guardadas se conservan en el navegador; los casos resueltos y los correos, no (se empieza de cero al recargar).

También está publicado como artefacto para jugarlo desde el móvil: https://claude.ai/artifact/QgHxcBtNP4yLWGyQ3VYhcJ

## Archivos

| Archivo | Qué es |
|---------|--------|
| [index.html](index.html) | La fuente. Es lo que se edita y lo que se publica como artefacto (sin `<!doctype>` ni `<head>`, que los pone la plataforma). |
| [office-work.html](office-work.html) | La versión para jugar en local. Se genera a partir de `index.html`; no se edita a mano. |
| [scripts/empaquetar.py](scripts/empaquetar.py) | Genera `office-work.html`: `python3 -I scripts/empaquetar.py` desde esta carpeta. Hay que ejecutarlo después de cada cambio en `index.html`. |
| [scripts/caso.py](scripts/caso.py), [scripts/humano.py](scripts/humano.py) | Generaron el caso 0001. |
| [scripts/generar_caso.py](scripts/generar_caso.py) | Genera y comprueba un caso a partir de un JSON (`caso2.json`, `caso3.json`): solución única y resoluble solo con deducciones. Se ejecuta desde `scripts/`: `python3 -I generar_caso.py caso2.json`. |
| `scripts/casoN.salida.json` | Resultado del generador (solución, asesino y pistas) que se copió a `index.html`. |
