import pytest

from src.domain.model.editeur import EditeurUpdateSchema, Editeur
from src.use_cases.editeur.creer_un_editeur import CreerUnediteur
from src.use_cases.editeur.recuperer_un_editeur import RecupererUnediteur
from src.use_cases.editeur.modifier_un_editeur import ModifierUnediteur
from src.infrastructure.persistance.inMemory_repository.in_memory_editeur_repository import InMemoryEditeurRepository

from tests.factory.editeur_factory import create_editeur

@pytest.mark.asyncio
async def test_mettre_a_jour_un_editeur(): 

    editeur_cree = create_editeur()
    repo = InMemoryEditeurRepository()

    creer_un_editeur = CreerUnediteur(repo)
    recuperer_un_editeur = RecupererUnediteur(repo)
    modifier_un_editeur = ModifierUnediteur(repo)

    nouveau_editeur: Editeur = await creer_un_editeur.executer(editeur_cree)
    editeur_recuperer: Editeur = await recuperer_un_editeur.executer(nouveau_editeur.id)
    editeur_modifier = EditeurUpdateSchema(nom="Nouveau nom")
    await modifier_un_editeur.executer(editeur_recuperer.id, editeur_modifier)
    editeur_modifier_recuperer: Editeur = await recuperer_un_editeur.executer(editeur_recuperer.id)

    assert editeur_modifier_recuperer.nom == "Nouveau nom"