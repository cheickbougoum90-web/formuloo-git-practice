# formuloo-git-practice

Dépôt d'entraînement du ticket T1 « Git & GitHub, versioning et collaboration » (FOR44A_26-5), stage Formuloo, parcours Dev IA.

Il reproduit les conventions du dépôt Formuloo OS (GitLab) :

- `main` et `develop` : branches protégées, jamais modifiées directement
- `cheick-bougoum` : branche de livraison, créée depuis `develop`
- `cheick-bougoum/feature/<tâche>` : une sous-branche par tâche
- pull request de la sous-branche vers `cheick-bougoum`
- messages de commit au format Conventional Commits (`feat:`, `fix:`, `docs:`, `chore:`)

## Installation (Windows, Git Bash)

```bash
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
cp .env.example .env
python scripts/verifier_environnement.py   # doit afficher « Environnement IA OK »
```
