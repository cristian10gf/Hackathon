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

ft.app(main, assets_dir="assets")
