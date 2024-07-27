import flet as ft


def main(page: ft.Page):
    st = ft.Stack(
        controls=[
            
            
            ft.Container(
                left=0,
                animate_position=ft.animation.Animation(
                    500, ft.AnimationCurve.EASE_OUT
                ),
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
                            width=340,
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
                height=690,
                border_radius=10,
                fit=ft.ImageFit.CONTAIN,
            ),
        ],
        width=340,
        height=695,
    )

    page.add(st)


ft.app(target=main)
