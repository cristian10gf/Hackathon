import jwt
from src.utils.constants import SECRET_KEY


def create_token(data) -> str:
    token: str = jwt.encode(data, SECRET_KEY, algorithm='HS256')
    return token

def verify_token(token: str) -> dict:
    data = None
    try: 
      data = jwt.decode(token, SECRET_KEY, algorithms='HS256')
    except:
      return None

    return data