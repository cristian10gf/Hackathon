import flet as ft

def get_Image(src: str):
  return ft.Image(
    src=src,
    fit=ft.ImageFit.CONTAIN,
    repeat=ft.ImageRepeat.NO_REPEAT,
    border_radius=ft.border_radius.all(10),
    opacity=0.9,
  )