from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class Livre(BaseModel):
    id: UUID
    titre: str
    contenu: str
    # Modify to UUID later if needed
    auteur: str
    date_publication: datetime
