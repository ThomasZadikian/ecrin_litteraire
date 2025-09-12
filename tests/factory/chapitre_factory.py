import uuid
from datetime import datetime
from typing import Optional

from src.domain.model.chapitre import Chapitre
from src.domain.model.livre import Livre

def create_chapitre(
    id: Optional[uuid.UUID] = None,
    titre: str = "Chapitre 1",
    contenu: str = "Je suis le contenu du chapitre 1",
    numero_chapitre: int = 1,
    date_modification: datetime = datetime(2023, 1, 1),
    livre_id: Optional[uuid.UUID] = None,
    livre: Optional[Livre] = None,
) -> Chapitre:
    """
    Crée une instance de l'objet Chapitre pour les tests unitaires.
    """
    if id is None:
        id = uuid.uuid4()
        
    return Chapitre(
        id=id,
        titre=titre,
        contenu=contenu,
        numero_chapitre=numero_chapitre,
        date_modification=date_modification,
        livre_id=livre_id,
        livre=livre,
    )