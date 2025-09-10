import uuid 
import pytest

from src.domain.model.utilisateur import Utilisateur
from src.infrastructure.persistance.inMemory_repository.in_memory_utilisateur_repository import InMemoryUtilisateurRepository

@pytest.mark.asyncio

async def test_lister_tout_les_utilisateurs(): 
    repo = InMemoryUtilisateurRepository()

    password_1 = "12345"
    password_2 = "67890"

    utilisateur_1 = Utilisateur(
        id=uuid.uuid4(), 
        prenom="Alice",
        nom_de_famille="Dupont",
        email="test1@test.com", 
        date_de_naissance="1990-01-01"
    )

    utilisateur_2 = Utilisateur(
        id=uuid.uuid4(), 
        prenom="Bob",
        nom_de_famille="Martin",
        email="test2@test.com",
        date_de_naissance="1985-05-15"
    )

    await repo.sauvegarder_un_utilisateur(utilisateur_1, password_1)
    await repo.sauvegarder_un_utilisateur(utilisateur_2, password_2)

    utilisateurs = await repo.lister_tout_les_utilisateurs()

    assert len(utilisateurs) == 2
    assert utilisateur_1 in utilisateurs
    assert utilisateur_2 in utilisateurs
    assert utilisateurs[0].email == "test1@test.com"
    assert utilisateurs[1].email == "test2@test.com"