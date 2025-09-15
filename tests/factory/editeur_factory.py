import uuid
from datetime import datetime
from typing import Optional

from src.domain.model.editeur import EditeurCreationSchema

def create_editeur(
        nom: str = "Éditeur Par Défaut",
) -> EditeurCreationSchema:
    """
    Crée une instance de l'objet Editeur pour les tests unitaires.
    """
        
    return EditeurCreationSchema(
        nom=nom,
    )