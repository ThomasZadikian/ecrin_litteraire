from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.domain.livre import Livre
from src.domain.livre_repository import LivreRepository
from src.infrastructure.persistance.models import LivreDB

class SQLAlchemyLivreRepository(LivreRepository):
    """
    Implémentation SQLAlchemy du repository de livres.
    """
    def __init__(self, session: AsyncSession):
        self.session = session

    async def sauvegarder(self, livre: Livre) -> None:
        """
        Traduit un objet du domaine Livre en modèle de BDD LivreDB
        et le sauvegarde en base.
        """
        livre_db = LivreDB(
            id=livre.id,
            titre=livre.titre,
            contenu=livre.contenu,
            auteur=livre.auteur,
            date_publication=livre.date_publication
        )
        self.session.add(livre_db)
        # Note: Le commit sera géré au niveau de la requête API
        # pour regrouper plusieurs opérations en une seule transaction.

    async def trouver_par_id(self, livre_id: UUID) -> Livre | None:
        """
        Récupère un LivreDB par son ID et le traduit
        en objet du domaine Livre.
        """
        result = await self.session.get(LivreDB, livre_id)
        if result is None:
            return None
        
        # Traduction du modèle BDD vers l'entité du domaine
        return Livre(
            id=result.id,
            titre=result.titre,
            contenu=result.contenu,
            auteur=result.auteur,
            date_publication=result.date_publication
        )