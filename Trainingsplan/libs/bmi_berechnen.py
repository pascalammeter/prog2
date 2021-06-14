from plotly.offline import plot
import plotly.graph_objects as go


# Quelle BMI: https://www.smart-rechner.de/bmi_erw/rechner.php


# Funktion für das Ermitteln des idealen BMIs für das jeweilige Alter des Users
def get_idealer_bmi(alter):
    if alter <= 24:
        idealer_bmi = "19-24"
        return idealer_bmi

    elif 25 <= alter <= 34:  # Quelle: https://stackoverflow.com/questions/13628791/determine-whether-integer-is-between-two-other-integers
        idealer_bmi = "20-25"
        return idealer_bmi

    elif 35 <= alter <= 44:
        idealer_bmi = "21-26"
        return idealer_bmi

    elif 45 <= alter <= 54:
        idealer_bmi = "22-27"
        return idealer_bmi

    elif 55 <= alter <= 64:
        idealer_bmi = "23-28"
        return idealer_bmi

    elif alter >= 65:
        idealer_bmi = "24-29"
        return idealer_bmi


# Funktion wo der BMI des Users berechnet wird.
def bmi_berechnen(gewicht, groesse):
    groesse_in_meter = groesse / 100  # User gibt Grösse in cm an, deshalb umrechnen in Meter
    bmi = gewicht // (groesse_in_meter ** 2)  # Formel um BMI zu berechnen, ohne Rest
    return bmi


# Funktion wo aufgrund des Geschlechts und des BMIs die dazugehörige BMI-Kategorie ermittelt wird.
def get_bmi(geschlecht, gewicht, groesse):
    bmi = bmi_berechnen(gewicht, groesse)
    if geschlecht == "maennlich":
        if bmi <= 19.9:
            bmi_kategorie = "Untergewicht"
            return bmi_kategorie

        elif 20 <= bmi <= 24.9:
            bmi_kategorie = "Normalgewicht"
            return bmi_kategorie

        elif 25 <= bmi <= 29.9:
            bmi_kategorie = "Übergewicht"
            return bmi_kategorie

        elif 30 <= bmi <= 34.9:
            bmi_kategorie = "Starkes Übergewicht"
            return bmi_kategorie

        elif bmi >= 35:
            bmi_kategorie = "Adipositas"
            return bmi_kategorie

    elif geschlecht == "weiblich":
        if bmi <= 18.9:
            bmi_kategorie = "Untergewicht"
            return bmi_kategorie

        elif 19 <= bmi <= 23.9:
            bmi_kategorie = "Normalgewicht"
            return bmi_kategorie

        elif 24 <= bmi <= 29.9:
            bmi_kategorie = "Übergewicht"
            return bmi_kategorie

        elif 30 <= bmi <= 34.9:
            bmi_kategorie = "Starkes Übergewicht"
            return bmi_kategorie

        elif bmi >= 35:
            bmi_kategorie = "Adipositas"
            return bmi_kategorie


# Funktion wo mittels Plotly den User-BMI und den idealen Durschnitts-BMI visualisiert wird.
def viz(geschlecht, gewicht, groesse):  # Quelle: https://plotly.com/python/bar-charts/
    bmi = bmi_berechnen(gewicht, groesse)
    kategorie = get_bmi(geschlecht, gewicht, groesse)

    beschreibung = [kategorie, 'Durschnitts-BMI bei Normalgewicht']
    data = [bmi, 24]
    fig = go.Figure([go.Bar(x=beschreibung, y=data)])

    div = plot(fig, output_type="div")
    return div
