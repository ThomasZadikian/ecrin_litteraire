import pytest

from src.domain.model.genre import GenreUpdateSchema, Genre
from src.use_cases.genre.creer_un_genre import CreerUnGenre
from src.use_cases.genre.recuperer_un_genre import RecupererUnGenre
from src.use_cases.genre.modifier_un_genre import ModifierUnGenre
from src.infrastructure.persistance.inMemory_repository.in_memory_genre_repository import InMemoryGenreRepository

from tests.factory.genre_factory import create_genre

@pytest.mark.asyncio
async def test_mettre_a_jour_un_genre(): 

    genre_cree = create_genre()
    repo = InMemoryGenreRepository()

    creer_un_genre = CreerUnGenre(repo)
    recuperer_un_genre = RecupererUnGenre(repo)
    modifier_un_genre = ModifierUnGenre(repo)

    nouveau_genre: Genre = await creer_un_genre.executer(genre_cree)
    genre_recuperer: Genre = await recuperer_un_genre.executer(nouveau_genre.id)
    genre_modifier = GenreUpdateSchema(nom="Nouveau nom")
    await modifier_un_genre.executer(genre_recuperer.id, genre_modifier)
    genre_modifier_recuperer: Genre = await recuperer_un_genre.executer(genre_recuperer.id)

    assert genre_modifier_recuperer.nom == "Nouveau nom"