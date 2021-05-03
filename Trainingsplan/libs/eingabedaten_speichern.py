from datetime import datetime
import json
# from libs import data


def speichern(datei, key, value, groesse, gewicht, alter):
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt[str(key)] = value

    print(datei_inhalt)

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file)


def eingabedaten(vorname, nachname, geschlecht, groesse, gewicht, alter):
    json_daten = "data.json"
    alle_personen = json_daten.get('personen', {})
    person = {"vorname": vorname, "nachname": nachname, "geschlecht": geschlecht, "groesse": groesse, "gewicht": gewicht, "alter": alter}
    alle_personen['person'][gewicht] = person
    json_daten["personen"] = alle_personen
    speichern(vorname, nachname, geschlecht, groesse, gewicht, alter)


def aktivitaet_speichern(aktivitaet):
    datei_name = "data.json"
    zeitpunkt = datetime.now()
    speichern(datei_name, zeitpunkt, aktivitaet)
    return zeitpunkt, aktivitaet


def aktivitaeten_laden():
    datei_name = "aktivitaeten.json"

    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt