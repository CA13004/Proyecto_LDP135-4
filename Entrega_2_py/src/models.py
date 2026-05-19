"""Módulo que contiene los modelos de datos y entidades de la plataforma."""

class Usuario:
    """Clase base para los usuarios del sistema."""
    def __init__(self, nombre: str):
        self.nombre = nombre

class Instructor(Usuario):
    """Representa a un instructor en la plataforma."""
    pass


class Estudiante(Usuario):
    """Representa a un estudiante en la plataforma."""
    def __init__(self, nombre: str):
        super().__init__(nombre)
        self.cursos_inscritos: list['Curso'] = []

    def inscribir_curso(self, curso: 'Curso') -> bool:
        """Agrega un curso a la lista de cursos inscritos del estudiante."""
        #Se evalúa y añade el objeto curso
        if any(c.id_curso == curso.id_curso for c in self.cursos_inscritos):
            return False
        self.cursos_inscritos.append(curso)
        return True
    
class Curso:
    """Representa un curso disponible en la plataforma."""
    def __init__(self, id_curso: int, nombre: str, instructor: Instructor):
        self.id_curso = id_curso
        self.nombre = nombre
        self.instructor = instructor
        self.estudiantes_inscritos: list[Estudiante] = []  #Para listar los estudiantes en el curso