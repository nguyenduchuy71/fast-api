from jose import JWTError, jwt
from datetime import datetime, timedelta
# SECRET_KEY
# Algorithm
SECRET_KEY = '18066791'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt


def verify_access_token(token: str, credentials_exception):
    jwt.decode(token, SECRET_KEY, algorithm=ALGORITHM)
