import pytest
from datetime import datetime
import uuid

from domain.livre import Livre
from domain.livre_repository import LivreRepository
from use_cases.recuperer_un_livre import RecupererLivreParAuteur
from infrastructure.persistance.in_memory_livre_repository import InMemoryLivreRepository

@pytest.mark.asyncio
async def test_recuperer_un_livre_par_auteur():
    auteur = "autheur_test"
    uuid_livre_1 = uuid.uuid4()
    uuid_livre_2 = uuid.uuid4()

    livre_1 = Livre(
        id=uuid_livre_1, 
        titre="Titre 1", 
        contenu="Contenu 1",
        auteur=auteur, 
        date_publication=datetime.now()
    )

    livre_2 = Livre(
        id=uuid_livre_2, 
        titre="Titre 2", 
        contenu="Contenu 2",
        auteur=auteur, 
        date_publication=datetime.now()
    )

    repo = InMemoryLivreRepository()

    use_case  = RecupererLivreParAuteur(repo)

    await repo.sauvegarder(livre_1)
    await repo.sauvegarder(livre_2)

    livres_recuperes: list[Livre] = await use_case.executer(auteur_name=auteur)

    assert len(livres_recuperes) == 2
    assert livres_recuperes[0].auteur == auteur


