from uuid import UUID
from src.domain.model.roles import Role, RoleUpdateSchema
from src.domain.repository.roles_repository import RoleRepository

class ModifierUnrole:
    def __init__(self, role_repository: RoleRepository): 
        self.role_repository = role_repository
    
    async def executer(self, role_id: UUID, role_data: RoleUpdateSchema) -> Role : 
        role = await self.role_repository.trouver_par_id(role_id)

        if not role:
            return None
        
        update_data = role_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(role, key, value) 

        role_a_jour = await self.role_repository.mettre_a_jour(role)
        return role_a_jour