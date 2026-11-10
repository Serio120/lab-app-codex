# Video Studio

**Estado del proyecto: definición y prototipo técnico. No es todavía un producto terminado ni un MVP de producción.**

Video Studio es un proyecto en Python para explorar un flujo reproducible de preproducción y montaje de vídeos a partir de un brief. La intención es separar guion, escenas, recursos, audio, subtítulos y renderizado para poder incorporar proveedores reales más adelante.

## Alcance actual

La rama principal contiene una primera prueba técnica que permite:

- Crear un manifiesto JSON con un brief y tres escenas de ejemplo.
- Generar subtítulos SRT con tiempos provisionales calculados de forma uniforme.
- Validar y conservar una URL de YouTube como referencia declarativa.
- Crear una previsualización FFmpeg de tarjeta de título, si FFmpeg está instalado.

**Todavía no hace** investigación automática, generación de guiones mediante IA, generación de imágenes o clips, síntesis de voz, búsqueda de música ni sincronización de subtítulos con audio real. Los protocolos de `providers.py` son contratos de integración, no proveedores implementados.

## Preparar el entorno

Requiere Python 3.11 o superior.

```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows PowerShell
# .venv\Scripts\Activate.ps1

python -m pip install -e ".[dev]"
```

Crear un paquete de producción de ejemplo:

```bash
video-studio "un corto sobre una ciudad sostenible" --duration 60 --output productions/ciudad
```

El comando escribe `production.json` y `captions.srt`. La opción `--render-preview` genera únicamente una tarjeta de título de prueba con FFmpeg; no representa el montaje final previsto.

## Documentación del proyecto

- [Definición del proyecto](docs/PROJECT_BRIEF.md): problema, usuarios, objetivos, límites y criterios de aceptación.
- [Arquitectura](docs/ARCHITECTURE.md): componentes actuales y arquitectura objetivo.
- [Hoja de ruta](docs/ROADMAP.md): fases, entregables y estado.
- [Contribuir](CONTRIBUTING.md): entorno, pruebas y flujo de cambios.

## Estado y principios

El trabajo se encuentra en fase de definición y validación técnica. Las decisiones de producto y las integraciones externas se abordarán por fases; no se deben presentar como implementadas hasta que exista código y pruebas que lo demuestren.

Las referencias audiovisuales solo podrán utilizarse como orientación editorial de alto nivel. Los recursos finales deberán ser originales o contar con licencias y permisos adecuados. No se deben almacenar claves ni credenciales en el repositorio ni en los manifiestos generados.

## Desarrollo

```bash
python -m pytest
```

La integración continua ejecuta las pruebas en Python 3.11 y 3.12.
