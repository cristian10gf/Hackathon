import flet as ft

from src.core.auth.tokens import create_token
from src.core.services.funcionalitys import get_response














































def home_view(page: ft.Page):
    page.title = "Home"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.height = 812
    page.window.width = 375
    page.bgcolor = "#a5d8ff"
    page.clean()
    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Image(src="/images/logo.png", width=300, height=300),
                    ft.Text("chat gpt", size=30),
                    ft.OutlinedButton(
                        text="log in", 
                        on_click=lambda e: page.go("/login"),
                        width=200,
                        height=60, 
                    ),
                    ft.Text("or", size=20),
                    ft.OutlinedButton(
                        text="sign in", 
                        on_click=lambda e: page.go("/sign"),
                        width=200,
                        height=60,
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
    )

def login_view(page: ft.Page):
    page.title = "login"
    page.bgcolor = "#a5d8ff"
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
                            ft.Image(src="/images/logo.png", width=300, height=300),
                            ft.TextField(hint_text="name", 
                                        border="underline",
                                        height=60,
                                        width=200),
                            ft.TextField(
                                hint_text="password", 
                                password=True, 
                                border="underline", 
                                can_reveal_password=True,
                                height=60,
                                width=200
                            ),
                            ft.ElevatedButton(
                                text="log in", 
                            ),
                            ft.Row([
                                ft.Text("dont have an account?"),
                                ft.TextButton(
                                    text="sign in here",
                                    on_click=lambda e: page.go("/sign")
                                ),
                            ], alignment=ft.MainAxisAlignment.CENTER)
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    )
                ]
            )
        )
    )

def sign_view(page: ft.Page):
    page.title = "sign"
    page.bgcolor = "#a5d8ff"
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
                                ft.Text("   get started now", size=30)]),
                            ft.Image(src="/images/logo.png", width=300, height=300),
                            ft.TextField(hint_text="name",
                                        border="underline",
                                        height=60,
                                        width=200),
                            ft.TextField(
                                hint_text="password", 
                                password=True, 
                                border="underline", 
                                can_reveal_password=True,
                                height=60,
                                width=200
                            ),
                            ft.ElevatedButton(
                                text="sign up", 
                            ),
                            ft.Row([
                                ft.Text("already have an account?"),
                                ft.TextButton(
                                    text="log in here",
                                    on_click=lambda e: page.go("/login")
                                ),
                            ], alignment=ft.MainAxisAlignment.CENTER)
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    )
                ]
            )
        )
    )

def main(page: ft.Page):
    def route_change(e):
        if page.route == "/":
            home_view(page)
        elif page.route == "/sign":
            sign_view(page)
        elif page.route == "/login":
            login_view(page)
    
    page.on_route_change = route_change
    page.go(page.route)


    token = create_token({"username":"Juan Perez","password":"securepassword123"})
    print(get_response(input("Ingrese su pregunta: "), token))


ft.app(main, assets_dir="assets")
