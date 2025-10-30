"""
Module gérant l'interface utilisateur
"""
from colors import Colors


def display_menu():
    """Affiche le menu principal"""
    print(f"\n{Colors.BLUE}{'='*40}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}      GESTIONNAIRE DE TÂCHES{Colors.RESET}")
    print(f"{Colors.BLUE}{'='*40}{Colors.RESET}")
    print(f"{Colors.GREEN}a.{Colors.RESET} Ajouter une tâche")
    print(f"{Colors.CYAN}l.{Colors.RESET} Lister les tâches")
    print(f"{Colors.YELLOW}m.{Colors.RESET} Marquer une tâche comme faite")
    print(f"{Colors.RED}s.{Colors.RESET} Supprimer une tâche")
    print(f"{Colors.MAGENTA}q.{Colors.RESET} Quitter")
    print(f"{Colors.BLUE}{'='*40}{Colors.RESET}")


def display_banner():
    """Affiche la bannière ASCII du programme"""
    banner = f"""{Colors.CYAN}
@@@@@@@   @@@@@@   @@@@@@@    @@@@@@       @@@@@@@  @@@       @@@     @@@@@@@@@@    @@@@@@   @@@  @@@   @@@@@@    @@@@@@@@  @@@@@@@@  @@@@@@@   
@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@     @@@@@@@@  @@@       @@@     @@@@@@@@@@@  @@@@@@@@  @@@@ @@@  @@@@@@@@  @@@@@@@@@  @@@@@@@@  @@@@@@@@  
  @@!    @@!  @@@  @@!  @@@  @@!  @@@     !@@       @@!       @@!     @@! @@! @@!  @@!  @@@  @@!@!@@@  @@!  @@@  !@@        @@!       @@!  @@@  
  !@!    !@!  @!@  !@!  @!@  !@!  @!@     !@!       !@!       !@!     !@! !@! !@!  !@!  @!@  !@!!@!@!  !@!  @!@  !@!        !@!       !@!  @!@  
  @!!    @!@  !@!  @!@  !@!  @!@  !@!     !@!       @!!       !!@     @!! !!@ @!@  @!@!@!@!  @!@ !!@!  @!@!@!@!  !@! @!@!@  @!!!:!    @!@!!@!   
  !!!    !@!  !!!  !@!  !!!  !@!  !!!     !!!       !!!       !!!     !@!   ! !@!  !!!@!!!!  !@!  !!!  !!!@!!!!  !!! !!@!!  !!!!!:    !!@!@!    
  !!:    !!:  !!!  !!:  !!!  !!:  !!!     :!!       !!:       !!:     !!:     !!:  !!:  !!!  !!:  !!!  !!:  !!!  :!!   !!:  !!:       !!: :!!   
  :!:    :!:  !:!  :!:  !:!  :!:  !:!     :!:        :!:      :!:     :!:     :!:  :!:  !:!  :!:  !:!  :!:  !:!  :!:   !::  :!:       :!:  !:!  
   ::    ::::: ::   :::: ::  ::::: ::      ::: :::   :: ::::   ::     :::     ::   ::   :::   ::   ::  ::   :::   ::: ::::   :: ::::  ::   :::  
   :      : :  :   :: :  :    : :  :       :: :: :  : :: : :  :        :      :     :   : :  ::    :    :   : :   :: :: :   : :: ::    :   : :
{Colors.RESET}"""
    print(banner)
