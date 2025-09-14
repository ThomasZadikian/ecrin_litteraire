import uuid
from datetime import datetime

from src.domain.model.roles import Role, RoleCreateSchema
from src.domain.repository.roles_repository import RoleRepository

class CreerUnRole: 
    def __init__(self, role_repository: RoleRepository):
        self.role_repository = role_repository  

    async def executer(self, role_data: RoleCreateSchema) -> Role: 
        nouveau_role = Role(
            id = uuid.uuid4(), 
            nom = role_data.nom,
            date_creation=datetime.now(),
            date_modification=datetime.now()
        )
        await self.role_repository.sauvegarder(nouveau_role)
        return nouveau_role