import flet as ft

def handle_dismissal(e):  # drawer event
        # page.add(ft.Text("Drawer dismissed"))
        print("Drawer dismissed")

def handle_change(e):  # drawer event
    print(f"Selected Index changed: {e.drawer.selected_index}")
    # page.close(drawer)

def get_appBar(charge_history, open_drawer) -> ft.AppBar:
  return ft.AppBar(
        leading=ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.icons.HISTORY,
                    on_click=charge_history,
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
                        on_click=open_drawer,
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


def get_drawer( charge_history ) -> ft.NavigationDrawer:
  return ft.NavigationDrawer(
            on_dismiss=handle_dismissal,
            on_change=charge_history,
            controls=[
                ft.Container(height=12),
                
            ],
            bgcolor="#0e1e36",
        )


def get_end_draw(cerrar_sesion, rol_user) -> ft.NavigationDrawer:
  return ft.NavigationDrawer(
        on_dismiss=handle_dismissal,
        on_change=handle_change, #por cambiar pa meter mensajes
        controls=[
            ft.Container(height=12),
            ft.Icon(ft.icons.ACCOUNT_CIRCLE_ROUNDED, size=200, color=ft.colors.WHITE),
            ft.Container(height=12),
            ft.Divider(thickness=2),
            ft.Text("Level access: "+rol_user[0].upper() + rol_user[1:], size=20, color=ft.colors.WHITE),
            ft.Divider(thickness=2),
            ft.Row([ft.TextButton( text="Cerrar sesión", on_click=cerrar_sesion, style=ft.ButtonStyle(color=ft.colors.WHITE,bgcolor=ft.colors.BLACK)),],alignment=ft.MainAxisAlignment.CENTER),
            ft.Divider(thickness=2),
        ],
        bgcolor="#0e1e36",
    )