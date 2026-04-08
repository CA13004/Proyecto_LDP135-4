Algoritmo PlataformaCursos_Completo
    // 1. Declaración de variables 
    Definir estudiante, curso, instructorNombre, instructorEspecialidad Como Cadena
    Definir cursosDisponibles, instructoresAsignados Como Cadena 
    Definir inscripciones Como Cadena
    
    Dimension cursosDisponibles[100], instructoresAsignados[100], inscripciones[100]
    
    Definir contadorInscripciones, contadorCursos, menuRol, menuAccion, cursoSeleccionado Como Entero
    Definir repetido Como Logico
    
    // 2. INICIALIZACIÓN
    // Cursos base
    cursosDisponibles[1] <- "Matematicas"; instructoresAsignados[1] <- "Ing. Herrera"
    cursosDisponibles[2] <- "Programacion"; instructoresAsignados[2] <- "Ing. Erick"
    cursosDisponibles[3] <- "Bases de Datos"; instructoresAsignados[3] <- "Ing Albaluz"
    cursosDisponibles[4] <- "Ingles"; instructoresAsignados[4] <- "Lic. Angelica"
    cursosDisponibles[5] <- "Redes"; instructoresAsignados[5] <- "Msc. Walter"
    
    contadorCursos <- 5
    contadorInscripciones <- 0 // Empezar en 0 
    
    // 3. SELECCIÓN DE ROL
    Repetir
        Escribir "--- BIENVENIDO A LA PLATAFORMA ---"
        Escribir "1. Entrar como Instructor"
        Escribir "2. Entrar como Estudiante"
        Escribir "3. Salir del programa"
        Leer menuRol
        
        Segun menuRol Hacer
            1: // LÓGICA DE INSTRUCTOR
                Escribir "Ingrese su nombre:"
                Leer instructorNombre
                Escribir "Ingrese su especialidad:"
                Leer instructorEspecialidad
                
                Repetir
                    Escribir "--- MENU INSTRUCTOR: ", instructorNombre, " ---"
                    Escribir "1. Crear nuevo curso"
                    Escribir "2. Ver mis cursos creados"
                    Escribir "3. Volver al inicio"
                    Leer menuAccion
                    
                    Si menuAccion = 1 Entonces
                        contadorCursos <- contadorCursos + 1
                        Escribir "Nombre del nuevo curso:"
                        Leer cursosDisponibles[contadorCursos]
                        instructoresAsignados[contadorCursos] <- instructorNombre
						Escribir "Curso " Sin Saltar
						Escribir cursosDisponibles[contadorCursos] Sin Saltar
						Escribir " creado con éxito."
                    FinSi
                    
                    Si menuAccion = 2 Entonces
                        Escribir "Cursos creados por usted:"
                        Para i <- 1 Hasta contadorCursos Hacer
                            Si instructoresAsignados[i] = instructorNombre Entonces
                                Escribir "- ", cursosDisponibles[i]
                            FinSi
                        FinPara
                    FinSi
                Hasta Que menuAccion = 3
                
            2: // LÓGICA DE ESTUDIANTE
                Escribir "Ingrese nombre del estudiante:"
                Leer estudiante
                Repetir
                    Escribir "--- MENU ESTUDIANTE: ", estudiante, " ---"
                    Escribir "1. Inscribir curso"
                    Escribir "2. Ver mis cursos inscritos"
                    Escribir "3. Volver al inicio"
                    Leer menuAccion
                    
                    Segun menuAccion Hacer
                        1:
                            Escribir "Cursos disponibles (y su instructor):"
                            Para i <- 1 Hasta contadorCursos Hacer
                                Escribir i, ". ", cursosDisponibles[i], " [Prof. ", instructoresAsignados[i], "]"
                            FinPara
                            Leer cursoSeleccionado
                            curso <- cursosDisponibles[cursoSeleccionado]
                            
							Si contadorInscripciones > 0 Entonces
								Para i <- 1 Hasta contadorInscripciones Hacer
									Si inscripciones[i] = curso Entonces
										repetido <- Verdadero
									FinSi
								FinPara
							FinSi
						
                            Si repetido Entonces
                                Escribir "Error: Ya estás inscrito en este curso."
                            Sino
                                contadorInscripciones <- contadorInscripciones + 1
                                inscripciones[contadorInscripciones] <- curso
                                Escribir "Inscrito correctamente en: ", curso
                            FinSi
                        2:
                            Escribir "Tus cursos:"
                            Para i <- 1 Hasta contadorInscripciones Hacer
                                Escribir "- ", inscripciones[i]
                            FinPara
                    FinSegun
                Hasta Que menuAccion = 3
        FinSegun
    Hasta Que menuRol = 3
FinAlgoritmo
