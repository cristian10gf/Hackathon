from re import T
import flet as ft
from sympy import false

def main(page: ft.Page):
    page.title = "GridView Example"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0
    page.update()

    images = ft.GridView(
        #expand=1,
        runs_count=1,
        max_extent=150,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
        #horizontal=True,
        auto_scroll=True,
        reverse=False,
        height=500,
        width=500,
        #rotate=-81,
        #on_scroll=lambda e: print(f"scrolling: {e}"),
    )
    ima= ft.Row(
        controls=[
            
        ],
        auto_scroll=True,
        scroll=ft.ScrollMode.HIDDEN,
        expand=True,
    )
    
    page.add(ima)

    for i in range(0, 20):
        ima.controls.append(
            ft.Image(
                src=f"https://picsum.photos/150/150?{i}",
                fit=ft.ImageFit.NONE,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),
            )
        )
    page.update()

ft.app(target=main)