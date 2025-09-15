import pytest

from src.domain.model.persona import PersonaUpdateSchema, Persona
from src.use_cases.persona.creer_un_persona import CreerUnPersona
from src.use_cases.persona.recuperer_un_persona import RecupererUnPersona
from src.use_cases.persona.modifier_un_persona import ModifierUnPersona
from src.infrastructure.persistance.inMemory_repository.in_memory_persona_repository import InMemoryPersonaRepository

from tests.factory.persona_factory import create_persona

@pytest.mark.asyncio
async def test_mettre_a_jour_un_persona(): 

    persona_cree = create_persona()
    repo = InMemoryPersonaRepository()

    creer_un_persona = CreerUnPersona(repo)
    recuperer_un_persona = RecupererUnPersona(repo)
    modifier_un_persona = ModifierUnPersona(repo)

    nouveau_persona: Persona = await creer_un_persona.executer(persona_cree)
    persona_recuperer: Persona = await recuperer_un_persona.executer(nouveau_persona.id)
    persona_modifier = PersonaUpdateSchema(nom="Persona de test unitaire")
    await modifier_un_persona.executer(persona_recuperer.id, persona_modifier)
    persona_modifier_recuperer: Persona = await recuperer_un_persona.executer(persona_recuperer.id)

    assert persona_modifier_recuperer.id == persona_recuperer.id
    assert persona_modifier_recuperer.nom == "Persona de test unitaire"