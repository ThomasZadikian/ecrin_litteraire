from uuid import UUID

from domain.model.utilisateur import Utilisateur
from domain.repository.utilisateur_repository import UtilisateurRepository

class SupprimerUnUtilisateur: 
    def __ini__(self, utilisateur_repository: UtilisateurRepository):
        self.utilisateur_repository = utilisateur_repository

    async def executer(self, utilisateur_id: UUID) -> None: 
        await self.utilisateur_repository.supprimer_un_utilisateur(utilisateur_id)
        return None