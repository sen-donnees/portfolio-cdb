# Portfolio CDB

**[→ Voir le site](https://sen-donnees.github.io/portfolio-cdb/)**

Portfolio de **Cheikh Darou Beye** : Data Scientist & développeur full stack.
Direction artistique : *Data × Code × Product*, sombre, bilingue FR/EN.

> État : 12 pages statiques (accueil, projets, approche, à propos, contact, 7 études de cas), CV téléchargeable.
> Servies telles quelles (HTML/CSS/JS autonomes, pas de templates Django). La migration vers de vraies routes
> `/fr/` et `/en/` viendra dans une prochaine étape.

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

Le serveur Django ci-dessus est un confort de développement local uniquement ; il n'est pas déployé.
En production, les pages sont servies en statique pur (voir `index.html` à la racine).

## Pages

| Adresse | Contenu |
|---|---|
| `/prototypes/hero-v1.html` | Accueil (nuage de points interactif) |
| `/prototypes/work-v1.html` | Projets sélectionnés + diagramme ternaire |
| `/prototypes/approche-v1.html` | Approche de travail |
| `/prototypes/about-v1.html` | À propos |
| `/prototypes/contact-v1.html` | Contact |
| `/prototypes/case-study-v1.html` | Étude de cas — DocuSen |
| `/prototypes/case-study-yoonujob-v1.html` | Étude de cas — YoonuJob |
| `/prototypes/case-study-senbiostat-v1.html` | Étude de cas — SenBioStat |
| `/prototypes/case-study-miellee-v1.html` | Étude de cas — Miellée (ITSAP / INRAE) |
| `/prototypes/case-study-microbes-v1.html` | Étude de cas — Microbes / ML |
| `/prototypes/case-study-sentazur-v1.html` | Étude de cas — Sentazur |
| `/prototypes/case-study-clients-v1.html` | Étude de cas — Sites clients (AJEL, Keur Moussa) |

Les couleurs, polices et mesures sont définies dans `prototypes/tokens.css`.
Le CV (PDF) est dans `prototypes/assets/`, généré par `cv/build_cv.py` (python-docx).

## Structure

```
index.html       redirection racine -> /prototypes/hero-v1.html (nécessaire pour GitHub Pages)
robots.txt, sitemap.xml
config/           réglages Django (serveur de dev local uniquement, sans base de données)
prototypes/       pages HTML autonomes + tokens.css + favicons + assets/
cv/               script de génération du CV (python-docx)
manage.py
requirements.txt
```

## Règles de contenu

- Aucune technologie ni chiffre non vérifié dans le code des projets présentés.
- Confidentialité : ITSAP / Miellée et bioMérieux uniquement en méthode et technologies.
- Pas de téléphone ni d'adresse en public sur le site (le CV téléchargeable en contient, à usage de candidature).
