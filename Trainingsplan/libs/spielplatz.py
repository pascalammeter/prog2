exercises = {
  "pull": {
    "0": {
      "name": "Kreuzheben",
      "schwierigkeitgrad": "advanced"
    },
    "1": {
      "name": "High Rows Maschine",
      "schwierigkeitgrad": "intermediate"
    }},
  "push": {

  },
  "legs": {

  }
}

daten = {
  "Pascal_Ammeter": [
    "maennlich",
    "180",
    "24",
    "advanced",
    "muskelaufbau",
    "viel",
    "unbestimmt"
  ],
  "Jeannine_Buerli": [
    "weiblich",
    "168", "24",
    "beginner",
    "mix",
    "mittel",
    "sechsmonate"
  ]
}

for id, data in exercises["pull"].items():
    if data["schwierigkeitgrad"] == "intermediate":
        print(data["name"])