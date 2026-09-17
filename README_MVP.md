# Don Olé — MVP

Primera versión de una web educativa de español para niños, jóvenes y adultos, con niveles A1–C2.

## Incluye

- selección de edad y nivel;
- vocabulario práctico para una situación cotidiana;
- juego de preguntas con puntuación;
- diseño adaptable a móvil;
- pruebas para las vistas y la puntuación.

## Ejecutar en local

```bash
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Abre `http://127.0.0.1:8000/`.

## Ejecutar las pruebas

```bash
python manage.py test
```

## Próximos pasos

1. Convertir las lecciones en modelos editables desde el panel de administración.
2. Añadir cuentas y guardar el progreso.
3. Crear más tipos de juegos y contenido por edad.
4. Integrar IA para generar prácticas personalizadas con controles de seguridad.

## Publicar en Render

El repositorio incluye `render.yaml` y `build.sh`. En Render, crea un Blueprint,
conecta este repositorio y aplica la configuración detectada. Render generará la
clave secreta y publicará la web en una dirección `.onrender.com`.
