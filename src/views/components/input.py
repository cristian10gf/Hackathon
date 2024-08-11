import flet as ft

def get_input_bar(onchage: callable) -> ft.TextField:
  return ft.TextField(
    hint_text="Write a message...",
    multiline=True,
    on_change=onchage,
    max_lines=5,
    filled=True,
    width=270,
    read_only=False,
    bgcolor=ft.colors.WHITE,
    color=ft.colors.GREEN,
    border=ft.InputBorder.OUTLINE,
    border_color=ft.colors.WHITE,
    hover_color=ft.colors.TRANSPARENT,
    text_style=ft.TextStyle(font_family="Roboto"),
    border_radius=10,
  )