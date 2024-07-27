import flet as ft


###### Readme ######
# Este archivo contiene las clases de los botones que se usan en la calculadora

#calculo de la razon de los tamaños del texto y el boton
#razonwitdh = botonwitdh / 1550
#razonheight = botonheight / 830
#razonsize = (botonsize /(windowheight / windowwitdh))/2









class DigitButton(ft.FloatingActionButton):
    """
    A custom floating action button for a calculator.

    Args:
        text (str): The text to be displayed on the button.
        on_click (function): The function to be called when the button is clicked.
    """

    def __init__(
        self,
        text,
        on_click=None,
        textsize=22,
        botonheight=55,
    ):
        super().__init__()
        self.content = ft.Text(
            color=ft.colors.WHITE, size=22, value=text
        )  # Text widget
        self.on_click = on_click  # Function to be called when the button is clicked
        self.elevation = 1  # Elevation of the button
        self.hover_elevation = 4  # Elevation of the button when hovered
        self.adaptive = (True,)
        # self.bgcolor = "#5D6D7E"  # Background color of the button
        self.bgcolor = ft.colors.WHITE24
        # self.bgcolor = ft.colors.BLUE_GREY_50  # Background color of the button
        self.foreground_color = ft.colors.RED  # Foreground color of the button
        self.shape = ft.RoundedRectangleBorder(radius=40)
        self.height = 55
        self.width = 89.375
        self.razonsize = 22
        self.razonheight = 55 / 830
        self.razonwidth = 89.375 / 1550

    def change_color(self, color):
        self.bgcolor = color

    
    def reshape(self, page: ft.Page):
        self.content.size = (23/(float(page.window_height)/float(page.window_width)))/2 # type: ignore
        self.height = self.razonheight * float(page.window_height)  # type: ignore
        self.width = self.razonwidth * float(page.window_width)  # type: ignore


class OtherOperations_Button(ft.TextButton):

    def __init__(
        self,
        text,
        on_click=None,
    ):
        super().__init__()
        self.texx = ft.Text(
            value=text,
            size=22,
            color=ft.colors.WHITE,
        )
        self.content = content = ft.Container(
            content=ft.Column(
                [
                    self.texx,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            padding=ft.padding.all(0),
        )  # Text widget
        self.on_click = on_click  # Function to be called when the button is clicked

        # self.shape = ft.RoundedRectangleBorder(radius=40)

        self.height = 55
        self.width = 89.375
        self.razonheight = 55 / 1504
        self.razonwidth = 22

    def change_color(self, color):
        self.bgcolor = color

    def set_size(self, page: ft.Page):
        self.texx.size = (23/(float(page.window_height)/float(page.window_width)))/2 # type: ignore

    def set_height(self, height):
        self.height = height

    def set_width(self, width):
        self.width = width


class Operation_Button(ft.IconButton):
    def __init__(
        self,
        icono,
        on_click=None,
    ):
        super().__init__()
        self.icon = icono
        self.height = 56.25
        self.width = 56.25

        # self.bgcolor = "#FFB450"  # Background color of the button
        self.bgcolor = ft.colors.ORANGE
        self.icon_color = ft.colors.WHITE  # Foreground color of the button
        self.on_click = on_click  # Function to be called when the button is clicked
        # self.shape = ft.RoundedRectangleBorder(radius=40)
    def change_color(self, color):
        self.bgcolor = color
    
    def set_height(self, height):
        self.height = height
    
    def set_width(self, width):
        self.width = width
    


class Equal_Button(ft.TextButton):
    def __init__(
        self,
        text,
        data=None,
        on_click=None,
    ):
        super().__init__()
        self.content = content = ft.Container(
            content=ft.Text(
                value=text,
                size=25,
                color=ft.colors.WHITE,
            ),
            padding=ft.padding.all(0),
        )  # Text widget
        self.data = data

        self.on_click = on_click  # Function to be called when the button is clicked
        # self.shape = ft.RoundedRectangleBorder(radius=40)
        self.foreground_color = ft.colors.WHITE


"""

),


"""
