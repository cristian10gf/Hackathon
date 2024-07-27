import flet as ft


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT

    shader_mask = ft.ShaderMask(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text("This text will be blurred"),
                    ft.Image(src="https://via.placeholder.com/150"),
                ]
            ),
            width=400,
            height=400,
            padding=10,
            alignment=ft.alignment.center,
            bgcolor=ft.colors.WHITE,
        ),
        shader=ft.RadialGradient(
            stops=[0, 1],
            tile_mode=ft.GradientTileMode.MIRROR,
            colors=[ft.colors.with_opacity(0.5,"#000000"), ft.colors.GREY],
        ),
    )

    page0 = ft.Container(
        left=0,
        animate_position=ft.animation.Animation(500, ft.AnimationCurve.EASE_OUT),
        blur=5,
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
                                    text_style=ft.TextStyle(font_family="Comfortaa"),
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
                            width=358,
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
                    width=400,
                    height=400,
                    spacing=0,
                    alignment=ft.MainAxisAlignment.START,
                ),
            ]
        ),
        # content=ft.Row(controls=[ft.Text("Pagina 2")]),
        # bgcolor=ft.colors.with_opacity(0.5, "#dfe2e1"),
        bgcolor=ft.colors.GREY,
        border_radius=10,
    )

    page1 = ft.Container(
        left=400,
        animate_position=ft.animation.Animation(500, ft.AnimationCurve.EASE_OUT),
        content=ft.Row(
            controls=[
                ft.Column(
                    controls=[
                        ft.Container(height=36, bgcolor=ft.colors.TRANSPARENT),
                        ft.Row(
                            [
                                ft.TextField(
                                    value="En donde no estoy ?",
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
                                    text_style=ft.TextStyle(font_family="Comfortaa"),
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
                            width=358,
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
                    width=400,
                    height=400,
                    spacing=0,
                    alignment=ft.MainAxisAlignment.START,
                ),
            ]
        ),
        # content=ft.Row(controls=[ft.Text("Pagina 2")]),
        # bgcolor=ft.colors.with_opacity(0.5, "#dfe2e1"),
        bgcolor=ft.colors.WHITE,
        border_radius=10,
    )

    page2 = ft.Container(
        left=800,
        animate_position=ft.animation.Animation(500, ft.AnimationCurve.EASE_OUT),
        content=ft.Row(
            controls=[
                ft.Column(
                    controls=[
                        ft.Container(height=36, bgcolor=ft.colors.TRANSPARENT),
                        ft.Row(
                            [
                                ft.TextField(
                                    value="En donde si estoy ?",
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
                                    text_style=ft.TextStyle(font_family="Comfortaa"),
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
                            width=358,
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
                    width=400,
                    height=400,
                    spacing=0,
                    alignment=ft.MainAxisAlignment.START,
                ),
            ]
        ),
        # content=ft.Row(controls=[ft.Text("Pagina 2")]),
        # bgcolor=ft.colors.with_opacity(0.5, "#dfe2e1"),
        bgcolor=ft.colors.WHITE,
        border_radius=10,
    )

    pagelist = [page0, page1, page2]

    i1 = ft.Image(
        src="https://picsum.photos/200/300?1",
        animate_position=ft.animation.Animation(500, ft.AnimationCurve.EASE_OUT),
        left=0,
    )
    i2 = ft.Image(
        src="https://picsum.photos/200/300?2",
        animate_position=ft.animation.Animation(500, ft.AnimationCurve.EASE_OUT),
        left=-400,
    )
    i3 = ft.Image(
        src="https://picsum.photos/200/300?3",
        animate_position=ft.animation.Animation(500, ft.AnimationCurve.EASE_OUT),
        left=400,
    )

    def animate(e):
        pos = nav_bar.selected_index
        if pos == 0:
            page0.left = 0
            page1.left = 400
            page2.left = 800

        elif pos == 1:
            page0.left = -400
            page1.left = 0
            page2.left = 400

        elif pos == 2:
            page0.left = -800
            page1.left = -400
            page2.left = 0
        page.update()

    nav_bar = ft.NavigationBar(
        selected_index=0,
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
        on_change=lambda e: animate(e),
        # bgcolor="#f9f8fe",
    )

    page.add(
        ft.Stack(
            [
                
                page0,
                page1,
                page2,
            ],
            width=400,
            height=400,
        ),
        
        nav_bar,
        # ft.ElevatedButton("Slide!", on_click=animate),
    )


ft.app(target=main)
