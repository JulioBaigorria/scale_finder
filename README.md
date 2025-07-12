# 🎵 Scale Finder

![Python](https://img.shields.io/badge/python-3.8+-blue?logo=python)
![License](https://img.shields.io/badge/license-MIT-green)
![GitHub stars](https://img.shields.io/github/stars/tuusuario/scale-finder?style=social)

**Herramienta para análisis armónico musical** que genera acordes válidos en diferentes escalas y modos. Ideal para compositores, arreglistas y estudiantes de teoría musical.

## 🚀 Características Principales
- **Búsqueda inteligente** de acordes por escala y nota raíz
- **Soporte para 3 escalas/modos**:
  - Menor Natural
  - Frigio
  - Armónica Menor
- **Base de datos con 1000+ acordes** incluyendo extensiones (7mas, 9nas, 11vas)
- **Salida en tablas ASCII** legibles
- **Tipado estático** para mayor confiabilidad

## 📦 Estructura del Proyecto
scale-finder/
├── data/
│ └── DATABASE.csv # Dataset de escalas y acordes
├── src/
│ ├── main.py # Lógica principal
│ └── utils.py # Se encuentra la funcion para formatear la respuesta en tabla
└── README.md

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