# Gestionnaire de Tâches (Todo Manager)

## Description

Application en ligne de commande (CLI) permettant de gérer simplement une liste de tâches. 
Le programme garde les tâches en mémoire pendant son exécution et permet d'effectuer les opérations de base : ajout, affichage, marquage comme terminée et suppression de tâches.

## Fonctionnalités

- **Ajouter une tâche** : Créer une nouvelle tâche avec un titre
- **Lister les tâches** : Afficher toutes les tâches avec leur statut
- **Marquer comme faite** : Cocher une tâche comme terminée
- **Supprimer une tâche** : Retirer une tâche de la liste
- **Quitter** : Fermer proprement l'application


## Exécution
```bash
python3 todocli.py
```

## Utilisation

Au lancement, un menu s'affiche avec 5 options :

```
========================================
      GESTIONNAIRE DE TÂCHES
========================================
1. Ajouter une tâche
2. Lister les tâches
3. Marquer une tâche comme faite
4. Supprimer une tâche
5. Quitter
========================================
```

### Exemples d'utilisation

**Ajouter une tâche :**
- Choisir l'option 1
- Entrer le titre de la tâche
- La tâche est ajoutée à la liste

**Voir ses tâches :**
- Choisir l'option 2
- Toutes les tâches s'affichent avec leur numéro et statut
- `[ ]` = tâche en cours
- `[✓]` = tâche terminée

**Marquer une tâche comme faite :**
- Choisir l'option 3
- La liste s'affiche automatiquement
- Entrer le numéro de la tâche à marquer
- La tâche est marquée avec un ✓

**Supprimer une tâche :**
- Choisir l'option 4
- La liste s'affiche automatiquement
- Entrer le numéro de la tâche à supprimer
- La tâche est retirée de la liste

## Structure du Code

Le programme est organisé en 3 parties principales :

### 1. Classe `Task`
Représente une tâche individuelle avec :
- Un titre
- Un statut (terminée ou non)
- Une date de création

### 2. Classe `TodoManager`
Gère l'ensemble des tâches avec les méthodes :
- `add_task()` : Ajoute une tâche
- `list_tasks()` : Affiche toutes les tâches
- `mark_task_done()` : Marque une tâche comme faite
- `delete_task()` : Supprime une tâche

### 3. Fonction `main()`
Boucle principale qui :
- Affiche le menu
- Récupère le choix de l'utilisateur
- Appelle les bonnes méthodes
- Gère les erreurs

## Gestion des Erreurs

L'application gère plusieurs types d'erreurs :

### Entrées invalides
- **Choix de menu invalide** : Si l'utilisateur entre autre chose que 1-5, un message d'erreur s'affiche
- **Numéro de tâche invalide** : Si le numéro n'existe pas, l'opération est annulée avec un message
- **Entrée non numérique** : Si l'utilisateur entre du texte au lieu d'un nombre, une erreur claire est affichée

### Cas particuliers
- **Tâche vide** : Impossible d'ajouter une tâche sans titre
- **Liste vide** : Message informatif si on essaie de lister/modifier sans tâches
- **Interruption** : Gestion propre de Ctrl+C pour quitter

Toutes les erreurs sont affichées à l'utilisateur avec un message clair et sont enregistrées dans les logs.

## Logs

Le programme génère automatiquement un fichier de logs `todo_app.log` qui enregistre :

- Le démarrage et l'arrêt de l'application
- Chaque ajout de tâche
- Les modifications (marquage comme fait)
- Les suppressions
- Toutes les erreurs rencontrées

### Format des logs :
```
2024-10-30 14:23:45,123 - INFO - Démarrage de l'application
2024-10-30 14:24:12,456 - INFO - Tâche ajoutée: Faire les courses
2024-10-30 14:25:03,789 - WARNING - Tentative d'ajout d'une tâche vide
2024-10-30 14:26:30,012 - ERROR - Numéro de tâche invalide: 10
```

Les logs permettent de :
- Suivre l'activité de l'application
- Déboguer en cas de problème
- Garder un historique des actions

## Choix Techniques

### Langage et outils
- **Python 3** : Langage simple et adapté pour une CLI
- **Module logging** : Pour une gestion professionnelle des logs
- **Classes** : Pour organiser le code de manière modulaire

### Architecture
Le code suit une approche orientée objet simple :
- Séparation des responsabilités (Task vs TodoManager)
- Méthodes courtes et dédiées
- Docstrings pour documenter les fonctions

### Gestion de la mémoire
Les tâches sont stockées dans une liste Python en mémoire. 
**Attention** : Les tâches sont perdues à la fermeture du programme (pas de sauvegarde sur disque).

### Interface utilisateur
- Menu textuel simple et clair
- Symboles visuels (✓, ✗) pour améliorer la lisibilité
- Messages d'erreur explicites
- Retours immédiats après chaque action

## Limitations Connues

- Les tâches ne sont pas sauvegardées (en mémoire uniquement)
- Pas de priorités ou de catégories pour les tâches
- Pas de dates d'échéance
- Interface en français uniquement

## Auteur

Projet réalisé dans le cadre d'un TP en B2 Informatique.

## Licence

Projet éducatif - Libre d'utilisation
