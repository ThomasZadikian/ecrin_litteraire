from uuid import UUID
from src.domain.model.genre import Genre, GenreUpdateSchema
from src.domain.repository.genre_repository import GenreRepository

class ModifierUnGenre:
    def __init__(self, genre_repository: GenreRepository): 
        self.genre_repository = genre_repository
    
    async def executer(self, genre_id: UUID, genre_data: GenreUpdateSchema) -> Genre : 
        genre = await self.genre_repository.trouver_par_id(genre_id)

        if not genre:
            return None
        
        update_data = genre_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(genre, key, value) 

        genre_a_jour = await self.genre_repository.mettre_a_jour(genre)
        return genre_a_jour