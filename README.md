# 📚 Ecrin Littéraire

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/ThomasZadikian/ecrin_litteraire/python.yml?branch=main)](https://github.com/ThomasZadikian/ecrin_litteraire/actions)
[![Docker](https://img.shields.io/badge/Docker-Yes-blue?logo=docker)](https://www.docker.com/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

**Projet Python à but pédagogique et expérimental**
⚠️ Contient des informations fictives ou critiques à des fins pédagogiques. Ne jamais inclure de vraies données sensibles.

---

<details>
<summary>📌 Table des matières</summary>

1. [🎯 Objectif du projet](#objectif-du-projet)
2. [🗂 Structure du projet](#structure-du-projet)
3. [⚙️ Installation](#installation)
4. [🚀 Utilisation](#utilisation)
5. [💬 Exemple de conversation](#exemple-de-conversation)
6. [🧪 Tests](#tests)
7. [💡 Bonnes pratiques](#bonnes-pratiques)
8. [🤝 Contribution](#contribution)
9. [📚 Futur développement](#futur-développement)

</details>

---

## 🎯 Objectif du projet

Ce projet vise à créer un **chatbot capable de** :

* Reconnaître les **émotions** et la **personnalité** des utilisateurs.
* Utiliser un **livre comme base de connaissances** pour générer des réponses contextualisées.

> Projet **éducatif et expérimental**, modulaire et évolutif.

---

## 🗂 Structure du projet

| Répertoire / Fichier  | Description                      |
| --------------------- | -------------------------------- |
| `src/`                | Code source principal            |
| `tests/`              | Tests unitaires et d’intégration |
| `alembic/`            | Migrations de base de données    |
| `docker-compose.yaml` | Configuration Docker Compose     |
| `requirements.txt`    | Dépendances Python               |
| `.github/workflows/`  | CI/CD via GitHub Actions         |
| `README.md`           | Documentation du projet          |

---

## ⚙️ Installation

1. **Cloner le dépôt** :

```bash
git clone https://github.com/ThomasZadikian/ecrin_litteraire.git
cd ecrin_litteraire
```

2. **Créer un environnement virtuel et installer les dépendances** :

```bash
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

3. **(Optionnel) Lancer Docker** :

```bash
docker-compose up
```

---

## 🚀 Utilisation

```python
from src.chatbot import ChatBot

# Initialiser le chatbot avec un livre
bot = ChatBot(book_path="books/moby_dick.txt")

# Interagir
response = bot.talk("Bonjour, comment ça va ?")
print(response)
```

* `book_path` : chemin vers le livre servant de base de connaissances.
* `talk()` : méthode pour dialoguer avec le chatbot.

---

## 💬 Exemple de conversation

```text
Utilisateur : Bonjour, je me sens triste aujourd'hui.
Chatbot  : Je comprends, la tristesse peut être difficile. Veux-tu en parler ?

Utilisateur : Oui, j’ai lu un passage de Moby Dick qui m’a bouleversé.
Chatbot  : Ah, ce passage peut toucher profondément. Parlons-en ensemble…
```

---

## 🧪 Tests

* Tests situés dans le répertoire `tests/`.
* Pour lancer les tests :

```bash
pytest
```

---

## 💡 Bonnes pratiques

* Ne jamais inclure de vraies données sensibles.
* Utiliser un fichier `.env` ou `config.py` pour les secrets.
* Ajouter des tests pour chaque nouvelle fonctionnalité.
* Maintenir un code propre et documenté.

---

## 🤝 Contribution

* Contributions bienvenues pour apprentissage et expérimentation.
* Respecter la structure du projet et ne pas committer de secrets réels.

---

## 📚 Futur développement

* Reconnaissance avancée des **émotions et personnalités**.
* Intégration de **plusieurs livres** pour enrichir le chatbot.
* Développement d’une **interface web ou GUI** pour faciliter l’interaction.
* Optimisation du modèle NLP pour des réponses plus naturelles et contextualisées.


README.md généré par IA. 