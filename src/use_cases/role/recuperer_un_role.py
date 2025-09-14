from uuid import UUID
from src.domain.model.roles import Role
from src.domain.repository.roles_repository import RoleRepository

class RecupererUnRole: 
    def __init__(self, role_repository: RoleRepository): 
        self.role_repository = role_repository  

    async def executer(self, role_id: UUID) -> Role | None: 
        role = await self.role_repository.trouver_par_id(role_id)
        return role