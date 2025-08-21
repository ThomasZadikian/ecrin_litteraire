from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

# URL de connexion à la base de données.
# Format: postgresql+asyncpg://utilisateur:motdepasse@hote:port/nom_de_la_bdd
# Pour un développement local avec Docker, ce sera souvent quelque chose comme ça.
DATABASE_URL = "postgresql+asyncpg://user:password@localhost/ecrin_litteraire_db"

# L'Engine est le point d'entrée central vers la base de données.
# Il est créé une seule fois par application.
engine = create_async_engine(DATABASE_URL, echo=True)

# Le SessionMaker est une "fabrique" qui crée de nouvelles sessions (conversations)
# avec la base de données quand on en a besoin.
AsyncSessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine, 
    class_=AsyncSession
)

# Dépendance pour obtenir une session de base de données par requête
async def get_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session