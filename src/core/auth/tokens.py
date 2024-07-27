from jwt import encode, decode

key = 'Esta es la clave secreta de la app chat bot, de la empresa Desarrollos Tech S.A.'

def create_token(data) -> str:
    token: str = encode(data, key, algorithm='HS256')
    return token

def verify_token(token: str) -> dict:
    data = None
    try: 
      data = decode(token, key, algorithms='HS256')
    except:
      return None

    return data