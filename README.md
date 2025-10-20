Projet Analyse Décisionnelle
===========================

Auteur : Konan Boh Christ
Date : 19 octobre 2025

Description :
Ce projet vise à optimiser les recommandations d'investissement court terme (horizon 2 ans) pour une société,
avec un budget maximum de 500 000 F CFA par client. L'objectif est de maximiser le profit total en sélectionnant
des actions (sans fractions, au plus une fois par action) à partir de datasets CSV.

Contenu :
- src/main.py : Code Python principal avec trois algorithmes :
  - Force Brute : Pour petits datasets (< 30 actions).
  - Programmation Dynamique (DP) : Solution optimale pour grands datasets.
  - Glouton : Approche rapide pour comparaison.
- data/data_small.csv : Dataset réduit (20 actions) pour tester Force Brute.
- data/data1.csv : Dataset 1 (957 actions) pour grands calculs.
- data/data2.csv : Dataset 2 (541 actions) pour grands calculs.

Outils Utilisés :
- **Python** : Version 3.8 ou supérieure (interpréteur principal).
- **pandas** : Bibliothèque pour manipuler les données CSV (version 1.5+ recommandée).
- **itertools** : Module standard Python pour les combinaisons (inclus avec Python).

Installation des Dépendances :
1. **Prérequis** : Assurez-vous d'avoir Python installé. Téléchargez-le depuis [python.org](https://www.python.org/downloads/)
   et installez-le (cochez "Add Python to PATH" lors de l'installation).
2. **Créer un environnement virtuel** (optionnel mais recommandé) :
   - Ouvre un terminal (PowerShell ou CMD) dans le dossier contenant ce projet.
   - Tape : `python -m venv venv` pour créer un environnement virtuel.
   - Active-le : `venv\Scripts\activate` (sur Windows) ou `source venv/bin/activate` (sur Mac/Linux).
3. **Installer pandas** :
   - Avec l’environnement activé (ou directement si pas d’environnement), tape :- Si une erreur survient, mets à jour pip : `python -m pip install --upgrade pip`.
4. **Vérification** :
- Tape `python --version` et `pip show pandas` pour confirmer les versions.

Instructions :
1. Placez les fichiers CSV (data_small.csv, data1.csv, data2.csv) dans un dossier 'data/' à la racine du projet.
2. Exécutez le script avec : `python src/main.py` dans le terminal, dans le dossier racine du projet, avec un environnement Python activé.
3. Les résultats affichent les actions sélectionnées, coûts, profits, et temps d'exécution pour chaque méthode.

Résultats :
- Force Brute : Exacte mais lente sur petits datasets.
- DP : Optimale mais plus lente sur grands datasets.
- Glouton : Rapide mais approximatif, utile pour comparaison.

Recommandation :
Préférer DP pour une solution optimale sur grands datasets, avec Glouton comme alternative rapide.