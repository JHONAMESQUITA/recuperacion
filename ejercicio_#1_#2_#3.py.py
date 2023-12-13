#nombres de los desarrolladores
#David Esteban Pantiño
#Jhon Sleyder Amesquita

#ejercicio #1

import random
import math

N = 1000
A = []

for i in range(N):
    val = random.randint(0, 511)
    A.append(val)

P = max(A)
R = min(A)

print(f"Tensión máxima: {P} (V)")
print(f"Tensión mínima: {R} (V)")

z = sum(A)
w = z / 1000
print(f"Tensión promedio: {w} (V)")

#ejercicio #2

Mac = 511
Mic = 0
Mav = 6
miv = 0

z = miv
p = Mav / Mac

def Vrms_1():
    CD = []

    for l in range(len(A)):
        CD.append(A[l] ** 2)

    SC = 0

    for i in range(len(A)):
        SC = SC + CD[i]

    vrms = math.sqrt(SC / len(A))
    y = p + z
    o = vrms * y
    print(f"voltaje rms de la ecuacion 1: {o}")
    return o

#ejercicio #3

b = float(input("Ingrese el valor pico:"))

def ri(b):
    return b / math.sqrt(2)

print(f"Voltaje rms de la ecuacion 2: {ri(b)}")

def margen_de_error(o, b):
    margen = round(b / (o / math.sqrt(2)), 2)  # Redondea a 2 decimales
    print(f"Margen de error: {margen}%")

# Llamada a la función Vrms_1
resultado_Vrms = Vrms_1()

# Llamada a la función margen_de_error
margen_de_error(resultado_Vrms,b)



