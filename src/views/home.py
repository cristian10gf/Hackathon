import flet as ft
from src.views.components.custom_bottons import get_main_button
from src.views.comuns import logo

def home_view(page: ft.Page):
    page.title = "home"
    page.clean()
    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    logo,
                    ft.Text("Guidie", size=30),
                    get_main_button("log in", lambda e: page.go("/login")),
                    ft.Text("or", size=20),
                    get_main_button("sign in", lambda e: page.go("/sign")),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
    )