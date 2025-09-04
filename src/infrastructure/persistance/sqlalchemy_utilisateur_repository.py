from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.domain.utilisateur import Utilisateur
from src.domain.utilisateur_repository import UtilisateurRepository
from src.infrastructure.persistance.models import UtilisateurDB

class SQLAlchemyUtilisateurRepository(UtilisateurRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def trouver_par_email(self, email: str) -> Utilisateur | None:
        result = await self.session.execute(
            select(UtilisateurDB).where(UtilisateurDB.email == email)
        )
        utilisateur_db = result.scalar_one_or_none()

        if utilisateur_db:
            return Utilisateur.model_validate(utilisateur_db)
        return None
    
    async def trouver_db_par_email(self, email: str) -> UtilisateurDB | None:
        result = await self.session.execute(
            select(UtilisateurDB).where(UtilisateurDB.email == email)
        )
        return result.scalar_one_or_none()