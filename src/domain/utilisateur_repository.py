from abc import ABC, abstractmethod
from .utilisateur import Utilisateur

class UtilisateurRepository(ABC): 
    @abstractmethod
    async def trouver_par_email(self, email:str) -> Utilisateur | None:
        pass