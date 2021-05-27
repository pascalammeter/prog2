from libs.eingabedaten_speichern import json_laden, speichern_list_exercises


def get_exercises(value, erfahrung, ziel, frequenz, zeitplan):
    exercises = json_laden("data/exercises.json")
    list_exercises = []

    # Conditions für Beginner
    # beginner, wenig, muskelaufbau & mix, zeitplan alle
    if erfahrung == "beginner" and ziel == "muskelaufbau" or ziel == "mix" and frequenz == "wenig" and zeitplan == "vierwochen" or zeitplan == "zwoelfwochen" or zeitplan == "sechsmonate" or zeitplan == "einjahr" or zeitplan == "unbestimmt":
        for number, data in exercises.items():
            if data["schwierigkeitgrad"] == "beginner" or data["splitc"] == "GK":
                list_exercises.append([value, data["training"], data["name"], data["muskel"], data["splitc"]])
                # https://docs.python.org/3/tutorial/datastructures.html

    # beginner, wenig, fettabbau, zeitplan alle
    elif erfahrung == "beginner" and ziel == "fettabbau" and frequenz == "wenig" and zeitplan == "vierwochen" or zeitplan == "zwoelfwochen" or zeitplan == "sechsmonate" or zeitplan == "einjahr" or zeitplan == "unbestimmt":
        for number, data in exercises.items():
            if data["schwierigkeitgrad"] == "beginner" or data["splitc"] == "GK" and data["muskel"] == "Bauch" and data["muskel"] == "Cardio":
                list_exercises.append([value, data["training"], data["name"], data["muskel"], data["splitc"]])

    # Conditions für Intermediate

    speichern_list_exercises(list_exercises)
    return list_exercises



