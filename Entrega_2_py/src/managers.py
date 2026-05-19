"""Módulo que contiene la lógica de negocio y gestión de datos de la plataforma."""

from models import Curso, Instructor, Estudiante

class GestorCursos:
    """Maneja el CRUD de los cursos y la lógica de negocio central."""
    def __init__(self):
        self.cursos: list[Curso] = []
        self.estudiantes: list[Estudiante] = []
        self._contador_id = 1

   # --- C (CREATE) ---
    def crear_curso(self, nombre: str, instructor: Instructor) -> Curso:
        """Crea un nuevo curso, lo registra en el sistema y retorna el objeto creado."""
        nuevo_curso = Curso(self._contador_id, nombre, instructor)
        self.cursos.append(nuevo_curso)
        self._contador_id += 1
        return nuevo_curso
    
    def obtener_o_crear_estudiante(self, nombre: str) -> Estudiante:
        """Busca un estudiante por nombre para no duplicarlo, si no existe lo crea."""
        nombre_normalizado = nombre.strip().lower()
        for est in self.estudiantes:
            if est.nombre.lower() == nombre_normalizado:
                return est
        nuevo_estudiante = Estudiante(nombre)
        self.estudiantes.append(nuevo_estudiante)
        return nuevo_estudiante
    
    def inscribir_estudiante_en_curso(self, estudiante: Estudiante, id_curso: int) -> bool:
        """Inscribe al alumno en el curso y establece una relación entre ambos objetos."""
        curso = next((c for c in self.cursos if c.id_curso == id_curso), None)
        if curso:
            # Intentar inscribir en el modelo del estudiante
            if estudiante.inscribir_curso(curso):
                # Si se logra, lo agregamos también a la lista del curso
                curso.estudiantes_inscritos.append(estudiante)
                return True
        return False

    # --- R (READ) ---
    def obtener_cursos_por_instructor(self, nombre_instructor: str) -> list[Curso]:
        """Devuelve una lista con todos los cursos impartidos por un instructor específico."""
        #Búsqueda más flexible que acepte "Erick" o "Ing. Erick" por igual
        nombre_limpio = nombre_instructor.strip().lower()
        return [c for c in self.cursos if nombre_limpio in c.instructor.nombre.lower()]

    def obtener_todos_los_cursos(self) -> list[Curso]:
        """Devuelve la lista completa de todos los cursos registrados."""
        return self.cursos
    
    def obtener_estudiantes_de_curso(self, id_curso: int) -> list[Estudiante]:
        """Devuelve los estudiantes de un curso específico."""
        curso = next((c for c in self.cursos if c.id_curso == id_curso), None)
        return curso.estudiantes_inscritos if curso else []

# --- U (UPDATE) ---
    def actualizar_curso(self, id_curso: int, nuevo_nombre: str, nombre_instructor: str) -> bool:
        """Actualiza el nombre de un curso si el ID y el nombre del instructor coinciden."""
        nombre_limpio = nombre_instructor.strip().lower()
        for curso in self.cursos:
            if curso.id_curso == id_curso and nombre_limpio in curso.instructor.nombre.lower():
                curso.nombre = nuevo_nombre
                return True
        return False

    # --- D (DELETE) ---
    def eliminar_curso(self, id_curso: int, nombre_instructor: str) -> bool:
        """Elimina un curso del sistema si el ID y el nombre del instructor coinciden."""
        nombre_limpio = nombre_instructor.strip().lower()
        for curso in self.cursos:
            if curso.id_curso == id_curso and nombre_limpio in curso.instructor.nombre.lower():
                self.cursos.remove(curso)
                return True
        return False