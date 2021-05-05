from flask import Flask, render_template, request, url_for, redirect

from libs.eingabedaten_speichern import speichern


app = Flask("Trainingsplan-Generator")


@app.route("/")
def startseite():
    name = False
    # Summary:
    # Zeigt die Startseite an, wenn die url/route '/' ist.
    # Auf der Startseite kann man wählen, ob ein Trainingsplan erstellt werden soll.
    # Returns:
    # template: Das HTML 'index.html' wird gerendert mit der Auswahlmöglichkeit
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
        print(entry)
        speichern(entry)
        # Daten in JSON File speichern, Funktion eingabedaten in eingabedaten_speichern.py
        # returned_data = eingabedaten_speichern.eingabedaten(vorname, nachname, geschlecht, groesse, gewicht, alter)
        # Weiterleitug auf Übungen, primar key mitnehmen?
        # return redirect(url_for('uebungen'))
        # Wenn nicht ausgefüllt, Startseite Laden
    return render_template("eingabedaten.html")

# @app.route("/speichern/<aktivitaet>")
# def speichern(aktivitaet):
#     zeitpunkt, aktivitaet = eingabedaten_speichern.aktivitaet_speichern(aktivitaet)
#
#     return "Gespeichert: " + aktivitaet + " um " + str(zeitpunkt)
#
#
# @app.route("/liste")
# def auflisten():
#     aktivitaeten = eingabedaten_speichern.aktivitaeten_laden()
#
#     aktivitaeten_liste = ""
#     for key, value in aktivitaeten.items():
#         zeile = str(key) + ": " + value + "<br>"
#         aktivitaeten_liste += zeile
#
#     return aktivitaeten_liste

@app.route("/uebungen")
def uebungen():
    """
    Summary:
        Hier werden alle Übungen angezeigt.
        Die url/route ist '/uebungen'.

    Returns:
        template: Das HTML 'uebungengeneriert.html' wird gerendert.
    """
    # todo_daten = data.load_json()
    return render_template("uebungengeneriert.html") #html und daten noch undefiniert


if __name__ == "__main__":
    app.run(debug=True, port=5000)
