"""
Module contenant la définition du modèle Task
"""
from datetime import datetime
from colors import Colors


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
        if self.done:
            status = f"{Colors.GREEN}+{Colors.RESET}"
            title = f"{Colors.WHITE}{self.title}{Colors.RESET}"
        else:
            status = f"{Colors.YELLOW} {Colors.RESET}"
            title = f"{Colors.CYAN}{self.title}{Colors.RESET}"

