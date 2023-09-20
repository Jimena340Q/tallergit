"""
    Fecha: 20/09/2023
    Autor: Grupo 6
    Objetivo: Versionar código Python en Github. Se requiere un software que calcule si un aprendiz tiene el estilo de
    aprendizaje Asimilador. Para ello deben realizarse 7 preguntas de respuesta SI o NO. Si el aprendiz obtuvo 4 o más 
    respuestas en SI entonces el sistema deberá indicarle que es Asimilador, de lo contrario le dirá que su estilo de 
    aprendizaje es otro.
"""

print("Bienvenido aprendiz SENA, A continuacion te haremos unas preguntas con respuesta de seleccion(SI O NO), al finalizar aparecera tu resultado en pantalla, Empecemos...")

result = 0

option1 = int(input("Cuando aprendes algo nuevo, ¿prefieres que te presenten teorías o conceptos antes que ejemplos prácticos? \n 1.SI \n 2.NO \n")) 
while option1 != 1 and option1 != 2: 
    print("Respuesta incorrecta")
    option1 = int(input("Digite 1.SI O 2.NO \n"))
if option1 == 1:
    result += 1   
option2 = int(input("¿Te sientes más cómodo aprendiendo a través de la lectura de libros o materiales escritos? \n 1.SI \n 2.NO \n"))
while option2 != 1 and option2 != 2: 
    print("Respuesta incorrecta")
    option2 = int(input("Digite 1.SI O 2.NO \n"))
if option2 == 1:
    result += 1
option3 = int(input("¿Te sientes más cómodo aprendiendo a través de la lectura de libros o materiales escritos? \n 1.SI \n 2.NO \n"))
while option3 != 1 and option3 != 2: 
    print("Respuesta incorrecta")
    option3 = int(input("Digite 1.SI O 2.NO \n"))
if option3 == 1:
    result += 1
option4 = int(input("¿Te gusta analizar y reflexionar sobre las ideas y conceptos antes de ponerlos en práctica? \n 1.SI \n 2.NO \n"))
while option4 != 1 and option4 != 2: 
    print("Respuesta incorrecta")
    option4 = int(input("Digite 1.SI O 2.NO \n"))
if option4 == 1:
    result += 1
option5 = int(input("¿Tienes tendencia a destacar en asignaturas que requieren comprensión de teorías y conceptos, como las matemáticas o la física? \n 1.SI \n 2.NO \n")) 
while option5 != 1 and option5 != 2: 
    print("Respuesta incorrecta")
    option5 = int(input("Digite 1.SI O 2.NO \n"))
if option5 == 1:
    result += 1
option6 = int(input("¿Te sientes más cómodo en entornos de aprendizaje estructurados, como conferencias o clases magistrales? \n 1.SI \n 2.NO \n"))
while option6 != 1 and option6 != 2: 
    print("Respuesta incorrecta")
    option6 = int(input("Digite 1.SI O 2.NO \n"))
if option6 == 1:
    result += 1
option7 = int(input("¿Prefieres aprender de manera independiente en lugar de trabajar en grupos o equipos? \n 1.SI \n 2.NO \n"))
while option7 != 1 and option7 != 2: 
    print("Respuesta incorrecta")
    option7 = int(input("Digite 1.SI O 2.NO \n"))
if option7 == 1:
    result += 1

if result >= 4:
    print("Su estilo de aprendizaje es asimilador: ")
else:
    print("Su estilo de aprendizaje es otro")
