# Buscaminas (título provisional)

| Ficha | |
|-------|---|
| Estado | movida |
| Plataforma candidata | Game Boy |
| Origen | Prototipo antiguo en Unity: `Minesweeper`. Su código se borró al limpiar la bandeja de entrada |
| Año | Por apuntar |

Un buscaminas clásico. Del prototipo de Unity gustaron mucho **el algoritmo de generación de mapas** y **el de resolución**, que estaban en su `GameManager.cs` (unos 38 KB).

Ya se desarrolla en el repo [gameboy](https://github.com/Manzupas/gameboy). La especificación (tablero de 9×9 con 10 minas, controles y menús) está en la rama [buscaminas/plan](https://github.com/Manzupas/gameboy/blob/buscaminas/plan/juegos/buscaminas/diseno.md), todavía sin juntar con `main`.

**Ojo**: esa especificación deja los algoritmos pendientes «de los de Unity del usuario», y ese código ya no está. Si aparece otra copia del prototipo, hay que llevar su `GameManager.cs` al repo gameboy. Si no, habrá que decidir los algoritmos de nuevo.
