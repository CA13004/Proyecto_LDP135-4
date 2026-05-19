<p align="center">
    <img src="assets/portada2.png" alt="Portada APPprende" width="600"/>
</p>

Integrantes
- Liliana Melissa Cruz Henriquez - CH20014
- Gerson Antonio Chámul Ramirez - CR25082
- Mario Ernesto Cruz Alvarado - CA13004

APPrende+ : Plataforma de Gestión de Aprendizaje (LMS)
Bienvenido al repositorio de APPrende+, una solución conceptual de LMS desarrollada en pseudocódigo (PSeInt). Este proyecto simula las interacciones básicas entre instructores y estudiantes, permitiendo la gestión dinámica de cursos y registros de inscripción.
*************************************************************************
##  Arquitectura de Datos

El sistema utiliza una estructura de almacenamiento basada en arreglos unidimensionales con una capacidad de 100 registros cada uno:

| Arreglo  | Propósito |
| :---     | :---     |
| `cursosDisponibles` | Almacena los nombres de las materias activas. |
| `instructoresAsignados` | Vincula el nombre del instructor con el curso (indexación paralela). |
| `inscripciones` | Registro temporal de cursos seleccionados por el estudiante en su sesión. |

---

##  Lógica de los Módulos Principales

El algoritmo se divide en dos flujos de trabajo independientes controlados por un menú de roles:

### 1. Módulo del Instructor 
Este módulo permite a los docentes gestionar la oferta académica mediante las siguientes funciones:
* **Creación Dinámica**: Los instructores pueden añadir nuevos cursos, los cuales se indexan automáticamente bajo su nombre de usuario.
* **Persistencia Global**: Al crear un curso, el contador global `contadorCursos` se incrementa, haciendo que el contenido sea visible para todos los estudiantes inmediatamente.
* **Filtro de Autoría**: El sistema recorre el arreglo global y filtra mediante una estructura `Si-Entonces` para mostrar únicamente los cursos creados por el instructor que tiene la sesión activa.

### 2. Módulo del Estudiante 
Diseñado para la consulta e inscripción de contenidos con validaciones integradas:
* **Catálogo en Tiempo Real**: El estudiante visualiza todos los cursos disponibles junto con el nombre del profesor asignado.
* **Validación de Inscripción**: 
    * El sistema verifica que la opción seleccionada sea válida dentro del rango de cursos existentes.
    * Incluye un algoritmo de búsqueda para evitar **inscripciones duplicadas** en un mismo curso.
* **Gestión de Sesión**: Al ingresar un nuevo nombre de estudiante, el arreglo de `inscripciones` se limpia para permitir un registro independiente.

---

##  Flujo de Control y Algoritmos
* **Ciclos de Repetición**: Se utilizan estructuras `Repetir...Hasta Que` para mantener al usuario dentro de su módulo hasta que decida volver al menú principal o salir.
* **Estructuras de Decisión**: Se implementan bloques `Segun` para la navegación de menús y `Si-Entonces` para las reglas de negocio (como el manejo de cursos vacíos o errores de selección).

---

