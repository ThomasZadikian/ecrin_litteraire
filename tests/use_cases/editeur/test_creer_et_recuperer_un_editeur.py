import pytest

from src.domain.model.editeur import EditeurCreationSchema, Editeur
from src.use_cases.editeur.creer_un_editeur import CreerUnediteur
from src.use_cases.editeur.recuperer_un_editeur import RecupererUnediteur
from src.infrastructure.persistance.inMemory_repository.in_memory_editeur_repository import InMemoryEditeurRepository

from tests.factory.editeur_factory import create_editeur

@pytest.mark.asyncio

async def test_creer_et_recuperer_un_editeur():
    nouveau_editeur: EditeurCreationSchema = create_editeur()

    repo = InMemoryEditeurRepository()
    creer_un_editeur = CreerUnediteur(repo)
    recuperer_un_editeur = RecupererUnediteur(repo)

    nouveau_editeur: Editeur = await creer_un_editeur.executer(nouveau_editeur)
    editeur_recuperer: Editeur = await recuperer_un_editeur.executer(nouveau_editeur.id)

    assert editeur_recuperer.id == nouveau_editeur.id

