from flask import Flask, render_template, request, redirect, url_for
from libs.eingabedaten_speichern import speichern_data, json_laden, speichern_logbuch
from libs.exercises_speichern import exercises
from libs.bmi_berechnen import get_idealer_bmi, bmi_berechnen, get_bmi, viz


app = Flask("Trainingsplan-Generator")


# Zeigt die Startseite an, wenn die url/route '/' ist.
# Auf der Startseite kann man wählen, ob ein Trainingsplan erstellt werden soll.
# template: Das HTML 'index.html' wird gerendert mit der Auswahlmöglichkeit
@app.route("/")
def startseite():
    return render_template('index.html')


# Hier kann der Trainingsplan erstellt werden. Dieser wird anhand der Eingabedaten generiert.
# Die url/route ist '/trainingsplan'.
@app.route("/trainingsplan", methods=['GET', 'POST'])
def trainingsplan():
    if request.method == 'POST':
        vorname = request.form['vorname']
        nachname = request.form['nachname']
        geschlecht = request.form['geschlecht']
        groesse = int(request.form['groesse'])
        gewicht = int(request.form['gewicht'])
        alter = int(request.form['alter'])
        erfahrung = request.form['erfahrung']
        ziel = request.form['ziel']
        frequenz = request.form['frequenz']
        zeitplan = request.form['zeitplan']
        entry_eingaben = {
            f"{vorname}_{nachname}": {
                "geschlecht": geschlecht,
                "groesse": groesse,
                "gewicht": gewicht,
                "alter": alter,
                "erfahrung": erfahrung,
                "ziel": ziel,
                "frequenz": frequenz,
                "zeitplan": zeitplan
            }
        }
        speichern_data(entry_eingaben)  # Daten in JSON File speichern.
        idealer_bmi = get_idealer_bmi(alter)  # Aufgrund vom Alter wird der alterspezifische ideale BMI ausgelesen.
        user_bmi = bmi_berechnen(gewicht, groesse)  # Berechnen des BMIs.
        bmi_kategorie = get_bmi(geschlecht, gewicht, groesse)  # Aufgrund von den Attributen wird die BMI-Kategorie ausgelesen.
        div = viz(geschlecht, gewicht, groesse)  # Plotly Visualisierung vom User-BMI und Idealen BMI.

        exercises_user = get_exercises_user()
        # Wenn user bereits in exercises_user.json vorhanden, gib seine logbuchübungen aus.
        for key, value in exercises_user.items():
            if value["user"] == f"{vorname}_{nachname}":
                return redirect(url_for("logbuch"))  # Quelle: https://stackoverflow.com/questions/14343812/redirecting-to-url-in-flask

        # Falls user nicht vorhanden (=neuer user):
        # Funktion 'exercises' ist in der Datei libs/exercises_speichern.py
        dict_exercises = exercises(f"{vorname}_{nachname}", erfahrung, ziel, frequenz, zeitplan)
        return render_template("uebungengeneriert.html",
                               vorname=vorname,
                               nachname=nachname,
                               idealer_bmi=idealer_bmi,
                               user_bmi=user_bmi,
                               bmi_kategorie=bmi_kategorie,
                               visualisierung=div,
                               dict_exercises=dict_exercises
                               )
    else:
        return render_template("eingabedaten.html")  # Wenn nicht ausgefüllt, Startseite Laden.


# Funktion, welche das JSON "exercises_user.json" lädt.
def get_exercises_user():
    daten_exercises_user = json_laden("data/exercises_user.json")
    return daten_exercises_user


# Funktion, welche das JSON "data.json" lädt.
def get_people():
    daten_people = json_laden("data/data.json")
    return daten_people


# Funktion, welche das JSON "exercises_logbuch.json" lädt.
def get_exercises_logbuch():
    exercises_logbuch = json_laden("data/exercises_logbuch.json")
    return exercises_logbuch


@app.route("/logbuch")
def logbuch():
    personen = get_people()  # Personendaten laden
    exercises_user = get_exercises_user()  # Generierte Übungen vom User laden
    people_with_exercises = {}
    for key, value in exercises_user.items():
        for name, person in personen.items():
            if value["user"] == name:  # Prüfen, ob der Vorname_Nachname identisch ist
                uebungen_hohlen = exercises(value["user"], person["erfahrung"], person["ziel"], person["frequenz"], person["zeitplan"])
                people_with_exercises.update(uebungen_hohlen)

    return render_template("logbuch.html", people_with_exercises=people_with_exercises)


@app.route("/logbucheintrag", methods=['GET', 'POST'])
def logbucheintrag():
    logbuch_exercices = get_exercises_user()

    if request.method == 'POST':
        satz1 = request.form['satz_1']  # https://stackoverflow.com/questions/64718832/flask-badrequestkeyerror-400-bad-request-the-browser-or-proxy-sent-a-reques
        gewicht1 = request.form['gewicht_1']
        satz2 = request.form['satz_2']
        gewicht2 = request.form['gewicht_2']
        satz3 = request.form['satz_3']
        gewicht3 = request.form['gewicht_3']

        for key, value in logbuch_exercices.items():
            entry_logbuch = {
                f"{key}": {
                    "user": value["user"],
                    "training": value["training"],
                    "name": value["name"],
                    "muskel": value["muskel"],
                    "split": value["splitc"],
                    "satz_1": satz1,
                    "gewicht_1": gewicht1,
                    "satz_2": satz2,
                    "gewicht_2": gewicht2,
                    "satz_3": satz3,
                    "gewicht_3": gewicht3
                }
            }
            speichern_logbuch(entry_logbuch)  # Daten in JSON File speichern

        logbuchdaten = get_exercises_logbuch()  # Logbuchdaten laden
        people_with_logbuch = {}
        for key, value in logbuchdaten.items():
            logbuchdaten_hohlen = key, value["user"], value["erfahrung"], value["ziel"], value["frequenz"], \
                                  value["zeitplan"], value["satz_1"], value["gewicht_1"], value["satz_2"], \
                                  value["gewicht_2"], value["satz_3"], value["gewicht_3"]
            people_with_logbuch.update(logbuchdaten_hohlen)

        return render_template("logbucheintrag.html", people_with_logbuch=people_with_logbuch)

    else:
        return render_template("logbuch.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
