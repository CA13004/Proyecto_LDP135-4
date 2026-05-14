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
        self.cursos_inscritos: list[str] = []

    def inscribir_curso(self, nombre_curso: str) -> bool:
        if nombre_curso in self.cursos_inscritos:
            return False
        self.cursos_inscritos.append(nombre_curso)
        return True

class Curso:
    """Representa un curso disponible en la plataforma."""
    def __init__(self, id_curso: int, nombre: str, instructor: Instructor):
        self.id_curso = id_curso
        self.nombre = nombre
        self.instructor = instructor