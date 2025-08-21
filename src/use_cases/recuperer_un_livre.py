from src.domain.livre import Livre
from src.domain.livre_repository import LivreRepository
from uuid import UUID

class RecupererUnLivre:
    def __init__(self, LivreRepository: LivreRepository):
        """
        Initialise le cas d'utilisation pour récupérer un livre.
        """
        self.livre_repository = LivreRepository
        pass

    def executer(self, livre_id: UUID) -> Livre | None : 
        """
        Args:
            livre_id (UUID): L'identifiant du livre à récupérer.
        returns:
            Livre | None: Le livre trouvé ou None si non trouvé.
        """
        return self.livre_repository.trouver_par_id(livre_id)