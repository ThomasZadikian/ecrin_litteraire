from uuid import UUID
from src.domain.model.persona import Persona, PersonaUpdateSchema
from src.domain.repository.persona_repository import PersonaRepository

class ModifierUnPersona:
    def __init__(self, persona_repository: PersonaRepository): 
        self.persona_repository = persona_repository
    
    async def executer(self, persona_id: UUID, persona_data: PersonaUpdateSchema) -> Persona : 
        persona = await self.persona_repository.trouver_par_id(persona_id)

        if not persona:
            return None
        
        update_data = persona_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(persona, key, value) 

        persona_a_jour = await self.persona_repository.mettre_a_jour(persona)
        return persona_a_jour