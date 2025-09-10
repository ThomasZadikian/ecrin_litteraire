from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.model.livre import Livre, LivreCreationSchema
from src.domain.repository.livre_repository import LivreRepository
from src.use_cases.livre.recuperer_un_livre import RecupererUnLivre
from src.use_cases.livre.recuperer_un_livre import RecupererLivreParAuteur
from src.use_cases.livre.creer_un_livre import CreerUnLivre
from src.domain.model.livre import LivreUpdateSchema
from src.use_cases.livre.mettre_a_jour_un_livre import MettreAJourUnLivre
from src.use_cases.livre.supprimer_un_livre import SupprimerUnLivre
from src.domain.exceptions import LivreNotFoundError
from src.infrastructure.persistance.sqlalchemy_livre_repository import SQLAlchemyLivreRepository
from src.infrastructure.persistance.database import get_session

router = APIRouter(
    prefix="/livres",
    tags=["Livres"]
)

def get_livre_repository(session: AsyncSession = Depends(get_session)) -> LivreRepository:
    return SQLAlchemyLivreRepository(session)


@router.get("/{livre_id}", response_model=Livre)
async def recuperer_livre_par_id(
    livre_id: UUID,
    livre_repository: LivreRepository = Depends(get_livre_repository)
):
    use_case = RecupererUnLivre(livre_repository)
    livre = await use_case.executer(livre_id)
    if not livre:
        raise HTTPException(status_code=404, detail=f"Livre avec l'id : {livre_id} non trouvé")
    return livre

@router.get("/", response_model=list[Livre])
async def recuperer_livre_par_auteur(
    auteur_name: str,
    livre_repository: LivreRepository = Depends(get_livre_repository)
):
    use_case = RecupererLivreParAuteur(livre_repository)
    livres = await use_case.executer(auteur_name)
    if not livres:
        raise HTTPException(status_code=404, detail=f"Aucun livre trouvé pour l'auteur : {auteur_name}")
    return livres

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Livre)
async def creer_un_livre(
    livre_data: LivreCreationSchema,
    livre_repository: LivreRepository = Depends(get_livre_repository)
):
    use_case = CreerUnLivre(livre_repository)
    nouveau_livre =  await use_case.executer(livre_data)
    await livre_repository.session.commit()
    return nouveau_livre

@router.put("/{livre_id}", response_model=Livre)
async def mettre_a_jour_un_livre(
    livre_id: UUID,
    livre_data: LivreUpdateSchema,
    livre_repository: LivreRepository = Depends(get_livre_repository)
):

    use_case = MettreAJourUnLivre(livre_repository)
    livre_mis_a_jour = await use_case.executer(livre_id, livre_data)
    
    if not livre_mis_a_jour:
        raise HTTPException(status_code=404, detail=f"Livre avec l'id : {livre_id} non trouvé")
    
    return livre_mis_a_jour

@router.delete("/{livre_id}", status_code=status.HTTP_204_NO_CONTENT)
async def supprimer_un_livre(
    livre_id: UUID,
    livre_repository: LivreRepository = Depends(get_livre_repository)
):
    use_case = SupprimerUnLivre(livre_repository)
    try:
        await use_case.executer(livre_id)
    except LivreNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))