"""Demostración en consola de las asignaciones del almuerzo."""
from datetime import date
from turnos import SistemaTurnos, ErrorAsignacion


def main() -> None:
    sistema = SistemaTurnos(capacidad_por_turno=30)
    print("Sistema universitario de turnos de almuerzo")
    print("Fechas de hoy:", date.today().isoformat())
    print("Ingrese códigos de estudiante; escriba 'salir' para finalizar.")
    while True:
        codigo = input("Código: ").strip()
        if codigo.lower() == "salir":
            break
        try:
            turno = sistema.asignar(codigo)
            print(f"Turno {turno.numero}: {turno.inicio:%H:%M} - {turno.fin:%H:%M}")
        except ErrorAsignacion as exc:
            print(f"Error: {exc}")


if __name__ == "__main__":
    main()
