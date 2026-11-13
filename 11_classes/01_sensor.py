###
# 11 - Classes i objectes
# Dues sessions de teoria d'1 hora. Projecte de monitoratge de sensors.
###

# OBJECTIUS D'APRENENTATGE
# - Distingir una classe de les seves instàncies.
# - Construir objectes amb __init__ i entendre el paper de self.
# - Agrupar atributs i mètodes que gestionen el mateix estat.
# - Mantenir les lectures de cada sensor independents i validades.

from math import isfinite


# 1. DE LES DADES A UN OBJECTE
# Fins ara podíem representar un sensor amb un diccionari.
# Una classe defineix les dades i les operacions dels seus objectes.
# Sensor és la classe. Sensor("T1", "°C") crea una instància concreta.
# Els atributs emmagatzemen estat. Els mètodes són funcions de la classe.

class Sensor:
    """Agrupa la identificació i l'històric d'un sensor simulat."""

    def __init__(self, nom, unitat):
        """Inicialitza una instància amb un històric buit propi."""
        # Python crida __init__ quan construïm l'objecte.
        # self identifica la instància que està executant el mètode.
        self.nom = nom
        self.unitat = unitat
        # Aquesta llista es crea per a cada objecte, dins d'__init__.
        self.lectures = []

    # 2. MÈTODES I CANVIS D'ESTAT
    # En sensor.registrar(22.5), Python passa sensor com a self.
    # La validació es fa abans de modificar l'històric.
    def registrar(self, valor):
        """Afegeix un int o float finit, o llança ValueError."""
        # bool és un subtipus d'int, però True no és una mesura.
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise ValueError("La lectura ha de ser un nombre.")
        # Els enters són finits. Els floats també poden ser inf o nan.
        if isinstance(valor, float) and not isfinite(valor):
            raise ValueError("La lectura ha de ser finita.")
        self.lectures.append(valor)

    # 3. MÈTODES QUE CONSULTEN L'ESTAT
    # None representa l'absència de lectura. 0 és una mesura vàlida.
    def ultima_lectura(self):
        """Retorna l'última lectura, o None si l'històric és buit."""
        if not self.lectures:
            return None
        return self.lectures[-1]

    def mitjana(self):
        """Retorna la mitjana aritmètica, o None si no hi ha lectures."""
        if not self.lectures:
            return None
        return sum(self.lectures) / len(self.lectures)


def main():
    """Mostra construcció, estat independent i consultes."""
    # Primera sessió. Constructor, atributs, mètodes i dues instàncies.
    temperatura = Sensor("T1", "°C")
    humitat = Sensor("H1", "%")
    print(temperatura.nom, temperatura.unitat)  # T1 °C
    print(temperatura.ultima_lectura())  # None

    temperatura.registrar(20.0)
    temperatura.registrar(24.0)
    humitat.registrar(55.0)
    print(temperatura.lectures)  # [20.0, 24.0]
    print(humitat.lectures)  # [55.0]

    # Segona sessió. Consultes, validació i evolució de l'estat.
    print(temperatura.ultima_lectura())  # 24.0
    print(temperatura.mitjana())  # 22.0
    try:
        temperatura.registrar("error")
    except ValueError as error:
        print(error)
    print(temperatura.lectures)  # [20.0, 24.0]
    # L'històric conserva les lectures acceptades.

    # ACTIVITAT GUIADA
    # Abans d'executar les línies següents, prediu els dos historials.
    # Dibuixa dues caixes, una per instància, amb nom, unitat i lectures.
    temperatura.registrar(0)
    print(temperatura.ultima_lectura())  # 0
    print(humitat.ultima_lectura())  # 55.0
    # Canviar temperatura no modifica humitat. Comprova també un sensor buit.
    tensio = Sensor("V1", "V")
    print(tensio.mitjana())  # None

# ENGINYERIA DEL PROGRAMARI
# Sensor té la responsabilitat de gestionar les seves lectures.
# Centralitzar la validació a registrar facilita la mantenibilitat.
# En aquest primer model lectures és públic. Utilitza registrar per afegir
# mesures i conservar la validació. El bloc opcional 15 amplia l'encapsulació.
# La composició de diversos sensors arriba al bloc 12.
# Exercicis a 01_sensor_exercicis.py i solucions a 01_sensor_solucions.py.

if __name__ == "__main__":
    main()###
# SOLUCIONS - Fitxers TXT
###

from pathlib import Path
from tempfile import TemporaryDirectory


# Exercici 1 - Bàsic - Desar un missatge
def desar_missatge(ruta, missatge):
    """Substitueix el contingut pel missatge rebut."""
    with open(ruta, "w", encoding="utf-8") as fitxer:
        fitxer.write(missatge)


def llegir_missatge(ruta):
    """Retorna tot el text, incloent-hi els salts de línia."""
    with open(ruta, "r", encoding="utf-8") as fitxer:
        return fitxer.read()


# Exercici 2 - Bàsic - Comptar lectures
def comptar_lectures(ruta):
    """Compta les línies amb contingut."""
    comptador = 0
    with open(ruta, "r", encoding="utf-8") as fitxer:
        for linia in fitxer:
            if linia.strip():
                comptador += 1
    return comptador


# Exercici 3 - Intermedi - Recuperar valors vàlids
def llegir_valides(ruta):
    """Recupera decimals i descarta les línies no convertibles."""
    lectures = []
    with open(ruta, "r", encoding="utf-8") as fitxer:
        for linia in fitxer:
            text = linia.strip()
            if text:
                try:
                    lectures.append(float(text))
                except ValueError:
                    continue
    return lectures


# Exercici 4 - Repte opcional - Registre acumulatiu
def afegir_esdeveniment(ruta, missatge):
    """Afegeix un missatge sense salts interns i un salt final."""
    with open(ruta, "a", encoding="utf-8") as fitxer:
        fitxer.write(missatge + "\n")


def main():
    """Mostra les quatre solucions amb dades temporals."""
    with TemporaryDirectory() as carpeta:
        ruta = Path(carpeta) / "prova.txt"
        desar_missatge(ruta, "Sensor de tensió actiu\n")
        print(repr(llegir_missatge(ruta)))
        desar_missatge(ruta, "")
        print(repr(llegir_missatge(ruta)))  # ''

        desar_missatge(ruta, "20.0\n\n21.5\n   \n")
        print(comptar_lectures(ruta))  # 2
        desar_missatge(ruta, "")
        print(comptar_lectures(ruta))  # 0
        try:
            comptar_lectures(Path(carpeta) / "absent.txt")
        except FileNotFoundError:
            print("S'ha propagat FileNotFoundError")

        desar_missatge(ruta, "20.0\nerror\n\n22.0\n")
        print(llegir_valides(ruta))  # [20.0, 22.0]
        desar_missatge(ruta, "error\n\n")
        print(llegir_valides(ruta))  # []

        registre = Path(carpeta) / "esdeveniments.txt"
        afegir_esdeveniment(registre, "Inici")
        afegir_esdeveniment(registre, "Aturada")
        print(repr(llegir_missatge(registre)))  # 'Inici\nAturada\n'
        afegir_esdeveniment(registre, "Inici")
        print(repr(llegir_missatge(registre)))


if __name__ == "__main__":
    main()