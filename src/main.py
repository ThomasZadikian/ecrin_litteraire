from src.domain.livre_repository import LivreRepository
from src.use_cases.recuperer_un_livre import RecupererUnLivre
from src.infrastructure.persistance.in_memory_livre_repository import InMemoryLivreRepository
from uuid import uuid4
from fastapi import FastAPI
from src.domain.livre import Livre 
from datetime import datetime

app = FastAPI(
    title="Écrin Littéraire",
    description="API pour la gestion de l'Écrin Littéraire",
    version="1.0.0"
)

livre_repository = InMemoryLivreRepository()

recuperer_un_livre_use_case = RecupererUnLivre(livre_repository = livre_repository)
livre_id = uuid4()

example_book = Livre(
    id=uuid4(), 
    titre="Exemple de Livre",
    contenu="Ceci est un exemple de contenu de livre.",
    auteur="Auteur Exemple",
    date_publication=datetime.now()
)

livre_repository.sauvegarder(example_book)
print(f"Livre sauvegardé : {example_book .titre} (ID: {example_book.id})")

livre_recupere = recuperer_un_livre_use_case.executer(livre_id=example_book.id)

if livre_recupere:
    print(f"Livre récupéré : {livre_recupere.titre}")
    assert livre_recupere.id == example_book .id
else:
    print("Erreur : Le livre n'a pas été retrouvé.")