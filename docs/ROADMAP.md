# Hoja de ruta

Los estados describen el código disponible en el repositorio, no una estimación de fechas.

## Fase 0 — Definición del proyecto
<badge>En curso</badge>

- [x] Documentar visión, usuarios hipotéticos y alcance inicial.
- [x] Separar funciones existentes de capacidades futuras.
- [x] Definir criterios de aceptación del MVP.
- [ ] Validar formatos, idiomas, duración y caso de uso prioritario.

## Fase 1 — Base técnica local
<badge>En curso</badge>

- [x] CLI y paquete Python instalable.
- [x] Manifiesto JSON básico.
- [x] Exportación SRT provisional.
- [x] Primera prueba de renderizado FFmpeg como tarjeta de título.
- [x] Pruebas unitarias iniciales y CI.
- [ ] Esquema validado para producción, escenas y assets.
- [ ] Proveedor local determinista de recursos visuales y audio.
- [ ] Gestión de errores y estado de cada etapa.

## Fase 2 — Flujo de preproducción
<badge color="secondary">Planificada</badge>

- [ ] Brief configurable: idioma, formato, audiencia y duración.
- [ ] Propuesta de estructura y escenas editable.
- [ ] Persistencia de revisiones y aprobaciones.
- [ ] Investigación con fuentes y trazabilidad, si se confirma como requisito.

## Fase 3 — Recursos y montaje
<badge color="secondary">Planificada</badge>

- [ ] Manifiesto de assets y proveedores locales.
- [ ] Adaptadores opcionales para servicios externos.
- [ ] Alineación de subtítulos basada en voz real.
- [ ] Render multi-escena con mezcla de audio.
- [ ] Pruebas de integración FFmpeg.

## Fase 4 — Calidad y distribución
<badge color="secondary">Futura</badge>

- [ ] Perfiles de exportación 16:9 y 9:16.
- [ ] Informes de costes, licencias y procedencia.
- [ ] Documentación de instalación multiplataforma.
- [ ] Evaluación con producciones reales y criterios de calidad.

## Regla de avance

No se marcará una tarea como terminada por estar documentada o diseñada. Debe existir implementación verificable y, cuando corresponda, pruebas automatizadas.
