from flask import Flask, render_template, request, url_for, redirect

from libs import eingabedaten_speichern

app = Flask("Trainingsplan-Generator")


@app.route("/")
def startseite():
    """
    Summary:
        Zeigt die Startseite an, wenn die url/route '/' ist.
        Auf der Startseite kann man wählen, ob ein Event oder To Do hinzugefügt werden soll.
    Returns:
        template: Das HTML 'index.html' wird gerendert mit der Auswahlmöglichkeit
    """
    return render_template('index.html')


@app.route("/trainingsplan", methods=['GET', 'POST'])
def trainingsplan():
    """
    Summary:
        Hier kann der Trainingsplan erstellt werden. Dieser wird anhand der Eingabedaten generiert.
        Die url/route ist '/trainingsplan'.
    """
    if request.method == 'POST':
        print(request.form)
        vorname = request.form['vorname']
        nachname = request.form['nachname']
        geschlecht = request.form['geschlecht']
        groesse = request.form['groesse']
        gewicht = request.form['gewicht']
        alter = request.form['alter']
        # Daten in JSON File speichern, Funktion eingabedaten_speichern in eingabedaten_speichern.py
        returned_data = eingabedaten_speichern.eingabedaten_speichern(vorname, nachname, geschlecht, groesse, gewicht, alter)
        # Weiterleitug auf Übungen, primar key gewicht mitnehmen
        return redirect(url_for('uebungen'))
        # Wenn nicht ausgefüllt, Startseite Laden
    return render_template("eingabedaten.html")


@app.route("/uebungen")
def uebungen():
    """
    Summary:
        Hier werden alle Übungen angezeigt.
        Die url/route ist '/uebungen'.

    Returns:
        template: Das HTML 'uebungengeneriert.html' wird gerendert.
    """
    todo_daten = data.load_json()
    return render_template("uebungengeneriert.html", daten=x_daten) #html und daten noch undefiniert


if __name__ == "__main__":
    app.run(debug=True, port=5000)
