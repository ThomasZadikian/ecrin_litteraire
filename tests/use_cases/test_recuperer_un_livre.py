import pytest
import uuid
from datetime import datetime

from src.use_cases.livre.recuperer_un_livre import RecupererUnLivre
from src.infrastructure.persistance.in_memory_livre_repository import InMemoryLivreRepository
from src.domain.model.livre import Livre

@pytest.mark.asyncio

async def test_recuperer_un_livre():
    """
    verifie que le cas d'usage retourne bien un livre
    lorsque celui-ci existe dans el repository
    """
    #ARRANCE : Préparation des données et des objects de test
    livre_id = uuid.uuid4()

    livre_existant = Livre(
        id=livre_id,
        titre="titre",
        contenu = "Contenu", 
        auteur="auteur",
        date_publication=datetime.now()
    )

    repo = InMemoryLivreRepository()
    await repo.sauvegarder(livre_existant)

    use_case = RecupererUnLivre(repo) 

    # ACT : Exécution de la méthode à tester
    livre_recupere = await use_case.executer(livre_id=livre_id)

    # ASSERT : Vérification du résultat
    assert livre_recupere is not None
    assert livre_recupere.id == livre_existant.id 
    assert livre_recupere.titre == "titre"

@pytest.mark.asyncio
async def test_recuperer_un_livre_inexistant():
    """
    verifie que le cas d'usage retourne None
    lorsque le livre n'existe pas dans le repository
    """
    #ARRANCE : Préparation des données et des objects de test
    repo = InMemoryLivreRepository()
    use_case = RecupererUnLivre(repo)
    id_inexistant = uuid.uuid4()

    # ACT : Exécution de la méthode à tester
    livre_recupere = await use_case.executer(livre_id=id_inexistant)

    # ASSERT : Vérification du résultat
    assert livre_recupere is None