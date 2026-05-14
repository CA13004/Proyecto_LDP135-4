# Importa las clases de tus otros archivos si los separas
from models import Instructor, Estudiante
from managers import GestorCursos

class PlataformaCLI:
    """Clase principal que maneja la interfaz de línea de comandos y los menús."""
    def __init__(self):
        self.gestor = GestorCursos()
        self._inicializar_datos_prueba()

    def _inicializar_datos_prueba(self):
        """Datos semilla para no iniciar con la plataforma vacía."""
        self.gestor.crear_curso("Matematicas", Instructor("Ing. Herrera"))
        self.gestor.crear_curso("Programacion", Instructor("Ing. Erick"))
        self.gestor.crear_curso("Bases de Datos", Instructor("Ing. Albaluz"))

    def ejecutar(self):
        while True:
            print("\n--- BIENVENID@ a >> APPrende+ :) ---")
            print("1. Entrar como Instructor")
            print("2. Entrar como Estudiante")
            print("3. Salir del programa")
            
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self._menu_instructor()
            elif opcion == '2':
                self._menu_estudiante()
            elif opcion == '3':
                print("Saliendo de la plataforma. ¡Hasta pronto!")
                break
            else:
                print("⚠️ Opción inválida. Intente de nuevo.")

    def _menu_instructor(self):
        nombre = input("Ingrese su nombre: ")
        instructor = Instructor(nombre)

        while True:
            print(f"\n--- MENU INSTRUCTOR: {instructor.nombre} ---")
            print("1. Crear nuevo curso (Create)")
            print("2. Ver mis cursos (Read)")
            print("3. Editar nombre de un curso (Update)")
            print("4. Eliminar un curso (Delete)")
            print("5. Volver al inicio")
            
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                nombre_curso = input("Nombre del nuevo curso: ")
                self.gestor.crear_curso(nombre_curso, instructor)
                print(f"Curso '{nombre_curso}' creado con éxito.")
            
            elif opcion == '2':
                cursos = self.gestor.obtener_cursos_por_instructor(instructor.nombre)
                if not cursos:
                    print("No tienes cursos creados.")
                else:
                    print("Tus cursos:")
                    for c in cursos:
                        print(f"[{c.id_curso}] - {c.nombre}")
            
            elif opcion == '3':
                try:
                    id_curso = int(input("Ingrese el ID del curso a editar: "))
                    nuevo_nombre = input("Ingrese el nuevo nombre del curso: ")
                    if self.gestor.actualizar_curso(id_curso, nuevo_nombre, instructor.nombre):
                        print("Curso actualizado correctamente.")
                    else:
                        print("Error: No se encontró el curso o no tienes permisos para editarlo.")
                except ValueError:
                    print("Por favor, ingrese un número de ID válido.")
            
            elif opcion == '4':
                try:
                    id_curso = int(input("Ingrese el ID del curso a eliminar: "))
                    if self.gestor.eliminar_curso(id_curso, instructor.nombre):
                        print("Curso eliminado correctamente.")
                    else:
                        print("Error: No se encontró el curso o no tienes permisos para eliminarlo.")
                except ValueError:
                    print("Por favor, ingrese un número de ID válido.")
                    
            elif opcion == '5':
                break
            else:
                print("⚠️ Opción inválida.")

    def _menu_estudiante(self):
        nombre = input("Ingrese nombre del estudiante: ")
        estudiante = Estudiante(nombre)

        while True:
            print(f"\n--- MENU ESTUDIANTE: {estudiante.nombre} ---")
            print("1. Inscribir curso")
            print("2. Ver mis cursos inscritos")
            print("3. Volver al inicio")
            
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                cursos = self.gestor.obtener_todos_los_cursos()
                print("Cursos disponibles:")
                for c in cursos:
                    print(f"[{c.id_curso}] - {c.nombre} (Prof. {c.instructor.nombre})")
                
                try:
                    id_seleccionado = int(input("Ingrese el ID del curso: "))
                    curso_encontrado = next((c for c in cursos if c.id_curso == id_seleccionado), None)
                    
                    if curso_encontrado:
                        if estudiante.inscribir_curso(curso_encontrado.nombre):
                            print(f" Inscrito correctamente en: {curso_encontrado.nombre}")
                        else:
                            print(" Error: Ya estás inscrito en este curso.")
                    else:
                        print(" Selección inválida.")
                except ValueError:
                    print(" Por favor, ingrese un número de ID válido.")

            elif opcion == '2':
                if not estudiante.cursos_inscritos:
                    print("Aún no ha inscrito ningún curso.")
                else:
                    print("Tus cursos inscritos:")
                    for c in estudiante.cursos_inscritos:
                        print(f"- {c}")
            
            elif opcion == '3':
                break
            else:
                print("Opción inválida.")

if __name__ == "__main__":
    app = PlataformaCLI()
    app.ejecutar()