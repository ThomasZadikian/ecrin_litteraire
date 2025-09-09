from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.use_cases.utilisateurs.creer_utilisateur import CreerUtilisateur
from src.domain.utilisateur_repository import UtilisateurRepository
from src.domain.utilisateur import Utilisateur, UtilisateurCreationSchema
from src.use_cases.utilisateurs.recupere_un_utilisateur import RecupererUnUtilisateur
from src.infrastructure.persistance.database import get_session
from src.infrastructure.persistance.sqlalchemy_utilisateur_repository import SQLAlchemyUtilisateurRepository

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

async def get_utilisateur_repository(session: AsyncSession = Depends(get_session)) -> UtilisateurRepository:
    return SQLAlchemyUtilisateurRepository(session)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Utilisateur)
async def creer_un_utilisateur(
    utilisateur_data: UtilisateurCreationSchema,
    utilisateur_repository: UtilisateurRepository = Depends(get_utilisateur_repository)
):
    use_case = CreerUtilisateur(utilisateur_repository)
    nouveau_livre =  await use_case.executer(utilisateur_data, utilisateur_data.mot_de_passe)
    await utilisateur_repository.session.commit()
    return nouveau_livre

@router.get("/{user_id}", response_model=Utilisateur)
async def recuperer_un_utilisateur(
    utilisateur_id: str, 
    utilisateur_repository: UtilisateurRepository = Depends(get_utilisateur_repository)
):
    use_case = RecupererUnUtilisateur(utilisateur_repository)
    utilisateur = await use_case.executer(utilisateur_id)
    if not utilisateur:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    return utilisateur