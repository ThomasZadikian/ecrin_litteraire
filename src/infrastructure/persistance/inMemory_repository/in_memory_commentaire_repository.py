from uuid import UUID
from src.domain.model.commentaire import Commentaire, CommentaireUpdateSchema

class InMemoryCommentaireRepository: 
    def __init__(self):  
        self.data: dict[UUID, Commentaire] = {}

    async def sauvegarder(self, commentaire: Commentaire)-> None: 
        self.data[commentaire.id] = commentaire

    async def trouver_par_id(self, commentaire_id: UUID) -> Commentaire | None: 
        return self.data.get(commentaire_id)
    
    async def mettre_a_jour(
            self, 
            commentaire: Commentaire)-> Commentaire | None:
         if commentaire.id in self.data:
            self.data[commentaire.id] = commentaire