# Historial de evolución

Este archivo registra la evolución funcional del proyecto desde su creación. Se
añaden entradas a cada cambio visible para que el estado del producto sea
auditable sin depender del historial de Git.

## [0.2.0] - 2026-09-10

### Añadido
- Primer *vertical slice* de producción: generación local y reproducible de un
  asset visual SVG por escena, una pista de voz WAV y una cama musical WAV.
- Manifiesto de assets (`assets.json`) que enlaza los recursos producidos con su
  escena, proveedor y prompt, listo para ser sustituido por proveedores cloud.
- Flag de CLI `--generate-assets` para producir el paquete completo sin claves
  de API ni consumo de créditos.
- Pruebas para la generación local y la escritura del manifiesto de assets.

## [0.1.0] - 2026-09-10

### Añadido
- Creación inicial de Video Studio como proyecto Python.
- Pipeline que convierte un brief en un manifiesto de producción con
  investigación editorial, tres escenas, narración y cues palabra a palabra.
- Exportación de `production.json` y subtítulos `captions.srt`.
- CLI inicial, contratos para proveedores de visuales, voz y música, y preview
  de FFmpeg sin APIs externas.
- Referencias de YouTube limitadas a orientación editorial de alto nivel y a la
  creación de contenido original.
