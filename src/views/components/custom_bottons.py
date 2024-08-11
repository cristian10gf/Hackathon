import flet as ft

def get_button_action(onClick: callable, icon) -> ft.IconButton:
  return ft.IconButton(
      icon=icon,
      on_click=onClick,
      bgcolor=ft.colors.BLACK,
      icon_color=ft.colors.WHITE,
      icon_size=35,
      enable_feedback=True,
      hover_color=ft.colors.with_opacity(0.1, "#ededed"),
      highlight_color=ft.colors.with_opacity(0.1, "#ededed"),
      focus_color=ft.colors.with_opacity(0.1, "#ededed"),
  )