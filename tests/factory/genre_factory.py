import uuid
from typing import Optional

from src.domain.model.genre import GenreCreationSchema

def create_genre(
    nom: str = "Genre de test"
) -> GenreCreationSchema:
    return GenreCreationSchema(
        nom=nom
    )