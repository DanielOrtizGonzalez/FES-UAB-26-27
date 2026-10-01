###
# 02 - types()
# Python té diversos tipus de dades
# int, float, complex, str, bool, NoneType, list, tuple, dict, range, set...
###

print("int:")  # Enters (números sense part decimal)
print(type(10))  # Nombre enter positiu
print(type(0))  # El número zero també és un enter
print(type(-5))  # Nombre enter negatiu
print(type(7238424723784278934789239874))  # Python permet nombres enters molt grans
# print(7238424723784278934789239874)

# print("float:")  # Nombres decimals (de coma flotant)
print(type(3.14))  # Nombre amb part decimal
print(type(1.0))  # També es considera un float, encara que sigui un nombre enter amb part decimal
print(type(1e3))  # Notació científica (equivalent a 1000.0)

print("complex:")  # Nombres complexos (amb part real i imaginària)
print(type(1 + 2j))  # Un nombre complex en Python (1 és la part real i 2j és la part imaginària)

print("str:")  # Cadenes de text (strings)
print(type("Hola"))  # Un string amb text
print(type(""))  # Un string buit
print(type("123"))  # Encara que sembli un número, està entre cometes i, per tant, és un string
print(type(""" 
  Multilínia
"""))  # Un string que ocupa diverses línies utilitzant cometes triples

print("bool:")  # Valors booleans (True o False)
print(type(True))  # Valor booleà veritable
print(type(False))  # Valor booleà fals
print(type(1 < 2))  # Comparació que retorna un booleà (True)

print("NoneType:")  # Representa l'absència de valor
print(type(None))  # `None` és un tipus especial de Python que representa "sense valor" o "nul"