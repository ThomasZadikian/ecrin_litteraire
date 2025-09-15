from uuid import UUID
from src.domain.model.commentaire import Commentaire
from src.domain.repository.commentaire_repository import CommentaireRepository

class RecupererUnCommentaire: 
    def __init__(self, commentaire_repository: CommentaireRepository)-> None: 
        self.commentaire_repository = commentaire_repository

    async def executer(self, commentaire_id: UUID) -> Commentaire: 
        commentaire = await self.commentaire_repository.trouver_par_id(commentaire_id)
        return commentaire