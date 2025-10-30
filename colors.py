class Colors:
    """Codes couleurs ANSI pour le terminal"""
    # Couleurs de base
    RESET = '\033[0m'
    BOLD = '\033[1m'
    
    # Couleurs principales
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    
    # Couleurs de fond
    BG_BLUE = '\033[44m'
    BG_GREEN = '\033[42m'
    
    @staticmethod
    def success(text):
        """Texte de succès en vert"""
        return f"{Colors.GREEN}[+] {text}{Colors.RESET}"

    @staticmethod
    def error(text):
        """Texte d'erreur en rouge"""
        return f"{Colors.RED}[X] {text}{Colors.RESET}"
    
    @staticmethod
    def info(text):
        """Texte informatif en cyan"""
        return f"{Colors.CYAN}{text}{Colors.RESET}"
    
    @staticmethod
    def warning(text):
        """Texte d'avertissement en jaune"""
        return f"{Colors.YELLOW}{text}{Colors.RESET}"
    
    @staticmethod
    def title(text):
        """Titre en bleu gras"""
        return f"{Colors.BOLD}{Colors.BLUE}{text}{Colors.RESET}"
    
    @staticmethod
    def highlight(text):
        """Texte en surbrillance magenta"""
        return f"{Colors.MAGENTA}{text}{Colors.RESET}"
