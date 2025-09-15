import pytest  

from src.domain.model.livre import Livre, LivreCreationSchema
from src.use_cases.livre.creer_un_livre import CreerUnLivre
from src.use_cases.livre.recuperer_un_livre import RecupererUnLivre
from src.infrastructure.persistance.inMemory_repository.in_memory_livre_repository import InMemoryLivreRepository

from src.infrastructure.persistance.inMemory_repository.in_memory_genre_repository import InMemoryGenreRepository
from src.use_cases.genre.creer_un_genre import CreerUnGenre
from src.use_cases.genre.recuperer_un_genre import RecupererUnGenre

from src.infrastructure.persistance.inMemory_repository.in_memory_utilisateur_repository import InMemoryUtilisateurRepository
from src.use_cases.utilisateurs.creer_utilisateur import CreerUtilisateur
from src.use_cases.utilisateurs.recupere_un_utilisateur import RecupererUnUtilisateur

from tests.factory.livre_factory import create_livre
from tests.factory.genre_factory import create_genre
from tests.factory.user_factory import create_utilisateur

@pytest.mark.asyncio
async def test_creer_et_recuperer_un_livre():

    auteur = create_utilisateur()
    genre = create_genre()

    repo_utilisateur = InMemoryUtilisateurRepository()
    repo_genre = InMemoryGenreRepository()
    repo_livre = InMemoryLivreRepository()

    creer_utilisateur = CreerUtilisateur(repo_utilisateur)
    creer_un_genre = CreerUnGenre(repo_genre)
    creer_un_livre = CreerUnLivre(repo_livre)

    recuperer_utilisateur = RecupererUnUtilisateur(repo_utilisateur)
    recuperer_un_genre = RecupererUnGenre(repo_genre)

    
    creer_utilisateur = await creer_utilisateur.executer(auteur, auteur.mot_de_passe)
    creer_genre = await creer_un_genre.executer(genre)

    utilisateur = await recuperer_utilisateur.executer(creer_utilisateur.id)
    genre = await recuperer_un_genre.executer(creer_genre.id)

    livre = create_livre()

    nouveau_livre = await creer_un_livre.executer(livre, auteur = utilisateur, genre=genre)

    livre_recuperer: Livre = await RecupererUnLivre(repo_livre).executer(nouveau_livre.id)

    assert livre_recuperer.id == nouveau_livre.id
