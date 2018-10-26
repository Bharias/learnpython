# Programa: 005_rectangulo.py
# Propósito: Calcula el perímetro y el área de un rectángulo a partir de su altura y anchura.
# Autor: Herbert Arias
# Fecha: 2018-10-24 10:01

# Petición de datos en metros.
altura = float(input('Dame la altura (en metros): '))
anchura = float(input('Dame la anchura (en metros): '))

# Cálculo de área y del perímetro
area = altura * anchura
perimetro = 2*altura + 2*anchura

# Impresión de resultados en pantalla.
print('El perímetro es de {0:6.2f} metros.'.format(perimetro))
print('El área es de {0:6.2f} metros cuadrados.'.format(area))
