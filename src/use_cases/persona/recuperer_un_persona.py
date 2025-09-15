from uuid import UUID
from src.domain.model.persona import Persona
from src.domain.repository.persona_repository import PersonaRepository

class RecupererUnPersona: 
    def __init__(self, persona_repository: PersonaRepository): 
        self.persona_repository = persona_repository  

    async def executer(self, persona_id: UUID) -> Persona | None: 
        persona = await self.persona_repository.trouver_par_id(persona_id)
        return persona