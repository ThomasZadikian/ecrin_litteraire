from abc import ABC, abstractmethod
from src.domain.model.utilisateur import Utilisateur
from uuid import UUID

class UtilisateurRepository(ABC): 
    @abstractmethod
    async def trouver_par_email(self, email:str) -> Utilisateur | None:
        pass

    @abstractmethod
    async def sauvegarder_un_utilisateur(self, utilisateur: Utilisateur, hashed_password: str) -> None:
        pass

    @abstractmethod
    async def trouver_par_id(self, id) -> Utilisateur | None: 
        pass

    @abstractmethod 
    async def lister_tout_les_utilisateurs(self) -> list[Utilisateur]:
        pass

    @abstractmethod
    async def supprimer_un_utilisateur(self, utilisateur_id) -> None: 
        pass

    @abstractmethod 
    async def modifier_un_utilisateur(self, utilisateur: Utilisateur, utilisateur_id: UUID) -> None: 
        pass