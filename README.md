<p align="center">
    <img src="assets/portada.png" alt="Portada APPprende" width="600"/>
</p>

Integrantes
- Liliana Melissa Cruz Henriquez - CH20014
- Gerson Antonio Chámul Ramirez - CR25082
- Mario Ernesto Cruz Alvarado - CA13004

APPrende+ : Plataforma de Gestión de Aprendizaje (LMS)
Bienvenido al repositorio de APPrende+, una solución conceptual de LMS desarrollada en pseudocódigo (PSeInt). Este proyecto simula las interacciones básicas entre instructores y estudiantes, permitiendo la gestión dinámica de cursos y registros de inscripción.
*************************************************************************
## 🏗️ Arquitectura de Datos

El sistema utiliza una estructura de almacenamiento basada en arreglos unidimensionales con una capacidad de 100 registros cada uno:

| Arreglo | Propósito |
| :--- | :--- |
| `cursosDisponibles` | Almacena los nombres de las materias activas. |
| `instructoresAsignados` | Vincula el nombre del instructor con el curso (indexación paralela)[cite: 1, 2]. |
| `inscripciones` | Registro temporal de cursos seleccionados por el estudiante en su sesión[cite: 1, 15]. |

---

## 🛠️ Lógica de los Módulos Principales

El algoritmo se divide en dos flujos de trabajo independientes controlados por un menú de roles[cite: 6, 25]:

### 1. Módulo del Instructor 👨‍🏫
Este módulo permite a los docentes gestionar la oferta académica mediante las siguientes funciones:
* **Creación Dinámica**: Los instructores pueden añadir nuevos cursos, los cuales se indexan automáticamente bajo su nombre de usuario[cite: 8, 11].
* **Persistencia Global**: Al crear un curso, el contador global `contadorCursos` se incrementa, haciendo que el contenido sea visible para todos los estudiantes inmediatamente[cite: 10, 11].
* **Filtro de Autoría**: El sistema recorre el arreglo global y filtra mediante una estructura `Si-Entonces` para mostrar únicamente los cursos creados por el instructor que tiene la sesión activa[cite: 13, 14].

### 2. Módulo del Estudiante 🎓
Diseñado para la consulta e inscripción de contenidos con validaciones integradas:
* **Catálogo en Tiempo Real**: El estudiante visualiza todos los cursos disponibles junto con el nombre del profesor asignado[cite: 20, 21].
* **Validación de Inscripción**: 
    * El sistema verifica que la opción seleccionada sea válida dentro del rango de cursos existentes[cite: 21].
    * Incluye un algoritmo de búsqueda para evitar **inscripciones duplicadas** en un mismo curso[cite: 22].
* **Gestión de Sesión**: Al ingresar un nuevo nombre de estudiante, el arreglo de `inscripciones` se limpia para permitir un registro independiente[cite: 15].

---

## 🚦 Flujo de Control y Algoritmos
* **Ciclos de Repetición**: Se utilizan estructuras `Repetir...Hasta Que` para mantener al usuario dentro de su módulo hasta que decida volver al menú principal o salir[cite: 7, 25].
* **Estructuras de Decisión**: Se implementan bloques `Segun` para la navegación de menús y `Si-Entonces` para las reglas de negocio (como el manejo de cursos vacíos o errores de selección)[cite: 5, 23].

---

## 🚀 Contribución para Desarrolladores

Si deseas aportar al repositorio, ten en cuenta:
1. **Manejo de Índices**: El sistema inicia el conteo de cursos en 5 (precargados)[cite: 1, 5].
2. **Validaciones**: Cualquier nueva funcionalidad debe incluir validaciones para evitar desbordamientos en los arreglos de tamaño 100.
3. **Modularización**: Se busca optimizar las búsquedas de "cursos repetidos" mediante funciones más eficientes.

---
*Desarrollado como prototipo educativo para la gestión de plataformas LMS.*
