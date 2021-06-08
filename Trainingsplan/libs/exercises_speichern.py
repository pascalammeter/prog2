from libs.eingabedaten_speichern import json_laden, speichern_dict_exercises


# Funktion, welche alle Übungen aus exercises.json wo if/else = true ins Dict "dict_exercises" updated.
# Anschliessend wird das Dict "dict_exercises" im JSON exercises.json gespeichert.
def exercises(value, erfahrung, ziel, frequenz, zeitplan):
    get_exercises = json_laden("data/exercises.json")
    # komplexer_key = f"{erfahrung}_{ziel}_{frequenz}_{zeitplan}"
    file_name = "data/exercises_user.json"
    dict_exercises = {}

    # Conditions für Beginner
    # beginner, muskelaufbau & mix, wenig, zeitplan alle
    if erfahrung == "beginner":  # Quelle: https://docs.python.org/3/tutorial/datastructures.html
        # print(erfahrung)
        if ziel == "muskelaufbau" or ziel == "mix":
            # print(ziel)
            if frequenz == "wenig":
                if zeitplan == "vierwochen" or zeitplan == "zwoelfwochen" or zeitplan == "sechsmonate" or zeitplan == "einjahr" or zeitplan == "unbestimmt":
                    # print(zeitplan)
                    for number, data in get_exercises.items():
                        condition = data["schwierigkeitgrad"] == "beginner" or data["splitc"] == "GK"
                        # print(condition)
                        if condition:  # ohne variable "condition", also if data["bsp"] == "bsp", konnte ich nicht mehrere Conditions gleichzeitig abfragen (AND/OR).
                            training_value = data["training"]
                            name_value = data["name"]
                            muskel_value = data["muskel"]
                            split_value = data["splitc"]
                            komplexer_key = f"{value}_{training_value}_{name_value}_{muskel_value}_{split_value}"
                            dict_exercises[komplexer_key] = {
                                "user": value,
                                "training": data["training"],
                                "name": data["name"],
                                "muskel": data["muskel"],
                                "split": data["splitc"]
                            }
                            dict_exercises.update()

    # beginner, fettabbau, wenig, zeitplan alle
    if erfahrung == "beginner":
        # print(erfahrung)
        if ziel == "fettabbau":
            # print(ziel)
            if frequenz == "wenig":
                if zeitplan == "vierwochen" or zeitplan == "zwoelfwochen" or zeitplan == "sechsmonate" or zeitplan == "einjahr" or zeitplan == "unbestimmt":
                    # print(zeitplan)
                    for number, data in get_exercises.items():
                        condition = data["schwierigkeitgrad"] == "beginner" or data["splitc"] == "GK" or data["muskel"] == "Bauch" or data["muskel"] == "Cardio"
                        # print(condition)
                        if condition:
                            training_value = data["training"]
                            name_value = data["name"]
                            muskel_value = data["muskel"]
                            split_value = data["splitc"]
                            komplexer_key = f"{value}_{training_value}_{name_value}_{muskel_value}_{split_value}"
                            dict_exercises[komplexer_key] = {
                                "user": value,
                                "training": data["training"],
                                "name": data["name"],
                                "muskel": data["muskel"],
                                "split": data["splitc"]
                            }
                            dict_exercises.update()
                            # print(dict_exercises)

    # beginner, muskelaufbau & mix, mittel, zeitplan alle
    # KeyError: 'splitb'
    if erfahrung == "beginner":
        # print(erfahrung)
        if ziel == "muskelaufbau" or ziel == "mix":
            # print(ziel)
            if frequenz == "mittel":
                if zeitplan == "vierwochen" or zeitplan == "zwoelfwochen" or zeitplan == "sechsmonate" or zeitplan == "einjahr" or zeitplan == "unbestimmt":
                    # print(zeitplan)
                    for number, data in get_exercises.items():
                        condition = data["schwierigkeitgrad"] == "beginner" or data["splitb"] == "OK/UK"
                        if condition:
                            training_value = data["training"]
                            name_value = data["name"]
                            muskel_value = data["muskel"]
                            split_value = data["splitb"]
                            komplexer_key = f"{value}_{training_value}_{name_value}_{muskel_value}_{split_value}"
                            dict_exercises[komplexer_key] = {
                                "user": value,
                                "training": data["training"],
                                "name": data["name"],
                                "muskel": data["muskel"],
                                "split": data["splitb"]
                            }
                            dict_exercises.update()
                            # print(dict_exercises)

    # beginner, fettabbau, mittel, zeitplan alle
    # KeyError: 'splitb'
    if erfahrung == "beginner":
        # print(erfahrung)
        if ziel == "fettabbau":
            # print(ziel)
            if frequenz == "mittel":
                if zeitplan == "vierwochen" or zeitplan == "zwoelfwochen" or zeitplan == "sechsmonate" or zeitplan == "einjahr" or zeitplan == "unbestimmt":
                    # print(zeitplan)
                    for number, data in get_exercises.items():
                        condition = data["schwierigkeitgrad"] == "beginner" or data["splitb"] == "OK/UK" or data["muskel"] == "Bauch" or data["muskel"] == "Cardio"
                        if condition:
                            training_value = data["training"]
                            name_value = data["name"]
                            muskel_value = data["muskel"]
                            split_value = data["splitb"]
                            komplexer_key = f"{value}_{training_value}_{name_value}_{muskel_value}_{split_value}"
                            dict_exercises[komplexer_key] = {
                                "user": value,
                                "training": data["training"],
                                "name": data["name"],
                                "muskel": data["muskel"],
                                "split": data["splitb"]
                            }
                            dict_exercises.update()
                            # print(dict_exercises)

    # beginner, muskelaufbau & mix, viel, zeitplan alle
    if erfahrung == "beginner":
        # print(erfahrung)
        if ziel == "muskelaufbau" or ziel == "mix":
            # print(ziel)
            if frequenz == "viel":
                if zeitplan == "vierwochen" or zeitplan == "zwoelfwochen" or zeitplan == "sechsmonate" or zeitplan == "einjahr" or zeitplan == "unbestimmt":
                    # print(zeitplan)
                    for number, data in get_exercises.items():
                        condition = data["schwierigkeitgrad"] == "beginner" or data["splita"] == "3er-Split"
                        if condition:
                            training_value = data["training"]
                            name_value = data["name"]
                            muskel_value = data["muskel"]
                            split_value = data["splita"]
                            komplexer_key = f"{value}_{training_value}_{name_value}_{muskel_value}_{split_value}"
                            dict_exercises[komplexer_key] = {
                                "user": value,
                                "training": data["training"],
                                "name": data["name"],
                                "muskel": data["muskel"],
                                "split": data["splita"]
                            }
                            dict_exercises.update()
                            # print(dict_exercises)

    # beginner, fettabbau, viel, zeitplan alle
    if erfahrung == "beginner":
        # print(erfahrung)
        if ziel == "fettabbau":
            # print(ziel)
            if frequenz == "viel":
                if zeitplan == "vierwochen" or zeitplan == "zwoelfwochen" or zeitplan == "sechsmonate" or zeitplan == "einjahr" or zeitplan == "unbestimmt":
                    # print(zeitplan)
                    for number, data in get_exercises.items():
                        condition = data["schwierigkeitgrad"] == "beginner" or data["splita"] == "3er-Split" or data["muskel"] == "Bauch" or data["muskel"] == "Cardio"
                        if condition:
                            training_value = data["training"]
                            name_value = data["name"]
                            muskel_value = data["muskel"]
                            split_value = data["splita"]
                            komplexer_key = f"{value}_{training_value}_{name_value}_{muskel_value}_{split_value}"
                            dict_exercises[komplexer_key] = {
                                "user": value,
                                "training": data["training"],
                                "name": data["name"],
                                "muskel": data["muskel"],
                                "split": data["splita"]
                            }
                            dict_exercises.update()
                            # print(dict_exercises)

    # Conditions für Intermediate
    # intermediate, muskelaufbau & mix, wenig, zeitplan kurzfristig
    if erfahrung == "intermediate":
        # print(erfahrung)
        if ziel == "muskelaufbau" or ziel == "mix":
            # print(ziel)
            if frequenz == "wenig":
                if zeitplan == "vierwochen" or zeitplan == "zwoelfwochen":
                    # print(zeitplan)
                    for number, data in get_exercises.items():
                        condition = data["schwierigkeitgrad"] == "intermediate" or data["splitc"] == "GK"
                        # print(condition)
                        if condition:
                            training_value = data["training"]
                            name_value = data["name"]
                            muskel_value = data["muskel"]
                            split_value = data["splitc"]
                            komplexer_key = f"{value}_{training_value}_{name_value}_{muskel_value}_{split_value}"
                            dict_exercises[komplexer_key] = {
                                "user": value,
                                "training": data["training"],
                                "name": data["name"],
                                "muskel": data["muskel"],
                                "split": data["splitc"]
                            }
                            dict_exercises.update()
                            # print(dict_exercises)

    # intermediate, muskelaufbau & mix, wenig, zeitplan langfristig
    # KeyError: 'splitb'
    if erfahrung == "intermediate":
        # print(erfahrung)
        if ziel == "muskelaufbau" or ziel == "mix":
            # print(ziel)
            if frequenz == "wenig":
                if zeitplan == "sechsmonate" or zeitplan == "einjahr" or zeitplan == "unbestimmt":
                    # print(zeitplan)
                    for number, data in get_exercises.items():
                        condition = data["schwierigkeitgrad"] == "intermediate" or data["splitb"] == "OK/UK"
                        # print(condition)
                        if condition:
                            training_value = data["training"]
                            name_value = data["name"]
                            muskel_value = data["muskel"]
                            split_value = data["splitb"]
                            komplexer_key = f"{value}_{training_value}_{name_value}_{muskel_value}_{split_value}"
                            dict_exercises[komplexer_key] = {
                                "user": value,
                                "training": data["training"],
                                "name": data["name"],
                                "muskel": data["muskel"],
                                "split": data["splitb"]
                            }
                            dict_exercises.update()
                            # print(dict_exercises)

    # intermediate, muskelaufbau & mix, mittel, zeitplan alle
    if erfahrung == "intermediate":
        # print(erfahrung)
        if ziel == "muskelaufbau" or ziel == "mix":
            # print(ziel)
            if frequenz == "mittel":
                if zeitplan == "vierwochen" or zeitplan == "zwoelfwochen" or zeitplan == "sechsmonate" or zeitplan == "einjahr" or zeitplan == "unbestimmt":
                    # print(zeitplan)
                    for number, data in get_exercises.items():
                        condition = data["schwierigkeitgrad"] == "intermediate" or data["splita"] == "3er-Split"
                        # print(condition)
                        if condition:
                            training_value = data["training"]
                            name_value = data["name"]
                            muskel_value = data["muskel"]
                            split_value = data["splita"]
                            komplexer_key = f"{value}_{training_value}_{name_value}_{muskel_value}_{split_value}"
                            dict_exercises[komplexer_key] = {
                                "user": value,
                                "training": data["training"],
                                "name": data["name"],
                                "muskel": data["muskel"],
                                "split": data["splita"]
                            }
                            dict_exercises.update()
                            # print(dict_exercises)

    # intermediate, muskelaufbau & mix, viel, zeitplan alle
    if erfahrung == "intermediate":
        # print(erfahrung)
        if ziel == "muskelaufbau" or ziel == "mix":
            # print(ziel)
            if frequenz == "viel":
                if zeitplan == "vierwochen" or zeitplan == "zwoelfwochen" or zeitplan == "sechsmonate" or zeitplan == "einjahr" or zeitplan == "unbestimmt":
                    # print(zeitplan)
                    for number, data in get_exercises.items():
                        condition = data["schwierigkeitgrad"] == "intermediate" or data["splita"] == "3er-Split" or data["muskel"] == "Bauch" or data["muskel"] == "Mobility"
                        # print(condition)
                        if condition:
                            training_value = data["training"]
                            name_value = data["name"]
                            muskel_value = data["muskel"]
                            split_value = data["splita"]
                            komplexer_key = f"{value}_{training_value}_{name_value}_{muskel_value}_{split_value}"
                            dict_exercises[komplexer_key] = {
                                "user": value,
                                "training": data["training"],
                                "name": data["name"],
                                "muskel": data["muskel"],
                                "split": data["splita"]
                            }
                            dict_exercises.update()
                            # print(dict_exercises)

    # intermediate, fettabbau, wenig & mittel, zeitplan alle
    # KeyError: 'splitb'
    if erfahrung == "intermediate":
        # print(erfahrung)
        if ziel == "fettabbau":
            # print(ziel)
            if frequenz == "wenig" or frequenz == "mittel":
                if zeitplan == "vierwochen" or zeitplan == "zwoelfwochen" or zeitplan == "sechsmonate" or zeitplan == "einjahr" or zeitplan == "unbestimmt":
                    # print(zeitplan)
                    for number, data in get_exercises.items():
                        condition = data["schwierigkeitgrad"] == "intermediate" or data["splitb"] == "OK/UK" or data["muskel"] == "Bauch" or data["muskel"] == "Cardio"
                        # print(condition)
                        if condition:
                            training_value = data["training"]
                            name_value = data["name"]
                            muskel_value = data["muskel"]
                            split_value = data["splitb"]
                            komplexer_key = f"{value}_{training_value}_{name_value}_{muskel_value}_{split_value}"
                            dict_exercises[komplexer_key] = {
                                "user": value,
                                "training": data["training"],
                                "name": data["name"],
                                "muskel": data["muskel"],
                                "split": data["splitb"]
                            }
                            dict_exercises.update()
                            # print(dict_exercises)

    # intermediate, fettabbau, viel, zeitplan alle
    if erfahrung == "intermediate":
        # print(erfahrung)
        if ziel == "fettabbau":
            # print(ziel)
            if frequenz == "viel":
                if zeitplan == "vierwochen" or zeitplan == "zwoelfwochen" or zeitplan == "sechsmonate" or zeitplan == "einjahr" or zeitplan == "unbestimmt":
                    # print(zeitplan)
                    for number, data in get_exercises.items():
                        condition = data["schwierigkeitgrad"] == "intermediate" or data["splita"] == "3er-Split" or data["muskel"] == "Bauch" or data["muskel"] == "Cardio" or data["muskel"] == "Mobility"
                        # print(condition)
                        if condition:
                            training_value = data["training"]
                            name_value = data["name"]
                            muskel_value = data["muskel"]
                            split_value = data["splita"]
                            komplexer_key = f"{value}_{training_value}_{name_value}_{muskel_value}_{split_value}"
                            dict_exercises[komplexer_key] = {
                                "user": value,
                                "training": data["training"],
                                "name": data["name"],
                                "muskel": data["muskel"],
                                "split": data["splita"]
                            }
                            dict_exercises.update()
                            # print(dict_exercises)

    # Conditions für Advanced
    # advanced, muskelaufbau & mix, wenig, zeitplan kurzfristig
    # KeyError: 'splitb'
    if erfahrung == "advanced":
        # print(erfahrung)
        if ziel == "muskelaufbau" or ziel == "mix":
            # print(ziel)
            if frequenz == "wenig":
                if zeitplan == "vierwochen" or zeitplan == "zwoelfwochen":
                    # print(zeitplan)
                    for number, data in get_exercises.items():
                        condition = data["schwierigkeitgrad"] == "intermediate" or data["splitb"] == "OK/UK"
                        # print(condition)
                        if condition:
                            training_value = data["training"]
                            name_value = data["name"]
                            muskel_value = data["muskel"]
                            split_value = data["splitb"]
                            komplexer_key = f"{value}_{training_value}_{name_value}_{muskel_value}_{split_value}"
                            dict_exercises[komplexer_key] = {
                                "user": value,
                                "training": data["training"],
                                "name": data["name"],
                                "muskel": data["muskel"],
                                "split": data["splitb"]
                            }
                            dict_exercises.update()
                            # print(dict_exercises)

    # advanced, muskelaufbau & mix, wenig, zeitplan langfristig
    # KeyError: 'splitb'
    if erfahrung == "advanced":
        # print(erfahrung)
        if ziel == "muskelaufbau" or ziel == "mix":
            # print(ziel)
            if frequenz == "wenig":
                if zeitplan == "sechsmonate" or zeitplan == "einjahr" or zeitplan == "unbestimmt":
                    # print(zeitplan)
                    for number, data in get_exercises.items():
                        condition = data["schwierigkeitgrad"] == "advanced" or data["splitb"] == "OK/UK"
                        # print(condition)
                        if condition:
                            training_value = data["training"]
                            name_value = data["name"]
                            muskel_value = data["muskel"]
                            split_value = data["splitb"]
                            komplexer_key = f"{value}_{training_value}_{name_value}_{muskel_value}_{split_value}"
                            dict_exercises[komplexer_key] = {
                                "user": value,
                                "training": data["training"],
                                "name": data["name"],
                                "muskel": data["muskel"],
                                "split": data["splitb"]
                            }
                            dict_exercises.update()
                            # print(dict_exercises)

    # advanced, muskelaufbau & mix, mittel, zeitplan alle
    if erfahrung == "advanced":
        # print(erfahrung)
        if ziel == "muskelaufbau" or ziel == "mix":
            # print(ziel)
            if frequenz == "mittel":
                if zeitplan == "vierwochen" or zeitplan == "zwoelfwochen" or zeitplan == "sechsmonate" or zeitplan == "einjahr" or zeitplan == "unbestimmt":
                    # print(zeitplan)
                    for number, data in get_exercises.items():
                        condition = data["schwierigkeitgrad"] == "advanced" or data["splita"] == "3er-Split"
                        # print(condition)
                        if condition:
                            training_value = data["training"]
                            name_value = data["name"]
                            muskel_value = data["muskel"]
                            split_value = data["splita"]
                            komplexer_key = f"{value}_{training_value}_{name_value}_{muskel_value}_{split_value}"
                            dict_exercises[komplexer_key] = {
                                "user": value,
                                "training": data["training"],
                                "name": data["name"],
                                "muskel": data["muskel"],
                                "split": data["splita"]
                            }
                            dict_exercises.update()
                            # print(dict_exercises)

    # advanced, muskelaufbau & mix, viel, zeitplan alle
    if erfahrung == "advanced":
        # print(erfahrung)
        if ziel == "muskelaufbau" or ziel == "mix":
            # print(ziel)
            if frequenz == "viel":
                if zeitplan == "vierwochen" or zeitplan == "zwoelfwochen" or zeitplan == "sechsmonate" or zeitplan == "einjahr" or zeitplan == "unbestimmt":
                    # print(zeitplan)
                    for number, data in get_exercises.items():
                        condition = data["schwierigkeitgrad"] == "advanced" or data["splita"] == "3er-Split" or data["muskel"] == "Bauch" or data["muskel"] == "Mobility"
                        # print(condition)
                        if condition:
                            training_value = data["training"]
                            name_value = data["name"]
                            muskel_value = data["muskel"]
                            split_value = data["splita"]
                            komplexer_key = f"{value}_{training_value}_{name_value}_{muskel_value}_{split_value}"
                            dict_exercises[komplexer_key] = {
                                "user": value,
                                "training": data["training"],
                                "name": data["name"],
                                "muskel": data["muskel"],
                                "split": data["splita"]
                            }
                            dict_exercises.update()
                            # print(dict_exercises)

    # advanced, fettabbau, wenig, zeitplan alle
    # KeyError: 'splitb'
    if erfahrung == "advanced":
        # print(erfahrung)
        if ziel == "fettabbau":
            # print(ziel)
            if frequenz == "wenig":
                if zeitplan == "vierwochen" or zeitplan == "zwoelfwochen" or zeitplan == "sechsmonate" or zeitplan == "einjahr" or zeitplan == "unbestimmt":
                    # print(zeitplan)
                    for number, data in get_exercises.items():
                        condition = data["schwierigkeitgrad"] == "advanced" or data["splitb"] == "OK/UK" or data["muskel"] == "Bauch" or data["muskel"] == "Cardio"
                        # print(condition)
                        if condition:
                            training_value = data["training"]
                            name_value = data["name"]
                            muskel_value = data["muskel"]
                            split_value = data["splitb"]
                            komplexer_key = f"{value}_{training_value}_{name_value}_{muskel_value}_{split_value}"
                            dict_exercises[komplexer_key] = {
                                "user": value,
                                "training": data["training"],
                                "name": data["name"],
                                "muskel": data["muskel"],
                                "split": data["splitb"]
                            }
                            dict_exercises.update()
                            # print(dict_exercises)

    # advanced, fettabbau, mittel, zeitplan alle
    if erfahrung == "advanced":
        # print(erfahrung)
        if ziel == "fettabbau":
            # print(ziel)
            if frequenz == "mittel":
                if zeitplan == "vierwochen" or zeitplan == "zwoelfwochen" or zeitplan == "sechsmonate" or zeitplan == "einjahr" or zeitplan == "unbestimmt":
                    # print(zeitplan)
                    for number, data in get_exercises.items():
                        condition = data["schwierigkeitgrad"] == "advanced" or data["splita"] == "3er-Split" or data["muskel"] == "Bauch" or data["muskel"] == "Cardio"
                        # print(condition)
                        if condition:
                            training_value = data["training"]
                            name_value = data["name"]
                            muskel_value = data["muskel"]
                            split_value = data["splita"]
                            komplexer_key = f"{value}_{training_value}_{name_value}_{muskel_value}_{split_value}"
                            dict_exercises[komplexer_key] = {
                                "user": value,
                                "training": data["training"],
                                "name": data["name"],
                                "muskel": data["muskel"],
                                "split": data["splita"]
                            }
                            dict_exercises.update()
                            # print(dict_exercises)

    # advanced, fettabbau, viel, zeitplan alle
    if erfahrung == "advanced":
        # print(erfahrung)
        if ziel == "fettabbau":
            # print(ziel)
            if frequenz == "viel":
                if zeitplan == "vierwochen" or zeitplan == "zwoelfwochen" or zeitplan == "sechsmonate" or zeitplan == "einjahr" or zeitplan == "unbestimmt":
                    # print(zeitplan)
                    for number, data in get_exercises.items():
                        condition = data["schwierigkeitgrad"] == "advanced" or data["splita"] == "3er-Split" or data["muskel"] == "Bauch" or data["muskel"] == "Cardio" or data["muskel"] == "Mobility"
                        # print(condition)
                        if condition:
                            training_value = data["training"]
                            name_value = data["name"]
                            muskel_value = data["muskel"]
                            split_value = data["splita"]
                            komplexer_key = f"{value}_{training_value}_{name_value}_{muskel_value}_{split_value}"
                            dict_exercises[komplexer_key] = {
                                "user": value,
                                "training": data["training"],
                                "name": data["name"],
                                "muskel": data["muskel"],
                                "split": data["splita"]
                            }
                            dict_exercises.update()
                            # print(dict_exercises)

    speichern_dict_exercises(file_name, dict_exercises)
    return dict_exercises


