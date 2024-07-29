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
    page.title = "home"
    page.clean()
    #set to none to remove the controls in non chat_view pages
    page.appbar = None
    page.drawer = None
    page.end_drawer = None
    page.bottom_appbar = None
    ##########################################################
    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    logo,
                    ft.Text("GuiDie", size=30),
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
    #set to none to remove the controls in non chat_view pages
    page.appbar = None
    page.drawer = None
    page.end_drawer = None
    page.bottom_appbar = None
    ##########################################################
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
    #set to none to remove the controls in non chat_view pages
    page.appbar = None
    page.drawer = None
    page.end_drawer = None
    page.bottom_appbar = None
    ##########################################################
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
    #####################################################################################
    # eventos drawer
    def handle_dismissal(e):  # drawer event
        # page.add(ft.Text("Drawer dismissed"))
        print("Drawer dismissed")

    def handle_change(e):  # drawer event
        print(f"Selected Index changed: {drawer.selected_index}")
        # page.close(drawer)

    #####################################################################################

    #####################################################################################

    drawer = ft.NavigationDrawer(
        on_dismiss=handle_dismissal,
        on_change=handle_change,
        controls=[
            ft.Container(height=12),
            ft.NavigationDrawerDestination(
                label="Item 1",
                icon=ft.icons.DOOR_BACK_DOOR_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.DOOR_BACK_DOOR),
            ),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.MAIL_OUTLINED),
                label="Item 2",
                selected_icon=ft.icons.MAIL,
            ),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.PHONE_OUTLINED),
                label="Item 3",
                selected_icon=ft.icons.PHONE,
            ),
        ],
        bgcolor="#0e1e36",
    )

    end_draw = ft.NavigationDrawer(
        on_dismiss=handle_dismissal,
        on_change=handle_change,
        controls=[
            ft.Container(height=12),
            ft.NavigationDrawerDestination(
                label="Item 1",
                icon=ft.icons.DOOR_BACK_DOOR_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.DOOR_BACK_DOOR),
            ),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.MAIL_OUTLINED),
                label="Item 2",
                selected_icon=ft.icons.MAIL,
            ),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.PHONE_OUTLINED),
                label="Item 3",
                selected_icon=ft.icons.PHONE,
            ),
        ],
        bgcolor="#0e1e36",
    )

    barra = ft.AppBar(
        leading=ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.icons.HISTORY,
                    on_click=lambda e: page.show_drawer(drawer),
                    bgcolor=ft.colors.BLACK,
                    icon_color=ft.colors.WHITE,
                    icon_size=35,
                    enable_feedback=True,
                    hover_color=ft.colors.with_opacity(0.1, "#ededed"),
                    highlight_color=ft.colors.with_opacity(0.1, "#ededed"),
                    focus_color=ft.colors.with_opacity(0.1, "#ededed"),
                )
            ]
        ),
        leading_width=40,
        title=ft.Text("Guidie", color=ft.colors.WHITE),
        toolbar_height=50,
        center_title=True,
        bgcolor=ft.colors.BLACK,
        actions=[
            ft.Row(
                controls=[
                    ft.IconButton(
                        icon=ft.icons.ACCOUNT_CIRCLE_ROUNDED,
                        on_click=lambda e: page.show_drawer(end_draw),
                        bgcolor=ft.colors.BLACK,
                        icon_color=ft.colors.WHITE,
                        icon_size=35,
                        # expand=True,
                        # enable_feedback=True,
                        hover_color=ft.colors.with_opacity(0.1, "#ededed"),
                        highlight_color=ft.colors.with_opacity(0.1, "#ededed"),
                        focus_color=ft.colors.with_opacity(0.1, "#ededed"),
                    ),
                ],
                spacing=0,
                alignment=ft.MainAxisAlignment.END,
                wrap=True,
            ),
            # boton_flecha,
        ],
    )

    borde = ft.Border(
        top=ft.BorderSide(1, ft.colors.with_opacity(1, "#d9d9d9")),
        bottom=ft.BorderSide(1, ft.colors.with_opacity(1, "#d9d9d9")),
        left=ft.BorderSide(1, ft.colors.with_opacity(1, "#d9d9d9")),
        right=ft.BorderSide(1, ft.colors.with_opacity(1, "#d9d9d9")),
    )

    def redimensionar_barrabaja(e):
        if len(message_bar.value) < 130:
            barrabaja.height = 80 + 20 * (len(message_bar.value) // 26)
        page.update()

    message_bar = ft.TextField(
        hint_text="Write a message...",
        # autofocus=True,
        multiline=True,
        on_change=redimensionar_barrabaja,
        # shift_enter=True,
        # min_lines=1,
        max_lines=5,
        filled=True,
        # expand=0.2,
        # on_submit=send_message_click,
        # max_length=500,
        width=270,
        # multiline=True,
        read_only=False,
        bgcolor=ft.colors.WHITE,
        color=ft.colors.GREEN,
        border=ft.InputBorder.OUTLINE,
        border_color=ft.colors.WHITE,
        hover_color=ft.colors.TRANSPARENT,
        text_style=ft.TextStyle(font_family="Roboto"),
        border_radius=10,
    )

    

   
    class texto_msg:
        def __init__(self, user_name: str, text: str, message_type: str):
            self.user_name = user_name
            self.text = text


    mensaje_basico = ft.Row(
        vertical_alignment=ft.CrossAxisAlignment.START,
        controls=[
            ft.CircleAvatar(
                content=ft.Image(
                    src="/images/Nao_nao.png",
                    # width=340,
                    # height=400,
                    border_radius=10,
                    fit=ft.ImageFit.CONTAIN,
                ),
                bgcolor=ft.colors.WHITE,
                # bgcolor=self.get_avatar_color(message.user_name),
            ),
            ft.Card(
                    content=ft.TextField(
                        value="""Guidie: Hola, ¿en qué puedo ayudarte?""",
                        multiline=True,
                        # min_lines=1,
                        # max_lines=8,
                        read_only=True,
                        # text_size=33,
                        filled=True,
                        text_align=ft.TextAlign.START,
                        bgcolor=ft.colors.TRANSPARENT,
                        color=ft.colors.BLACK,
                        border=ft.InputBorder.NONE,
                        border_color=ft.colors.TRANSPARENT,
                        hover_color=ft.colors.TRANSPARENT,
                        # height=74,
                        width=200,
                        # expand=True,
                        text_style=ft.TextStyle(font_family="Roboto"),
                        border_radius=10,
                       
                    ),
                    width=300,
                    # height=,
                    elevation=5,
                    expand=True,
                )
        ],
        # border=borde,
        # border_radius=10,
        # bgcolor=ft.colors.WHITE,
        width=270,
        # height=74,
    )

    mensaje_basico_user = ft.Row(
        controls=[
            ft.Card(
                    content=ft.TextField(
                        value="""Fernando: Me gustaría saber si tienes información sobre el clima laboral de la empresa, por favor.""",
                        multiline=True,
                        # min_lines=1,
                        # max_lines=8,
                        read_only=True,
                        # text_size=33,
                        filled=True,
                        text_align=ft.TextAlign.START,
                        bgcolor=ft.colors.TRANSPARENT,
                        color=ft.colors.BLACK,
                        border=ft.InputBorder.NONE,
                        border_color=ft.colors.TRANSPARENT,
                        hover_color=ft.colors.TRANSPARENT,
                        # height=74,
                        width=200,
                        # expand=True,
                        text_style=ft.TextStyle(font_family="Roboto"),
                        border_radius=10,
                       
                    ),
                    width=300,
                    # height=,
                    elevation=5,
                    expand=True,
                ),
            ft.CircleAvatar(
                content=ft.Text("F"),
                color=ft.colors.WHITE,
                bgcolor=ft.colors.CYAN,
                # bgcolor=self.get_avatar_color(message.user_name),
            ),
        ],
        vertical_alignment = ft.CrossAxisAlignment.START,
        width=270,
        
    )
    class Mensaje_basico_user(ft.Row):
        def __init__(self, mensage_content: texto_msg):
            super().__init__()
            self.vertical_alignment = ft.CrossAxisAlignment.START
            self.width = 270
            self.controls = [
                ft.Card(
                    content=ft.TextField(
                        value=mensage_content.text,
                        multiline=True,
                        # min_lines=1,
                        # max_lines=8,
                        read_only=True,
                        # text_size=33,
                        filled=True,
                        text_align=ft.TextAlign.START,
                        bgcolor=ft.colors.TRANSPARENT,
                        color=ft.colors.BLACK,
                        border=ft.InputBorder.NONE,
                        border_color=ft.colors.TRANSPARENT,
                        hover_color=ft.colors.TRANSPARENT,
                        # height=74,
                        width=200,
                        # expand=True,
                        text_style=ft.TextStyle(font_family="Roboto"),
                        border_radius=10,
                       
                    ),
                    width=300,
                    # height=,
                    elevation=5,
                    expand=True,
                ),
                ft.CircleAvatar(
                    content=ft.Text(self.get_initials(mensage_content.user_name)),
                    color=ft.colors.WHITE,
                    bgcolor=self.get_avatar_color(mensage_content.user_name),
                    # bgcolor=self.get_avatar_color(message.user_name),
                ),
            ]

        def get_initials(self, user_name: str):
            if user_name:
                return user_name[:1].capitalize()
            else:
                return "Unknown"  # or any default value you prefer

        def get_avatar_color(self, user_name: str):
            colors_lookup = [
                ft.colors.AMBER,
                ft.colors.BLUE,
                ft.colors.BROWN,
                ft.colors.CYAN,
                ft.colors.GREEN,
                ft.colors.INDIGO,
                ft.colors.LIME,
                ft.colors.ORANGE,
                ft.colors.PINK,
                ft.colors.PURPLE,
                ft.colors.RED,
                ft.colors.TEAL,
                ft.colors.YELLOW,
            ]
            return colors_lookup[hash(user_name) % len(colors_lookup)]

    class Mensaje_basico_bot(ft.Row):
        def __init__(self, mensage_content: texto_msg):
            super().__init__()
            self.vertical_alignment = ft.CrossAxisAlignment.START
            self.width = 270
            self.controls = [
                ft.CircleAvatar(
                content=ft.Image(
                    src="/images/Nao_nao.png",
                    # width=340,
                    # height=400,
                    border_radius=10,
                    fit=ft.ImageFit.CONTAIN,
                ),
                bgcolor=ft.colors.TRANSPARENT,
                # bgcolor=self.get_avatar_color(message.user_name),
            ),
                ft.Card(
                    content=ft.TextField(
                        value=mensage_content.text,
                        multiline=True,
                        # min_lines=1,
                        # max_lines=8,
                        read_only=True,
                        # text_size=33,
                        filled=True,
                        text_align=ft.TextAlign.START,
                        bgcolor=ft.colors.TRANSPARENT,
                        color=ft.colors.BLACK,
                        border=ft.InputBorder.NONE,
                        border_color=ft.colors.TRANSPARENT,
                        hover_color=ft.colors.TRANSPARENT,
                        # height=74,
                        width=200,
                        # expand=True,
                        text_style=ft.TextStyle(font_family="Roboto"),
                        border_radius=10,
                       
                    ),
                    width=300,
                    # height=,
                    elevation=5,
                    expand=True,
                ),
            ]

        
    

    """
    ft.PopupMenuButton(
                    icon=ft.icons.MORE_VERT,
                    items=[
                        ft.PopupMenuItem(text="Item 1"),
                        ft.PopupMenuItem(),  # divider
                        ft.PopupMenuItem(
                            text="Checked item",
                            checked=False,
                        ),
                    ],
                ),
    """

    def add_message_user(e):
        chat_principal.controls.append(
           
            Mensaje_basico_user(
                mensage_content=texto_msg(
                    user_name="Fernando",
                    text=message_bar.value,
                    message_type="user",
                )
            ),
        ),

        chat_principal.update()

    def add_message_bot(e, texto):
        chat_principal.controls.append(
           
            Mensaje_basico_bot(
                mensage_content=texto_msg(
                    user_name="Guidie",
                    text=texto,
                    message_type="bot",
                )
            ),
        ),

        chat_principal.update()


    barrabaja = ft.BottomAppBar(
        bgcolor=ft.colors.BLACK,
        shape=ft.NotchShape.CIRCULAR,
        # width=375,
        content=ft.Row(
            controls=[
                ft.Row(
                    [
                        message_bar,
                    ],
                    auto_scroll=True,
                    scroll=ft.ScrollMode.AUTO,
                ),
                # ft.Container(expand=True),
                ft.IconButton(
                    icon=ft.icons.SEND_ROUNDED,
                    on_click=lambda e: add_message_user(e),
                    bgcolor=ft.colors.BLACK,
                    icon_color=ft.colors.WHITE,
                    icon_size=30,
                    # expand=True,
                    # enable_feedback=True,
                    hover_color=ft.colors.with_opacity(0.1, "#ededed"),
                    highlight_color=ft.colors.with_opacity(0.1, "#ededed"),
                    focus_color=ft.colors.with_opacity(0.1, "#ededed"),
                ),
            ],
            # auto_scroll=True,
        ),
        height=80,
    )

    page.fonts = {
        "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
        "Comfortaa": r"fonts\Comfortaa-Regular.ttf",
        "Roboto": r"fonts\Roboto-Medium.ttf",
    }

    page.appbar = barra

    # page.navigation_bar = nav_bar

    page.drawer = drawer
    page.end_drawer = end_draw
    page.bottom_appbar = barrabaja

    chat_principal = ft.ListView(
        controls=[
            ft.Container(height=36, bgcolor=ft.colors.TRANSPARENT),
            mensaje_basico,
            mensaje_basico_user,
        ],
        # width=340,
        # height=693,
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
                            # expand=True,
                            width=338,
                            # height=693,
                            alignment=ft.MainAxisAlignment.START,
                            auto_scroll=True,
                           
                            
                        )
    
    pagina0 = ft.Stack(
        left=0,
        animate_position=ft.animation.Animation(500, ft.AnimationCurve.EASE_OUT),
        controls=[
            ft.Image(
                src="/images/robot_logo.png",
                width=340,
                height=400,
                border_radius=10,
                fit=ft.ImageFit.SCALE_DOWN,
            ),
            ft.Column(
                controls=[
                    ft.Container(height=15, bgcolor=ft.colors.TRANSPARENT),
                    ft.Container(
                        content= columna_chat,
                        # content=ft.Row(controls=[ft.Text("Pagina 2")]),
                        # bgcolor=ft.colors.with_opacity(0.5, "#dfe2e1"),
                        height=638,
                        padding=20,
                        margin=-18,
                        bgcolor=ft.colors.TRANSPARENT,
                        border_radius=10,
                        
                    ),
                ]
            ),
        ],
        width=340,
        height=695,
    )

    home_page = ft.Pagelet(
        content=ft.Stack(
            [
                pagina0,
            ],
        ),
        expand=True,
        bgcolor=ft.colors.TRANSPARENT,
    )

    page.add(home_page)
    print(page.window.height)
    print(page.window.width)
    page.update()



def main(page: ft.Page):
    page.title = "Hack_demo"
    page.theme_mode = ft.ThemeMode.LIGHT
    #set to none to remove the controls in non chat_view pages
    page.appbar = ft.AppBar(
        leading=ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.icons.HISTORY,
                    on_click=lambda e: page.show_drawer(drawer),
                    bgcolor=ft.colors.BLACK,
                    icon_color=ft.colors.WHITE,
                    icon_size=35,
                    enable_feedback=True,
                    hover_color=ft.colors.with_opacity(0.1, "#ededed"),
                    highlight_color=ft.colors.with_opacity(0.1, "#ededed"),
                    focus_color=ft.colors.with_opacity(0.1, "#ededed"),
                )
            ]
        ),
        leading_width=40,
        title=ft.Row(
            controls=[
                ft.Image(
                    src="/images/robot_logo_peq.png",
                    width=42,
                    height=43,
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
                    ft.IconButton(
                        icon=ft.icons.ACCOUNT_CIRCLE_ROUNDED,
                        on_click=lambda e: page.show_drawer(end_draw),
                        bgcolor=ft.colors.BLACK,
                        icon_color=ft.colors.WHITE,
                        icon_size=35,
                        # expand=True,
                        # enable_feedback=True,
                        hover_color=ft.colors.with_opacity(0.1, "#ededed"),
                        highlight_color=ft.colors.with_opacity(0.1, "#ededed"),
                        focus_color=ft.colors.with_opacity(0.1, "#ededed"),
                    ),
                ],
                spacing=0,
                alignment=ft.MainAxisAlignment.END,
                wrap=True,
            ),
            # boton_flecha,
        ],
    )
    page.drawer = None
    page.end_drawer = None
    page.bottom_appbar = None
    ##########################################################
    # page.scroll= ft.ScrollMode.AUTO
    page.theme = ft.Theme(
        color_scheme_seed=ft.colors.with_opacity(0.5, "#f1edf1"),
        appbar_theme=ft.AppBarTheme(
            bgcolor="#f3edf7",
        ),
        navigation_bar_theme=ft.NavigationBarTheme(
            bgcolor="#fffbfe",
            # bgcolor="#c4dbff",
            indicator_color=ft.colors.with_opacity(1, "#e8def8"),
            label_text_style=ft.TextStyle(color=ft.colors.WHITE),
        ),
        search_bar_theme=ft.SearchBarTheme(
            bgcolor="#f3edf7",
        ),
        use_material3=True,
    )  # type: ignore

    # page.window_height = 800
    page.window.height = 812
    # page.window_width = 360
    page.window.width = 375

    page.window.resizable = False
    page.window.max_height = 812
    page.window.max_width = 375
    page.window.center()
    page.bgcolor = ft.colors.with_opacity(1, "#f1ebe0")
    page.auto_scroll = True


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