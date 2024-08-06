import flet as ft
from src.views.comuns import logo, name, password


def login_view(page: ft.Page, iniciar_sesion: callable):
    page.title = "login"
    page.clean()
    page.add(
        ft.Container(
            content=ft.Stack(
                controls=[
                    ft.Column(
                        controls=[
                            ft.Row(
                                controls=[ft.IconButton(
                                    icon=ft.icons.ARROW_BACK,
                                    on_click=lambda e: page.go("/"),
                                    width=40,
                                    height=40,
                                    icon_size=30),
                                ft.Text("   welcome back", size=30)]),
                            logo,
                            name,
                            password,
                             ft.ElevatedButton(
                                text="log in",
                                bgcolor="#007bff",
                                color="#ffffff",
                                on_click=iniciar_sesion
                             ),
                            ft.Row([
                                ft.Text("dont have an account?"),
                                ft.TextButton(
                                    text="sign in here",
                                    on_click=lambda e: page.go("/sign"),
                                    style=ft.ButtonStyle(
                                        color="#007bff"
                                    )
                                ),
                            ], alignment=ft.MainAxisAlignment.CENTER)
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    )
                ]
            )
        )
    )