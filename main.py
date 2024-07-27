from src.core.services.funcionalitys import get_response
import flet as ft

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.title = "Flet Chat"

    print(get_response(input("Ingrese su pregunta: "), "Juan Perez","securepassword123" ))

print(get_response(input("Ingrese su pregunta: ")))