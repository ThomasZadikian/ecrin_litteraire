import pytest
import uuid

from src.use_cases.commentaire.creer_un_commentaire import CreerUnCommentaire
from src.use_cases.commentaire.recuperer_un_commentaire import RecupererUnCommentaire
from src.domain.model.commentaire import Commentaire, CommentaireCreationSchema
from src.infrastructure.persistance.inMemory_repository.in_memory_commentaire_repository import InMemoryCommentaireRepository

from src.domain.model.utilisateur import Utilisateur, UtilisateurCreationSchema
from src.infrastructure.persistance.inMemory_repository.in_memory_utilisateur_repository import InMemoryUtilisateurRepository
from src.use_cases.utilisateurs.creer_utilisateur import CreerUtilisateur
from src.use_cases.utilisateurs.recupere_un_utilisateur import RecupererUnUtilisateur

from src.domain.model.genre import Genre, GenreCreationSchema
from src.infrastructure.persistance.inMemory_repository.in_memory_genre_repository import InMemoryGenreRepository
from src.use_cases.genre.creer_un_genre import CreerUnGenre
from src.use_cases.genre.recuperer_un_genre import RecupererUnGenre

from src.domain.model.livre import Livre, LivreCreationSchema
from src.infrastructure.persistance.inMemory_repository.in_memory_livre_repository import InMemoryLivreRepository
from src.use_cases.livre.creer_un_livre import CreerUnLivre
from src.use_cases.livre.recuperer_un_livre import RecupererUnLivre

from tests.factory.user_factory import create_utilisateur
from tests.factory.genre_factory import create_genre
from tests.factory.livre_factory import create_livre
from tests.factory.commentaire_factory import create_commentaire

@pytest.mark.asyncio
async def test_creer_et_recuperer_un_commentaire(): 
    nouvel_utilisateur: UtilisateurCreationSchema = create_utilisateur()
    nouveau_genre: GenreCreationSchema = create_genre()
    nouveau_livre: LivreCreationSchema = create_livre()
    nouveau_commentaire: CommentaireCreationSchema = create_commentaire()
    
    repo_utilisateur = InMemoryUtilisateurRepository()
    repo_genre = InMemoryGenreRepository()
    repo_livre = InMemoryLivreRepository()
    repo_commentaire = InMemoryCommentaireRepository()

    creer_un_utilisateur = CreerUtilisateur(repo_utilisateur)
    creer_un_genre = CreerUnGenre(repo_genre)
    creer_un_livre = CreerUnLivre(repo_livre)
    creer_un_commentaire = CreerUnCommentaire(repo_commentaire)

    recupere_un_utilisateur = RecupererUnUtilisateur(repo_utilisateur)
    recuperer_un_genre = RecupererUnGenre(repo_genre)
    recuperer_un_livre = RecupererUnLivre(repo_livre)
    recuperer_un_commentaire = RecupererUnCommentaire(repo_commentaire)

    utilisateur = await creer_un_utilisateur.executer(
        nouvel_utilisateur, 
        nouvel_utilisateur.mot_de_passe)
    utilisateur_recuperer = await recupere_un_utilisateur.executer(
        utilisateur.id)
    
    genre = await creer_un_genre.executer(nouveau_genre)
    genre_recuperer = await recuperer_un_genre.executer(genre.id)

    livre = await creer_un_livre.executer(
        nouveau_livre,
        auteur= utilisateur_recuperer, 
        genre= genre_recuperer
    )
    livre_recuperer = await recuperer_un_livre.executer(livre.id)

    commentaire = await creer_un_commentaire.executer(
        nouveau_commentaire, 
        auteur=utilisateur_recuperer, 
        livre= livre_recuperer
    )
    
    commentaire_recuperer = await recuperer_un_commentaire.executer(
        commentaire.id
    )

    assert commentaire_recuperer is not None
    assert commentaire_recuperer.auteur.id == utilisateur.id
