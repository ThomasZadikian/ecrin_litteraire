from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from src.use_cases.authentifier_utilisateur import AuthentifierUtilisateur
from src.infrastructure.persistance.database import get_session
from src.infrastructure.persistance.sqlalchemy_utilisateur_repository import SQLAlchemyUtilisateurRepository
from src.infrastructure.security import creer_access_token

router = APIRouter(tags=["Authentification"])

@router.post("/token")
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), 
    session: AsyncSession = Depends(get_session)
): 
    repo = SQLAlchemyUtilisateurRepository(session)
    use_case = AuthentifierUtilisateur(repo)

    user = await use_case.executer(email=form_data.username, mot_de_passe=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Email ou mot de passe incorrect", 
            headers={"WWW-Authenticate":"Bearer"},
        )
    access_token = creer_access_token(data={"sub":user.email})
    return {"acces_token": access_token, "token_type":"bearer"}