from flask import Flask, render_template, request, url_for, redirect
from libs.eingabedaten_speichern import speichern, json_laden

app = Flask("Trainingsplan-Generator")


@app.route("/")
def startseite():
    name = False
    # Summary:
    # Zeigt die Startseite an, wenn die url/route '/' ist.
    # Auf der Startseite kann man wählen, ob ein Trainingsplan erstellt werden soll.
    # Returns:
    # template: Das HTML 'index2.html' wird gerendert mit der Auswahlmöglichkeit
    return render_template('index.html', name=name)


@app.route("/trainingsplan", methods=['GET', 'POST'])
def trainingsplan():
    # Summary:
    # Hier kann der Trainingsplan erstellt werden. Dieser wird anhand der Eingabedaten generiert.
    # Die url/route ist '/trainingsplan'.
    if request.method == 'POST':
        vorname = request.form['vorname']
        nachname = request.form['nachname']
        geschlecht = request.form['geschlecht']
        groesse = request.form['groesse']
        alter = request.form['alter']
        erfahrung = request.form['erfahrung']
        ziel = request.form['ziel']
        frequenz = request.form['frequenz']
        zeitplan = request.form['zeitplan']
        entry = {f"{vorname}_{nachname}": [geschlecht, groesse, alter, erfahrung, ziel, frequenz, zeitplan]}
        # entry = {User: {f"{vorname}_{nachname}"}: {geschlecht, groesse, alter, erfahrung, ziel, frequenz, zeitplan}}
        speichern(entry)  # Daten in JSON File speichern, Funktion eingabedaten in eingabedaten_speichern.py
        auflisten = excercises_auflisten(vorname, nachname, erfahrung, ziel, frequenz, zeitplan)
        return auflisten
        # return redirect(url_for('excercises_auflisten'))
        # Wenn nicht ausgefüllt, Startseite Laden

    return render_template("eingabedaten.html")


@app.route("/exercises")
def excercises_auflisten(vorname, nachname, erfahrung, ziel, frequenz, zeitplan):
    exercises = json_laden("data/exercises.json")
    daten = json_laden("data/data.json")

    exercises_list = []
    if erfahrung == "beginner" and frequenz == "wenig" and zeitplan == "vierwochen" or zeitplan == "zwoelfwochen":
        for id, data in exercises["pull"].items():
            if data["schwierigkeitgrad"] == "beginner" or data["split-c"] == "GK":
                print(data["name"])
                exercises_list.append(data["name"])

        for id, data in exercises["push"].items():
            if data["schwierigkeitgrad"] == "beginner" or data["split-c"] == "GK":
                print(data["name"])
                exercises_list.append(data["name"])

        for id, data in exercises["legs"].items():
            if data["schwierigkeitgrad"] == "beginner" or data["split-c"] == "GK":
                print(data["name"])
                exercises_list.append(data["name"])

    elif erfahrung == "beginner" and ziel == "fettabbau" and frequenz == "wenig" and zeitplan == "sechsmonate" or zeitplan == "einjahr" or zeitplan == "unbestimmt":
        for id, data in exercises["pull"].items() and exercises["push"].items() and exercises["legs"].items():
            if data["schwierigkeitgrad"] == "beginner" or data["split-c"] == "GK" or data["muskel"] == "Bauch" or data["muskel"] == "Cardio":
                print(data["name"])
                exercises_list.append(data["name"])

    elif erfahrung == "beginner" and frequenz == "mittel" and zeitplan == "vierwochen" or zeitplan == "zwoelfwochen":
        for id, data in exercises["pull"].items() and exercises["push"].items() and exercises["legs"].items():
            if data["schwierigkeitgrad"] == "beginner" or data["split-c"] == "GK":
                print(data["name"])
                exercises_list.append(data["name"])

    elif erfahrung == "beginner" and ziel == "fettabbau" and frequenz == "mittel" and zeitplan == "sechsmonate" or zeitplan == "einjahr" or zeitplan == "unbestimmt":
        for id, data in exercises["pull"].items() and exercises["push"].items() and exercises["legs"].items():
            if data["schwierigkeitgrad"] == "beginner" or data["split-c"] == "GK" or data["muskel"] == "Bauch" or data["muskel"] == "Cardio":
                print(data["name"])
                exercises_list.append(data["name"])

    elif erfahrung == "beginner" and frequenz == "viel" and zeitplan == "vierwochen" or zeitplan == "zwoelfwochen":
        for id, data in exercises["pull"].items() and exercises["push"].items() and exercises["legs"].items():
            if data["schwierigkeitgrad"] == "beginner" or data["split-c"] == "GK" or data["training"] == "D":
                print(data["name"])
                exercises_list.append(data["name"])

    elif erfahrung == "beginner" and frequenz == "viel" and zeitplan == "sechsmonate" or zeitplan == "einjahr" or zeitplan == "unbestimmt":
        for id, data in exercises["pull"].items() and exercises["push"].items() and exercises["legs"].items():
            if data["schwierigkeitgrad"] == "beginner" or data["split-c"] == "GK" or data["training"] == "D":
                print(data["name"])
                exercises_list.append(data["name"])


    return render_template("uebungengeneriert.html", vorname=vorname, nachname=nachname, exercises_list=exercises_list)


@app.route("/uebungen")
def uebungen():
    # Summary:
    # Hier werden alle Übungen angezeigt.
    # Die url/route ist '/uebungen'.
    # Template: Das HTML 'uebungengeneriert.html' wird gerendert.

    return render_template("uebungengeneriert.html")  # html und daten noch undefiniert


if __name__ == "__main__":
    app.run(debug=True, port=5000)
