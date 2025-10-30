"""
Gestionnaire de tâches CLI
Programme simple pour gérer une liste de tâches en mémoire
"""

import logging
import argparse
from manager import TodoManager
from ui import display_banner, display_menu
from colors import Colors



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






def parse_arguments():
    """Parse les arguments de la ligne de commande"""
    parser = argparse.ArgumentParser(
        description='Gestionnaire de tâches en ligne de commande',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples d'utilisation:
  python3 todocli.py              Lance le mode interactif
  python3 todocli.py -a "Faire les courses"
  python3 todocli.py -l
  python3 todocli.py -m 1
  python3 todocli.py -s 2
        """
    )
    
    parser.add_argument('-a', '--add', metavar='TITRE', 
                        help='Ajouter une nouvelle tâche')
    parser.add_argument('-l', '--list', action='store_true',
                        help='Lister toutes les tâches')
    parser.add_argument('-m', '--mark', metavar='NUM', type=int,
                        help='Marquer une tâche comme terminée')
    parser.add_argument('-s', '--supprimer', metavar='NUM', type=int,
                        help='Supprimer une tâche')
    
    return parser.parse_args()

def main():
    """Fonction principale du programme"""
    args = parse_arguments()
    manager = TodoManager()
    logger.info("Démarrage de l'application")
    
    # Mode ligne de commande
    if args.add:
        if manager.add_task(args.add):
            print(Colors.success("Tâche ajoutée avec succès!"))
        else:
            print(Colors.error("Erreur: La tâche ne peut pas être vide."))
        return
        
    if args.list:
        manager.list_tasks()
        return
        
    if args.mark:
        if manager.mark_task_done(args.mark):
            print(Colors.success("Tâche marquée comme terminée!"))
        else:
            print(Colors.error("Erreur: Numéro de tâche invalide."))
        return
        
    if args.supprimer:
        if manager.delete_task(args.supprimer):
            print(Colors.success("Tâche supprimée!"))
        else:
            print(Colors.error("Erreur: Numéro de tâche invalide."))
        return
    
    # Mode interactif (si aucun argument)
    display_banner()
    
    while True:
        display_menu()
        
        try:
            choice = input(f"\n{Colors.YELLOW}➤ Votre choix:{Colors.RESET} ").strip().lower()
            
            if choice == "a":
                # Ajouter une tâche
                title = input(f"{Colors.highlight('📝 Titre de la tâche:')} ")
                if manager.add_task(title):
                    print(Colors.success("Tâche ajoutée avec succès!"))
                else:
                    print(Colors.error("Erreur: La tâche ne peut pas être vide."))
                    
            elif choice == "l":
                # Lister les tâches
                manager.list_tasks()
                
            elif choice == "m":
                # Marquer comme faite
                manager.list_tasks()
                if len(manager.tasks) > 0:
                    try:
                        num = int(input(f"{Colors.highlight('🎯 Numéro de la tâche à marquer:')} "))
                        if manager.mark_task_done(num):
                            print(Colors.success("Tâche marquée comme terminée!"))
                        else:
                            print(Colors.error("Erreur: Numéro de tâche invalide."))
                    except ValueError:
                        print(Colors.error("Erreur: Veuillez entrer un nombre valide."))
                        logger.warning("Entrée invalide pour marquer une tâche")
                        
            elif choice == "s":
                # Supprimer une tâche
                manager.list_tasks()
                if len(manager.tasks) > 0:
                    try:
                        num = int(input(f"{Colors.highlight('🗑️  Numéro de la tâche à supprimer:')} "))
                        if manager.delete_task(num):
                            print(Colors.success("Tâche supprimée!"))
                        else:
                            print(Colors.error("Erreur: Numéro de tâche invalide."))
                    except ValueError:
                        print(Colors.error("Erreur: Veuillez entrer un nombre valide."))
                        logger.warning("Entrée invalide pour supprimer une tâche")
                        
            elif choice == "q":
                # Quitter
                print(f"\n{Colors.success('Merci d\'avoir utilisé le gestionnaire de tâches. À bientôt! 👋')}")
                logger.info("Fermeture de l'application")
                break
                
            else:
                print(Colors.error("Choix invalide. Veuillez choisir une option entre 1 et 5."))
                logger.warning(f"Choix de menu invalide: {choice}")
                
        except KeyboardInterrupt:
            print(f"\n\n{Colors.warning('Interruption détectée. Fermeture du programme...')}")
            logger.info("Interruption par l'utilisateur (Ctrl+C)")
            break
        except Exception as e:
            print(Colors.error(f"Une erreur inattendue s'est produite: {e}"))
            logger.error(f"Erreur inattendue: {e}", exc_info=True)


if __name__ == "__main__":
    main()
