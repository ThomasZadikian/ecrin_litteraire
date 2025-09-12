import pytest
import uuid
from src.domain.model.utilisateur import UtilisateurUpdateSchema
from src.use_cases.utilisateurs.creer_utilisateur import CreerUtilisateur
from src.use_cases.utilisateurs.modifier_un_utilisateur import ModifierUnUtilisateur
from src.use_cases.utilisateurs.recupere_un_utilisateur import RecupererUnUtilisateur
from src.infrastructure.persistance.inMemory_repository.in_memory_utilisateur_repository import InMemoryUtilisateurRepository

from tests.factory.user_factory import create_utilisateur

@pytest.mark.asyncio

async def test_mettre_a_jour_un_utilisateur():
    nouvel_utilisateur = create_utilisateur()
    nouvel_auteur_prefere= uuid.uuid4()
    nouveau_chatbot_prefere = uuid.uuid4()

    repo = InMemoryUtilisateurRepository()
    creer_utilisateur = CreerUtilisateur(repo)
    modifier_un_utilisateur = ModifierUnUtilisateur(repo)
    recuperer_un_utilisateur = RecupererUnUtilisateur(repo)

    utilisateur_creer = await creer_utilisateur.executer(nouvel_utilisateur, nouvel_utilisateur.mot_de_passe)

    utilisateur_modifier = UtilisateurUpdateSchema(
        email="modification.test",
        auteur_prefere_id=nouvel_auteur_prefere,
        chatbot_prefere_id=nouveau_chatbot_prefere
    )

    await modifier_un_utilisateur.executer(utilisateur_data=utilisateur_modifier, utilisateur_id=utilisateur_creer.id)

    utilisateur_recuperer = await recuperer_un_utilisateur.executer(utilisateur_id=utilisateur_creer.id)

    assert utilisateur_recuperer.email == "modification.test"
    assert utilisateur_recuperer.auteur_prefere_id == nouvel_auteur_prefere
    assert utilisateur_recuperer.chatbot_prefere_id == nouveau_chatbot_prefere