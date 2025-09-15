from uuid import UUID
from src.domain.model.persona import Persona

class InMemoryPersonaRepository:
    def __init__ (self): 
        self.data: dict[UUID, Persona] = {}

    async def sauvegarder(self, persona: Persona) -> None: 
        self.data[persona.id] = persona

    async def trouver_par_id(self, persona_id: UUID) -> Persona | None: 
        return self.data.get(persona_id)
    
    async def mettre_a_jour(self, persona: Persona) -> Persona | None: 
         if persona.id in self.data:
            self.data[persona.id] = persona