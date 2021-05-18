import json


def speichern(entry):
    try:
        with open("data/data.json") as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt.update(entry)

    with open("data/data.json", "w") as open_file:
        json.dump(datei_inhalt, open_file, indent=4)

# def speichern2(entry):
#     try:
#         with open("data/data2.json") as open_file:
#             datei_inhalt2 = json.load(open_file)
#     except FileNotFoundError:
#         datei_inhalt2 = {}
#
#     datei_inhalt2.update(entry)
#         entry = {
#             "vorname": vorname,
#             "nachname": nachname,
#             "geschlecht": geschlecht,
#             "groess": groesse,
#             "alter": alter,
#             "erfahrung": erfahrung,
#             "ziel": ziel,
#             "frequenz": frequenz,
#             "zeitplan": zeitplan
#         }
#     with open("data/data2.json", "w") as open_file:
#         json.dump(datei_inhalt2, open_file)


def json_laden(datei_name):

    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt