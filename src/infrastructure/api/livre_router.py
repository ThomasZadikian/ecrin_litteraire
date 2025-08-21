from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID

from src.domain.livre import Livre
from src.domain.livre_repository import LivreRepository
from src.use_cases.recuperer_un_livre import RecupererUnLivre
from src.infrastructure.persistance.in_memory_livre_repository import InMemoryLivreRepository

router = APIRouter(
    prefix="/livres",
    tags=["livres"]
)

def get_livre_repository():
    return InMemoryLivreRepository()

@router.get("/{livre_id}", response_model=Livre)
def recuperer_livre_par_id(
    livre_id: UUID,
    livre_repository: Livre = Depends(get_livre_repository())
    ) :
    use_case = recuperer_livre_par_id(livre_repository)
    livre = use_case.executer(livre_id)

    if not livre:
        raise HTTPException(status_code=404, detail="Livre non trouvé")
    
    return livre
