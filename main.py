import flet as ft
from src.core.services.funcionalitys import get_response, guardar_mensaje, login
from src.views.home import home_view
from src.views.login import login_view
from src.views.comuns import logo, name, password, pr, error
from src.views.chat import chat_view

# Controles comunes
chats = []
titlechat = ""
rol_user = ""

loadedhistory = False

def iniciar_sesion(e: ft.ControlEvent):
    datos = login(name.value,password.value)
    print(datos)
    if datos == "Usuario no encontrado":
        if error not in e.page.controls:
            e.page.add(error)
        return
    
    token, chatsviejos, rol = datos 
    global chats, rol_user
    chats = list(set(chatsviejos))
    rol_user = rol

    if token == "Usuario no encontrado":
        print("Usuario no encontrado")
        return
    e.page.client_storage.set("token", token)

    
    e.page.go("/chat")

def cerrar_sesion(e: ft.ControlEvent):
    e.page.client_storage.set("token", "")

    global titlechat, chats, loadedhistory, rol_user

    titlechat = ""
    chats = []
    loadedhistory = False
    rol_user = ""

    e.page.drawer = None
    e.page.end_drawer = None
    e.page.appbar = None
    e.page.bottom_appbar = None

    e.page.clean()
    e.page.go("/")
    e.page.update()

def responder(e: ft.ControlEvent, texto: str = "") -> str:
    token = e.page.client_storage.get("token")
    e.page.add(pr)
    e.page.update()

    response = get_response(texto, token)

    e.page.remove(pr)

    global titlechat
    global loadedhistory

    titlechat = guardar_mensaje(token, texto, response, titlechat)

    if titlechat not in chats:
        chats.append(titlechat)

    return response

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


def main(page: ft.Page):
    page.title = "Home"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.height = 812
    page.window.width = 375
    page.bgcolor = "#a5d8ff"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.fonts = {
        "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
        "Comfortaa": "fonts/Comfortaa-Regular.ttf",
        "Roboto": "fonts/Roboto-Medium.ttf",
    }

    def route_change(e):
        page.controls.clear()
        if page.route == "/":
            home_view(page)
        elif page.route == "/sign":
            sign_view(page)
        elif page.route == "/login":
            login_view(page, iniciar_sesion)
        elif page.route == "/chat":
            chat_view(page, responder, chats, cerrar_sesion, rol_user)
    
    page.on_route_change = route_change
    page.go(page.route)

ft.app(main, assets_dir="assets")