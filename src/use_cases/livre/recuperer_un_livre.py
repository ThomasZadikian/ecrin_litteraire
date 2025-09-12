from src.domain.model.livre import Livre
from src.domain.repository.livre_repository import LivreRepository
from src.domain.model.utilisateur import Utilisateur
from uuid import UUID

class RecupererUnLivre:
    def __init__(self, livre_repository: LivreRepository):
        """
        Initialise le cas d'utilisation pour récupérer un livre.
        """
        self.livre_repository = livre_repository 
        pass

    async def executer(self, livre_id: UUID) -> Livre | None : 
        """
        Args:
            livre_id (UUID): L'identifiant du livre à récupérer.
        returns:
            Livre | None: Le livre trouvé ou None si non trouvé.
        """
        livre = await self.livre_repository.trouver_par_id(livre_id)
        return livre
    
class RecupererLivreParAuteur:
    def __init__(self, livre_repository: LivreRepository):
        self.livre_repository = livre_repository
        pass
    
    async def executer(self, auteur_name : Utilisateur) -> list[Livre] | None:
        """
        Args:
            auteur_name (str): Le nom de l'auteur dont on veut récupérer les livres.
        returns:
            list[Livre] | None: La liste des livres trouvés ou None si aucun trouvé.
        """
        livres = await self.livre_repository.trouver_par_auteur(auteur_name)
        return livres