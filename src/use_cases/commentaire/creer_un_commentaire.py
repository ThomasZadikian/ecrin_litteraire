import uuid
from datetime import datetime

from src.domain.model.utilisateur import Utilisateur
from src.domain.model.livre import Livre
from src.domain.repository.commentaire_repository import CommentaireRepository
from src.domain.model.commentaire import Commentaire, CommentaireCreationSchema

class CreerUnCommentaire: 
    def __init__ (self, commentaire_repository: CommentaireRepository)-> None: 
        self.commentaire_repository = commentaire_repository

    async def executer(
            self, 
            commentaire_data: CommentaireCreationSchema,
            auteur: Utilisateur, 
            livre: Livre
            ) -> Commentaire: 
        nouveau_commentaire= Commentaire(
            id = uuid.uuid4(),
            contenu = commentaire_data.contenu, 
            date_creation=datetime.now(), 
            auteur_id=auteur.id,
            auteur = auteur, 
            livre_id = livre.id, 
            livre = livre
        )
        await self.commentaire_repository.sauvegarder(nouveau_commentaire)
        return nouveau_commentaire

