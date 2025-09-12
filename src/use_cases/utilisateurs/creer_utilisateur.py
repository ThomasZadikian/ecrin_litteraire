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
            date_de_naissance=utilisateur.date_de_naissance if utilisateur.date_de_naissance else None,
            email=utilisateur.email,
            avatar=utilisateur.avatar if utilisateur.avatar else None,
            cgu=utilisateur.cgu,
            rgpd=utilisateur.rgpd,
            cookies=utilisateur.cookies,
            date_de_creation_du_compte=datetime.now(),
            date_de_modification=datetime.now(),
            mot_de_passe_hache=hashed_password,
            livre=None,
            commentaire=None,
            auteur_prefere_id=None,
            chatbot_prefere_id=None,
            role_id=uuid.uuid4()
        )
        await self.utilisateur_repository.sauvegarder_un_utilisateur(nouveau_utilisateur, hashed_password)
        return nouveau_utilisateur