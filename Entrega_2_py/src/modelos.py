class Persona:
    def __init__(self, carné, nombre): 
        self.carné = carné
        self.nombre = nombre

class Instructor(Persona):
    def __init__(self, carné, nombre, especialidad):
        super().__init__(carné, nombre)
        self.especialidad = especialidad

class Estudiante(Persona):
    def __init__(self, carné, nombre):
        super().__init__(carné, nombre)
        self.cursos_inscritos = []

class Curso:
    def __init__(self, nombre_curso, instructor):
        self.nombre_curso = nombre_curso
        self.instructor = instructor  #objeto Instructor
        self.estudiantes_inscritos = []