class LivreNotFoundError(Exception):
    """Exception levée lorsque le livre n'est pas trouvé dans le dépôt."""
    pass

class AutheurNotFoundError(Exception):
    """Exception levée lorsque l'auteur n'est pas trouvé dans le dépôt."""
    pass