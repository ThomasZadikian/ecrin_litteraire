from uuid import UUID
from domain.model.genre import Genre

class InMemoryGenreRepository:
    def __init__ (self): 
        self.date: dict[UUID, Genre] = {}

    async def sauvegarder(self, genre: Genre) -> None: 
        self.date[genre.id] = genre

    async def recuperer_un_genre(self, genre_id: UUID) -> Genre | None: 
        return self.date.get(genre_id)