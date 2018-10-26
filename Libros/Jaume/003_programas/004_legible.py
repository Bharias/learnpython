print('Programa para el cálculo del perímetro y el área de un rectángulo.')

altura = float(input('Dame la altura (en metros): '))
anchura = float(input('Dame la anchura (en metros): '))

area = altura * anchura
perimetro = 2*altura + 2*anchura

print('El perímetro es de {0:6.2f} metros.'.format(perimetro))
print('El área es de {0:6.2f} metros cuadrados.'.format(area))
