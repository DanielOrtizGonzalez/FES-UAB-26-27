###
# EXERCICIS (while)
###

# Exercici 1: Compte enrere
# Imprimeix els números del 10 a l'1 fent servir un bucle while.

i = 1

while(i <= 10):
    print(i)
    i = i + 1

# Exercici 2: Suma de números parells (while)
# Calcula la suma dels números parells entre 1 i 20 (inclosos) fent servir un bucle while.

i = 1
suma = 0

while(i <= 20):
    if(i % 2 == 0):
        suma = suma + i
    i = i + 1

print("La suma dels números parells entre 1 i 20 és:", suma)

# Exercici 3: Factorial d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Calcula el seu factorial fent servir un bucle while.
# El factorial d'un número enter positiu és el producte de tots els números de l'1 fins a aquest número. Per exemple, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.

num = int(input("Introdueix un número: "))
i = 0
factorial = 1
num2 = num

while(i < num - 1):
    i = i + 1
    factorial = num2 * factorial
    num2 = num2 - 1

print(f"El factorial de {num}! és: {factorial}\n")

# Exercici 4: Validació de contrasenya
# Demana a l'usuari que introdueixi una contrasenya.
# La contrasenya ha de tenir almenys 8 caràcters.
# Fes servir un bucle while per continuar demanant la contrasenya fins que compleixi els requisits.
# Si la contrasenya és vàlida, imprimeix "Contrasenya vàlida".

contrasenya = input("Introdueix una contrasenya: ")
while(len(contrasenya) < 8):
    print("La contrasenya ha de tenir almenys 8 caràcters.")
    contrasenya = input("Introdueix una contrasenya: ")
print("Contrasenya vàlida")

# Exercici 5: Taula de multiplicar
# Demana a l'usuari que introdueixi un número.
# Imprimeix la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle while.

num = int(input("Introdueix un número: "))
i = 1
while(i <= 10):
    print(f"{num} x {i} = {num * i}")
    i = i + 1

# Exercici 6: Números primers fins a N
# Demana a l'usuari que introdueixi un número enter positiu N.
# Imprimeix tots els números primers menors o iguals que N fent servir un bucle while.
# Un número és primer si només és divisible per 1 i per ell mateix.

num = int(input("Introdueix un número enter positiu: "))
i = 2
print(f"Números primers fins a {num}:")
while(i <= num):
    j = 2
    es_primer = True
    while(j < i):
        if(i % j == 0):
            es_primer = False
            break
        j = j + 1
    if(es_primer):
        print(i)
    i = i + 1

# Exercici 7: Suma fins al zero
# Demana a l'usuari que introdueixi números enters.
# Ves sumant els números introduïts fins que l'usuari introdueixi el 0.
# Al final, imprimeix la suma total. El 0 només serveix per acabar i no s'ha de sumar.

num = int(input("Introdueix un número (0 per acabar): "))
suma = 0
while(num != 0):
    suma = suma + num
    num = int(input("Introdueix un número (0 per acabar): "))
print(f"La suma total és: {suma}")

# Exercici 8: Comptar les xifres d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Comptabilitza quantes xifres té fent servir un bucle while.
# Finalment, imprimeix el nombre de xifres.

num = int(input("Introdueix un número enter positiu: "))
if(num == 0):
    print("El número té 1 xifra.")
else:
    xifres = 0
    while(num > 0):
        num = num // 10
        xifres = xifres + 1
    print(f"El número té {xifres} xifres.")

# Exercici 9: Seqüència de Fibonacci
# Demana a l'usuari quants termes de la seqüència de Fibonacci vol veure.
# Imprimeix aquest nombre de termes fent servir un bucle while.
# La seqüència comença per 0 i 1; cada terme següent és la suma dels dos anteriors.

num_terms = int(input("Quants termes de la seqüència de Fibonacci vols veure? "))
a, b = 0, 1
count = 0
while(count < num_terms):
    print(a)
    a, b = b, a + b
    count = count + 1

# Exercici 10: Joc d'endevinar el número
# El número secret és el 7.
# Demana a l'usuari que provi d'endevinar-lo i continua demanant números amb un bucle while
# fins que l'encerti.
# Després de cada intent incorrecte, indica si el número secret és més gran o més petit.

secret_number = 7
guess = int(input("Endevina el número secret (entre 1 i 10): "))
while(guess != secret_number):
    if(guess < secret_number):
        print("El número secret és més gran.")
    else:
        print("El número secret és més petit.")
    guess = int(input("Torna a provar: "))
print("Felicitats! Has endevinat el número secret.")