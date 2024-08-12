import flet as ft
from src.core.services.funcionalitys import cargar_chat
from src.views.components.custom_bottons import get_button_action
from src.views.components.input import get_input_bar
from src.views.comuns import name
from src.views.components.messages import texto_msg, Mensaje_basico_user, Mensaje_basico_bot
from src.views.components.navegation import get_end_draw, get_drawer

def chat_view(page: ft.Page, responder: callable, chats, cerrar_sesion: callable, rol_user):
    page.title = "chat"
    page.clean()

    # Funciones

    def charge_history(e):
        titulo = chats[drawer.selected_index]
        super_dic = cargar_chat(page.client_storage.get("token"), titulo)
        chat_principal.controls.clear()
        chat_principal.controls.append(ft.Container(height=36, bgcolor=ft.colors.TRANSPARENT))
        for dic in super_dic:
            charge_message_user(dic["usuario"])
            add_message_bot(e,dic["bot"])
        e.page.close(drawer)
    
    def load_history(history: list[str]):
        drawer.controls.clear()
    
        history_list = []
        for conversation in history:
            history_list.extend([
                    ft.NavigationDrawerDestination(
                        label=conversation,
                        icon=ft.icons.DOOR_BACK_DOOR_OUTLINED,
                        selected_icon_content=ft.Icon(ft.icons.DOOR_BACK_DOOR),
                    ),
                    ft.Divider(thickness=2), 
                ]
            )
            
        drawer.controls.extend(history_list)
        page.show_drawer(drawer)
        page.update()
        
    def redimensionar_barrabaja(e):
        if len(message_bar.value) < 130:
            barrabaja.height = 80 + 20 * (len(message_bar.value) // 26)
        page.update()
          
    def add_message_user(e):
        chat_principal.controls.append(
            Mensaje_basico_user(
                mensage_content=texto_msg(
                    user_name=name.value,
                    text=message_bar.value,
                    message_type="user",
                )
            )
        ),
        add_message_bot(e,responder(e, message_bar.value))
        message_bar.value = ""
        
        chat_principal.update()
    
    def charge_message_user(texto):
        chat_principal.controls.append(
            Mensaje_basico_user(
                texto_msg(
                    user_name=name.value,
                    text=texto,
                    message_type="user",
                )
            ),
        ),
        message_bar.value = ""
        chat_principal.update()

    def add_message_bot(e, texto):
        chat_principal.controls.append(
            Mensaje_basico_bot(
                texto_msg(
                    user_name="Guidie",
                    text=texto,
                    message_type="bot",
                )
            ),
        ),

        chat_principal.update()


    # Componentes de la vista

    drawer = get_drawer(charge_history)
    end_draw = get_end_draw(cerrar_sesion, rol_user)
    message_bar = get_input_bar(onchage=redimensionar_barrabaja)

    barra = ft.AppBar(
        leading=ft.Row(
            controls=[get_button_action(lambda e: load_history(chats), ft.icons.HISTORY),]
        ),
        leading_width=40,
        title=ft.Row(
            controls=[
                ft.Image(
                    src="/images/robot_logo_peq.png",
                    width=42, height=43,
                    border_radius=10,
                    fit=ft.ImageFit.CONTAIN,
                ),
                ft.Text("Guidie", color=ft.colors.WHITE),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        toolbar_height=50,
        center_title=True,
        bgcolor=ft.colors.BLACK,
        actions=[
            ft.Row(
                controls=[
                    get_button_action(lambda e: page.show_drawer(end_draw), ft.icons.ACCOUNT_CIRCLE_ROUNDED),
                ],
                spacing=0,
                alignment=ft.MainAxisAlignment.END,
                wrap=True,
            ),
        ],
    )

    barrabaja = ft.BottomAppBar(
        bgcolor=ft.colors.BLACK,
        shape=ft.NotchShape.CIRCULAR,
        content=ft.Row(
            controls=[
                ft.Row(
                    [message_bar,],
                    auto_scroll=True,
                    scroll=ft.ScrollMode.AUTO,
                ),
                get_button_action(lambda e: add_message_user(e), ft.icons.SEND_ROUNDED),
            ],
        ),
        height=80,
    )

    chat_principal = ft.ListView(
        controls=[ft.Container(height=36, bgcolor=ft.colors.TRANSPARENT),],
        expand=True,
        spacing=10,
        padding=10,
        auto_scroll=True,
    )

    columna_chat = ft.Column(
        controls=[
            chat_principal,
            ft.Container(height=12, bgcolor=ft.colors.TRANSPARENT),
        ],
        width=338,
        alignment=ft.MainAxisAlignment.START,
        auto_scroll=True,                  
    )

    home_page = ft.Pagelet(
        expand=True, 
        bgcolor=ft.colors.TRANSPARENT,
        content=ft.Stack(
            controls=[
                ft.Stack(
                    left = 0,
                    animate_position=ft.animation.Animation(500, ft.AnimationCurve.EASE_OUT),
                    controls=[
                        ft.Image(
                            src="/images/robot_logo.png",
                            width=340, height=400,
                            border_radius=10,
                            fit=ft.ImageFit.SCALE_DOWN,
                        ),
                        ft.Column(
                            controls=[
                                ft.Container(height=15, bgcolor=ft.colors.TRANSPARENT),
                                ft.Container(
                                    content= columna_chat,
                                    height=638,
                                    padding=20,
                                    margin=-18,
                                    bgcolor=ft.colors.TRANSPARENT,
                                    border_radius=10,
                                ),
                            ]
                        ),
                    ],
                    width=340, height=695,
                ),
            ]
        ),
    )

    page.appbar = barra
    page.bottom_appbar = barrabaja
    page.drawer = drawer
    page.end_drawer = end_draw

    page.add(home_page)
    page.update()