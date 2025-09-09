from abc import ABC, abstractmethod
from .utilisateur import Utilisateur

class UtilisateurRepository(ABC): 
    @abstractmethod
    async def trouver_par_email(self, email:str) -> Utilisateur | None:
        pass

    @abstractmethod
    async def sauvegarder_un_utilisateur(self, utilisateur: Utilisateur, hashed_password: str) -> None:
        pass

    @abstractmethod
    async def trouver_un_utilisateur_par_id(self, id) -> Utilisateur | None: 
        pass

    @abstractmethod 
    async def lister_tout_les_utilisateurs(self) -> list[Utilisateur]:
        pass
