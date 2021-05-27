from flask import Flask, render_template, request, redirect, url_for
from libs.eingabedaten_speichern import speichern_data, json_laden, speichern_logbuch
from libs.exercises_speichern import get_exercises

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

        # Wenn key=user bereits in exercises_user.json vorhanden, gib seine logbuchübungen aus.
        for key in exercises_user.keys():
            if key == f"{vorname}_{nachname}":
                exercises_user_vorhanden = logbucheintrag()
                return render_template("logbuch.html", people_with_exercises=exercises_user_vorhanden)

        # Falls user nicht vorhanden (=neuer user)
        list_exercises = get_exercises(f"{vorname}_{nachname}", erfahrung, ziel, frequenz, zeitplan)
        print(list_exercises)
        # get_exercises ist in libs/exercises_speichern.py
        return render_template("uebungengeneriert.html", vorname=vorname, nachname=nachname,
                                       list_exercises=list_exercises)

    return render_template("eingabedaten.html")  # Wenn nicht ausgefüllt, Startseite Laden.


def get_exercises_user():
    daten_exercises_user = json_laden("data/exercises_user.json")
    return daten_exercises_user


def get_people():
    daten_people = json_laden("data/data.json")
    return daten_people


def get_logbuch():
    logbuch_laden = json_laden("data/logbuch.json")
    return logbuch_laden


@app.route("/logbuch")
def logbuch():
    personen = get_people()  # Personendaten laden

    people_with_exercises = []  # Muss dieses dict als .json abgespeichert werden?
    for key, person in personen.items():
        uebungen_hohlen = get_exercises(key, person["erfahrung"], person["ziel"], person["frequenz"], person["zeitplan"])
        people_with_exercises.append(uebungen_hohlen)
        print(people_with_exercises)

    return render_template("logbuch.html", people_with_exercises=people_with_exercises)


@app.route("/logbucheintrag", methods=['GET', 'POST'])
def logbucheintrag():
    personen = get_people()

    if request.method == 'POST':
        satz_1 = request.form['satz_1']
        gewicht_1 = request.form['gewicht_1']
        satz_2 = request.form['satz_2']
        gewicht_2 = request.form['gewicht_2']
        satz_3 = request.form['satz_3']
        gewicht_3 = request.form['gewicht_3']

        for key, person in personen.items():
            if key in personen == personen[key]:
                entry_logbuch = {
                    f"{key}": {
                        "satz_1": satz_1,
                        "gewicht_1": gewicht_1,
                        "satz_2": satz_2,
                        "gewicht_2": gewicht_2,
                        "satz_3": satz_3,
                        "gewicht_3": gewicht_3
                    }
                }
                speichern_logbuch(entry_logbuch)  # Daten in JSON File speichern
                # auflisten_logbuch = logbuch_auflisten(key, satz_1, gewicht_1, satz_2, gewicht_2, satz_3, gewicht_3)
                dict_logbuch = get_logbuch()

                return redirect(url_for("logbucheintrag"))
                # return redirect(url_for("logbuch_auflisten"))
                # Wenn nicht ausgefüllt, Trainingsplan Laden
    return render_template("eingabedaten.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
