###
# exercicis-basics.py
# Exercicis per practicar els conceptes apresos a les lliçons.
###

print("\nExercici 1: Imprimir missatges")
print("Escriu un programa que imprimeixi el teu nom i la teva ciutat en línies separades.")

### Completa aquí
print("Daniel Ortiz González\n Barcelona")

print("--------------")

print("\nExercici 2: Mostra els tipus de dades de les variables següents:")
print("Utilitza la comanda 'type()' per determinar el tipus de dades de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí
print(type(a), "\n", type(b), "\n", type(c), "\n", type(d), "\n", type(e))


print("--------------")

print("\nExercici 3: Conversió de tipus")
print("Converteix la cadena \"12345\" a un enter i després a un float.")
print("Converteix el float 3.99 a un enter. Què passa?")

### Completa aquí
a = 12345
b = 3.99

print(type(a), " = ", a)
d = float(a)
print(type(d), " = ", d)

c = int(b)
print(type(c), " = ", c)

print("--------------")

print("\nExercici 4: Variables")
print("Crea variables per al teu nom, edat i alçada.")
print("Utilitza f-strings per imprimir una presentació.")

# "Hola! Em dic Marc, tinc 38 anys i faig 1.75 metres"
#name = "Marc"
#age = 38

### Completa aquí
nom = "Daniel"
edat = 21
alt = 1.87

print(f"Hola! Em dic {nom}, tinc {edat} i alçada {alt}")

print("--------------")

print("\nExercici 5: Nombres")
print("1. Crea una variable amb el nombre PI (sense assignar una variable)")
print("2. Arrodoneix el nombre amb round()")
print("3. Fes la divisió entera entre el nombre resultant i el nombre 2")
print("4. El resultat hauria de ser 1")

### Completa aquí
pi = 3.14159
print(pi)
a = round(pi)
print(a)
div = int(pi / a)
print("Divisió: ", div)

print("--------------")

print("\nExercici 6: Conversor de temperatura")
print("Demana a l'usuari una temperatura en graus Celsius.")
print("Converteix aquest valor a Fahrenheit amb la fórmula: F = (C * 9/5) + 32")
print("Mostra els dos valors amb un missatge clar.")

### Completa aquí

print("Entra una temperatura en Celsius: ")
temp = input()
faren = (float(temp) * 9/5 + 32)
print(f"La temperatura en Fahrenheit es de {faren}")

print("--------------")

print("\nExercici 7: Calculadora de propina")
print("Demana el total d'un compte i el percentatge de propina.")
print("Calcula quant és la propina i el total final que s'ha de pagar.")
print("Mostra els resultats amb 2 decimals.")

### Completa aquí
print("Quina es la quantiat del compte?: ")
compte = input()
print("I la propina(en percentatge)?: ")
b = input()
c = float(compte)
d = float(b)

propina = (c * d)/100
total = c + propina

print(f"El compte surt per {total:.2f}")

print("--------------")

print("\nExercici 8: Validador de contrasenya simple")
print("Demana una contrasenya a l'usuari.")
print("Comprova si té almenys 8 caràcters.")
print("Mostra 'Contrasenya vàlida' o 'Contrasenya no vàlida'.")

### Completa aquí

print("Introdueix la teva contrasenya: ")
pas = input()

if(len(pas) < 8):

    print("Contrasenya no vàlida") 
else:
    
    print("Contrasenya vàlida")

