import flet as ft

def handle_dismissal(e):  # drawer event
  # page.add(ft.Text("Drawer dismissed"))
  print("Drawer dismissed")

def handle_change(e):  # drawer event
  print(f"Selected Index changed: {e.control.selected_index}")
  # page.close(drawer)


def drawer() -> ft.NavigationDrawer:
    return ft.NavigationDrawer(
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


def nav_bar(animate: callable) -> ft.NavigationBar:
  return ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(
                icon_content=ft.Icon(
                    ft.icons.LOCATION_ON_OUTLINED, color=ft.colors.BLACK
                ),
                selected_icon=ft.icons.LOCATION_ON,
                label="Explore",
                data="/Explore",
                # bgcolor=ft.colors.RED,
            ),
            ft.NavigationBarDestination(
                icon_content=ft.Icon(ft.icons.EXPLORE_OUTLINED, color=ft.colors.BLACK),
                selected_icon=ft.icons.EXPLORE,
                label="Find",
                data="/Find",
            ),
            ft.NavigationBarDestination(
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


def barra(page: ft.Page, reloj:ft.Text) -> ft.AppBar:  
   return ft.AppBar(
        leading=ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.icons.MENU,
                    on_click=lambda e: page.open(page.drawer),
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
        title=reloj,
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
        ],
    )