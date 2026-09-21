# Portfolio CDB

Portfolio de **Cheikh Darou Beye** : Data Scientist & développeur full stack.
Direction artistique : *Data × Code × Product*, sombre, bilingue FR/EN.

> État : prototypes de design validés. Le vrai site (templates Django, URLs `/fr/` et `/en/`) reste à construire.

## Lancer en local

```bash
cd ~/mes_projets/portfolio-cdb
conda create -n portfolio_cdb python=3.12 -y   # une seule fois
conda activate portfolio_cdb
pip install -r requirements.txt                # une seule fois
python manage.py runserver
```

Puis ouvrir **http://localhost:8000/** (et non `0.0.0.0`).
Si le port 8000 est pris : `python manage.py runserver 8001`.

## Pages (prototypes)

| Adresse | Contenu |
|---|---|
| `/prototypes/hero-v1.html` | Hero (nuage de points interactif) |
| `/prototypes/work-v1.html` | Index des projets + diagramme ternaire |
| `/prototypes/case-study-v1.html` | Étude de cas DocuSen |
| `/prototypes/case-study-yoonujob-v1.html` | Étude de cas YoonuJob |
| `/prototypes/design-system-v1.html` | Design system (palette, typo, grille, composants…) |

Les couleurs, polices et mesures sont définies dans `prototypes/tokens.css`.

## Structure

```
config/          réglages Django (serveur de prototypes, sans base de données)
prototypes/      pages HTML autonomes + tokens.css + favicon
manage.py
requirements.txt
```

## Règles de contenu

- Aucune technologie ni chiffre non vérifié dans le code des projets présentés.
- Confidentialité : ITSAP / Miellée et bioMérieux uniquement en méthode et technologies.
- Pas de téléphone ni d'adresse en public.
