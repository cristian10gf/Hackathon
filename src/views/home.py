import flet as ft
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
                    ft.OutlinedButton(
                        text="log in",
                        on_click=lambda e: page.go("/login"),
                        width=200,
                        height=60,
                        style=ft.ButtonStyle(
                            color="#ffffff",
                            bgcolor="#28a745",
                        ),
                    ),
                    ft.Text("or", size=20),
                    ft.OutlinedButton(
                        text="sign in",
                        on_click=lambda e: page.go("/sign"),
                        width=200,
                        height=60,
                        style=ft.ButtonStyle(
                            color="#ffffff",
                            bgcolor="#28a745",
                        ),
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
    )
