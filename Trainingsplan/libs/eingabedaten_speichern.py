import json


# Funktion für das Speichern der Eingangseinträge ins JSON data.json
def speichern_data(entry_eingaben):
    try:
        with open("data/data.json") as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt.update(entry_eingaben)

    with open("data/data.json", "w", encoding="utf-8") as open_file:
        json.dump(datei_inhalt, open_file, indent=4)


# Funktion für das Laden für JSON data.json, exercises.json, exercises_user.json
def json_laden(dateiname):

    try:
        with open(dateiname) as open_file:
            datei_inhalt = json.load(open_file)
        return datei_inhalt

    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt


# Funktion für das Speichern von Userspezifischen Übungen im JSON exercises_user.json
def speichern_dict_exercises(file_name, dict_exercises):

    try:
        with open(file_name) as open_file:
            datei_inhalt = json.load(open_file)

    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt.update(dict_exercises)

    with open(file_name, "w", encoding="utf-8") as open_file:
        json.dump(datei_inhalt, open_file, indent=4)


# Funktion für das Speichern von Logbucheinträgen zu den Userspezifischen Übungen im JSON exercises_logbuch.json
def speichern_logbuch(entry_logbuch):
    try:
        with open("data/exercises_logbuch.json") as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt.update(entry_logbuch)

    with open("data/exercises_logbuch.json", "w", encoding="utf-8") as open_file:
        json.dump(datei_inhalt, open_file, indent=4)




