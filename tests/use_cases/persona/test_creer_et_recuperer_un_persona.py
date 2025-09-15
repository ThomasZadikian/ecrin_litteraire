import pytest

from src.domain.model.persona import PersonaCreationSchema, Persona
from src.use_cases.persona.creer_un_persona import CreerUnPersona
from src.use_cases.persona.recuperer_un_persona import RecupererUnPersona
from src.infrastructure.persistance.inMemory_repository.in_memory_persona_repository import InMemoryPersonaRepository

from tests.factory.persona_factory import create_persona

@pytest.mark.asyncio

async def test_creer_et_recuperer_un_persona():
    nouveau_persona: PersonaCreationSchema = create_persona()

    repo = InMemoryPersonaRepository()
    creer_un_persona = CreerUnPersona(repo)
    recuperer_un_persona = RecupererUnPersona(repo)

    nouveau_persona: Persona = await creer_un_persona.executer(nouveau_persona)
    persona_recuperer: Persona = await recuperer_un_persona.executer(nouveau_persona.id)

    assert persona_recuperer.id == nouveau_persona.id

