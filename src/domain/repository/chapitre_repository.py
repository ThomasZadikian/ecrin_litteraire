from uuid import UUID
from abc import ABC, abstractmethod
from datetime import datetime 

from src.domain.model.chapitre import Chapitre, ChapitreUpdateSchema

class ChapitreRepository: 
    @abstractmethod
    async def sauvegarder(self, chapitre: Chapitre)-> None: 
        """Sauvegarder un chapitre """
        pass

    @abstractmethod
    async def trouver_par_id(self, chapitre_id: UUID) -> Chapitre: 
        """ Trouver un chapitre avec un ID """
        pass

    @abstractmethod
    async def mettre_a_jour(
        self, 
        chapitre_modifier: ChapitreUpdateSchema)-> Chapitre:
        """Modifier un chapitre"""
        pass
