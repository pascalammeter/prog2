import json


def speichern(entry):
    try:
        with open("data/data.json") as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt.update(entry)

    with open("data/data.json", "w") as open_file:
        json.dump(datei_inhalt, open_file)


def excercises_laden():
     datei_name = "data/exercises.json"

     try:
         with open(datei_name) as open_file:
             datei_inhalt = json.load(open_file)
     except FileNotFoundError:
         datei_inhalt = {}

     return datei_inhalt


# def data_laden():
#     datei_name = "data.json"
#
#     try:
#         with open(datei_name) as open_file:
#             datei_inhalt = json.load(open_file)
#     except FileNotFoundError:
#         datei_inhalt = {}
#
#     return datei_inhalt
