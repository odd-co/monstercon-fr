import UnityPy
import os
import shutil

BUNDLE_PATH = "/Applications/Monster Prom 4 Monster Con.app/Contents/Resources/Data/StreamingAssets/aa/StandaloneOSX/texts_assets_all.bundle"
FRENCH_DIR = os.path.expanduser("./french")
OUTPUT_PATH = os.path.expanduser("./texts_assets_all.bundle")
french_files = {}
for filename in os.listdir(FRENCH_DIR):
    if filename.endswith(".bytes"):
        with open(os.path.join(FRENCH_DIR, filename), 'r', encoding='utf-8') as f:
            french_files[filename.replace(".bytes", "")] = f.read()

print(f"{len(french_files)} fichiers français chargés\n")
shutil.copy2(BUNDLE_PATH, OUTPUT_PATH)
env = UnityPy.load(OUTPUT_PATH)

replaced = 0
for obj in env.objects:
    if obj.type.name == "TextAsset":
        data = obj.read()
        name = data.m_Name  # ex: "english_events_guestintro"
        
        # Cherche le fichier french correspondant parce que PUTAIN EVIDEMENT C'ÉTAIT TROP COMPLIQUÉ DE JUSTE MODIFIER CEUX DANS ENGLISH
        french_name = name.replace("english_", "french_", 1)
        
        if french_name in french_files:
            data.m_Script = french_files[french_name]
            data.save()
            print(f"  ✓ {name} → {french_name}")
            replaced += 1
        else:
            print(f"  - {name} (pas de traduction, laissé en anglais)")

# Sauvegarder et compil avec le ptn de truc de unity la
with open(OUTPUT_PATH, "wb") as f:
    f.write(env.file.save(packer="lz4"))

print(f"\n{replaced} assets remplacés")
print(f"Bundle sauvegardé : {OUTPUT_PATH}")
print(f"\nDossiers:")
print(f"  Mac   : /Applications/Monster Prom 4 Monster Con.app/Content/Ressources/NTM Cherche toi même sur le readme")
print(f"  Win   : StreamingAssets/aa/StandaloneWindows64/")
print("")
print("Fichiers chargés :")
for k in sorted(french_files.keys()):
    print(f"  '{k}'")