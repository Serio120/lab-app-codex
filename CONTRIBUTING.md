# Contribuir

El repositorio está en fase de definición y prototipo. Se priorizan cambios pequeños que mejoren la base técnica sin presentar funciones futuras como terminadas.

## Preparación

- Python 3.11 o superior.
- FFmpeg solo para probar `--render-preview`.

```bash
python -m venv .venv
python -m pip install -e ".[dev]"
python -m pytest
```

## Criterios para cambios

1. Mantener el núcleo independiente de proveedores externos.
2. No introducir claves, tokens ni datos personales en código, fixtures o logs.
3. Añadir pruebas para comportamiento nuevo y casos de error.
4. Actualizar README y documentación si cambia el alcance observable.
5. No afirmar que se genera vídeo, voz o imágenes reales si solo se crean datos de ejemplo.
6. Registrar licencias y procedencia de cualquier recurso de demostración.

## Flujo de trabajo

- Crear una rama descriptiva desde `main`.
- Mantener commits pequeños y con mensajes claros.
- Ejecutar `python -m pytest`.
- Abrir una Pull Request explicando alcance, pruebas y limitaciones.
- No fusionar sin revisión explícita del propietario.
