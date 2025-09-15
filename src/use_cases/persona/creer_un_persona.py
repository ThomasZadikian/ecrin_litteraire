import uuid
from datetime import datetime

from src.domain.model.persona import Persona, PersonaCreationSchema
from src.domain.repository.persona_repository import PersonaRepository

class CreerUnPersona: 
    def __init__(self, persona_repository: PersonaRepository):
        self.persona_repository = persona_repository  

    async def executer(self, persona_data: PersonaCreationSchema) -> Persona: 
        nouveau_persona = Persona(
            id = uuid.uuid4(), 
            nom = persona_data.nom,
            date_modification=datetime.now()
        )
        await self.persona_repository.sauvegarder(nouveau_persona)
        return nouveau_persona