from datetime import datetime
import json


def speichern(entry):
    try:
        with open("data/data.json") as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    # datei_inhalt[str(key)] = value
    datei_inhalt.update(entry)

    with open("data/data.json", "w") as open_file:
        json.dump(datei_inhalt, open_file)
#
#
# def aktivitaet_speichern(aktivitaet):
#     datei_name = "workout.json"
#     zeitpunkt = datetime.now()
#     speichern(datei_name, zeitpunkt, aktivitaet)
#     return zeitpunkt, aktivitaet
#
#
# def aktivitaeten_laden():
#     datei_name = "aktivitaeten.json"
#
#     try:
#         with open(datei_name) as open_file:
#             datei_inhalt = json.load(open_file)
#     except FileNotFoundError:
#         datei_inhalt = {}
#
#     return datei_inhalt