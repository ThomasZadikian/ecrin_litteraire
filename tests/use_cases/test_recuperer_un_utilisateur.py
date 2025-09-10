import uuid
import pytest

from src.domain.model.utilisateur import Utilisateur
from src.use_cases.utilisateurs.recupere_un_utilisateur import RecupererUnUtilisateur
from src.infrastructure.persistance.inMemory_repository.in_memory_utilisateur_repository import InMemoryUtilisateurRepository

@pytest.mark.asyncio

async def test_recuperer_un_utilisateur():

    user_id = uuid.uuid4()
    hashed_password = "12345"

    nouvel_utilisateur = Utilisateur(
        id=user_id,
        prenom="John",
        nom_de_famille="Doe",
        date_de_naissance="1990-01-01",
        email="test@mail.com"
    )
    repo = InMemoryUtilisateurRepository()
    use_case = RecupererUnUtilisateur(repo)

    await repo.sauvegarder_un_utilisateur(utilisateur=nouvel_utilisateur, hashed_password = hashed_password)

    utilisateur_recuperer = await use_case.executer(utilisateur_id=nouvel_utilisateur.id)

    assert utilisateur_recuperer is not None
    assert utilisateur_recuperer.nom_de_famille == "Doe"
    assert utilisateur_recuperer.id == nouvel_utilisateur.id


