
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
    date_publication=Column(DateTime, nullable=False)

    def __repr__(self):
        return f"<LivreDB(id={self.id}, titre={self.titre})>"