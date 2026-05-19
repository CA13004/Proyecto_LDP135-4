"""Módulo que contiene la lógica de negocio y gestión de datos de la plataforma."""

from models import Curso, Instructor
class GestorCursos:
    """Maneja el CRUD de los cursos y la lógica de negocio central."""
    def __init__(self):
        self.cursos: list[Curso] = []
        self._contador_id = 1

   # --- C (CREATE) ---
    def crear_curso(self, nombre: str, instructor: Instructor) -> Curso:
        """Crea un nuevo curso, lo registra en el sistema y retorna el objeto creado."""
        nuevo_curso = Curso(self._contador_id, nombre, instructor)
        self.cursos.append(nuevo_curso)
        self._contador_id += 1
        return nuevo_curso

    # --- R (READ) ---
    def obtener_cursos_por_instructor(self, nombre_instructor: str) -> list[Curso]:
        """Devuelve una lista con todos los cursos impartidos por un instructor específico."""
        return [c for c in self.cursos if c.instructor.nombre.lower() == nombre_instructor.lower()]

    def obtener_todos_los_cursos(self) -> list[Curso]:
        """Devuelve la lista completa de todos los cursos registrados."""
        return self.cursos

# --- U (UPDATE) ---
    def actualizar_curso(self, id_curso: int, nuevo_nombre: str, nombre_instructor: str) -> bool:
        """Actualiza el nombre de un curso si el ID y el nombre del instructor coinciden."""
        for curso in self.cursos:
            # Dividimos el 'if' largo usando paréntesis:
            if (curso.id_curso == id_curso and
                curso.instructor.nombre.lower() == nombre_instructor.lower()):
                curso.nombre = nuevo_nombre
                return True
        return False

    # --- D (DELETE) ---
    def eliminar_curso(self, id_curso: int, nombre_instructor: str) -> bool:
        """Elimina un curso del sistema si el ID y el nombre del instructor coinciden."""
        for curso in self.cursos:
            # Dividimos el 'if' largo usando paréntesis:
            if (curso.id_curso == id_curso and
                curso.instructor.nombre.lower() == nombre_instructor.lower()):
                self.cursos.remove(curso)
                return True
        return False
