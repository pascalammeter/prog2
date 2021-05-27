import json


def speichern_data(entry_eingaben):
    try:
        with open("data/data.json") as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt.update(entry_eingaben)

    with open("data/data.json", "w", encoding="utf-8") as open_file:
        json.dump(datei_inhalt, open_file, indent=4)


# Funktion für das JSON Laden für data.json, exercises.json, exercises_user.json
def json_laden(dateiname):

    try:
        with open(dateiname) as open_file:
            datei_inhalt = json.load(open_file)
        return datei_inhalt

    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt


def speichern_logbuch(entry_logbuch):
    try:
        with open("data/exercises_user.json") as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt.update(entry_logbuch)

    with open("data/exercises_user.json", "w", encoding="utf-8") as open_file:
        json.dump(datei_inhalt, open_file, indent=4)


def speichern_list_exercises(entry_logbuch):
    try:
        with open("data/exercises_user.json") as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt["logbuch"] = entry_logbuch

    with open("data/exercises_user.json", "w", encoding="utf-8") as open_file:
        json.dump(datei_inhalt, open_file, indent=4)
