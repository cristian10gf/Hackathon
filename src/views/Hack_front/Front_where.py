# Frontend de la aplicacion UniWhere

from fastapi.background import P
import flet as ft
import asyncio

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from src.constants import PLACES
from datetime import datetime
import time


""" now = datetime.now()
formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
hora = now.strftime("%H:%M")
print("Fecha y hora actual:", formatted_now)
 """


class reloj(
    ft.Text
):  # dado que es un evento async, se sigue ejecutando en un hilo diferente
    """A class representing a clock widget."""

    def __init__(
        self,
        color=ft.colors.WHITE,
        pag=None,
    ):
        """
        Initialize the reloj object.

        Args:
            color (str, optional): The color of the clock widget. Defaults to ft.colors.WHITE.
            pag (object, optional): The page object to update. Defaults to None.
        """
        super().__init__()
        self.value = datetime.now().strftime("%H:%M")
        self.color = color
        self.pagina = pag

    async def updatedd(self):
        """
        Update the clock widget with the current time.

        This method runs in an infinite loop and updates the clock widget every 15 seconds.
        """
        while True:
            print("Actualizando reloj")
            hora = datetime.now().strftime("%H:%M")
            self.value = hora
            self.pagina.update()  # type: ignore
            await asyncio.sleep(15)  # Espera sin bloquear


# f3edf7
def main(page: ft.Page):
    page.title = "UniWhere"
    page.theme_mode = ft.ThemeMode.LIGHT
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
    page.bgcolor = ft.colors.WHITE
    page.auto_scroll = True
    # page.bgcolor="#c4dbff"
    # page.drawer = drawer
    """ page.add(
        ft.AppBar(
            title=ft.Text("UniWhere"),
            # leading=ft.IconButton(icon=ft.icons.MENU, on_click=lambda e: page.show_drawer(drawer)),
            actions=[
                ft.IconButton(icon=ft.icons.MAIL),
                ft.IconButton(icon=ft.icons.SOAP),
            ],
        ),
        ,
    ) """

    def handle_dismissal(e):  # drawer event
        # page.add(ft.Text("Drawer dismissed"))
        print("Drawer dismissed")

    def handle_change(e):  # drawer event
        print(f"Selected Index changed: {drawer.selected_index}")
        # page.close(drawer)

    def change_page1(e):
        page.controls.clear()  # type: ignore
        boton_flecha.icon = ft.icons.ARROW_BACK_IOS
        boton_flecha.on_click = change_page2
        # barra.title = ft.Text("Pagina 2")
        # page.add(barra)
        page.add(page2)
        # page.add(nav_bar)
        page.update()

    def change_page2(e):
        page.controls.clear()  # type: ignore
        boton_flecha.icon = ft.icons.ARROW_FORWARD_IOS
        boton_flecha.on_click = change_page1
        # barra.title = ft.Text("Pagina 1")
        # page.add(barra)
        page.add(page1)
        # page.add(nav_bar)
        page.update()

    def animate(e):
        pos = nav_bar.selected_index
        if pos == 0:
            pagina0.left = 0
            pagina1.left = 400
            pagina2.left = 800

        elif pos == 1:
            pagina0.left = -400
            pagina1.left = 0
            pagina2.left = 400

        elif pos == 2:
            pagina0.left = -800
            pagina1.left = -400
            pagina2.left = 0
        page.update()

    def add_image(e, contain: ft.Row, image_route="Images\Image_blanck.png"):  # type: ignore
        contain.controls.insert(
            -2,
            ft.Image(
                src=f"{image_route}",
                fit=ft.ImageFit.NONE,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),
                opacity=0.9,
            ),
        )
        page.update()

    #####################################################################################

    def close_search(e):
        text = f"{e.control.data}"
        print(f"closing view from {text}")
        busqueda.close_view(text)  # cambia el texto y cierra el view

    list_items = [
        ft.ListTile(
            title=ft.Text(name),
            data=name,
            leading=ft.Icon(ft.icons.ACCESSIBILITY),
            on_click=close_search,
        )
        for name in PLACES
    ]

    def search_handle_change(e):

        # print(f"handle_change e.data: {busqueda.value}")
        str_lower = e.control.value.lower()  # type: ignore
        pattern = re.compile(
            re.escape(str_lower), re.IGNORECASE
        )  # re.escape is used to escape any special characters
        nombres_matchs = [n for n in PLACES if pattern.search(n)]
        for i in range(len(nombres_matchs)):
            e.control.controls[i].title = ft.Text(nombres_matchs[i])
            e.control.controls[i].data = nombres_matchs[i]
            e.control.controls[i].leading = ft.Icon(ft.icons.ACCESSIBILITY)
            e.control.controls[i].on_click = close_search
        
        for k in range(len(nombres_matchs), len(e.control.controls)):

            e.control.controls[k].title = ft.Text("")
            e.control.controls[k].data = ""
            e.control.controls[k].leading = None
            e.control.controls[k].on_click = None

        #e.control.controls[1].title = ft.Text(e.control.value)
        # Modificar la lista original
        # sort_items_by_match(list_items, e.control.value)
        busqueda.update()
        page.update()

    def search_handle_submit(e):
        print(f"handle_submit e.data: {busqueda.value}")

    

    #####################################################################################

    busqueda = ft.SearchBar(
        bar_leading=ft.IconButton(
            icon=ft.icons.MENU,
            icon_color=ft.colors.BLACK,
            on_click=lambda _: busqueda.open_view(),
        ),
        bar_trailing=[
            ft.IconButton(
                icon=ft.icons.SEARCH_SHARP,
                icon_color=ft.colors.BLACK,
                on_click=search_handle_submit,
                # on_click=lambda e: add_image(e, images),
            ),
        ],
        controls=list_items,  # type: ignore
        value="",
        bar_hint_text="Ingresé su ubicación actual",
        view_hint_text="Ingresé su ubicación actual",
        width=338,
        height=56,
        view_elevation=4,
        bar_bgcolor="#f3edf7",
        bar_overlay_color="#ffffff",
        # capitalization=ft.TextCapitalization.WORDS,
        on_submit=search_handle_submit,
        on_change=search_handle_change,
        on_animation_end=lambda e: busqueda.update(),
        on_tap=lambda e: busqueda.open_view(),
    )

    relo = reloj(pag=page)
    """ async def acturelo():
        task = asyncio.create_task(relo.updatedd())
    #page.on_event_async = lambda e: relo.updatedd() """

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

    boton_flecha = ft.IconButton(
        icon=ft.icons.ARROW_FORWARD_IOS,
        on_click=change_page1,
        bgcolor=ft.colors.BLACK,
        icon_color=ft.colors.WHITE,
        enable_feedback=True,
        hover_color=ft.colors.with_opacity(0.1, "#ededed"),
        highlight_color=ft.colors.with_opacity(0.1, "#ededed"),
        focus_color=ft.colors.with_opacity(0.1, "#ededed"),
    )

    barra = ft.AppBar(
        leading=ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.icons.MENU,
                    on_click=lambda e: page.show_drawer(drawer),
                    bgcolor=ft.colors.BLACK,
                    icon_color=ft.colors.WHITE,
                    enable_feedback=True,
                    hover_color=ft.colors.with_opacity(0.1, "#ededed"),
                    highlight_color=ft.colors.with_opacity(0.1, "#ededed"),
                    focus_color=ft.colors.with_opacity(0.1, "#ededed"),
                )
            ]
        ),
        leading_width=40,
        title=relo,
        toolbar_height=44,
        center_title=True,
        bgcolor=ft.colors.BLACK,
        actions=[
            ft.Row(
                controls=[
                    ft.IconButton(
                        icon=ft.icons.MAIL,
                        bgcolor=ft.colors.BLACK,
                        icon_color=ft.colors.WHITE,
                        # enable_feedback=True,
                        highlight_color=ft.colors.with_opacity(0.1, "#ededed"),
                        focus_color=ft.colors.with_opacity(0.1, "#ededed"),
                    ),
                    ft.IconButton(
                        icon=ft.icons.CAMERA_ALT_ROUNDED,
                        bgcolor=ft.colors.BLACK,
                        icon_color=ft.colors.WHITE,
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
            boton_flecha,
        ],
    )

    views = {
        "Explore": ft.Pagelet(ft.Text("Home Page")),
        "Find": ft.Pagelet(ft.Text("About Page")),
        "Discover": ft.Pagelet(ft.Text("Contact Page")),
    }

    nav_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(
                icon_content=ft.Icon(
                    ft.icons.LOCATION_ON_OUTLINED, color=ft.colors.BLACK
                ),
                selected_icon=ft.icons.LOCATION_ON,
                label="Explore",
                data="/Explore",
                # bgcolor=ft.colors.RED,
            ),
            ft.NavigationDestination(
                icon_content=ft.Icon(ft.icons.EXPLORE_OUTLINED, color=ft.colors.BLACK),
                selected_icon=ft.icons.EXPLORE,
                label="Find",
                data="/Find",
            ),
            ft.NavigationDestination(
                icon_content=ft.Icon(ft.icons.MAP_OUTLINED, color=ft.colors.BLACK),
                selected_icon_content=ft.Icon(ft.icons.MAP),
                label="Discover",
                data="/Discover",
            ),
        ],
        height=75,
        # indicator_color="e8def8",
        # indicator_color=ft.colors.with_opacity(0.5, "#0e1e36"),
        indicator_color=ft.colors.with_opacity(1, "#e8def8"),
        # indicator_color=ft.colors.with_opacity(2, "#c4dbff"),
        # bgcolor="#0e1e36",
        bgcolor="#fffbfe",
        # bgcolor="#c4dbff",
        # overlay_color=ft.colors.WHITE,
        label_behavior=ft.NavigationBarLabelBehavior.ONLY_SHOW_SELECTED,
        overlay_color=ft.colors.with_opacity(0.05, "#ffffff"),
        animation_duration=350,
        on_change=animate,
        # bgcolor="#f9f8fe",
    )

    images = ft.Row(
        controls=[
            ft.Column(width=15),
            ft.Image(
                src=r"Images\Image_blanck.png",
                fit=ft.ImageFit.NONE,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),
                opacity=0.9,
            ),
            ft.Image(
                src=r"Images\Image_blanck.png",
                fit=ft.ImageFit.NONE,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),
                opacity=0.9,
            ),
            ft.Column(width=12),
        ],
        auto_scroll=True,
        spacing=8,
        scroll=ft.ScrollMode.AUTO,
        # scroll=ft.ScrollMode.HIDDEN,
        width=500,
        height=231,
        alignment=ft.MainAxisAlignment.CENTER,
    )

    images2 = ft.Row(
        controls=[
            ft.Column(width=15),
            ft.Image(
                src=r"Images\Image_blanck.png",
                fit=ft.ImageFit.NONE,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),
                opacity=0.9,
            ),
            ft.Image(
                src=r"Images\Image_blanck.png",
                fit=ft.ImageFit.NONE,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),
                opacity=0.9,
            ),
            ft.Column(width=12),
        ],
        auto_scroll=True,
        spacing=8,
        scroll=ft.ScrollMode.AUTO,
        # scroll=ft.ScrollMode.HIDDEN,
        width=500,
        height=231,
        alignment=ft.MainAxisAlignment.CENTER,
    )

    borde = ft.Border(
        top=ft.BorderSide(1, ft.colors.with_opacity(1, "#d9d9d9")),
        bottom=ft.BorderSide(1, ft.colors.with_opacity(1, "#d9d9d9")),
        left=ft.BorderSide(1, ft.colors.with_opacity(1, "#d9d9d9")),
        right=ft.BorderSide(1, ft.colors.with_opacity(1, "#d9d9d9")),
    )

    # si no hay archivos seleccionados, se muestra "Cancelled!"
    # con la funcion map se obtiene el nombre de los archivos seleccionados separados por coma
    # busca el parametro name en cada archivo de e.files
    def pick_files_result(
        e: ft.FilePickerResultEvent,
    ):  # nombre de los archivos seleccionados separados por coma

        print(
            "|:  :|".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        )
        # selected_files.value = (
        #    "|:  :|".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        # )
        # imprime el nombre del ultimo archivo seleccionado
        # print(e.files[-1].name),  # type: ignore
        page.update()
        # selected_files.update()

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    # selected_files = ft.Text()
    page.overlay.extend([pick_files_dialog])
    
    container_picker = ft.Stack(
        [
            ft.Card(
                content=ft.Container(
                    content=ft.TextField(
                        value="Ingresé una imagen o video de su ubicación actual.",
                        multiline=True,
                        read_only=True,
                        # text_size=33,
                        text_align=ft.TextAlign.CENTER,
                        bgcolor=ft.colors.TRANSPARENT,
                        color=ft.colors.BLACK,
                        border=ft.InputBorder.NONE,
                        border_color=ft.colors.TRANSPARENT,
                        hover_color=ft.colors.TRANSPARENT,
                        height=74,
                        width=342,
                        adaptive=True,
                        text_style=ft.TextStyle(font_family="Roboto"),
                        border_radius=10,
                    ),
                    width=342,
                    height=94,
                    padding=10,
                    # alignment=ft.Alignment(0, 0),
                    border=borde,
                    border_radius=10,
                    # bgcolor=ft.colors.GREY,
                ),
                elevation=10,
                color=ft.colors.with_opacity(1, "#F5F5F5"),
            ),
            ft.GestureDetector(
                mouse_cursor=ft.MouseCursor.CLICK,
                # on_vertical_drag_update=lambda e: on_pan_update(e),
                on_tap=lambda _: pick_files_dialog.pick_files(
                    allowed_extensions=[
                        "jpg",
                        "png",
                        "mp4",
                        "avi",
                        "mov",
                        "wmv",
                        "flv",
                        "mkv",
                        "webm",
                    ],
                    allow_multiple=True,
                ),
                width=342,
                height=94,
                # left=400,
                # top=100,
            ),
        ],
    )

    page.fonts = {
        "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
        "Comfortaa": r"fonts\Comfortaa-Regular.ttf",
        "Roboto": r"fonts\Roboto-Medium.ttf",
    }

    page.appbar = barra

    page.navigation_bar = nav_bar

    page.drawer = drawer

    barrabaja = ft.BottomAppBar(
        bgcolor=ft.colors.BLUE,
        shape=ft.NotchShape.CIRCULAR,
        content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.MENU, icon_color=ft.colors.WHITE),
                ft.IconButton(icon=ft.icons.SEARCH, icon_color=ft.colors.WHITE),
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
                ft.Container(expand=True),
                ft.IconButton(icon=ft.icons.FAVORITE, icon_color=ft.colors.WHITE),
            ]
        ),
    )

    page1 = ft.Pagelet(
        content=ft.Container(
            content=ft.Row(
                controls=[
                    ft.Column(
                        controls=[
                            ft.Container(height=36, bgcolor=ft.colors.TRANSPARENT),
                            ft.Row(
                                [
                                    ft.TextField(
                                        value="En donde estoy ?",
                                        read_only=True,
                                        text_size=33,
                                        text_align=ft.TextAlign.CENTER,
                                        bgcolor=ft.colors.TRANSPARENT,
                                        color=ft.colors.BLACK,
                                        border=ft.InputBorder.NONE,
                                        hover_color=ft.colors.TRANSPARENT,
                                        # height=56,
                                        width=326,
                                        adaptive=True,
                                        text_style=ft.TextStyle(
                                            font_family="Comfortaa"
                                        ),
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                            ft.Container(height=15.5, bgcolor=ft.colors.TRANSPARENT),
                            ft.SearchBar(
                                bar_leading=ft.IconButton(
                                    icon=ft.icons.MENU, icon_color=ft.colors.BLACK
                                ),
                                bar_trailing=[
                                    ft.IconButton(
                                        icon=ft.icons.SEARCH_SHARP,
                                        icon_color=ft.colors.BLACK,
                                    ),
                                ],
                                value="",
                                bar_hint_text="Ingresé su ubicación actual",
                                view_hint_text="Ingresé su ubicación actual",
                                # width=358,
                                width=338,
                                height=56,
                                view_elevation=4,
                                bar_bgcolor="#f3edf7",
                                bar_overlay_color="#ffffff",
                                capitalization=ft.TextCapitalization.WORDS,
                            ),
                            ft.Text("u no "),
                            ft.Container(content=ft.Text(" "), bgcolor=ft.colors.RED),
                            # ft.Container(height=12, bgcolor=ft.colors.RED),
                        ],
                        expand=True,
                        spacing=0,
                        alignment=ft.MainAxisAlignment.START,
                    ),
                ]
            ),
            # content=ft.Row(controls=[ft.Text("Pagina 2")]),
            # bgcolor=ft.colors.with_opacity(0.5, "#dfe2e1"),
            bgcolor=ft.colors.WHITE,
            border_radius=10,
            expand=True,
        ),
        expand=True,
        bgcolor=ft.colors.TRANSPARENT,
    )

    

    pagina0 = ft.Stack(
        left=0,
        animate_position=ft.animation.Animation(500, ft.AnimationCurve.EASE_OUT),
        controls=[
            ft.Image(
                src=r"Images\gran-composicion-universidad-isometrica-casas-patios-campus-campus-sombras-futbol-playgro.png",
                width=340,
                height=695,
                border_radius=10,
                fit=ft.ImageFit.CONTAIN,
            ),
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Column(
                            controls=[
                                ft.ListView(
                                    [
                                        ft.Container(
                                            height=36, bgcolor=ft.colors.TRANSPARENT
                                        ),
                                        ft.Row(
                                            [
                                                ft.TextField(
                                                    value="En donde estoy ?",
                                                    read_only=True,
                                                    text_size=33,
                                                    text_align=ft.TextAlign.CENTER,
                                                    bgcolor=ft.colors.TRANSPARENT,
                                                    color=ft.colors.BLACK,
                                                    border=ft.InputBorder.NONE,
                                                    hover_color=ft.colors.TRANSPARENT,
                                                    # height=56,
                                                    width=342,
                                                    adaptive=True,
                                                    text_style=ft.TextStyle(
                                                        font_family="Comfortaa"
                                                    ),
                                                ),
                                            ],
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            # width=365,
                                        ),
                                        ft.Container(
                                            height=15.5, bgcolor=ft.colors.TRANSPARENT
                                        ),
                                        busqueda,
                                        ft.Text("u no "),
                                        ft.Container(
                                            content=ft.Text(" "), bgcolor=ft.colors.RED
                                        ),
                                        images,
                                    ],
                                    # width=340,
                                    # height=693,
                                    expand=True,
                                    spacing=0,
                                    auto_scroll=True,
                                ),
                                # ft.Container(height=12, bgcolor=ft.colors.RED),
                            ],
                            # expand=True,
                            width=338,
                            height=693,
                            spacing=0,
                            alignment=ft.MainAxisAlignment.START,
                        ),
                    ]
                ),
                # content=ft.Row(controls=[ft.Text("Pagina 2")]),
                # bgcolor=ft.colors.with_opacity(0.5, "#dfe2e1"),
                bgcolor=ft.colors.TRANSPARENT,
                border_radius=10,
                expand=True,
            ),
        ],
        width=340,
        height=695,
    )

    pagina1 = ft.Stack(
        left=400,
        animate_position=ft.animation.Animation(500, ft.AnimationCurve.EASE_OUT),
        controls=[
            ft.Image(
                src=r"Images\gran-composicion-universidad-isometrica-casas-patios-campus-campus-sombras-futbol-playgro.png",
                width=340,
                height=695,
                border_radius=10,
                fit=ft.ImageFit.CONTAIN,
            ),
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Column(
                            controls=[
                                ft.ListView(
                                    [
                                        ft.Container(
                                            height=36, bgcolor=ft.colors.TRANSPARENT
                                        ),
                                        ft.Row(
                                            [
                                                ft.TextField(
                                                    value="En donde estoy ?",
                                                    read_only=True,
                                                    text_size=33,
                                                    text_align=ft.TextAlign.CENTER,
                                                    bgcolor=ft.colors.TRANSPARENT,
                                                    color=ft.colors.BLACK,
                                                    border=ft.InputBorder.NONE,
                                                    hover_color=ft.colors.TRANSPARENT,
                                                    # height=56,
                                                    width=342,
                                                    adaptive=True,
                                                    text_style=ft.TextStyle(
                                                        font_family="Comfortaa"
                                                    ),
                                                ),
                                            ],
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            # width=365,
                                        ),
                                        ft.Container(
                                            height=0.5, bgcolor=ft.colors.TRANSPARENT
                                        ),
                                        container_picker,
                                        ft.Text(
                                            "La duración del video no debe superar los 5 segundos.",
                                            color="#747474",
                                            text_align=ft.TextAlign.CENTER,
                                            font_family="Roboto",
                                            size=11,
                                        ),
                                        ft.Container(
                                            content=ft.Text(" "), bgcolor=ft.colors.RED
                                        ),
                                        images2,
                                    ],
                                    # width=340,
                                    # height=693,
                                    expand=True,
                                    spacing=0,
                                    auto_scroll=True,
                                ),
                                # ft.Container(height=12, bgcolor=ft.colors.RED),
                            ],
                            # expand=True,
                            width=338,
                            height=693,
                            spacing=0,
                            alignment=ft.MainAxisAlignment.START,
                        ),
                    ]
                ),
                # content=ft.Row(controls=[ft.Text("Pagina 2")]),
                # bgcolor=ft.colors.with_opacity(0.5, "#dfe2e1"),
                bgcolor=ft.colors.TRANSPARENT,
                border_radius=10,
                expand=True,
            ),
        ],
        width=340,
        height=695,
    )
    pagina2 = ft.Stack(
        left=800,
        animate_position=ft.animation.Animation(500, ft.AnimationCurve.EASE_OUT),
        controls=[
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Container(height=36, bgcolor=ft.colors.TRANSPARENT),
                                ft.Row(
                                    [
                                        ft.TextField(
                                            value="En donde estoy ?",
                                            read_only=True,
                                            text_size=33,
                                            text_align=ft.TextAlign.CENTER,
                                            bgcolor=ft.colors.TRANSPARENT,
                                            color=ft.colors.BLACK,
                                            border=ft.InputBorder.NONE,
                                            hover_color=ft.colors.TRANSPARENT,
                                            # height=56,
                                            width=342,
                                            adaptive=True,
                                            text_style=ft.TextStyle(
                                                font_family="Comfortaa"
                                            ),
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    # width=365,
                                ),
                                ft.Container(
                                    height=15.5, bgcolor=ft.colors.TRANSPARENT
                                ),
                                ft.SearchBar(
                                    bar_leading=ft.IconButton(
                                        icon=ft.icons.MENU, icon_color=ft.colors.BLACK
                                    ),
                                    bar_trailing=[
                                        ft.IconButton(
                                            icon=ft.icons.SEARCH_SHARP,
                                            icon_color=ft.colors.BLACK,
                                        ),
                                    ],
                                    value="",
                                    bar_hint_text="Ingresé su ubicación actual",
                                    view_hint_text="Ingresé su ubicación actual",
                                    width=338,
                                    height=56,
                                    view_elevation=4,
                                    bar_bgcolor="#f3edf7",
                                    bar_overlay_color="#ffffff",
                                    capitalization=ft.TextCapitalization.WORDS,
                                ),
                                ft.Text("u no "),
                                ft.Container(
                                    content=ft.Text(" "), bgcolor=ft.colors.RED
                                ),
                                # ft.Container(height=12, bgcolor=ft.colors.RED),
                            ],
                            # expand=True,
                            width=338,
                            height=693,
                            spacing=0,
                            alignment=ft.MainAxisAlignment.START,
                        ),
                    ]
                ),
                # content=ft.Row(controls=[ft.Text("Pagina 2")]),
                # bgcolor=ft.colors.with_opacity(0.5, "#dfe2e1"),
                bgcolor=ft.colors.WHITE,
                border_radius=10,
                expand=True,
            ),
            ft.Image(
                src=r"Images\gran-composicion-universidad-isometrica-casas-patios-campus-campus-sombras-futbol-playgro.png",
                width=340,
                height=695,
                border_radius=10,
                fit=ft.ImageFit.CONTAIN,
            ),
        ],
        width=340,
        height=695,
    )

    page2 = ft.Pagelet(
        content=ft.Stack(
            [
                pagina0,
                pagina1,
                pagina2,
            ],
        ),
        expand=True,
        bgcolor=ft.colors.TRANSPARENT,
    )

    # page.add(barra)
    page.add(page1)
    # page.add(nav_bar)
    # page.add(barrabaja)
    print(page.window.height)
    print(page.window.width)
    page.update()

    asyncio.run(relo.updatedd())


ft.app(target=main)
