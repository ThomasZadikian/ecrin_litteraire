import uuid
import pytest

from src.domain.model.utilisateur import Utilisateur
from src.infrastructure.persistance.inMemory_repository.in_memory_utilisateur_repository import InMemoryUtilisateurRepository

@pytest.mark.asyncio

async def test_supprimer_un_utilisateur(): 
    mot_de_passe = "12345"
    utilisateur_a_supprimer = Utilisateur(
        id= uuid.uuid4(), 
        prenom = "Test", 
        nom_de_famille="test", 
        date_de_naissance="1994-08-15", 
        email="test@test.com", 
    )

    repo = InMemoryUtilisateurRepository()

    await repo.sauvegarder_un_utilisateur(utilisateur_a_supprimer, hashed_password=mot_de_passe)
    await repo.supprimer_un_utilisateur(utilisateur_a_supprimer.id)
    
    utilisateur = await repo.trouver_un_utilisateur_par_id(utilisateur_a_supprimer.id)

    assert utilisateur is None