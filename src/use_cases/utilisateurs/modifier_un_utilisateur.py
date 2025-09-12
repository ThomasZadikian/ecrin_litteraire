from uuid import UUID
from datetime import datetime
from src.domain.model.utilisateur import Utilisateur, UtilisateurUpdateSchema
from src.domain.repository.utilisateur_repository import UtilisateurRepository

class ModifierUnUtilisateur:  
    def __init__(self, utilisateur_repository: UtilisateurRepository):
        self.utilisateur_repository = utilisateur_repository
        pass

    async def executer(self, utilisateur_data: UtilisateurUpdateSchema, utilisateur_id: UUID) -> Utilisateur | None: 
        utilisateur_a_modifier = await self.utilisateur_repository.trouver_un_utilisateur_par_id(utilisateur_id)
        if not utilisateur_a_modifier: 
            return None
        
        update_data = utilisateur_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(utilisateur_a_modifier, key, value)
        update_data['date_de_modification'] = datetime.now()

        await self.utilisateur_repository.modifier_un_utilisateur(utilisateur_a_modifier, utilisateur_id=utilisateur_id)
        utilisateur_a_jour = await self.utilisateur_repository.trouver_un_utilisateur_par_id(utilisateur_id)
        return utilisateur_a_jour