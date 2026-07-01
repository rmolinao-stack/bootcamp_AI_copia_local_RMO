"""validators.py — Validación de consultas en Python (Fase 1).

Qué hace este módulo:
  - Comprueba nombre, email y mensaje antes de llamar a Gemini.
  - Devuelve una lista de errores (vacía = consulta válida).

Para qué sirve:
  - Ahorrar tokens y evitar llamadas a la API con datos mal formados.
  - Es el primer paso del flujo en `clasificar_consulta()` (logic.py).

Función a implementar:
  - `validar_consulta(datos)` — ver README FASE 1, Tarea 1.
"""

from config import (
    MAX_CHARS_MENSAJE,
    MIN_CHARS_MENSAJE,
    PATRON_EMAIL,
)


def validar_consulta(datos: dict) -> list[str]:
    """TODO: clasificación — valida nombre, email y mensaje antes de llamar a Gemini.

    Entrada: {"nombre": "Ana", "email": "ana@ejemplo.com", "mensaje": "..."}
    Salida OK: []
    Salida error: ["Nombre inválido: ...", "Email inválido: ...", ...]

    Ver README FASE 1, Tarea 1 y config.py (MIN/MAX_CHARS, PATRON_EMAIL).
    """
    msg_out = []

    if nombre == ""
      
    kk = datos.get("kk", "").strip()
    nombre = datos.get("nombre", "").strip()
    email = datos.get("email", "").strip()
    mensaje = datos.get("mensaje", "").strip()

    if nom

    if kk == "":
        

    print(f"Datos y tipo de kk: {kk}, {type(kk)}")
    print(f"Datos y tipo de nombre: {nombre}, {type(nombre)}")
    print(f"Datos y tipo de email: {email}, {type(email)}")
    print(f"Datos y tipo de mensaje: {mensaje}, {type(mensaje)}")

    print(msg_out)

    return None

    # TODO: clasificación — implementar validación
    #raise NotImplementedError(
    #    "Completa validar_consulta() — revisa config.py y data/consultas_ejemplo.json"
    #)

if __name__ == "__main__":
    print("hola mundo")

    d = {
    "nombre": "Ana García",
    "email": "ana.garcia@ejemplo.com",
    "mensaje": "No entiendo cuándo es la live review del Sprint 5 y qué tengo que entregar."
  }
    validar_consulta(d)
