###
# Exercicis - input()
# Practica l'entrada de dades i la conversió de tipus amb exemples de telecomunicacions.
###

# Exercici 1
# Demana el nom d'un tècnic i el nom de la xarxa que està instal·lant.
# Després, mostra un missatge amb aquesta informació.

nom = input("Nom del tècnic: ")
xarxa = input("Nom de la xarxa: ")

print(f"El nom del tècnic es, {nom} i el nom de la xarxa és, {xarxa}")

# Exercici 2
# Demana la longitud d'un enllaç de fibra en quilòmetres i la velocitat de transmissió
# en Gbps. Mostra quants segons caldrien per transmetre 1 GB de dades.
# Suposa que 1 GB = 8 Gb i que la velocitat es manté constant.



# Exercici 3
# Demana el nombre d'hores de feina i el preu per hora d'una instal·lació de xarxa.
# Demana també el preu del material.
# Mostra el cost total de la instal·lació.

hores = input("Nombre d'hores: ")
preu_hora = input("Preu per hora: ")
preu = input("Preu material: ")

hores_feina = hores * preu_hora

print(F"El cost total de la instal·lació és de {hores_feina + preu} ")