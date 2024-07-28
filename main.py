import flet as ft

from src.core.auth.tokens import create_token
from src.core.services.funcionalitys import get_response


def main(page: ft.Page):
    page.title = "Text theme styles"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.window_height = 812
    page.window_width = 375
    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Image(src=f"/images/logo.png",width=300,height=300),
                    ft.Text("chat gpt",size=30),
                    ft.OutlinedButton("log in"),
                    ft.Text("or",size=20),
                    ft.OutlinedButton("sign in")
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
    )
    token = create_token({"username":"Juan Perez","password":"securepassword123"})
    print(get_response(input("Ingrese su pregunta: "), token))


ft.app(main, assets_dir="assets")
