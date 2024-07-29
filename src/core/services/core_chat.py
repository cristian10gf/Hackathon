import google.generativeai as genai

from src.core.db.db import get_all_clients, get_all_projects, get_all_tools, get_all_users
from src.core.db.other_info import empresa
from src.utils.constants import API_KEY, BASE_PROMT


class GeminiModel:
    def __init__(self, api_key):
        self.api_key = api_key
        genai.configure(api_key=self.api_key)
        self.gemini_model = genai.GenerativeModel("gemini-1.5-flash")
    
    def generate_prompt(self, message, modo):
        new_prompt = ""
        
        if modo == 0:
          new_prompt = BASE_PROMT + '\n' + f'esta es la pregunta de un empleado: {message}, responde a la pregunta del empleado basado en la informacion de la empresa. {empresa}'
        elif modo == 1:
          new_prompt = BASE_PROMT + '\n' + f'esta es la pregunta de un empleado: {message}, responde a la pregunta del empleado basado en la informacion de la empresa. {empresa},{get_all_clients()}'
        elif modo == 2:
          new_prompt = BASE_PROMT + '\n' + f'esta es la pregunta de un empleado: {message}, responde a la pregunta del empleado basado en la informacion de la empresa. {empresa},{get_all_projects()}, {get_all_tools()}'
        elif modo == 3:
          new_prompt = BASE_PROMT + '\n' + f'esta es la pregunta de un empleado: {message}, responde a la pregunta del empleado basado en la informacion de la empresa. {empresa},{get_all_users()}'
        elif modo == 4:
          new_prompt = BASE_PROMT + '\n' + f'esta es la pregunta de un empleado: {message}, responde a la pregunta del empleado basado en la informacion de la empresa. {empresa},{get_all_projects()}'
        elif modo == -2:
           new_prompt = f"crea un unico titulo muy corto para este mensaje {message} (solo responde con el primer titulo que tengas)"
        else:
          new_prompt = BASE_PROMT + '\n' + f'esta es la pregunta de un empleado: {message}, responde a la pregunta del empleado basado en la informacion de la empresa. {empresa},{get_all_clients()}, {get_all_projects()},{get_all_users()}, {get_all_tools()}'
        
        return new_prompt
    
    def generate_text(self, message, modo = -1):
        prompt = self.generate_prompt(message, modo)
        response = self.gemini_model.generate_content([prompt])
        lista = response.text.splitlines()
        lista_filtrada = list(filter(None, lista))
        return "\n".join(lista_filtrada)

gemini_model = GeminiModel(api_key=API_KEY)