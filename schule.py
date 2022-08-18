import math
import sympy

print((3+7) / 2)
print(pow(2,1000))
powpow = pow(2,pow(3,2))
print(powpow)

pow_a = pow(2,3)
pow_b = pow(pow_a, 2)
print(pow_b)
print(pow(pow(2,3),2))

print(math.sqrt(49))

exaktes_ergebnis = 23 / 5
abgerundet = 23 // 5
rest = 23 % 5

print(exaktes_ergebnis)
print(abgerundet)
print(rest)

my_var = 10
my_var += 1
my_var -= 6
my_var *= 6
my_var /= 2
my_var *= my_var

print(my_var)

def primzahl_berechnung(number):
    primzahlen = []

    for item in range(number + 1):
        calc = pow(2, pow(2, item)) + 1
        if sympy.isprime(calc):
            primzahlen.append(item)
        else:
            print(item, " ergibt keine Primzahl in der Berechnung")

    print(primzahlen)

primzahl_berechnung(10)
