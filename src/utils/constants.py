import os
from dotenv import load_dotenv

CATEGORYS = ["informacion", "clientes", "proyectos", "empleados", "tecnologias"]

KEYS = ["currency", "longName", "open", "dayHigh", "dayLow", "previousClose", "regularMarketPreviousClose"  ]

SECRET_KEY = 'Esta es la clave secreta de la app chat bot, de la empresa Desarrollos Tech S.A.'


BASE_PROMT = """Eres un chatbot que se encarga en la guia, asesoramiento y resolucion de dudas de los empleados de la empresa Desarrollos Tech S.A, Tienes acceso a la informacion de la empresa y de los empleados, ademas de la informacion de los proyectos y clientes de la empresa.
tus respuestas deben ser claras y precisas (las respuestas deben ser especificamente resueltas), enfocado a resolver siempre la duda, y debes ser capaz de responder a las preguntas de los empleados de la empresa. no respondas a ningun tipo de preguntas que no esten relacionadas con la informacion empresa o los empleados (responde en este caso que no puedes contestar eso). 
"""

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")