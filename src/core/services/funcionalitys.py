from src.core.auth.tokens import create_token, verify_token
from src.core.db.db import add_message, get_all_name_messages, get_chat, get_user
from src.core.services.core_chat import gemini_model
from src.utils.constants import CATEGORYS

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


def cargar_chat(token: str, name: str) -> list[dict[str, str]]:
    data = verify_token(token)
    if not data:
        return []
    
    user = get_user(data["username"], data["password"])
    mensages = get_chat(user.id, name).sort(key=lambda x: x.fecha)

    return [{"usuario": message.texto, "bot": message.response }  for message in mensages]

def guardar_mensaje(token: str, message: str, response: str, name: str = "") -> str:
    data = verify_token(token)
    if not data:
        return None
    
    user = get_user(data["username"], data["password"])
    titulo = gemini_model.generate_text(message, -2) if name == "" else name

    add_message(user.id, message, response, titulo)
    return titulo

def cargar_name_chats(token: str) -> list[str]:
    data = verify_token(token)
    if not data:
        return []
    
    user = get_user(data["username"], data["password"])
    return get_all_name_messages(user.nombre)


def login(username: str, password: str) -> str | tuple[str, list[str], str]:
  rol = validate_user(username, password)

  if rol == "Usuario no encontrado":
    return "Usuario no encontrado"
  
  token = create_token({"username": username, "password": password})

  chats = cargar_name_chats(token)

  return token, chats, rol

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
    elif rol == "empleado" and category == 3:
        return "No tienes permiso para acceder a la información de todos los empleados."
    
    pront = f"{message}, esta es mi informacion personal en la empresa= {get_user(data['username'], data['password'])}"
    print(pront)
    return gemini_model.generate_text(pront,  category)