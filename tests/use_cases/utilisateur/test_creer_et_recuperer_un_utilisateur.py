import pytest

from src.domain.model.utilisateur import UtilisateurCreationSchema
from src.use_cases.utilisateurs.creer_utilisateur import CreerUtilisateur
from src.use_cases.utilisateurs.recupere_un_utilisateur import RecupererUnUtilisateur
from src.infrastructure.persistance.inMemory_repository.in_memory_utilisateur_repository import InMemoryUtilisateurRepository

from tests.factory.user_factory import create_utilisateur

@pytest.mark.asyncio

async def test_creer_et_recuperer_un_utilisateur():
    nouvel_utilisateur: UtilisateurCreationSchema = create_utilisateur()

    repo = InMemoryUtilisateurRepository()
    creer_un_utilisateur = CreerUtilisateur(repo)
    recuperer_un_utilisateur = RecupererUnUtilisateur(repo)

    utilisateur_creer = await creer_un_utilisateur.executer(nouvel_utilisateur, nouvel_utilisateur.mot_de_passe)
    utilisateur = await recuperer_un_utilisateur.executer(utilisateur_creer.id)

    assert utilisateur is not None
    assert utilisateur.id == utilisateur_creer.id
    assert utilisateur.email == nouvel_utilisateur.email
    assert utilisateur.prenom == nouvel_utilisateur.prenom

