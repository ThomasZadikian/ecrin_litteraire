from src.domain.model.roles import RoleCreateSchema

def create_role(
        nom: str = "Testeur",
) -> RoleCreateSchema:
    """
    Crée une instance de l'objet Role pour les tests unitaires.
    """

    return RoleCreateSchema(
        nom=nom,
)