import uuid
from datetime import datetime
from typing import Optional

from src.domain.model.editeur import Editeur

def create_editeur(
        id: Optional[uuid.UUID] = None,
        nom: str = "Éditeur Par Défaut",
        date_modification: datetime = datetime(2025, 11, 9)
) -> Editeur:
    """
    Crée une instance de l'objet Editeur pour les tests unitaires.
    """
    if id is None:
        id = uuid.uuid4()
        
    return Editeur(
        id=id,
        nom=nom,
        date_modification=date_modification
    )