# # beginner, mittel, muskelaufbau & mix, zeitplan alle
# elif erfahrung == "beginner" and frequenz == "mittel" and ziel == "muskelaufbau" or ziel == "mix" and zeitplan == "vierwochen" or zeitplan == "zwoelfwochen" or zeitplan == "sechsmonate" or zeitplan == "einjahr" or zeitplan == "unbestimmt":
#     for number, data in get_exercises.items():
#         if data["schwierigkeitgrad"] == "beginner" or data["splitb"] == "OK/UK":
#             list_exercises.append([value, data["training"], data["name"], data["muskel"], data["splitb"]])
#             speichern_list_exercises(list_exercises)
#
# # beginner, mittel, fettabbau, zeitplan alle
# elif erfahrung == "beginner" and frequenz == "mittel" and ziel == "fettabbau" and zeitplan == "vierwochen" or zeitplan == "zwoelfwochen" or zeitplan == "sechsmonate" or zeitplan == "einjahr" or zeitplan == "unbestimmt":
#     for number, data in get_exercises.items():
#         if data["schwierigkeitgrad"] == "beginner" or data["splitb"] == "OK/UK" or data["muskel"] == "Bauch" or data["muskel"] == "Cardio":
#             list_exercises.append([value, data["training"], data["name"], data["muskel"], data["splitb"]])
#             speichern_list_exercises(list_exercises)
#
# # beginner, viel, muskelaufbau & mix, zeitplan alle
# elif erfahrung == "beginner" and frequenz == "viel" and ziel == "muskelaufbau" or ziel == "mix" and zeitplan == "vierwochen" or zeitplan == "zwoelfwochen" or zeitplan == "sechsmonate" or zeitplan == "einjahr" or zeitplan == "unbestimmt":
#     for number, data in get_exercises.items():
#         if data["schwierigkeitgrad"] == "beginner" or data["splita"] == "3er-Split":
#             list_exercises.append([value, data["training"], data["name"], data["muskel"], data["splita"]])
#             speichern_list_exercises(list_exercises)
#
# # beginner, viel, fettabbau, zeitplan alle
# elif erfahrung == "beginner" and frequenz == "viel" and ziel == "fettabbau" and zeitplan == "vierwochen" or zeitplan == "zwoelfwochen" or zeitplan == "sechsmonate" or zeitplan == "einjahr" or zeitplan == "unbestimmt":
#     for number, data in get_exercises.items():
#         if data["schwierigkeitgrad"] == "beginner" or data["splita"] == "3er-Split" or data["muskel"] == "Bauch" or data["muskel"] == "Cardio":
#             list_exercises.append([value, data["training"], data["name"], data["muskel"], data["splita"]])
#             speichern_list_exercises(list_exercises)




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