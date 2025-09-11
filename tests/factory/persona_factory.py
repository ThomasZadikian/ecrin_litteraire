import uuid
from datetime import datetime
from typing import Optional

from src.domain.model.persona import Persona

def create_persona(
        id: Optional[uuid.UUID] = None,
        nom: str = "Persona Par Défaut",
        date_modification: datetime = datetime(2025, 11, 9)
)-> Persona :
    """
    Crée une instance de l'objet Persona pour les tests unitaires.
    """
    if id is None:
        id = uuid.uuid4()
        
    return Persona(
        id=id,
        nom=nom,
        date_modification=date_modification
    )