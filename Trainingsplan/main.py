from flask import Flask, render_template, request
from libs.eingabedaten_speichern import speichern_data, json_laden, speichern_logbuch
from libs.exercises_speichern import exercises

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
        entry_eingaben = {
            f"{vorname}_{nachname}": {
                "geschlecht": geschlecht,
                "groesse": groesse,
                "alter": alter,
                "erfahrung": erfahrung,
                "ziel": ziel,
                "frequenz": frequenz,
                "zeitplan": zeitplan
            }
        }
        speichern_data(entry_eingaben)  # Daten in JSON File speichern.
        # auflisten = exercises_auflisten(vorname, nachname, erfahrung, ziel, frequenz, zeitplan)

        exercises_user = get_exercises_user()

        # Wenn user bereits in exercises_user.json vorhanden, gib seine logbuchübungen aus.
        for key, value in exercises_user.items():
            for item in value:
                if item == f"{vorname}_{nachname}":
                    exercises_user_vorhanden = logbucheintrag()
                    return render_template("logbuch.html", people_with_exercises=exercises_user_vorhanden)

        # Falls user nicht vorhanden (=neuer user):
        dict_exercises = exercises(f"{vorname}_{nachname}", erfahrung, ziel, frequenz, zeitplan)

        # get_exercises ist in libs/exercises_speichern.py
        return render_template("uebungengeneriert.html", vorname=vorname, nachname=nachname, dict_exercises=dict_exercises)

    return render_template("eingabedaten.html")  # Wenn nicht ausgefüllt, Startseite Laden.


def get_exercises_user():
    daten_exercises_user = json_laden("data/exercises_user.json")
    return daten_exercises_user


def get_people():
    daten_people = json_laden("data/data.json")
    return daten_people


@app.route("/logbuch")
def logbuch():
    personen = get_people()  # Personendaten laden

    people_with_exercises = {}
    for key, person in personen.items():
        uebungen_hohlen = exercises(key, person["erfahrung"], person["ziel"], person["frequenz"], person["zeitplan"])
        people_with_exercises.update(uebungen_hohlen)
        # uebungen_hohlen = exercises(key, person["erfahrung"], person["ziel"], person["frequenz"], person["zeitplan"])
        # people_with_exercises.append(uebungen_hohlen)

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

        # for key, person in personen.items():
        #     print(key)
        #     if key in personen == personen[key]:
        #         print(key)
        #         print(personen[key])

        entry_logbuch = {  # f"{key}": {
                "satz_1": satz1,
                "gewicht_1": gewicht1,
                "satz_2": satz2,
                "gewicht_2": gewicht2,
                "satz_3": satz3,
                "gewicht_3": gewicht3
        }

        for key, values in logbuch_exercices.items():
            for item in values:
                speichern_logbuch(entry_logbuch[item])  # Daten in JSON File speichern
                print(item)
                print(speichern_logbuch())
        # auflisten_logbuch = logbuch_auflisten(key, satz_1, gewicht_1, satz_2, gewicht_2, satz_3, gewicht_3)

        people_with_exercises = logbuch()
        print(people_with_exercises)
        logbuch_daten = get_exercises_user()
        print(logbuch_daten)

        eintrag_logbuch = []
        for key, value in logbuch_daten.items():
            print(key)
            print(value)
            logbuch_hohlen = logbuch_daten(f"{key}", satz1, gewicht1, satz2, gewicht2, satz3, gewicht3)
            eintrag_logbuch.append(logbuch_hohlen)
            print(eintrag_logbuch)

        return render_template("logbucheintrag.html", people_with_exercises=people_with_exercises, eintrag_logbuch=eintrag_logbuch)
        # return redirect(url_for("logbuch_auflisten"))
        # Wenn nicht ausgefüllt, Trainingsplan Laden
    else:
        return render_template("logbuch.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
