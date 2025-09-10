
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Base(DeclarativeBase):
    pass

class LivreDB(Base):
    __tablename__ = "livres"

    id=Column(UUID(as_uuid=True),primary_key=True, default=uuid.uuid4)
    titre=Column(String, nullable=False)
    auteur=Column(String, nullable=False)
    contenu=Column(String, nullable=False)
    date_publication=Column(DateTime, nullable=False)

    def __repr__(self):
        return f"<LivreDB(id={self.id}, titre={self.titre})>"
    
class UtilisateurDB(Base): 
    __tablename__ = "utilisateurs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    prenom = Column(String, nullable = False)
    nom_de_famille = Column(String, nullable=False)
    date_de_naissance = Column(String, nullable=False)
    email = Column(String, unique=True, nullable = False)
    mot_de_passe_hache = Column(String, nullable=False)

    def __repr__(self):
        return f"<UtilisateurDB(id={self.id}, prenom={self.prenom})>"