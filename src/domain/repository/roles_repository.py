from uuid import UUID
from abc import ABC, abstractmethod
from datetime import datetime 

from src.domain.model.roles import Role, RoleUpdateSchema

class RoleRepository: 
    @abstractmethod
    async def sauvegarder(self, role: Role)-> None: 
        """Sauvegarder un chapitre """
        pass

    @abstractmethod
    async def trouver_par_id(self, role_id: UUID) -> Role: 
        """ Trouver un chapitre avec un ID """
        pass

    @abstractmethod
    async def mettre_a_jour(
        self, 
        chapitre_modifier: RoleUpdateSchema)-> Role:
        """Modifier un chapitre"""
        pass
