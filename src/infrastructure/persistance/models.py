import uuid
from datetime import datetime
from sqlalchemy import Column, String, Text, ForeignKey, Table, DateTime, Boolean, text
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

Base = declarative_base()

livres_genres_association_table = Table(
    "livres_genres_association",
    Base.metadata,
    Column("livre_id", PG_UUID(as_uuid=True), ForeignKey("livres.id"), primary_key=True),
    Column("genre_id", PG_UUID(as_uuid=True), ForeignKey("genres.id"), primary_key=True),
)

class Role(Base):
    """
    Modèle de la table 'roles'.
    Gère les permissions des utilisateurs (par exemple, 'admin', 'utilisateur').
    """
    __tablename__ = "roles"
    id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nom: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    date_creation: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("now()"))
    date_modification: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("now()"))

class Utilisateur(Base):
    """
    Modèle de la table 'utilisateurs' pour la base de données.
    """
    __tablename__ = "utilisateurs"
    id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    prenom: Mapped[str] = mapped_column(String(50), nullable=False)
    nom_de_famille: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    mot_de_passe_hache: Mapped[str] = mapped_column(String(255), nullable=False)
    avatar: Mapped[str] = mapped_column(String(255), nullable=True)
    date_de_naissance: Mapped[datetime] = mapped_column(String, nullable=True)
    date_de_creation_du_compte: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("now()"))
    date_modification: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("now()"), onupdate=text("now()"))
    cgu: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    rgpd: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    cookies: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    livres: Mapped[list["Livre"]] = relationship(back_populates="auteur")
    commentaires: Mapped[list["Commentaire"]] = relationship(back_populates="auteur")
    auteur_prefere_id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), ForeignKey("utilisateurs.id"), nullable=True)
    chatbot_prefere_id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), ForeignKey("chatbots.id"), nullable=True)
    role_id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), ForeignKey("roles.id"), nullable=False, default=text("uuid_generate_v4()"))
    
    role: Mapped["Role"] = relationship(back_populates="utilisateurs")

class Livre(Base):
    """
    Modèle de la table 'livres'.
    Conteneur de métadonnées pour les chapitres.
    """
    __tablename__ = "livres"
    id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    titre: Mapped[str] = mapped_column(String(255), nullable=False)
    contenu_pour_majeur: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    date_de_publication: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    date_d_ajout: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("now()"))
    date_modification: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("now()"))

    auteur_id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), ForeignKey("utilisateurs.id"))
    auteur: Mapped["Utilisateur"] = relationship(back_populates="livres")
    genres: Mapped[list["Genre"]] = relationship(
        secondary=livres_genres_association_table, back_populates="livres"
    )

class Chapitre(Base):
    """
    Modèle de la table 'chapitres'.
    Contient le contenu réel d'un livre.
    """
    __tablename__ = "chapitres"
    id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    titre: Mapped[str] = mapped_column(String(255), nullable=True)
    contenu: Mapped[str] = mapped_column(Text, nullable=True)
    numero_chapitre: Mapped[int] = mapped_column(nullable=False)
    date_modification: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("now()"))

    livre_id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), ForeignKey("livres.id"))
    livre: Mapped["Livre"] = relationship(back_populates="chapitres")

class Commentaire(Base):
    """
    Modèle de la table 'commentaires'.
    Permet aux utilisateurs de commenter un livre.
    """
    __tablename__ = "commentaires"
    id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    contenu: Mapped[str] = mapped_column(Text, nullable=False)
    date_creation: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("now()"))

    auteur_id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), ForeignKey("utilisateurs.id"))
    auteur: Mapped["Utilisateur"] = relationship(back_populates="commentaires")
    livre_id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), ForeignKey("livres.id"))
    livre: Mapped["Livre"] = relationship(back_populates="commentaires")

class Genre(Base):
    """
    Modèle de la table 'genres'.
    Sert à taguer les livres avec des genres.
    """
    __tablename__ = "genres"
    id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nom: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    

class Chatbot(Base):
    """
    Modèle de la table 'chatbots'.
    Représente les différents modèles de chatbot disponibles.
    """
    __tablename__ = "chatbots"
    id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nom: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    
class Persona(Base):
    """
    Modèle de la table 'personas'.
    Définit les personnalités possibles pour un chatbot.
    """
    __tablename__ = "personas"
    id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nom: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    date_modification: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("now()"))

class Editeur(Base):
    """
    Modèle de la table 'editeurs'.
    Représente les personnes ou les rôles d'éditeur.
    """
    __tablename__ = "editeurs"
    id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nom: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    date_modification: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("now()"))

class Emotion(Base):
    """
    Modèle de la table 'emotions'.
    Liste les émotions qui peuvent être associées à un texte.
    """
    __tablename__ = "emotions"
    id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nom: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    comportement: Mapped[str] = mapped_column(String(250), nullable=False)
    date_modification: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("now()"))
