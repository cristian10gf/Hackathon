from src.core.auth.tokens import create_token
from src.core.services.funcionalitys import get_response
import flet as ft

import flet as ft

def main(page: ft.Page):
    page.title = "Text theme styles"
    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Image(src=f"/images/logo.png"),
                    ft.Text("chat gpt",size=30),
                    ft.TextButton("log in")
                ]
            )
        )
    )
    token = create_token({"username":"Juan Perez","password":"securepassword123"})
    print(get_response(input("Ingrese su pregunta: "), token))

ft.app(main, assets_dir="assets")
