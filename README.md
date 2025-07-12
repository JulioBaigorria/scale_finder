# 🎵 Scale Finder

**¿Por qué este "proyecto"?**
La idea de Scale Finder es que dándole una **nota** y una **escala**, muestre 1 **acorde** random y válido por **nota** de la **escala**. Además cómo se compone dicho **acorde**.

Usando este sitio [All Guitar Chords](https://www.all-guitar-chords.com/chords/identifier) (héroes sin capa)
se puede ejercitar encontrar los acordes en el mástil.


## 🚀 Características Principales
- **Sin librerías de terceros** Solo nativas de python, nada de 3ros.
- **Búsqueda inteligente** Tampoco para taaanto...
- **Escalas Menor, Armónica y Frigia** La idea es que hayan más en el futuro!
- **Salida en tablas ASCII** Re linda
- **Tipado estático** Para parecer mas profesional(?)

## Ejemplo Entrada

En la raiz del proyecto, en la consola, escribir: 

`python main.py`

🎼 Enter musical parameters
Root note (C, C#, D, etc.):

Available Scales: {'frigia', 'armonica', 'menor'} (Dado una Root note, buscara las disponibles y sugerirá)

Scale name: menor

## Ejemplo Salida
╔════════════╦═══════╦════════════════════╗
║ Scale Note ║ Chord ║ Chord Notes        ║
╠════════════╬═══════╬════════════════════╣
║ E          ║ Em7   ║ E - G - B - D      ║
║ F#         ║ F#dim ║ F# - A - C         ║
║ G          ║ G     ║ G - B - D          ║
║ A          ║ Am7   ║ A - C - E - G      ║
║ B          ║ Bm7b5 ║ B - D - F# - A     ║
║ C          ║ C     ║ C - E - G          ║
║ D          ║ Dm9   ║ D - F# - A - C - E ║
╚════════════╩═══════╩════════════════════╝


## Sobre aporte y el software
Es público, de libre uso, clonalo y haz con él lo que quieras. Lo que importa es pensar en la comunidad.

## Si vas a agregar acordes, asegúrate de:
- **Respetar la estructura de datos del archivo CSV**
- **Agregar acordes válidos para la escala** El software escrito en el proyecto no puede validar si un acorde pertenece o no a una escala.
Por el momento es algo que se debe hacer a conciencia.

## Si vas a modificar el código, asegúrate de:
- **Respetar el tipado** Se puede mejorar
- **Mantenerlo simple** Se puede mejorar
