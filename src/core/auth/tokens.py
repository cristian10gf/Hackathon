import jwt

key = 'Esta es la clave secreta de la app chat bot, de la empresa Desarrollos Tech S.A.'

def create_token(data) -> str:
    token: str = jwt.encode(data, key, algorithm='HS256')
    return token

def verify_token(token: str) -> dict:
    data = None
    try: 
      data = jwt.decode(token, key, algorithms='HS256')
    except:
      return None

    return data