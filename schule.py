import math

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


myVar = 0
primzahlen = []

while myVar <= 20:
    calc = pow(2, pow(2, myVar)) + 1
    if calc % calc == 0:
        primzahlen.append(myVar)
    else:
        print(calc + " ergibt keine Primzahl in der Berechnung")
    myVar += 1

print(primzahlen)