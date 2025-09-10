import uuid
from datetime import datetime

from src.domain.model.utilisateur import Utilisateur
from src.domain.repository.utilisateur_repository import UtilisateurRepository

class CreerUtilisateur: 
    def __init__(self, utilisateur_repository: UtilisateurRepository):
        self.utilisateur_repository = utilisateur_repository

    async def executer(self, utilisateur: Utilisateur, hashed_password: str) -> Utilisateur:
        nouveau_utilisateur= Utilisateur(
            id=uuid.uuid4(),
            prenom=utilisateur.prenom,
            nom_de_famille=utilisateur.nom_de_famille,
            date_de_naissance=utilisateur.date_de_naissance,
            email=utilisateur.email,
            mot_de_passe_hache=hashed_password,
        )
        await self.utilisateur_repository.sauvegarder_un_utilisateur(nouveau_utilisateur, hashed_password)
        return nouveau_utilisateur