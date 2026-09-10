# Video Studio

Un estudio de producción de vídeo en Python dirigido por agentes. Convierte una
instrucción en un paquete de producción reproducible: investigación editorial,
guion por escenas, prompts visuales originales, dirección de música, locución y
subtítulos palabra a palabra.

## Inicio rápido

```bash
python -m venv .venv && . .venv/bin/activate
pip install -e '.[dev]'
video-studio 'crea un corto animado sobre un plátano solitario que encuentra un amigo' --duration 60 --output productions/banana
```

El resultado contiene `production.json` (brief, investigación, escenas y
prompts) y `captions.srt`. Para validar el montaje local con FFmpeg, sin consumir
ninguna API, añade `--render-preview`.

```bash
video-studio 'anuncio cinematográfico para una interfaz neuronal' --reference-url https://youtu.be/VIDEO_ID --render-preview
```

## Flujo y límites creativos

`Studio` coordina las etapas de investigación, guion, dirección visual, voz,
música, subtitulado y ensamblaje. Los protocolos de `providers.py` son el punto
de integración para proveedores de LLM, imagen/vídeo, TTS y catálogos de música
con licencia. Las claves deben estar en variables de entorno; no se escriben en
los manifiestos.

Un enlace de YouTube se trata únicamente como referencia de ritmo y observaciones
editoriales de alto nivel. El sistema no descarga ni copia el audiovisual, guion,
voz o música de la referencia: los recursos del resultado deben ser originales y
con licencia apropiada. Revise los datos investigados, licencias musicales y
derechos de marca antes de publicar.

## Desarrollo

```bash
pytest
```
