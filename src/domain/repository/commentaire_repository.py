from uuid import UUID
from abc import ABC, abstractmethod
from datetime import datetime 

from src.domain.model.commentaire import Commentaire, CommentaireUpdateSchema

class CommentaireRepository: 
    @abstractmethod
    async def sauvegarder(self, commentaire: Commentaire)-> None: 
        """Sauvegarder un commentaire """
        pass

    @abstractmethod
    async def trouver_par_id(self, commentaire_id: UUID) -> Commentaire: 
        """ Trouver un commentaire avec un ID """
        pass

    @abstractmethod
    async def mettre_a_jour(
        self, 
        commentaire_modifier: CommentaireUpdateSchema)-> Commentaire:
        """Modifier un commentaire"""
        pass
