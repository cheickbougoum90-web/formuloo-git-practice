"""Vérifie que les dépendances du projet sont installées."""
import importlib
import sys

MODULES = ["numpy", "pandas", "sklearn", "matplotlib", "dotenv"]


def main() -> int:
    print(f"Python {sys.version.split()[0]}")
    manquants = []
    for nom in MODULES:
        try:
            importlib.import_module(nom)
            print(f"  OK   {nom}")
        except ImportError:
            manquants.append(nom)
            print(f"  ABSENT {nom}")
    if manquants:
        print("Environnement incomplet : pip install -r requirements.txt")
        return 1
    print("Environnement IA OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
