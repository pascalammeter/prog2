import json
from libs import data

# wird von main ausgerufen, funktion safetojson wird abgespielt
# daten in json format gegliedert

def eingabedaten_speichern(vorname, nachname, geschlecht, groesse, gewicht, alter):
    json_daten = data.load_json()
    alle_personen = json_daten.get('personen', {})
    person = {"vorname": vorname, "nachname": nachname, "geschlecht": geschlecht, "groesse": groesse, "gewicht": gewicht, "alter": alter}
    alle_personen['person'][gewicht] = person
    json_daten["personen"] = alle_personen

    data.save_to_json(json_daten)
    return json_daten