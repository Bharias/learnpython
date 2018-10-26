from turtle import Screen, Turtle

# Calificaciones
suspensos = 10
aprobados = 20
notables = 40
sobresalientes = 30

# Radio del circulo
radio = 300

# Inicializacion
pantalla = Screen()
tortuga = Turtle()
tortuga.speed(0)

# Dibujo del circulo exterior
tortuga.penup()
tortuga.goto(0, -radio)
tortuga.pendown()
tortuga.circle(radio)
tortuga.penup()
tortuga.home()
tortuga.pendown()

# Dibujo de la linea para los suspensos
angulo = 360 * suspensos / 100
tortuga.left(angulo)
tortuga.forward(radio)
tortuga.backward(radio)

# Escribir el texto para los suspensos
tortuga.penup()
tortuga.right(angulo / 2)
tortuga.forward(radio / 2)
tortuga.write('suspensos')
tortuga.backward(radio / 2)
tortuga.left(angulo / 2)
tortuga.pendown()

# Dibujo de la linea para los aprobados
angulo = 360 * aprobados / 100
tortuga.left(angulo)
tortuga.forward(radio)
tortuga.backward(radio)

# Escribir el texto para los aprobados
tortuga.penup()
tortuga.right(angulo / 2)
tortuga.forward(radio / 2)
tortuga.write('aprobados')
tortuga.backward(radio / 2)
tortuga.left(angulo / 2)
tortuga.pendown()

# Dibujo de la linea para los notables
angulo = 360 * notables / 100
tortuga.left(angulo)
tortuga.forward(radio)
tortuga.backward(radio)

# Escribir el texto para los notables
tortuga.penup()
tortuga.right(angulo / 2)
tortuga.forward(radio / 2)
tortuga.write('notables')
tortuga.backward(radio / 2)
tortuga.left(angulo / 2)
tortuga.pendown()

# Dibujo de la linea para los sobresalientes
angulo = 360 * sobresalientes / 100
tortuga.left(angulo)
tortuga.forward(radio)
tortuga.backward(radio)

# Escribir el texto para los sobresalientes
tortuga.penup()
tortuga.right(angulo / 2)
tortuga.forward(radio / 2)
tortuga.write('sobresalientes')
tortuga.backward(radio / 2)
tortuga.left(angulo / 2)
tortuga.pendown()

# Ocultar la tortuga
tortuga.hideturtle()

# Salir cuando se pulse el boton en la ventana
pantalla.exitonclick()
