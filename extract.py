import UnityPy
import os

BUNDLE_PATH = "/Applications/Monster Prom 4 Monster Con.app/Contents/Resources/Data/StreamingAssets/aa/StandaloneOSX/texts_assets_all.bundle"
OUTPUT_DIR = os.path.expanduser("~/Desktop/monsterprom_fr/english")

os.makedirs(OUTPUT_DIR, exist_ok=True)

env = UnityPy.load(BUNDLE_PATH)

count = 0
for obj in env.objects:
    if obj.type.name == "TextAsset":
        data = obj.read()
        name = data.m_Name
        raw = data.m_Script
        if isinstance(raw, bytes):
            raw = raw.decode('utf-8', errors='replace')
        
        out_path = os.path.join(OUTPUT_DIR, f"{name}.bytes")
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(raw)
        print(f"  ✓ {name}.bytes")
        count += 1

print(f"\n{count} fichiers extraits dans {OUTPUT_DIR}")
print("job done")
