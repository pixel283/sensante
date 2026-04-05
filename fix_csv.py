import pandas as pd

# Lire le fichier avec les bons paramètres
df = pd.read_csv("data/patients_dakar.csv", encoding="latin-1")

# Le réécrire au format standard (UTF-8, virgule comme séparateur)
df.to_csv("data/patients_dakar.csv", encoding="utf-8", index=False)

print("Fichier CSV nettoyé et converti en UTF-8 avec succès !")