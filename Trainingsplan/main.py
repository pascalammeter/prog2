from flask import Flask, render_template, request, url_for, redirect
from libs.eingabedaten_speichern import speichern
from libs.eingabedaten_speichern import excercises_laden

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
        entry = {f"{vorname}_{nachname}":[geschlecht, groesse, alter, erfahrung, ziel, frequenz, zeitplan]}
        # entry = {User: {f"{vorname}_{nachname}"}: {geschlecht, groesse, alter, erfahrung, ziel, frequenz, zeitplan}}
        speichern(entry) # Daten in JSON File speichern, Funktion eingabedaten in eingabedaten_speichern.py

        # erhaltene_daten = eingabedaten_speichern.funktion(erfahrung, ziel, frequenz, zeitplan)

        # Weiterleitug auf Übungen, primary key mitnehmen?
        return redirect(url_for('excercises_auflisten'))
        # Wenn nicht ausgefüllt, Startseite Laden

    return render_template("eingabedaten.html")


@app.route("/exercises")
def excercises_auflisten():
    uebungen = excercises_laden()
    # daten = data_laden()

    for id, data in uebungen["pull"].items():
        if data["schwierigkeitgrad"] == "intermediate":
            print(data["name"])

    # return uebungen
    return render_template("uebungengeneriert.html")

    # for id, data in daten["Pascal_Ammeter"].items():
    #     if data[] == "viel":
    #         print(data[""])
    #
    # return daten


@app.route("/uebungen")
def uebungen():
    # Summary:
    # Hier werden alle Übungen angezeigt.
    # Die url/route ist '/uebungen'.
    # Template: Das HTML 'uebungengeneriert.html' wird gerendert.

    return render_template("uebungengeneriert.html") #html und daten noch undefiniert


if __name__ == "__main__":
    app.run(debug=True, port=5000)
