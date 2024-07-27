import flet as ft


def main(page: ft.Page):

    c1 = ft.Container(
        ft.Text("Hello!", style=ft.TextThemeStyle.HEADLINE_MEDIUM),
        alignment=ft.alignment.center,
        width=200,
        height=200,
        bgcolor=ft.colors.GREEN,
    )
    c2 = ft.Container(
        ft.Text("Bye!", size=50),
        alignment=ft.alignment.center,
        width=200,
        height=200,
        bgcolor=ft.colors.YELLOW,
    )
    page.session.set("previewindex", 0)
    page0 = ft.Container(
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
        bgcolor=ft.colors.WHITE,
        border_radius=10,
       
    )

    page1 = ft.Container(
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
    
    page2= ft.Container(
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
    
    c = ft.AnimatedSwitcher(
        page0,
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=250,
        reverse_duration=100,
        switch_in_curve=ft.AnimationCurve.EASE_IN_OUT_QUAD,
        switch_out_curve=ft.AnimationCurve.EASE_IN_OUT_QUAD,
        # switch_in_curve=ft.AnimationCurve.DECELERATE,
        # switch_out_curve=ft.AnimationCurve.DECELERATE,
    )

    pagelist=[page0,page1,page2]
    def animate(e,index):
        c.content = pagelist[int(index)]
        c.update()
        page.session.set("previewindex", int(index))
    def indexselec():

        return nav_bar.selected_index

    

    nav_bar= ft.NavigationBar(
        selected_index=0,
        destinations=[
            ft.NavigationDestination(
                icon_content=ft.Icon(
                    ft.icons.LOCATION_ON_OUTLINED, color=ft.colors.BLACK
                ),
                
                selected_icon=ft.icons.LOCATION_ON,
                label="Explore",
                data="/Explore"
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
        on_change= lambda e: animate(e,indexselec()),
        # bgcolor="#f9f8fe",
    )

    
    page.add(
        c,
        #ft.ElevatedButton("Animate!", on_click=animate),
        nav_bar,
        
    )


ft.app(target=main)
