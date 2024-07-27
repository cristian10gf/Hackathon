import google.generativeai as genai
import os
from dotenv import load_dotenv
from src.core.db.db import get_all_clients, get_all_projects, get_all_users
from src.core.db.other_info import empresa

base_prompt = """Eres un chatbot que se encarga en la guia, asesoramiento y resolucion de dudas de los empleados de la empresa Desarrollos Tech S.A, Tienes acceso a la informacion de la empresa y de los empleados, ademas de la informacion de los proyectos y clientes de la empresa.
tus respuestas deben ser claras y precisas, enfocado a resolver siempre la duda, y debes ser capaz de responder a las preguntas de los empleados de la empresa. no respondas a ningun tipo de preguntas que no esten relacionadas con la empresa o los empleados (responde en este caso que no puedes contestar eso). 
"""

class GeminiModel:
    def __init__(self, api_key):
        self.api_key = api_key
        genai.configure(api_key=self.api_key)
        self.gemini_model = genai.GenerativeModel("gemini-1.5-flash")
    
    def generate_prompt(self, message, modo=0):
        new_prompt = ""
        
        if modo == 0:
          new_prompt = base_prompt + '\n' + f'esta es la pregunta de un empleado: {message}, responde a la pregunta del empleado basado en la informacion de la empresa. {empresa}'
        elif modo == 1:
          new_prompt = base_prompt + '\n' + f'esta es la pregunta de un empleado: {message}, responde a la pregunta del empleado basado en la informacion de la empresa. {empresa},{get_all_clients()}'
        elif modo == 2:
          new_prompt = base_prompt + '\n' + f'esta es la pregunta de un empleado: {message}, responde a la pregunta del empleado basado en la informacion de la empresa. {empresa},{get_all_projects()}'
        elif modo == 3:
          new_prompt = base_prompt + '\n' + f'esta es la pregunta de un empleado: {message}, responde a la pregunta del empleado basado en la informacion de la empresa. {empresa},{get_all_users()}'
        else:
          new_prompt = base_prompt + '\n' + f'esta es la pregunta de un empleado: {message}, responde a la pregunta del empleado basado en la informacion de la empresa. {empresa},{get_all_clients()}, {get_all_projects()},{get_all_users()}'
        return new_prompt
    
    def generate_text(self, message, modo = 0):
        prompt = self.generate_prompt(message, modo)
        response = self.gemini_model.generate_content([prompt])
        lista = response.text.splitlines()
        lista_filtrada = list(filter(None, lista))
        return "\n".join(lista_filtrada)

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
gemini_model = GeminiModel(api_key=API_KEY)


