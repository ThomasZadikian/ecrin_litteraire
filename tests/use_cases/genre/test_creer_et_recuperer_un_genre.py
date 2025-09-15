import pytest

from src.domain.model.genre import GenreCreationSchema, Genre
from src.use_cases.genre.creer_un_genre import CreerUnGenre
from src.use_cases.genre.recuperer_un_genre import RecupererUnGenre
from src.infrastructure.persistance.inMemory_repository.in_memory_genre_repository import InMemoryGenreRepository

from tests.factory.genre_factory import create_genre

@pytest.mark.asyncio

async def test_creer_et_recuperer_un_genre():
    nouveau_genre: GenreCreationSchema = create_genre()

    repo = InMemoryGenreRepository()
    creer_un_genre = CreerUnGenre(repo)
    recuperer_un_genre = RecupererUnGenre(repo)

    nouveau_genre: Genre = await creer_un_genre.executer(nouveau_genre)
    genre_recuperer: Genre = await recuperer_un_genre.executer(nouveau_genre.id)

    assert genre_recuperer.id == nouveau_genre.id

