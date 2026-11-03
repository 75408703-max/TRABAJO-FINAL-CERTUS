# Sistema de gestión de turnos de almuerzo universitario

Proyecto académico DataOps. El sistema asigna estudiantes a **10 turnos consecutivos de 15 minutos entre 12:00 y 14:30**. Utiliza Git y un esquema de ramas de funcionalidad para controlar versiones.

## Características
- Asignación al turno disponible con menor ocupación, con desempate por hora de inicio.
- Validación del cupo máximo por turno.
- Impide una segunda asignación del mismo código en una misma fecha.
- Historial diario en memoria (sin persistencia en base de datos).

## Requisitos
Python 3.10 o superior. Sin dependencias externas.

## Ejecución rápida
```bash
python app.py
python -m unittest discover -s tests -v
```

## Ramas utilizadas
- `main`: versión integrada y estable.
- `feature/asignacion-turnos`: lógica de asignación.
- `feature/control-cupos`: cupos y duplicados.
- `feature/pruebas`: pruebas automáticas.

**Nota de alcance:** el ZIP adjunto incluye el historial Git real ejecutado localmente. No debe confundirse con un repositorio publicado en GitHub; los Pull Requests requieren publicarlo y realizarlos allí. Consulte `docs/PUBLICAR_EN_GITHUB.md`.
