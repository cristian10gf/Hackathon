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

def get_response(message: str, usuario: str, contraseña: str) -> str:
    if not validate_message(message):
        return "Por favor, proporcione una pregunta más detallada."
    
    rol = validate_user(usuario, contraseña)
    if rol == "Usuario no encontrado":
        return "No tienes permiso para acceder a esta información."
    
    category = search_category(message)
    if category == -1:
        return get_simple_response(message)
    
    if rol != "gerente" and category == 1:
        return "No tienes permiso para acceder a la información de los clientes."
    elif rol != "empleado" and category == 2:
        return "No tienes permiso para acceder a la información de todos los empleados."
    
    return gemini_model.generate_text(message, category)

