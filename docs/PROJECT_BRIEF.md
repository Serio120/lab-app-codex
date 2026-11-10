# Definición del proyecto — Video Studio

- **Estado:** propuesta en definición + prototipo técnico inicial.
- **Versión de referencia:** 0.1.x.
- **Tipo:** herramienta local extensible, desarrollada en Python.
- **No es:** un servicio de generación de vídeo con IA listo para producción.

## 1. Visión

Explorar una herramienta que transforme un brief creativo en un paquete de producción organizado y reproducible. El paquete deberá separar decisiones editoriales, escenas, prompts, recursos audiovisuales, subtítulos y configuración de montaje.

La arquitectura debe permitir empezar con proveedores locales deterministas y, más adelante, integrar servicios externos sin acoplar el núcleo a una marca o API concreta.

## 2. Problema que se quiere resolver

Los flujos de creación audiovisual suelen dispersar brief, guion, referencias, recursos, voz, música y subtítulos en herramientas y archivos diferentes. El proyecto busca investigar si un manifiesto común y un pipeline por etapas pueden hacer el proceso más trazable, repetible y fácil de revisar.

## 3. Usuarios iniciales

- Creadores individuales que preparan vídeos cortos.
- Desarrolladores que quieran automatizar partes de un flujo audiovisual.
- Equipos pequeños que necesiten organizar briefs, escenas y recursos.

Estos perfiles son hipótesis iniciales; deberán validarse antes de ampliar el alcance.

## 4. Objetivos

1. Definir un modelo de datos estable para una producción y sus escenas.
2. Generar un paquete local reproducible a partir de un brief.
3. Mantener trazabilidad entre escena, prompt y recurso generado.
4. Permitir sustituir proveedores locales por proveedores externos mediante interfaces.
5. Construir un renderizador verificable que combine vídeo, voz, música y subtítulos.
6. Documentar límites, licencias, costes y requisitos de cada integración.

## 5. Fuera del alcance inicial

- Plataforma web multiusuario, cuentas, pagos o almacenamiento en la nube.
- Generación autónoma de vídeos de calidad comercial.
- Clonación de voces o imitación de personas reales.
- Descarga, copia o reutilización de vídeos protegidos como material de salida.
- Publicación automática en redes sociales.
- Prometer sincronización de subtítulos palabra a palabra sin alineación con audio real.

## 6. Flujo de usuario previsto

1. El usuario introduce un brief, duración aproximada, idioma y formato.
2. El sistema propone una estructura editorial y escenas.
3. El usuario revisa y aprueba el guion y la dirección visual.
4. Se generan o incorporan recursos para cada escena.
5. Se produce o importa voz y música con derechos adecuados.
6. El sistema alinea subtítulos con la pista de voz.
7. El renderizador monta una previsualización y exporta el resultado.
8. El paquete conserva manifiestos, fuentes y metadatos necesarios para reproducir el proceso.

La aprobación humana debe mantenerse en los pasos editoriales y antes de exportar o publicar.

## 7. Criterios de aceptación del primer MVP

El MVP se considerará alcanzado cuando:

- [ ] Un brief válido produzca un manifiesto estructurado y validado.
- [ ] El usuario pueda revisar y editar escenas antes de generar recursos.
- [ ] Cada recurso tenga identificador, escena asociada, proveedor, ruta y metadatos.
- [ ] Exista al menos un proveedor local determinista para visuales y audio de demostración.
- [ ] El renderizador pueda combinar varias escenas, voz, música y subtítulos en un archivo reproducible.
- [ ] Los subtítulos se basen en tiempos de audio o alineación, no en reparto uniforme ficticio.
- [ ] Los errores de entrada, recursos ausentes y fallos de FFmpeg se comuniquen claramente.
- [ ] Las pruebas cubran el flujo principal y los casos de error.
- [ ] CI ejecute las pruebas en las versiones de Python soportadas.
- [ ] La documentación describa con precisión las funciones reales y sus limitaciones.

## 8. Riesgos y decisiones pendientes

| Tema | Riesgo / pregunta | Tratamiento propuesto |
|---|---|---|
| Proveedores de IA | Coste, límites, disponibilidad y dependencia | Interfaces intercambiables; no elegir proveedor por adelantado |
| Audio y subtítulos | Duraciones artificiales o mala sincronización | Incorporar alineación basada en audio antes de declarar la función completa |
| FFmpeg | Diferencias de codecs y filtros entre sistemas | Pruebas de integración opcionales y diagnóstico de capacidades |
| Licencias | Uso no autorizado de imagen, música o referencias | Metadatos de procedencia y revisión humana |
| Reproducibilidad | Modelos y APIs pueden cambiar | Guardar versiones, parámetros y metadatos sin secretos |
| Alcance | Intentar construir todo a la vez | Entregas pequeñas con criterios de aceptación |

## 9. Decisiones que deben validarse

- Formatos de salida prioritarios (por ejemplo, 16:9 y 9:16).
- Duraciones objetivo y tipos de vídeo.
- Idiomas iniciales.
- Si la primera integración real será visual, voz o investigación.
- Proveedores compatibles y presupuesto máximo por producción.
- Sistema de edición manual del guion y las escenas.
