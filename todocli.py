"""
Gestionnaire de tâches CLI
Programme simple pour gérer une liste de tâches en mémoire
"""

import logging
from datetime import datetime

# Configuration du logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('todo_app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


class Task:
    """Représente une tâche avec un titre et un statut"""
    
    def __init__(self, title):
        self.title = title
        self.done = False
        self.created_at = datetime.now()
        
    def mark_done(self):
        """Marque la tâche comme terminée"""
        self.done = True
        
    def __str__(self):
        status = "✓" if self.done else " "
        return f"[{status}] {self.title}"


class TodoManager:
    """Gestionnaire principal des tâches"""
    
    def __init__(self):
        self.tasks = []
        logger.info("Initialisation du gestionnaire de tâches")
    
    def add_task(self, title):
        """
        Ajoute une nouvelle tâche
        
        Args:
            title (str): Le titre de la tâche
            
        Returns:
            bool: True si succès, False sinon
        """
        if not title or title.strip() == "":
            logger.warning("Tentative d'ajout d'une tâche vide")
            return False
            
        task = Task(title.strip())
        self.tasks.append(task)
        logger.info(f"Tâche ajoutée: {title}")
        return True
    
    def list_tasks(self):
        """Affiche toutes les tâches"""
        if len(self.tasks) == 0:
            print("\nAucune tâche pour le moment.")
            logger.info("Liste des tâches demandée (vide)")
            return
            
        print("\n=== Liste des tâches ===")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")
        print()
        logger.info(f"Affichage de {len(self.tasks)} tâche(s)")
    
    def mark_task_done(self, task_number):
        """
        Marque une tâche comme terminée
        
        Args:
            task_number (int): Le numéro de la tâche (commence à 1)
            
        Returns:
            bool: True si succès, False sinon
        """
        if task_number < 1 or task_number > len(self.tasks):
            logger.error(f"Numéro de tâche invalide: {task_number}")
            return False
            
        task = self.tasks[task_number - 1]
        task.mark_done()
        logger.info(f"Tâche {task_number} marquée comme terminée")
        return True
    
    def delete_task(self, task_number):
        """
        Supprime une tâche
        
        Args:
            task_number (int): Le numéro de la tâche (commence à 1)
            
        Returns:
            bool: True si succès, False sinon
        """
        if task_number < 1 or task_number > len(self.tasks):
            logger.error(f"Tentative de suppression d'une tâche inexistante: {task_number}")
            return False
            
        task = self.tasks.pop(task_number - 1)
        logger.info(f"Tâche supprimée: {task.title}")
        return True


def display_menu():
    """Affiche le menu principal"""
    print("\n" + "="*40)
    print("      GESTIONNAIRE DE TÂCHES")
    print("="*40)
    print("1. Ajouter une tâche")
    print("2. Lister les tâches")
    print("3. Marquer une tâche comme faite")
    print("4. Supprimer une tâche")
    print("5. Quitter")
    print("="*40)


def main():
    """Fonction principale du programme"""
    manager = TodoManager()
    logger.info("Démarrage de l'application")
    
    print("\nBienvenue dans le gestionnaire de tâches !")
    
    while True:
        display_menu()
        
        try:
            choice = input("\nVotre choix: ").strip()
            
            if choice == "1":
                # Ajouter une tâche
                title = input("Titre de la tâche: ")
                if manager.add_task(title):
                    print("✓ Tâche ajoutée avec succès!")
                else:
                    print("✗ Erreur: La tâche ne peut pas être vide.")
                    
            elif choice == "2":
                # Lister les tâches
                manager.list_tasks()
                
            elif choice == "3":
                # Marquer comme faite
                manager.list_tasks()
                if len(manager.tasks) > 0:
                    try:
                        num = int(input("Numéro de la tâche à marquer: "))
                        if manager.mark_task_done(num):
                            print("✓ Tâche marquée comme terminée!")
                        else:
                            print("✗ Erreur: Numéro de tâche invalide.")
                    except ValueError:
                        print("✗ Erreur: Veuillez entrer un nombre valide.")
                        logger.warning("Entrée invalide pour marquer une tâche")
                        
            elif choice == "4":
                # Supprimer une tâche
                manager.list_tasks()
                if len(manager.tasks) > 0:
                    try:
                        num = int(input("Numéro de la tâche à supprimer: "))
                        if manager.delete_task(num):
                            print("✓ Tâche supprimée!")
                        else:
                            print("✗ Erreur: Numéro de tâche invalide.")
                    except ValueError:
                        print("✗ Erreur: Veuillez entrer un nombre valide.")
                        logger.warning("Entrée invalide pour supprimer une tâche")
                        
            elif choice == "5":
                # Quitter
                print("\nMerci d'avoir utilisé le gestionnaire de tâches. À bientôt!")
                logger.info("Fermeture de l'application")
                break
                
            else:
                print("✗ Choix invalide. Veuillez choisir une option entre 1 et 5.")
                logger.warning(f"Choix de menu invalide: {choice}")
                
        except KeyboardInterrupt:
            print("\n\nInterruption détectée. Fermeture du programme...")
            logger.info("Interruption par l'utilisateur (Ctrl+C)")
            break
        except Exception as e:
            print(f"✗ Une erreur inattendue s'est produite: {e}")
            logger.error(f"Erreur inattendue: {e}", exc_info=True)


if __name__ == "__main__":
    main()
