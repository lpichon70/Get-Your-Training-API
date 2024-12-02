# Get-Your-Training-API

<br>

## Description

API qui à pour but de décomposer chaques groupes musclulaires afin de mieux connaitre le fonctionnement de notre corp.

<br>

## Axes d'évolutions

Les axes d'éolutions sont de créer une applciation afin de générer des programmes de musculations adaptatif en fonction de la morfologie de chacun.

<br>

## Installation

1. Installer python (version du projet : 3.12.7)

2. Cloner votre dépôt à l'aide de l'outil GitHub Desktop ou avec cette commande de terminal :

```sh
   git clone https://github.com/lpichon70/Get-Your-Training-API.git
```

3. Créer un environnement virtuel python à la racine du projet : 

```sh
   python -m venv .env
```

4. Activer l'environnement virtuel

```sh
   .env\Scripts\activate
```

5. Télécharger les bibliothèques python utilisées par le projet

```sh
    pip install -r requirements.txt
```

6. Créer dans le dossier Get-Your-Training-API/src/Database un fichier config.ini.

7. Remplir les valeurs de connections à la base de données dans le fichier config.ini :

```
    [database]
    username= database_username
    password= database_password
```

8. Lancer L'API :

```sh
    fastapi dev main.py
```
