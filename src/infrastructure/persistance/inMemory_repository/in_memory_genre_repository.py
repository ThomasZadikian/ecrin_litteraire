from uuid import UUID
from src.domain.model.genre import Genre

class InMemoryGenreRepository:
    def __init__ (self): 
        self.data: dict[UUID, Genre] = {}

    async def sauvegarder(self, genre: Genre) -> None: 
        self.data[genre.id] = genre

    async def trouver_par_id(self, genre_id: UUID) -> Genre | None: 
        return self.data.get(genre_id)
    
    async def mettre_a_jour(self, genre: Genre) -> Genre | None: 
         if genre.id in self.data:
            self.data[genre.id] = genre