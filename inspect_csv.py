with open("data/patients_dakar.csv", "r", encoding="latin-1") as f:
    lines = f.readlines()
    
print(f"Nombre total de lignes : {len(lines)}")
print("\n--- Lignes 90 à 100 ---")
for i in range(89, min(100, len(lines))):
    print(f"Ligne {i+1}: {repr(lines[i][:100])}")