import uuid
from datetime import datetime, date, timezone
from typing import Optional

from src.domain.model.utilisateur import Utilisateur
from src.domain.model.livre import Livre
from src.domain.model.commentaire import Commentaire
from src.domain.model.roles import Role
from src.domain.model.chatbot import Chatbot

from tests.factory.role_factory import create_role
from tests.factory.livre_factory import create_livre
from tests.factory.user_factory import create_utilisateur
from tests.factory.commentaire_factory import create_commentaire
from tests.factory.chatbot_factory import create_chatbot

mock_role: Role = create_role()
mock_livre: Livre = create_livre()
mock_utilisateur: Utilisateur = create_utilisateur()
mock_commentaire: Commentaire = create_commentaire()
mock_chatbot: Chatbot = create_chatbot()

def create_utilisateur(
    id: Optional[uuid.UUID] = None,
    prenom: str = "Thomas",
    nom_de_famille: str = "Zadikian",
    email: str = "thomas@example.com",
    date_de_naissance: date = date(1990, 1, 1),
    avatar: str = "avatar.jpg",
    date_de_creation: datetime = datetime.date(2025,11,9),
    cgu: bool = True,
    rgpd: bool = True,
    cookies: bool = True,
    date_modification: datetime = datetime.date(2025,11,9),
    livre: list[Livre] = [mock_livre],
    commentaire: list[Commentaire] = [mock_commentaire],
    auteur_prefere: uuid.UUID = mock_utilisateur.id,
    chatbot_prefere: uuid.UUID = mock_chatbot.id,
    role_id: uuid.UUID = mock_role.id,
    role: Role = mock_role

) -> Utilisateur:
    """
    Crée une instance de l'objet Utilisateur pour les tests unitaires.
    """
    if id is None:
        id = uuid.uuid4()
        
    return Utilisateur(
        id=id,
        prenom=prenom,
        nom_de_famille=nom_de_famille,
        email=email,
        date_de_naissance=date_de_naissance,
        avatar=avatar,
        date_de_creation=date_de_creation,
        cgu=cgu,
        rgpd=rgpd,
        cookies=cookies,
        date_modification=date_modification,
        livre=livre,
        commentaire=commentaire,
        auteur_prefere=auteur_prefere,
        chatbot_prefere=chatbot_prefere,
        role_id=role_id,
        role=role
    )