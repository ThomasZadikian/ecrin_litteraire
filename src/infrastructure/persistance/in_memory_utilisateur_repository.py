from uuid import UUID
from domain.model.utilisateur import Utilisateur
from domain.repository.utilisateur_repository import UtilisateurRepository

class InMemoryUtilisateurRepository: 
    def __init__(self): 
        self.data: dict[UUID, Utilisateur] = {}
        self.hashed_passwords: dict[UUID, str] = {}


    async def sauvegarder_un_utilisateur(self, utilisateur: Utilisateur, hashed_password: str) -> Utilisateur | None: 
        self.data[utilisateur.id] = utilisateur
        self.hashed_passwords[utilisateur.id] = hashed_password

    async def trouver_un_utilisateur_par_id(self, utilisateur_id: UUID) -> Utilisateur | None: 
        return self.data.get(utilisateur_id)
    
    async def lister_tout_les_utilisateurs(self) -> list[Utilisateur]: 
        return list(self.data.values())