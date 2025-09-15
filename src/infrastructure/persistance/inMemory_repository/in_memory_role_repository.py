from uuid import UUID
from src.domain.model.roles import Role

class InMemoryRoleRepository:
    def __init__ (self): 
        self.data: dict[UUID, Role] = {}

    async def sauvegarder(self, role: Role) -> None: 
        self.data[role.id] = role

    async def trouver_par_id(self, role_id: UUID) -> Role | None: 
        return self.data.get(role_id)
    
    async def mettre_a_jour(self, role: Role) -> Role | None: 
         if role.id in self.data:
            self.data[role.id] = role