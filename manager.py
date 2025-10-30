"""
Module contenant le gestionnaire de tâches
"""
import logging
from models import Task
from colors import Colors

logger = logging.getLogger(__name__)


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
            print(f"\n{Colors.info('Aucune tâche pour le moment.')}")
            logger.info("Liste des tâches demandée (vide)")
            return
            
        print(f"\n{Colors.title('═══ Liste des tâches ═══')}")
        for i, task in enumerate(self.tasks, 1):
            print(f"{Colors.MAGENTA}{i}.{Colors.RESET} {task}")
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
