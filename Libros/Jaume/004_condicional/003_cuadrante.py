from math import floor  # La función floor redondea hacia abajo

grados = float(input('Dame un ángulo (en grados): '))

cuadrante = floor(grados) % 360 // 90

if cuadrante == 0:
    print('primer cuadrante')
if cuadrante == 1:
    print('Segundo cuadrante')
if cuadrante == 2:
    print('Tercer cuadrante')
if cuadrante == 3:
    print('Cuarto cuadrante')
