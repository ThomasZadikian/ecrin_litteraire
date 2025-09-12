import uuid
from datetime import datetime

from src.domain.model.genre import Genre, GenreCreationSchema
from src.domain.repository.genre_repository import GenreRepository

class CreerUnGenre: 
    def __init__(self, genre_repository: GenreRepository):
        self.genre_repository = genre_repository  

    async def executer(self, genre_data: GenreCreationSchema) -> Genre: 
        nouveau_genre = Genre(
            id = uuid.uuid4(), 
            nom = genre_data.nom
        )
        await self.genre_repository.sauvegarder(nouveau_genre)
        return nouveau_genre