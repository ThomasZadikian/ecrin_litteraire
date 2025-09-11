import uuid
from datetime import datetime
from typing import Optional
from src.domain.model.roles import Role

def create_role(
        id: Optional[uuid.UUID] = None,
        nom: str = "Rôle Par Défaut",
        date_creation: datetime = datetime(2025, 11, 9),
        date_modification: datetime = datetime(2025, 11, 9)
) -> Role:
    """
    Crée une instance de l'objet Role pour les tests unitaires.
    """
    if id is None:
        id = uuid.uuid4()
        
    return Role(
        id=id,
        nom=nom,
        date_creation=date_creation,
        date_modification=date_modification
)