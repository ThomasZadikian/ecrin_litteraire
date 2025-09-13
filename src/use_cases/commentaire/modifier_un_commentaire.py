from uuid import UUID
from src.domain.model.commentaire import Commentaire, CommentaireUpdateSchema
from src.domain.repository.commentaire_repository import CommentaireRepository

class ModifierUnCommentaire: 
    def __init__(self, commentaire_repository: CommentaireRepository):
        self.commentaire_repository = commentaire_repository

    async def executer(self, commentaire_id: UUID, commentaire_data: CommentaireUpdateSchema) -> Commentaire: 
        commentaire = await self.commentaire_repository.trouver_par_id(commentaire_id)

        if not commentaire:  
            return None
        
        update_data = commentaire_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(commentaire, key, value)

        commentaire_a_jour = await self.commentaire_repository.mettre_a_jour(commentaire)
        return commentaire_a_jour
