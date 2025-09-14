import pytest  

from src.domain.model.livre import Livre, LivreCreationSchema
from src.use_cases.livre.creer_un_livre import CreerUnLivre
from src.use_cases.livre.recuperer_un_livre import RecupererUnLivre
from src.infrastructure.persistance.inMemory_repository.in_memory_livre_repository import InMemoryLivreRepository

from src.domain.model.genre import Genre, GenreCreationSchema
from src.infrastructure.persistance.inMemory_repository.in_memory_genre_repository import InMemoryGenreRepository
from src.use_cases.genre.creer_un_genre import CreerUnGenre
from src.use_cases.genre.recuperer_un_genre import RecupererUnGenre

from src.domain.model.utilisateur import Utilisateur, UtilisateurCreationSchema
from src.infrastructure.persistance.inMemory_repository.in_memory_utilisateur_repository import InMemoryUtilisateurRepository
from src.use_cases.utilisateurs.creer_utilisateur import CreerUtilisateur
from src.use_cases.utilisateurs.recupere_un_utilisateur import RecupererUnUtilisateur

from src.domain.model.chapitre import Chapitre, CreationChapitreSchema, ChapitreUpdateSchema
from src.infrastructure.persistance.inMemory_repository.in_memory_chapitre_repository import InMemoryChapitreRepository
from src.use_cases.chapitre.creer_un_chapitre import CreerUnChapitre
from src.use_cases.chapitre.recuperer_un_chapitre import RecupererUnChapitre
from src.use_cases.chapitre.modifier_un_chapitre import ModifierUnChapitre

from tests.factory.livre_factory import create_livre
from tests.factory.genre_factory import create_genre
from tests.factory.user_factory import create_utilisateur
from tests.factory.chapitre_factory import create_chapitre

@pytest.mark.asyncio
async def test_creer_et_recuperer_un_livre():

    auteur: UtilisateurCreationSchema = create_utilisateur()
    genre: GenreCreationSchema = create_genre()
    livre: LivreCreationSchema = create_livre()
    chapitre: CreationChapitreSchema = create_chapitre()

    repo_utilisateur = InMemoryUtilisateurRepository()
    repo_genre = InMemoryGenreRepository()
    repo_livre = InMemoryLivreRepository()
    repo_chapitre = InMemoryChapitreRepository()

    creer_utilisateur = CreerUtilisateur(repo_utilisateur)
    creer_un_genre = CreerUnGenre(repo_genre)
    creer_un_livre = CreerUnLivre(repo_livre)
    creer_un_chapitre = CreerUnChapitre(repo_chapitre)

    recuperer_utilisateur = RecupererUnUtilisateur(repo_utilisateur)
    recuperer_un_genre = RecupererUnGenre(repo_genre)
    recuperer_un_chapitre = RecupererUnChapitre(repo_chapitre)
    modifier_un_chapitre = ModifierUnChapitre(repo_chapitre)

    creer_utilisateur = await creer_utilisateur.executer(auteur, auteur.mot_de_passe)
    creer_genre = await creer_un_genre.executer(genre)

    utilisateur: Utilisateur = await recuperer_utilisateur.executer(creer_utilisateur.id)
    genre: Genre = await recuperer_un_genre.executer(creer_genre.id)

    nouveau_livre = await creer_un_livre.executer(livre, auteur = utilisateur, genre=genre)
    livre_recuperer: Livre = await RecupererUnLivre(repo_livre).executer(nouveau_livre.id)

    chapitre_creer = await creer_un_chapitre.executer(chapitre, livre_recuperer)
    chapitre_recuperer: Chapitre = await recuperer_un_chapitre.executer(chapitre_creer.id)
    chapitre_modifier = ChapitreUpdateSchema(
        titre="Nouveau chapitre",
        contenu="Faute corrigées"
    )
    await modifier_un_chapitre.exectuer(chapitre_recuperer.id, chapitre_modifier)
    chapitre_definitif: Chapitre = await recuperer_un_chapitre.executer(chapitre_recuperer.id)

    assert chapitre_definitif.livre_id == livre_recuperer.id
    assert chapitre_definitif.titre == "Nouveau chapitre"
    assert chapitre_definitif.contenu == "Faute corrigées"
    assert chapitre_definitif.numero_chapitre == chapitre_recuperer.numero_chapitre