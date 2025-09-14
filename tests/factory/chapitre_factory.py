from src.domain.model.chapitre import CreationChapitreSchema
from src.domain.model.livre import Livre
from src.domain.model.chapitre import Chapitre

Livre.model_rebuild()
Chapitre.model_rebuild()

def create_chapitre(
    titre: str = "Chapitre 1",
    contenu: str = "Je suis le contenu du chapitre 1",
    numero_chapitre: int = 1,
) -> CreationChapitreSchema:
    """
    Crée une instance de l'objet Chapitre pour les tests unitaires.
    """
        
    return CreationChapitreSchema(
        titre=titre,
        contenu=contenu,
        numero_chapitre=numero_chapitre,
    )