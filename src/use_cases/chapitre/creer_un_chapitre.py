import uuid
from datetime import datetime

from src.domain.model.chapitre import Chapitre, CreationChapitreSchema
from src.domain.model.livre import Livre
from src.domain.repository.chapitre_repository import ChapitreRepository

class CreerUnChapitre:
    def __init__(self, chapitre_repository: ChapitreRepository): 
        self.chapitre_repository = chapitre_repository

    async def executer(
            self, 
            chapitre_data: CreationChapitreSchema, 
            livre: Livre
            )-> Chapitre: 
        nouveau_chapitre=Chapitre(
            id= uuid.uuid4(),
            titre=chapitre_data.titre,
            contenu=chapitre_data.contenu,
            numero_chapitre=chapitre_data.numero_chapitre,
            date_modification=datetime.now(),
            livre_id=livre.id, 
            livre=livre
        )
        await self.chapitre_repository.sauvegarder(nouveau_chapitre)
        return nouveau_chapitre

