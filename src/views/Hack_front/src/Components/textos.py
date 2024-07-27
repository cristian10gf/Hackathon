import flet as ft

def get_title(title: str, size: float = 33, width: float = 342) -> ft.TextField:
    return ft.TextField(
        value=title,
        read_only=True,
        text_size=size,
        text_align=ft.TextAlign.CENTER,
        bgcolor=ft.colors.TRANSPARENT,
        color=ft.colors.BLACK,
        border=ft.InputBorder.NONE,
        hover_color=ft.colors.TRANSPARENT,
        # height=56,
        width=width,
        adaptive=True,
        text_style=ft.TextStyle(
            font_family="Comfortaa"
        ),
    )