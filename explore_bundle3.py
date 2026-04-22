#!/usr/bin/env python3
import UnityPy
import argparse
import sys
from pathlib import Path
from glob import glob

DEFAULT_BUNDLE_DIR = "/Users/aalllaaasss/Bordel/Monster Prom 4 Monster Con.app/Contents/Resources/Data/StreamingAssets/aa/StandaloneOSX"

def load_assets(bundle_dir):
    """Charge tous les TextAssets de tous les bundles du dossier"""
    bundle_path = Path(bundle_dir)
    
    if not bundle_path.exists():
        print(f"❌ Dossier introuvable: {bundle_dir}", file=sys.stderr)
        sys.exit(1)
    
    # Trouver tous les fichiers bundle (pas d'extension ou pas de point)
    bundle_files = [f for f in bundle_path.iterdir() 
                    if f.is_file() and not f.name.startswith('.')]
    
    if not bundle_files:
        print(f"❌ Aucun bundle trouvé dans: {bundle_dir}", file=sys.stderr)
        sys.exit(1)
    
    print(f"📦 {len(bundle_files)} bundle(s) trouvé(s)", file=sys.stderr)
    
    assets = []
    
    for bundle_file in bundle_files:
        try:
            print(f"  ⏳ Chargement: {bundle_file.name}", file=sys.stderr)
            env = UnityPy.load(str(bundle_file))
            
            for obj in env.objects:
                if obj.type.name == "TextAsset":
                    data = obj.read()
                    raw = data.m_Script
                    
                    if isinstance(raw, bytes):
                        raw = raw.decode('utf-8', errors='replace')
                    
                    assets.append({
                        'id': obj.path_id,
                        'name': data.m_Name,
                        'bundle': bundle_file.name,
                        'content': raw if raw else "",
                        'preview': str(raw)[:80].replace('\n', ' ') if raw else "(vide)"
                    })
        except Exception as e:
            print(f"  ⚠️  Erreur avec {bundle_file.name}: {e}", file=sys.stderr)
            continue
    
    return assets

def search_assets(assets, query):
    """Filtre les assets par contenu (case-insensitive)"""
    query_lower = query.lower()
    return [a for a in assets if query_lower in a['content'].lower()]

def sort_assets(assets, sort_by):
    """Trie les assets selon le critère"""
    if sort_by == 'name':
        return sorted(assets, key=lambda x: x['name'])
    elif sort_by == 'size':
        return sorted(assets, key=lambda x: len(x['content']), reverse=True)
    elif sort_by == 'bundle':
        return sorted(assets, key=lambda x: (x['bundle'], x['name']))
    elif sort_by == 'id':
        return sorted(assets, key=lambda x: x['id'])
    return assets

def main():
    parser = argparse.ArgumentParser(
        description="Cherche et trie les TextAssets de tous les bundles d'un dossier",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples:
  python bundle_search.py                                    # Dossier par défaut, liste tous
  python bundle_search.py "SMART"                            # Cherche "SMART"
  python bundle_search.py "dialogue" --sort name             # Cherche et trie par nom
  python bundle_search.py "quest" --dir /chemin/custom       # Dossier custom
  python bundle_search.py "SMART" --sort size -v             # Verbose + tri
        """
    )
    
    parser.add_argument(
        'search',
        nargs='?',
        default=None,
        help="Mot-clé à chercher dans le contenu (case-insensitive)"
    )
    
    parser.add_argument(
        '--dir',
        dest='bundle_dir',
        default=DEFAULT_BUNDLE_DIR,
        help=f"Dossier contenant les bundles (défaut: {DEFAULT_BUNDLE_DIR})"
    )
    
    parser.add_argument(
        '--sort',
        choices=['name', 'size', 'id', 'bundle'],
        default='id',
        help="Trier par: name (alphabétique), size (contenu), bundle, id (défaut)"
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help="Afficher le contenu complet au lieu du preview"
    )
    
    parser.add_argument(
        '-c', '--count',
        action='store_true',
        help="Afficher juste le nombre de résultats"
    )
    
    args = parser.parse_args()
    
    print("⏳ Chargement des bundles...", file=sys.stderr)
    assets = load_assets(args.bundle_dir)
    print(f"✓ {len(assets)} assets trouvés\n", file=sys.stderr)
    
    # Filtrer par recherche
    if args.search:
        assets = search_assets(assets, args.search)
        print(f"🔍 Résultats pour '{args.search}': {len(assets)} asset(s)\n", file=sys.stderr)
    
    # Trier
    assets = sort_assets(assets, args.sort)
    
    # Afficher
    if args.count:
        print(len(assets))
        return
    
    if not assets:
        print("❌ Aucun asset trouvé", file=sys.stderr)
        return
    
    for asset in assets:
        if args.verbose:
            print(f"\n[{asset['bundle']}] [{asset['id']}] {asset['name']}")
            print("─" * 80)
            print(asset['content'][:500])  # Premiers 500 caractères
            if len(asset['content']) > 500:
                print(f"... (+{len(asset['content']) - 500} chars)")
        else:
            print(f"  [{asset['bundle']}] {asset['name']} → {asset['preview']}")

if __name__ == "__main__":
    main()