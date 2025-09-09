from uuid import UUID
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from domain.model.livre import Livre
from domain.repository.livre_repository import LivreRepository
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
        await self.session.flush() 

    async def trouver_par_id(self, livre_id: UUID) -> Livre | None:
        result_db = await self.session.get(LivreDB, livre_id)
        if result_db is None:
            return None
        return Livre.model_validate(result_db)
    
    async def trouver_par_auteur(self, auteur_name: str) -> list[Livre] | None: 
        result_db = await self.session.execute(
            select(LivreDB).where(LivreDB.auteur == auteur_name)
        )
        livres_db = result_db.scalars().all()
        if not livres_db:
            return None
        return [Livre.model_validate(livre) for livre in livres_db]

    async def mettre_a_jour(self, livre: Livre) -> None:
        livre_db = await self.session.get(LivreDB, livre.id)
        if livre_db:
            livre_db.titre = livre.titre
            livre_db.contenu = livre.contenu
            livre_db.auteur = livre.auteur
            self.session.add(livre_db)
            await self.session.flush()

    async def supprimer(self, livre: Livre) -> None:
        livre_db = await self.session.get(LivreDB, livre.id)
        if livre_db:
            await self.session.delete(livre_db)
            await self.session.flush()