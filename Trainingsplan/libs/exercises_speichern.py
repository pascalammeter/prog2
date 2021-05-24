import json
from libs.eingabedaten_speichern import json_laden, speichern_logbuch


def get_exercises(key, erfahrung, ziel, frequenz, zeitplan):
    exercises = json_laden("data/exercises.json")
    dict_exercises = {}

    if erfahrung == "beginner" and frequenz == "wenig" and zeitplan == "vierwochen" or zeitplan == "zwoelfwochen":
        for id, data in exercises.items():
            if data["schwierigkeitgrad"] == "beginner" or data["split-c"] == "GK":
                dict_exercises.update({key: {
                    "training": data["training"],
                    "name": data["name"],
                    "muskel": data["muskel"],
                    "split-a": data["split-a"]}})
                print(key)
                # print(dict_exercises)


    # exercises.json
    # if erfahrung == "beginner" and frequenz == "wenig" and zeitplan == "vierwochen" or zeitplan == "zwoelfwochen":
    #     for id, data in exercises["pull"].items():
    #         if data["schwierigkeitgrad"] == "beginner" or data["split-c"] == "GK":
    #             dict_exercises.update({"training": data["training"], "name": data["name"], "muskel": data["muskel"], "split-a": data["split-a"]})
    #             print(dict_exercises)
    #
    #
    #     for id, data in exercises["push"].items():
    #         if data["schwierigkeitgrad"] == "beginner" or data["split-c"] == "GK":
    #             dict_exercises.update({"training": data["training"], "name": data["name"], "muskel": data["muskel"], "split-a": data["split-a"]})
    #
    #     for id, data in exercises["legs"].items():
    #         if data["schwierigkeitgrad"] == "beginner" or data["split-c"] == "GK":
    #             dict_exercises.update({"training": data["training"], "name": data["name"], "muskel": data["muskel"], "split-a": data["split-a"]})

    # list
    # if erfahrung == "beginner" and frequenz == "wenig" and zeitplan == "vierwochen" or zeitplan == "zwoelfwochen":
    #     for id, data in exercises["pull"].items():
    #         if data["schwierigkeitgrad"] == "beginner" or data["split-c"] == "GK":
    #             dict_exercises.update([data["training"], data["name"], data["muskel"], data["split-a"]]) # https://docs.python.org/3/tutorial/datastructures.html extend für mehrere values
    #             print(dict_exercises)

    # elif erfahrung == "beginner" and ziel == "fettabbau" and frequenz == "wenig" and zeitplan == "sechsmonate" or zeitplan == "einjahr" or zeitplan == "unbestimmt":
    #     for id, data in exercises["pull"].items() and exercises["push"].items() and exercises["legs"].items():
    #         if data["schwierigkeitgrad"] == "beginner" or data["split-c"] == "GK" or data["muskel"] == "Bauch" or data[
    #             "muskel"] == "Cardio":
    #             print(data["name"])
    #             # list_exercises.extend(data["name"])
    #             # list_muscle.extend(data["training"], data["name"], data["muskel"], data["split-a"])
    #
    # elif erfahrung == "beginner" and frequenz == "mittel" and zeitplan == "vierwochen" or zeitplan == "zwoelfwochen":
    #     for id, data in exercises["pull"].items() and exercises["push"].items() and exercises["legs"].items():
    #         if data["schwierigkeitgrad"] == "beginner" or data["split-c"] == "GK":
    #             print(data["name"])
    #             # list_exercises.extend(data["name"])
    #             # list_muscle.append(data["muskel"])
    #
    # elif erfahrung == "beginner" and ziel == "fettabbau" and frequenz == "mittel" and zeitplan == "sechsmonate" or zeitplan == "einjahr" or zeitplan == "unbestimmt":
    #     for id, data in exercises["pull"].items() and exercises["push"].items() and exercises["legs"].items():
    #         if data["schwierigkeitgrad"] == "beginner" or data["split-c"] == "GK" or data["muskel"] == "Bauch" or data[
    #             "muskel"] == "Cardio":
    #             print(data["name"])
    #             # list_exercises.extend(data["name"])
    #             # list_muscle.append(data["muskel"])
    #
    # elif erfahrung == "beginner" and frequenz == "viel" and zeitplan == "vierwochen" or zeitplan == "zwoelfwochen":
    #     for id, data in exercises["pull"].items() and exercises["push"].items() and exercises["legs"].items():
    #         if data["schwierigkeitgrad"] == "beginner" or data["split-c"] == "GK" or data["training"] == "D":
    #             print(data["name"])
    #             # list_exercises.extend(data["name"])
    #             # list_muscle.append(data["muskel"])
    #
    # elif erfahrung == "beginner" and frequenz == "viel" and zeitplan == "sechsmonate" or zeitplan == "einjahr" or zeitplan == "unbestimmt":
    #     for id, data in exercises["pull"].items() and exercises["push"].items() and exercises["legs"].items():
    #         if data["schwierigkeitgrad"] == "beginner" or data["split-c"] == "GK" or data["training"] == "D":
    #             print(data["name"])
                # list_exercises.extend(data["name"])
                # list_muscle.append(data["muskel"])

    speichern_logbuch(dict_exercises)
    return dict_exercises
