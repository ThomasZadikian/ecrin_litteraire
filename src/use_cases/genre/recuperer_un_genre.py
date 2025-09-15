from uuid import UUID
from src.domain.model.genre import Genre
from src.domain.repository.genre_repository import GenreRepository

class RecupererUnGenre: 
    def __init__(self, genre_repository: GenreRepository): 
        self.genre_repository = genre_repository  

    async def executer(self, genre_id: UUID) -> Genre | None: 
        genre = await self.genre_repository.trouver_par_id(genre_id)
        return genre