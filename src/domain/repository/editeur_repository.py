from uuid import UUID
from abc import ABC, abstractmethod
from datetime import datetime 

from src.domain.model.editeur import Editeur, EditeurUpdateSchema

class EditeurRepository: 
    @abstractmethod
    async def sauvegarder(self, editeur: Editeur)-> None: 
        """Sauvegarder un editeur """
        pass

    @abstractmethod
    async def trouver_par_id(self, editeur_id: UUID) -> Editeur: 
        """ Trouver un editeur avec un ID """
        pass

    @abstractmethod
    async def mettre_a_jour(
        self, 
        editeur_modifier: EditeurUpdateSchema)-> Editeur:
        """Modifier un editeur"""
        pass
