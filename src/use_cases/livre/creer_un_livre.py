import uuid
from datetime import datetime

from src.domain.model.livre import Livre, LivreCreationSchema
from src.domain.repository.livre_repository import LivreRepository
from src.domain.model.utilisateur import Utilisateur
from src.domain.model.genre import Genre

class CreerUnLivre:
    def __init__ (self, livre_repository: LivreRepository): 
        self.livre_repository = livre_repository

    async def executer(self, livre_data: LivreCreationSchema, auteur: Utilisateur, genre: Genre ) -> Livre: 
        nouveau_livre = Livre(
            id= uuid.uuid4(),
            titre = livre_data.titre,
            date_publication = livre_data.date_publication,
            contenu_pour_majeur = livre_data.contenu_pour_majeur,
            date_d_ajout = datetime.now(),
            date_de_modification = datetime.now(),
            auteur_id = auteur.id,
            auteur =  auteur,
            genre = genre
        )
        await self.livre_repository.sauvegarder(nouveau_livre)
        return nouveau_livre 