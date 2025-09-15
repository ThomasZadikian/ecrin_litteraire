import uuid
from datetime import datetime
from typing import Optional

from src.domain.model.persona import PersonaCreationSchema

def create_persona(
        nom: str = "Persona Par Défaut",
)-> PersonaCreationSchema :
    """
    Crée une instance de l'objet Persona pour les tests unitaires.
    """

    return PersonaCreationSchema(
        nom=nom
    )