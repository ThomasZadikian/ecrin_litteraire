from domain.model.utilisateur import Utilisateur
from domain.repository.utilisateur_repository import UtilisateurRepository
from src.infrastructure.security import verifier_mot_de_passe

class AuthentifierUtilisateur:
    def __init__(self, utilisateur_repository: UtilisateurRepository):
        self.utilisateur_repository = utilisateur_repository

    async def executer(self, email: str, mot_de_passe: str) -> Utilisateur | None:
        utilisateur = await self.utilisateur_repository.trouver_par_email(email)
        if not utilisateur:
            return None
        utilisateur_db = await self.utilisateur_repository.trouver_db_par_email(email)
        if not verifier_mot_de_passe(mot_de_passe, utilisateur_db.hashed_password):
            return None
            
        return utilisateur