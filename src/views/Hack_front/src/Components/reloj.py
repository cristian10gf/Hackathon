import flet as ft
from datetime import datetime
import asyncio

class Reloj(ft.Text):  # dado que es un evento async, se sigue ejecutando en un hilo diferente
    def __init__(self, color=ft.colors.WHITE,pag=None,):
        """
        Initialize the reloj object.

        Args:
            color (str, optional): The color of the clock widget. Defaults to ft.colors.WHITE.
            pag (object, optional): The page object to update. Defaults to None.
        """
        super().__init__()
        self.value = datetime.now().strftime("%H:%M")
        self.color = color
        self.pagina = pag

    async def updatedd(self):
        """
        Update the clock widget with the current time.

        This method runs in an infinite loop and updates the clock widget every 15 seconds.
        """
        while True:
            print("Actualizando reloj")
            hora = datetime.now().strftime("%H:%M")
            self.value = hora
            self.pagina.update()
            await asyncio.sleep(15)  # Espera sin bloquear
