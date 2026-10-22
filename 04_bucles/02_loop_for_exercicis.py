###
# EXERCICIS (for)
###

# Exercici 1: Imprimir números parells
# Imprimeix tots els números parells del 2 al 20 (inclosos) fent servir un bucle for.

for i in range(2, 21, 2):
    print(i)

# Exercici 2: Calcular la mitjana d'una llista
# Donada la llista de números següent:
# numeros = [10, 20, 30, 40, 50]
# Calcula la mitjana dels números fent servir un bucle for.

numeros = [10, 20, 30, 40, 50]
suma = 0
for num in numeros:
    suma += num
mitjana = suma / len(numeros)
print(f"La mitjana dels números és: {mitjana}")

# Exercici 3: Buscar el màxim d'una llista
# Donada la llista de números següent:
# numeros = [15, 5, 25, 10, 20]
# Troba el número màxim de la llista fent servir un bucle for.

numeros = [15, 5, 25, 10, 20]
maxim = numeros[0]
for num in numeros:
    if num > maxim:
        maxim = num
print(f"El número màxim de la llista és: {maxim}")

# Exercici 4: Filtrar cadenes per longitud
# Donada la llista de paraules següent:
# paraules = ["casa", "arbre", "sol", "elefant", "lluna"]
# Crea una llista nova que contingui només les paraules amb més de 5 lletres
# fent servir un bucle for i list comprehension.

paraules = ["casa", "arbre", "sol", "elefant", "lluna"]
paraules_filtrades = [paraula for paraula in paraules if len(paraula) > 5]
print(f"Paraules amb més de 5 lletres: {paraules_filtrades}")

# Exercici 5: Comptar paraules que comencen per una lletra
# Donada la llista de paraules següent:
# paraules = ["casa", "arbre", "sol", "elefant", "lluna", "cotxe"]
# Demana a l'usuari que introdueixi una lletra.
# Compta quantes paraules de la llista comencen per aquesta lletra (sense diferenciar majúscules/minúscules).
paraules = ["casa", "arbre", "sol", "elefant", "lluna", "cotxe"]
lletra = input("Introdueix una lletra: ").lower()
comptador = 0
for paraula in paraules:
    if paraula.lower().startswith(lletra):
        comptador += 1
print(f"Nombre de paraules que comencen per '{lletra}': {comptador}")

# Exercici 6: Mesures de tensió d'un sensor
# Durant una prova s'han registrat les tensions següents (en volts):
# tensions = [4.8, 5.0, 5.1, 4.9, 5.2]
# Fent servir un bucle for, calcula la tensió mitjana i imprimeix-la.

tensions = [4.8, 5.0, 5.1, 4.9, 5.2]
suma_tensions = 0
for tensio in tensions:
    suma_tensions += tensio
tensio_mitjana = suma_tensions / len(tensions)
print(f"La tensió mitjana és: {tensio_mitjana} V")

# Exercici 7: Corrent en resistències
# En un circuit s'aplica una tensió de 12 V a aquestes resistències:
# resistencies = [100, 220, 470, 1000]
# Fent servir la llei d'Ohm (I = V / R) i un bucle for, calcula i imprimeix
# el corrent que circula per cada resistència, en ampers.

resistencies = [100, 220, 470, 1000]
tensio_aplicada = 12  # volts
for resistencia in resistencies:
    corrent = tensio_aplicada / resistencia
    print(f"Resistència: {resistencia} Ω, Corrent: {corrent:.4f} A")    

# Exercici 8: Mostres que superen el llindar de soroll
# Un receptor ha mesurat aquests nivells de soroll (en dBm):
# nivells_soroll = [-92, -85, -78, -95, -81, -88]
# Compta, amb un bucle for, quantes mostres superen el llindar de -80 dBm
# (és a dir, tenen un valor més gran que -80) i imprimeix el resultat.

nivells_soroll = [-92, -85, -78, -95, -81, -88]
llindar = -80
comptador_superiors = 0
for nivell in nivells_soroll:
    if nivell > llindar:
        comptador_superiors += 1
print(f"Nombre de mostres que superen el llindar de {llindar} dBm: {comptador_superiors}")

# Exercici 9: Càlcul de la taxa d'error de bits
# Compara els bits transmesos i rebuts:
# bits_transmesos = [1, 0, 1, 1, 0, 0, 1, 0]
# bits_rebuts =     [1, 0, 0, 1, 0, 1, 1, 0]
# Fent servir un bucle for i els índexs de les llistes, compta quants bits
# són diferents. Calcula i imprimeix la taxa d'error (bits diferents / total de bits).

bits_transmesos = [1, 0, 1, 1, 0, 0, 1, 0]
bits_rebuts = [1, 0, 0, 1, 0, 1, 1, 0]
diferents = 0
for i in range(len(bits_transmesos)):
    if bits_transmesos[i] != bits_rebuts[i]:
        diferents += 1
taxa_error = diferents / len(bits_transmesos)
print(f"Nombre de bits diferents: {diferents}")
print(f"Taxa d'error de bits: {taxa_error:.2%}")

# Exercici 10: Període d'un senyal
# Donades les freqüències següents, en hertzs:
# frequencies = [50, 100, 500, 1000]
# Fent servir un bucle for, calcula el període de cada senyal amb la fórmula
# T = 1 / f i imprimeix cada freqüència amb el seu període en segons.

frequencies = [50, 100, 500, 1000]
for f in frequencies:
    periode = 1 / f
    print(f"Freqüència: {f} Hz, Període: {periode:.6f} s")