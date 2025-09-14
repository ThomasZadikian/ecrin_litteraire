import pytest

from src.domain.model.roles import RoleUpdateSchema, Role
from src.use_cases.role.creer_un_role import CreerUnRole
from src.use_cases.role.recuperer_un_role import RecupererUnRole
from src.use_cases.role.modifier_un_role import ModifierUnrole
from src.infrastructure.persistance.inMemory_repository.in_memory_role_repository import InMemoryRoleRepository

from tests.factory.role_factory import create_role

@pytest.mark.asyncio
async def test_mettre_a_jour_un_genre(): 

    role_cree = create_role()
    repo = InMemoryRoleRepository()

    creer_un_role = CreerUnRole(repo)
    recuperer_un_role = RecupererUnRole(repo)
    modifier_un_role = ModifierUnrole(repo)

    nouveau_role: Role = await creer_un_role.executer(role_cree)
    role_recuperer: Role = await recuperer_un_role.executer(nouveau_role.id)
    role_modifier = RoleUpdateSchema(nom="Testeur deux")
    await modifier_un_role.executer(role_recuperer.id, role_modifier)
    role_modifier_recuperer: Role = await recuperer_un_role.executer(role_recuperer.id)

    assert role_modifier_recuperer.nom == "Testeur deux"
    assert role_modifier_recuperer.id == role_recuperer.id