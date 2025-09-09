import uuid
from datetime import datetime

from src.domain.livre import Livre, LivreCreationSchema
from src.domain.livre_repository import LivreRepository

class CreerUnLivre:
    def __init__ (self, livre_repository: LivreRepository):
        self.livre_repository = livre_repository

    async def executer(self, livre_data: LivreCreationSchema) -> Livre: 
        nouveau_livre = Livre(
            id=uuid.uuid4(),
            titre=livre_data.titre, 
            contenu=livre_data.contenu, 
            auteur=livre_data.auteur,
            date_publication=datetime.now()
        )
        await self.livre_repository.sauvegarder(nouveau_livre)
        return nouveau_livre 