# Buscaminas (título provisional)

| Ficha | |
|-------|---|
| Estado | movida |
| Plataforma candidata | Game Boy |
| Origen | Prototipo antiguo en Unity: `Minesweeper`. Su código se borró al limpiar la bandeja de entrada |
| Año | Por apuntar |

Un buscaminas clásico. Del prototipo de Unity gustaron mucho **el algoritmo de generación de mapas** y **el de resolución**, que estaban en su `GameManager.cs` (unos 38 KB).

Ya se desarrolla en el repo [gameboy](https://github.com/Manzupas/gameboy): [juegos/buscaminas/](https://github.com/Manzupas/gameboy/tree/main/juegos/buscaminas). Es un tablero de 9×9 con 10 minas, una estética de homenaje al Buscaminas de Windows 98 y un modo campaña de 30 niveles.

El código de Unity no apareció, así que el 4 de noviembre de 2026 se decidieron algoritmos nuevos: las minas se colocan en el primer destape, ese primer destape es seguro y no se garantizan tableros que se resuelvan sin adivinar.
