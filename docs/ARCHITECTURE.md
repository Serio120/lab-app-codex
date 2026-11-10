# Arquitectura — Video Studio

## Estado actual

La implementación actual es un prototipo pequeño y determinista. No contiene agentes LLM ni adaptadores reales de generación audiovisual.

| Módulo | Responsabilidad actual | Evolución prevista |
|---|---|---|
| `models.py` | Modelos `Production`, `Scene` y `WordCue`; exportación JSON | Añadir validación, recursos y metadatos tipados |
| `pipeline.py` | Crear tres escenas de ejemplo y cues provisionales | Orquestar etapas independientes y revisables |
| `reference.py` | Validar dominio y conservar URL | Añadir análisis permitido de metadatos y notas aportadas por el usuario |
| `providers.py` | Protocolos para visual, voz y música | Adaptadores locales y externos con contratos comprobables |
| `render.py` | Tarjeta de título FFmpeg de prueba | Montaje multi-escena, mezcla de audio y subtítulos |
| `cli.py` | Entrada por línea de comandos | Comandos por etapa, configuración y validación |

## Arquitectura objetivo

```text
Brief + configuración
        |
        v
Validación y modelo de producción
        |
        v
Plan editorial / escenas <---- revisión humana
        |
        v
Generación de recursos mediante providers
        |
        v
Manifiesto de assets + validación de archivos
        |
        v
Voz / música / alineación de subtítulos
        |
        v
Renderizador FFmpeg
        |
        v
Paquete exportable + informe de ejecución
```

## Principios

- **Núcleo independiente de proveedores:** el pipeline depende de protocolos, no de SDKs concretos.
- **Reproducibilidad:** guardar brief, configuración no sensible, versiones y metadatos de recursos.
- **Revisión humana:** el guion y la dirección se pueden revisar antes de gastar créditos o renderizar.
- **Seguridad:** secretos solo en variables de entorno o gestores de secretos; nunca en JSON, logs o commits.
- **Procedencia:** registrar origen y licencia de los recursos.
- **Fallos explícitos:** un recurso que falta no debe convertirse silenciosamente en un resultado aparentemente correcto.

## Contratos de datos por definir

Antes de integrar proveedores reales habrá que definir formalmente:

- Identificador estable de producción y escena.
- Relación entre escena y uno o varios assets.
- Tipo MIME, extensión, duración, dimensiones y tamaño del asset.
- Proveedor, modelo, versión, parámetros y fecha de generación.
- Estado de generación y error asociado.
- Procedencia, licencia y restricciones de uso.

## Límites actuales

- Los textos de escenas son plantillas, no contenido generado por IA.
- La investigación es una nota de revisión, no una búsqueda factual.
- Los cues de palabra reparten la duración total de forma uniforme y no representan sincronización real.
- La previsualización FFmpeg es una tarjeta de título, no una composición de escenas.
