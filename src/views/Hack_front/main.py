import flet as ft
import asyncio, re
from src.Components.reloj import Reloj
from src.Components.textos import get_title
from src.Components.Image import get_Image
from src.Components.Busqueda import get_busqueda
from src.constants import PLACES
from src.Components.Navegacion import barra, drawer, nav_bar

def main(page: ft.Page):
    # Configuración de la App -------------------------------------------------------

    page.title = "UniWhere"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = ft.Theme(
        color_scheme_seed=ft.colors.with_opacity(0.5, "#f1edf1"),
        appbar_theme=ft.AppBarTheme(bgcolor="#f3edf7",),
        navigation_bar_theme=ft.NavigationBarTheme(
            bgcolor="#fffbfe",
            indicator_color=ft.colors.with_opacity(1, "#e8def8"),
            label_text_style=ft.TextStyle(color=ft.colors.WHITE),
        ),
        search_bar_theme=ft.SearchBarTheme(bgcolor="#f3edf7",),
        use_material3=True,
    )

    page.window.height = 812
    page.window.width = 375

    page.window.resizable = False
    page.window.center()
    page.bgcolor = ft.colors.WHITE
    page.auto_scroll = True
    page.fonts = {
        "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
        "Comfortaa": "/src/fonts/Comfortaa-Regular.ttf",
        "Roboto": "/src/fonts/Roboto-Medium.ttf",
    }

    reloj = Reloj(pag=page)

    # Funciones de la App -----------------------------------------------------

    def animate(e):
        pos = page.navigation_bar.selected_index # type: ignore
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

    def add_image(e, contain: ft.Row, image_route="/images/Image_blanck.png"):  
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

    def close_search(e):
        text = f"{e.control.data}"
        print(f"closing view from {text}")
        busqueda.close_view(text)  # cambia el texto y cierra el view

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

    def pick_files_result(e: ft.FilePickerResultEvent,):  # nombre de los archivos seleccionados separados por coma
        print( "|:  :|".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!")
        # selected_files.value = (
        #    "|:  :|".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        # )
        # imprime el nombre del ultimo archivo seleccionado
        # print(e.files[-1].name)
        page.update()
        # selected_files.update()


    # Navegacion ---------------------------------------------------------------------

    page.appbar = barra(page, reloj)
    page.navigation_bar = nav_bar(animate)
    page.drawer = drawer()


    # Creación de los widgets (UI) -----------------------------------------------------

    images = ft.Row(
        controls=[
            ft.Column(width=15),
            get_Image("/images/Image_blanck.png"),
            get_Image("/images/Im
                      age_blanck.png"),
            ft.Column(width=12),
        ],
        auto_scroll=True,
        spacing=8,
        scroll=ft.ScrollMode.AUTO,
        width=500,
        height=231,
        alignment=ft.MainAxisAlignment.CENTER,
    )

    images2 = ft.Row(
        controls=[
            ft.Column(width=15),
            get_Image("/images/Image_blanck.png"),
            get_Image("/images/Image_blanck.png"),
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

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
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

    list_items = [
        ft.ListTile(
            title=ft.Text(name),
            data=name,
            leading=ft.Icon(ft.icons.ACCESSIBILITY),
            on_click=close_search,
        )
        for name in PLACES
    ]

    busqueda = get_busqueda(search_handle_submit, search_handle_change,  list_items)

    pagina0 = ft.Stack(
        left=0,
        animate_position=ft.animation.Animation(500, ft.AnimationCurve.EASE_OUT),
        controls=[
            ft.Image(
                src="/images/mapa_ejemplo.png",
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
                                        ft.Container(height=36, bgcolor=ft.colors.TRANSPARENT),
                                        ft.Row([get_title("En donde estoy ?"),],alignment=ft.MainAxisAlignment.CENTER,),
                                        ft.Container(height=15.5, bgcolor=ft.colors.TRANSPARENT),
                                        busqueda,
                                        ft.Text("u no "),
                                        ft.Container(content=ft.Text(" "), bgcolor=ft.colors.RED),
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
                src="/images/mapa_ejemplo.png",
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
                                        ft.Container(height=36, bgcolor=ft.colors.TRANSPARENT),
                                        ft.Row(
                                            [get_title("En donde estoy ?"),],
                                            alignment=ft.MainAxisAlignment.CENTER,
                                        ),
                                        ft.Container(height=0.5, bgcolor=ft.colors.TRANSPARENT),
                                        container_picker,
                                        ft.Text(
                                            "La duración del video no debe superar los 5 segundos.",
                                            color="#747474",
                                            text_align=ft.TextAlign.CENTER,
                                            font_family="Roboto",
                                            size=11,
                                        ),
                                        ft.Container(content=ft.Text(" "), bgcolor=ft.colors.RED),
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
                                    [get_title("En donde estoy ?"),],
                                    alignment=ft.MainAxisAlignment.CENTER,
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
                src="/images/mapa_ejemplo.png",
                width=340,
                height=695,
                border_radius=10,
                fit=ft.ImageFit.CONTAIN,
            ),
        ],
        width=340,
        height=695,
    )

    home_page = ft.Pagelet(
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


    page.add(home_page)
    page.update()
    asyncio.run(reloj.updatedd())

ft.app(target=main, assets_dir="assets")