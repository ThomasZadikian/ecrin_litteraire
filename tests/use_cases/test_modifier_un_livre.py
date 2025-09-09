import pytest
import uuid
from datetime import datetime

from src.use_cases.livre.recuperer_un_livre import RecupererUnLivre
from src.use_cases.livre.mettre_a_jour_un_livre import MettreAJourUnLivre
from src.infrastructure.persistance.in_memory_livre_repository import InMemoryLivreRepository
from src.domain.model.livre import Livre, LivreUpdateSchema

@pytest.mark.asyncio
async def test_modifier_un_livre_avec_id_valide(): 
    livre_id = uuid.uuid4()

    livre_existant = Livre(
        id = livre_id,
        titre = "titre",
        contenu = "Contenu",
        auteur = "auteur",
        date_publication = datetime.now()
    )

    repo = InMemoryLivreRepository()
    use_case = MettreAJourUnLivre(repo)
    use_case_recuperer = RecupererUnLivre(repo)

    await repo.sauvegarder(livre_existant)

    livre_mis_a_jour = LivreUpdateSchema(
        titre = "Nouveau titre",
        contenu = "Nouveau Contenu", 
        auteur = "Nouveau auteur"
        )
    
    await use_case.executer(livre_existant.id, livre_mis_a_jour)  

    livre_existant = await use_case_recuperer.executer(livre_id=livre_existant.id)

    assert livre_existant.titre == "Nouveau titre" 
