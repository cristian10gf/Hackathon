import flet as ft


class Special_container(ft.Container):
    def __init__(self, content, on_click=None):
        super().__init__()
        self.content = content
        self.on_click = on_click
        self.height = 147.5
        self.width = 412.5
        self.bgcolor = ft.colors.BLACK54
        self.padding = 10
        self.border_radius = 10
    
    def reshape(self,page: ft.Page):
        self.height = 147.5/830 * page.window_height # type: ignore
        self.width = 412.5/1550 * page.window_width # type: ignore