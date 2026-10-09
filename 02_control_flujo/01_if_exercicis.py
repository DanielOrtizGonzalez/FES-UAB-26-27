###
# EXERCICIS
###

# Exercici 1: Qualitat del senyal Wi-Fi
# Demana el nivell de senyal rebut (RSSI) en dBm i classifica la cobertura:
# - -50 dBm o superior: excel·lent
# - Entre -67 dBm i menys de -50 dBm: bona
# - Entre -75 dBm i menys de -67 dBm: feble
# - Inferior a -75 dBm: molt feble

rssi = float(input("Introdueix el nivell de senyal Wi-Fi en dBm: "))

if rssi >= -50:
    print("La cobertura Wi-Fi és excel·lent.\n")
elif -67 <= rssi < -50:
    print("La cobertura Wi-Fi és bona.\n")
elif -75 <= rssi < -67:
    print("La cobertura Wi-Fi és feble.\n")
else:
    print("La cobertura Wi-Fi és molt feble.\n")


# Exercici 2: Nivell de recepció d'una connexió de fibra òptica
# Demana la potència òptica rebuda en dBm. Per a aquest exercici, considera
# acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
# Indica si el nivell és massa baix, acceptable o massa alt.

potencia = float(input("Introdueix la potència òptica rebuda en dBm: "))

if potencia >= -27 or potencia <= -8:
    print("El nivell de recepció és acceptable.\n")
else:
    print("El nivell de recepció no és acceptable.\n")

# Exercici 3: Consum mensual de dades mòbils
# Demana el consum de dades en GB d'una línia mòbil. El pla inclou 20 GB.
# Indica si el consum és dins del límit o si l'ha superat; en aquest últim cas,
# calcula quants GB addicionals s'han consumit.

gb = float(input("Introdueix el consum de dades mòbils en GB:"))

if gb <= 20:
    print("Ell consum de dades està dins del límit del pla.\n")
else:
    excedent = gb - 20
    print(f"Has superat el límit del pla per {excedent}\n")

# Exercici 4: Diagnòstic d'una connexió de fibra
# Demana si l'indicador LOS del terminal òptic està encès i si l'indicador
# d'Internet del router està encès. Segons aquestes dues dades, indica si cal
# revisar el cable de fibra, comprovar el servei del proveïdor o si la connexió
# sembla funcionar correctament.

los = input("L'indicador LOS del terminal òptic està encès? (sí/no): ")

if los.lower() == "sí":
    print("Cal revisar el cable de fibra.\n")
else:
    router = input("L'indicador del router està encès? (sí/no): ")
    if router.lower() == "sí" or router.lower() == "si":
        print("Cal comprovar el servei del proveïdor\n")
    else:
        print("La connexió sembla funcionar correctament\n")

# Demana el percentatge de bateria disponible al SAI que alimenta un armari
# de comunicacions. Indica si el nivell és crític (menys del 20 %), baix
# (del 20 % al 49 %) o suficient (50 % o més). Rebutja valors fora del rang
# del 0 % al 100 %.

sai = int(input("Quin es el percentatge de la bateria del SAI? (0% al 100%): "))

if  0 > sai > 100:
    while(0 > sai > 100):
        sai = int(input("Quin es el percentatge de la bateria del SAI? (0% al 100%): "))


if sai < 20:
    print("Nivell crític de bateria\n")
elif sai >= 20 or sai < 49:
    print("Nivell baix de bateria\n")
else:
    print("Nivell suficient de bateria\n")