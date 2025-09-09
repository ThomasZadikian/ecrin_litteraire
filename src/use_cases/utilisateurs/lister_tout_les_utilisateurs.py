from uuid import UUID
from src.domain.utilisateur import Utilisateur
from src.domain.utilisateur_repository import UtilisateurRepository

class ListerToutLesUtilisateurs: 
    def __init__(self, utilisateur_repository: UtilisateurRepository):
        self.utilisateur_repository = utilisateur_repository
        pass

    async def executer(self) -> list[Utilisateur]: 
        liste_utilisateur = await self.utilisateur_repository.lister_tout_les_utilisateurs()
        return liste_utilisateur

