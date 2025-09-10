import uuid
import pytest

from src.infrastructure.persistance.inMemory_repository.in_memory_utilisateur_repository import InMemoryUtilisateurRepository
from domain.model.utilisateur import Utilisateur, UtilisateurUpdateSchema

@pytest.mark.asyncio
async def test_modifier_un_utilisateur_avec_id_valide(): 
    utilisateur_id = uuid.uuid4()
    mot_de_passe = "12345"

    utilisateur_existant = Utilisateur(
        id = utilisateur_id,
        prenom = "prenom",
        nom_de_famille = "nom",
        email = "test@test.com", 
        date_de_naissance="01/10/10"
        )
    
    repo = InMemoryUtilisateurRepository()

    await repo.sauvegarder_un_utilisateur(utilisateur_existant, mot_de_passe)

    utilisateur_mis_a_jour = UtilisateurUpdateSchema(
        email = "nouvel_email@new.new")
    
    await repo.modifier_un_utilisateur(utilisateur_mis_a_jour, utilisateur_existant.id)
    utilisateur = await repo.trouver_un_utilisateur_par_id(utilisateur_existant.id)

    assert utilisateur is not None
    assert utilisateur.email == "nouvel_email@new.new"
