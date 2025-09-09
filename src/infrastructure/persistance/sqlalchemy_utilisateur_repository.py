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
    
    async def sauvegarder_un_utilisateur(self, utilisateur: Utilisateur, hashed_password: str) -> None :
        utilisateur_db = UtilisateurDB(
            id= utilisateur.id, 
            prenom = utilisateur.prenom, 
            nom_de_famille = utilisateur.nom_de_famille, 
            date_de_naissance = utilisateur.date_de_naissance, 
            email = utilisateur.email, 
            mot_de_passe_hache = hashed_password
        )
        self.session.add(utilisateur_db)
        await self.session.flush()

    async def trouver_un_utilisateur_par_id(self, id) -> Utilisateur | None: 
        result = await self.session.execute(
            select(UtilisateurDB).where(UtilisateurDB.id == id)
        )
        utilisateur_db = result.scalar_one_or_none()

        if utilisateur_db:
            return Utilisateur.model_validate(utilisateur_db)
        return None
    
    async def lister_tout_les_utilisateurs(self) -> list[Utilisateur]: 
        result = await self.session.execute(select(UtilisateurDB))
        utilisateurs_db = result.scalars().all()
        return [Utilisateur.model_validate(user_db) for user_db in utilisateurs_db]