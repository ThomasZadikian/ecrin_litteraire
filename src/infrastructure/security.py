from datetime import datetime, timedelta, timezone
from typing import Optional

from jose import JWTError, jwt
from passlib.context import CryptContext

SECRET_KEY = ""
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verifier_mot_de_passe(mot_de_passe: str, mot_de_passe_hashe:str) -> bool: 
    return pwd_context.verify(mot_de_passe, mot_de_passe_hashe)

def hasher_mot_de_passe(mot_de_passe: str) -> str :
    return pwd_context.hash(mot_de_passe)

def creer_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str :
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else :
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decoder_access_token(token: str) -> Optional[str] : 
    try :
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: Optional[str] = payload.get("sub")
        if email is None:
            return None
        return email
    except JWTError:
        return None