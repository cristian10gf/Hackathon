import flet as ft
from src.core.services.funcionalitys import get_response, login

# Controles comunes

logo = ft.Image(src="/images/logo.png", width=300, height=300)
name = ft.TextField(hint_text="name", border="underline", height=60, width=200)
password = ft.TextField(hint_text="password", password=True, border="underline", can_reveal_password=True, height=60, width=200)
input = ft.TextField(hint_text="message", border="underline", height=60, width=200)
pr = ft.ProgressRing(width=50, height=50, stroke_width = 2)

# Eventos

def iniciar_sesion(e: ft.ControlEvent):
    token = login(name.value,password.value)
    
    if token == "Usuario no encontrado":
        print("Usuario no encontrado")
        return
    e.page.client_storage.set("token", token)

    e.page.go("/chat")

def responder(e: ft.ControlEvent):
    token = e.page.client_storage.get("token")
    e.page.add(pr)
    e.page.update()

    response = get_response(input.value, token)

    e.page.remove(pr)
    e.page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Markdown(response),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
    )


# Vistas

def home_view(page: ft.Page):
    page.title = "chat"
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


def login_view(page: ft.Page):
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

def sign_view(page: ft.Page):
    page.title = "sign"
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
                            logo,
                            name,
                            password,
                            ft.ElevatedButton(
                                text="sign up",
                                bgcolor="#28a745",
                                color="#ffffff",
                                on_click=iniciar_sesion
                            ),
                            ft.Row([
                                ft.Text("already have an account?"),
                                ft.TextButton(
                                    text="log in here",
                                    style=ft.ButtonStyle(
                                        color="#007bff",
                                    ),
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

def chat_view(page: ft.Page):
    page.title = "chat"
    page.clean()
    page.add(
        ft.Container(
            content=ft.Stack(
                controls=[
                    ft.Column(
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.IconButton(
                                        icon=ft.icons.ARROW_BACK,
                                        on_click=lambda e: page.go("/"),
                                        width=40,
                                        height=40,
                                        icon_size=30
                                    ),
                                    ft.Text("   chat", size=30)
                                ]
                            ),
                            logo,
                            input,
                            ft.ElevatedButton(
                                text="send", 
                                on_click=responder
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    )
                ]
            )
        )
    )



def main(page: ft.Page):
    page.title = "Home"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.height = 812
    page.window.width = 375
    page.bgcolor = "#a5d8ff"
    page.theme_mode = ft.ThemeMode.LIGHT

    def route_change(e):
        if page.route == "/":
            home_view(page)
        elif page.route == "/sign":
            sign_view(page)
        elif page.route == "/login":
            login_view(page)
        elif page.route == "/chat":
            chat_view(page)
    
    page.on_route_change = route_change
    page.go(page.route)

ft.app(main, assets_dir="assets")