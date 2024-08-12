import flet as ft

class texto_msg:
    def __init__(self, user_name: str, text: str, message_type: str):
        self.user_name = user_name
        self.text = text


class Mensaje_basico_user(ft.Row):
    def __init__(self, mensage_content: texto_msg):
        super().__init__()
        self.vertical_alignment = ft.CrossAxisAlignment.START
        self.width = 270
        self.controls = [
            ft.Card(
                content=ft.TextField(
                    value=mensage_content.text,
                    multiline=True,
                    read_only=True,
                    filled=True,
                    text_align=ft.TextAlign.START,
                    bgcolor=ft.colors.TRANSPARENT,
                    color=ft.colors.BLACK,
                    border=ft.InputBorder.NONE,
                    border_color=ft.colors.TRANSPARENT,
                    hover_color=ft.colors.TRANSPARENT,
                    width=200,
                    text_style=ft.TextStyle(font_family="Roboto"),
                    border_radius=10,
                ),
                width=300,
                elevation=5,
                expand=True,
            ),
            ft.CircleAvatar(
                content=ft.Text(self.get_initials(mensage_content.user_name)),
                color=ft.colors.WHITE,
                bgcolor=self.get_avatar_color(mensage_content.user_name),
            ),
        ]

    def get_initials(self, user_name: str):
        if user_name:
            return user_name[:1].capitalize()
        else:
            return "Unknown"  # or any default value you prefer

    def get_avatar_color(self, user_name: str):
        colors_lookup = [
            ft.colors.AMBER,
            ft.colors.BLUE,
            ft.colors.BROWN,
            ft.colors.CYAN,
            ft.colors.GREEN,
            ft.colors.INDIGO,
            ft.colors.LIME,
            ft.colors.ORANGE,
            ft.colors.PINK,
            ft.colors.PURPLE,
            ft.colors.RED,
            ft.colors.TEAL,
            ft.colors.YELLOW,
        ]
        return colors_lookup[hash(user_name) % len(colors_lookup)]


class Mensaje_basico_bot(ft.Row):
    def __init__(self, mensage_content: texto_msg):
        super().__init__()
        self.vertical_alignment = ft.CrossAxisAlignment.START
        self.width = 270
        self.controls = [
            ft.CircleAvatar(
            content=ft.Image(
                src="/images/robot_logo_peq.png",
                border_radius=10,
                fit=ft.ImageFit.FILL,
            ),
            bgcolor=ft.colors.TRANSPARENT,
        ),
            
            ft.Card(
                content=ft.TextField(
                    value=mensage_content.text,
                    multiline=True,
                    read_only=True,
                    filled=True,
                    text_align=ft.TextAlign.START,
                    bgcolor=ft.colors.TRANSPARENT,
                    color=ft.colors.BLACK,
                    border=ft.InputBorder.NONE,
                    border_color=ft.colors.TRANSPARENT,
                    hover_color=ft.colors.TRANSPARENT,
                    width=200,
                    text_style=ft.TextStyle(font_family="Roboto"),
                    border_radius=10,
                ),
                width=300,
                elevation=5,
                expand=True,
            ),
    ]
          