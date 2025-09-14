import pytest

from src.domain.model.roles import RoleCreateSchema, Role
from src.use_cases.role.creer_un_role import CreerUnRole
from src.use_cases.role.recuperer_un_role import RecupererUnRole
from src.infrastructure.persistance.inMemory_repository.in_memory_role_repository import InMemoryRoleRepository

from tests.factory.role_factory import create_role

@pytest.mark.asyncio

async def test_creer_et_recuperer_un_role():
    nouveau_role: RoleCreateSchema = create_role()

    repo = InMemoryRoleRepository()
    creer_un_role = CreerUnRole(repo)
    recuperer_un_role = RecupererUnRole(repo)

    nouveau_role: Role = await creer_un_role.executer(nouveau_role)
    role_recuperer: Role = await recuperer_un_role.executer(nouveau_role.id)

    assert role_recuperer.id == nouveau_role.id

