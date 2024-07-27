from src.core.auth.tokens import create_token, verify_token
from src.core.db.db import get_user
from src.core.services.core_chat import gemini_model

CATEGORYS = ["informacion", "clientes", "proyectos", "empleados"]

def search_category(message: str) -> int:
    message_keywords = filter(lambda me: len(me) > 6, message.split())
    for keyword in message_keywords:
        if keyword in CATEGORYS:
            return CATEGORYS.index(keyword)
    return -1

def validate_message(message: str) -> bool:
    return len(message) > 6

def get_simple_response(message: str) -> str:
    response = gemini_model.generate_text(message)
    return response

def validate_user(username: str, password: str) -> str:
    usuario = get_user(username, password)
    if usuario:
        return usuario.rol
    
    return "Usuario no encontrado"


def login(username: str, password: str) -> str:
  rol = validate_user(username, password)

  if rol == "Usuario no encontrado":
    return "Usuario no encontrado"
  
  token = create_token(username, password)

  return token

def get_response(message: str, token: str) -> str:
    if not validate_message(message):
        return "Por favor, proporcione una pregunta más detallada."
    
    data = verify_token(token)

    if not data:
        return "Token invalido"
    
    rol = validate_user(data["username"], data["password"])
    if rol == "Usuario no encontrado":
        return "No tienes permiso para acceder a esta información."
    
    category = search_category(message)
    if category == -1:
        return get_simple_response(message)
    
    if rol != "gerente" and category == 1:
        return "No tienes permiso para acceder a la información de los clientes."
    elif rol != "empleado" and category == 3:
        return "No tienes permiso para acceder a la información de todos los empleados."
    
    return gemini_model.generate_text(message, category)

