import uuid
from datetime import datetime

from src.domain.model.editeur import Editeur, EditeurCreationSchema
from src.domain.repository.editeur_repository import EditeurRepository

class CreerUnediteur: 
    def __init__ (self, editeur_repository: EditeurRepository)-> None: 
        self.editeur_repository = editeur_repository

    async def executer(
            self, 
            editeur_data: EditeurCreationSchema
            ) -> Editeur: 
        nouveau_editeur= Editeur(
            id = uuid.uuid4(),
            nom = editeur_data.nom, 
            date_modification=datetime.now()
        )
        await self.editeur_repository.sauvegarder(nouveau_editeur)
        return nouveau_editeur

