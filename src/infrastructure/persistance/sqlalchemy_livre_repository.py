from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.livre import Livre
from src.domain.livre_repository import LivreRepository
from src.infrastructure.persistance.models import LivreDB

class SQLAlchemyLivreRepository(LivreRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def sauvegarder(self, livre: Livre) -> None:
        livre_db = LivreDB(
            id=livre.id,
            titre=livre.titre,
            contenu=livre.contenu,
            auteur=livre.auteur,
            date_publication=livre.date_publication
        )
        self.session.add(livre_db)

    async def trouver_par_id(self, livre_id: UUID) -> Livre | None:
        result_db = await self.session.get(LivreDB, livre_id)
        
        if result_db is None:
            return None
        
        return Livre(
            id=result_db.id,
            titre=result_db.titre,
            contenu=result_db.contenu,
            auteur=result_db.auteur,
            date_publication=result_db.date_publication
        )