import uuid
from typing import Optional

from src.domain.model.genre import Genre

def create_genre(
    id: Optional[uuid.UUID] = None,
    nom: str = "Genre"
) -> Genre:
    return Genre(
        id=id or uuid.uuid4(),
        nom=nom
    )