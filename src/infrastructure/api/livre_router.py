from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.livre import Livre, LivreCreationSchema
from src.domain.livre_repository import LivreRepository
from src.use_cases.recuperer_un_livre import RecupererUnLivre
from src.use_cases.creer_un_livre import CreerUnLivre
# On importe le nouveau repository et la dépendance de session
from src.infrastructure.persistance.sqlalchemy_livre_repository import SQLAlchemyLivreRepository
from src.infrastructure.persistance.database import get_session

router = APIRouter(
    prefix="/livres",
    tags=["Livres"]
)

# NOUVELLE VERSION de la "factory" à repository
def get_livre_repository(session: AsyncSession = Depends(get_session)) -> LivreRepository:
    return SQLAlchemyLivreRepository(session)

# --- Les Routes (elles ne changent pas, mais leur dépendance est maintenant réelle) ---

@router.get("/{livre_id}", response_model=Livre)
async def recuperer_livre_par_id(
    livre_id: UUID,
    livre_repository: LivreRepository = Depends(get_livre_repository)
):
    use_case = RecupererUnLivre(livre_repository)
    # Notez l'ajout de 'await' car notre repository est maintenant asynchrone
    livre = await use_case.executer(livre_id)
    if not livre:
        raise HTTPException(status_code=404, detail="Livre non trouvé")
    return livre

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Livre)
async def creer_un_livre(
    livre_data: LivreCreationSchema,
    livre_repository: LivreRepository = Depends(get_livre_repository)
):
    use_case = CreerUnLivre(livre_repository)
    # Notez l'ajout de 'await'
    nouveau_livre = await use_case.executer(livre_data)
    # Nous devons maintenant commiter la transaction
    await livre_repository.session.commit()
    await livre_repository.session.refresh(nouveau_livre) # Pour récupérer les valeurs par défaut de la BDD
    return nouveau_livre