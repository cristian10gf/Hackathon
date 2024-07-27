import google.generativeai as genai
import os
from dotenv import load_dotenv

base_prompt = "Eres un guia perteneciente a la universidad del Norte, tus respuestas deben ser claras y precisas, no debes dar informacion que no sea relevante a la pregunta, favorablemente de 20 palabras o menos."

class GeminiModel:
    def __init__(self, api_key):
        self.api_key = api_key
        genai.configure(api_key=self.api_key)
        self.gemini_model = genai.GenerativeModel("gemini-1.5-flash")
    
    def generate_prompt(self, message, modo=1, adicional=""):
        new_prompt = ""
        if modo == 1:
            new_prompt = f"""{base_prompt}, Estas para ayudar con las dudas de los estudiantes con respecto a lugares de la universidad.
            puedes guiarte de la imagen del mapa de la universidad para responder las preguntas.
            Pregunta: ¿{message} en la universidad del Norte? Respuesta:"""
        elif modo == 2:
            new_prompt = f"¿{message}? esta informacion es util para responder la pregunta: {adicional}"
        elif modo == 3:
            new_prompt = f"""{base_prompt}, guiate de la imagen del mapa de la universidad para responder las preguntas.
            usa la siguiente informacion para responder la pregunta: {adicional}. 
            Mi pregunta es ¿{message}?"""
        
        return new_prompt
    
    def generate_text(self, message, modo = 1, adicional = ""):
        prompt = self.generate_prompt(message, modo, adicional)
        response = self.gemini_model.generate_content([prompt, mapa])
        lista = response.text.splitlines()
        lista_filtrada = list(filter(None, lista))
        return "\n".join(lista_filtrada)

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
gemini_model = GeminiModel(api_key=API_KEY)


