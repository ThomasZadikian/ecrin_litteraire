from uuid import UUID
from src.domain.model.utilisateur import Utilisateur
from src.domain.repository.utilisateur_repository import UtilisateurRepository

class RecupererUnUtilisateur: 
    def __init__(self, utilisateur_repository: UtilisateurRepository): 
        self.utilisateur_repository = utilisateur_repository
        pass

    async def executer(
        self, 
        utilisateur_id: UUID
        ): 
        utilisateur = await self.utilisateur_repository.trouver_un_utilisateur_par_id(utilisateur_id)
        return utilisateur