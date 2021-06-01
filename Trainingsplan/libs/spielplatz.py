from libs.eingabedaten_speichern import json_laden, speichern_dict_exercises


def exercises(value, erfahrung, ziel, frequenz, zeitplan):
    get_exercises = json_laden("data/exercises.json")
    dict_exercises = {}

    # Conditions für Beginner
    # beginner, wenig, muskelaufbau & mix, zeitplan alle
    if erfahrung == "beginner" and ziel == "muskelaufbau" or ziel == "mix" and frequenz == "wenig" and zeitplan == "vierwochen" or zeitplan == "zwoelfwochen" or zeitplan == "sechsmonate" or zeitplan == "einjahr" or zeitplan == "unbestimmt":
        for number, data in get_exercises.items():
            if data["schwierigkeitgrad"] == "beginner" or data["splitc"] == "GK":
                ausgabe_exercises = {
                    value: {"training": data["training"], "name": data["name"], "muskel": data["muskel"],
                            "split": data["splitc"]}}
                # dict_exercises[value] = {"training": data["training"], "name": data["name"], "muskel": data["muskel"], "split": data["splitc"]}
                dict_exercises.update(ausgabe_exercises)

                # https://docs.python.org/3/tutorial/datastructures.html

    # # beginner, wenig, fettabbau, zeitplan alle
    # elif erfahrung == "beginner" and ziel == "fettabbau" and frequenz == "wenig" and zeitplan == "vierwochen" or zeitplan == "zwoelfwochen" or zeitplan == "sechsmonate" or zeitplan == "einjahr" or zeitplan == "unbestimmt":
    #     for number, data in get_exercises.items():
    #         if data["schwierigkeitgrad"] == "beginner" or data["splitc"] == "GK" and data["muskel"] == "Bauch" and data["muskel"] == "Cardio":
    #             list_exercises.append([value, data["training"], data["name"], data["muskel"], data["splitc"]])
    #
    # # beginner, mittel, muskelaufbau & mix, zeitplan alle
    # elif erfahrung == "beginner" and frequenz == "mittel" and ziel == "muskelaufbau" or ziel == "mix" and zeitplan == "vierwochen" or zeitplan == "zwoelfwochen" or zeitplan == "sechsmonate" or zeitplan == "einjahr" or zeitplan == "unbestimmt":
    #     for number, data in get_exercises.items():
    #         if data["schwierigkeitgrad"] == "beginner" or data["splitb"] == "OK/UK":
    #             list_exercises.append([value, data["training"], data["name"], data["muskel"], data["splitb"]])
    #
    # # beginner, mittel, fettabbau, zeitplan alle
    # elif erfahrung == "beginner" and frequenz == "mittel" and ziel == "fettabbau" and zeitplan == "vierwochen" or zeitplan == "zwoelfwochen" or zeitplan == "sechsmonate" or zeitplan == "einjahr" or zeitplan == "unbestimmt":
    #     for number, data in get_exercises.items():
    #         if data["schwierigkeitgrad"] == "beginner" or data["splitb"] == "OK/UK" or data["muskel"] == "Bauch" or \
    #                 data["muskel"] == "Cardio":
    #             list_exercises.append([value, data["training"], data["name"], data["muskel"], data["splitb"]])
    #
    # # beginner, viel, muskelaufbau & mix, zeitplan alle
    # elif erfahrung == "beginner" and frequenz == "viel" and ziel == "muskelaufbau" or ziel == "mix" and zeitplan == "vierwochen" or zeitplan == "zwoelfwochen" or zeitplan == "sechsmonate" or zeitplan == "einjahr" or zeitplan == "unbestimmt":
    #     for number, data in get_exercises.items():
    #         if data["schwierigkeitgrad"] == "beginner" or data["splita"] == "3er-Split":
    #             list_exercises.append([value, data["training"], data["name"], data["muskel"], data["splita"]])
    #
    # # beginner, viel, fettabbau, zeitplan alle
    # elif erfahrung == "beginner" and frequenz == "viel" and ziel == "fettabbau" and zeitplan == "vierwochen" or zeitplan == "zwoelfwochen" or zeitplan == "sechsmonate" or zeitplan == "einjahr" or zeitplan == "unbestimmt":
    #     for number, data in get_exercises.items():
    #         if data["schwierigkeitgrad"] == "beginner" or data["splita"] == "3er-Split" or data["muskel"] == "Bauch" or \
    #                 data["muskel"] == "Cardio":
    #             list_exercises.append([value, data["training"], data["name"], data["muskel"], data["splita"]])

    # Conditions für Intermediate
    # elif erfahrung == "intermediate" and frequenz == "wenig" and zeitplan == "vierwochen" or zeitplan == "zwoelfwochen":
    #     for number, data in get_exercises.items():
    #         if data["schwierigkeitgrad"] == "intermediate" or data["splitc"] == "GK":
    #             list_exercises.append([value, data["training"], data["name"], data["muskel"], data["splitc"]])
    #
    # elif erfahrung == "intermediate" and frequenz == "wenig" or ziel == "fettabbau" and zeitplan == "sechsmonate" or zeitplan == "einjahr" or zeitplan == "unbestimmt":
    #     for number, data in get_exercises.items():
    #         if data["schwierigkeitgrad"] == "intermediate" or data["splitc"] == "GK" and data["muskel"] == "Bauch" and data["muskel"] == "Cardio":
    #             list_exercises.append([value, data["training"], data["name"], data["muskel"], data["splitc"]])
    #
    # elif erfahrung == "intermediate" and frequenz == "mittel" and zeitplan == "vierwochen" or zeitplan == "zwoelfwochen":
    #     for number, data in get_exercises.items():
    #         if data["schwierigkeitgrad"] == "intermediate" or data["splitb"] == "OK/UK":
    #             list_exercises.append([value, data["training"], data["name"], data["muskel"], data["splitb"]])
    #
    # # KeyError: 'splitb'
    # elif erfahrung == "intermediate" and frequenz == "mittel" or ziel == "fettabbau" and zeitplan == "sechsmonate" or zeitplan == "einjahr" or zeitplan == "unbestimmt":
    #     for number, data in get_exercises.items():
    #         if data["schwierigkeitgrad"] == "intermediate" or data["splitb"] == "OK/UK" or data["muskel"] == "Bauch" or data["muskel"] == "Cardio":
    #             list_exercises.append([value, data["training"], data["name"], data["muskel"], data["splitb"]])
    #
    # elif erfahrung == "intermediate" and frequenz == "viel" and ziel == "fettabbau":
    #     for number, data in get_exercises.items():
    #         if data["schwierigkeitgrad"] == "intermediate" or data["splita"] == "3er-Split" or data["muskel"] == "Bauch" or data["muskel"] == "Cardio" or data["muskel"] == "Mobility":
    #             list_exercises.append([value, data["training"], data["name"], data["muskel"], data["splita"]])
    #
    # elif erfahrung == "intermediate" and frequenz == "viel" or ziel == "muskelaufbau":
    #     for number, data in get_exercises.items():
    #         if data["schwierigkeitgrad"] == "intermediate" or data["splita"] == "3er-Split" or data["muskel"] == "Bauch" or data["muskel"] == "Cardio" or data["muskel"] == "Mobility":
    #             list_exercises.append([value, data["training"], data["name"], data["muskel"], data["splita"]])
    #
    # elif erfahrung == "intermediate" and frequenz == "viel" or ziel == "muskelaufbau" and zeitplan == "vierwochen" or zeitplan == "zwoelfwochen" or zeitplan == "sechsmonate" or zeitplan == "einjahr" or zeitplan == "unbestimmt":
    #     for number, data in get_exercises.items():
    #         if data["schwierigkeitgrad"] == "intermediate" or data["splita"] == "3er-Split" or data["muskel"] == "Bauch" or data["muskel"] == "Cardio" or data["muskel"] == "Mobility":
    #             list_exercises.append([value, data["training"], data["name"], data["muskel"], data["splita"]])



    # for item in list_exercises:
    #     sorted_list_exercises = sorted(list_exercises, key=operator.itemgetter(item[1]))
    #
    #     speichern_list_exercises(sorted_list_exercises)
    speichern_dict_exercises(dict_exercises)
    return dict_exercises
