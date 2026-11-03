# Manual de usuario

1. Instale Python 3.10 o superior.
2. Abra una terminal en la carpeta del proyecto.
3. Ejecute `python app.py`.
4. Escriba el código del estudiante. El sistema responderá con el número de turno y las horas de inicio y fin.
5. No use el mismo código dos veces el mismo día: el programa rechazará duplicados.
6. Para terminar escriba `salir`.

Para probar el proyecto automáticamente ejecute `python -m unittest discover -s tests -v`.

**Limitación:** el almacenamiento es temporal en memoria; no se conservan asignaciones al cerrar el programa ni existe interfaz web. Este trabajo es una demostración de control de versiones, no un despliegue universitario en producción.
