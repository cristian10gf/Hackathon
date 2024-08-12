import flet as ft

def handle_dismissal(e):  # drawer event
        # page.add(ft.Text("Drawer dismissed"))
        print("Drawer dismissed")

def handle_change(e):  # drawer event
    print(f"Selected Index changed: {e.drawer.selected_index}")
    # page.close(drawer)

def get_drawer( charge_history ) -> ft.NavigationDrawer:
  return ft.NavigationDrawer(
        on_dismiss=handle_dismissal,
        on_change=charge_history,
        controls=[ft.Container(height=12),],
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