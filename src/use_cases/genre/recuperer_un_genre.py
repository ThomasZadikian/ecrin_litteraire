from uuid import UUID
from src.domain.model.genre import Genre
from src.domain.repository.genre_repository import GenreRepository

class RecupererUnGenre: 
    def __init__(self, genre_repository: GenreRepository):
        self.genre_repository = genre_repository  

    async def executer(self, genre_id: UUID) -> Genre | None: 
        return await self.genre_repository.recuperer_un_genre(genre_id)