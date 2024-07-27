from os import read
from re import T
import flet as ft
import time


def main(page: ft.Page):
    page.title = "Prueba Conceptual"
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.window_center()
    # page.window_full_screen=True
    # page.window_frameless=True
    # page.window_title_bar_buttons_hidden= True
    page.window_width = 1280
    page.window_height = 720
    page.window_max_width = 1920
    page.window_max_height = 1080
    page.window_resizable = False

    print(page.route)
    page.add(ft.Text(f"Por favor seleccione una interfaz de visualizacion:"))
    page.appbar = ft.AppBar(
        title=ft.Text("Prueba Conceptual"),
        bgcolor=ft.colors.BLUE,
        center_title=True,
    )

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.SET_MEAL, on_click=lambda e: page.show_dialog(dlg2)
    )

    nombreboton = ft.TextField(
        label="Texto del Boton",
        # on_change=print("Texto del Boton"),
    )
    dlg = ft.AlertDialog(
        title=ft.Text("Crear Botonones"),
        content=ft.Text("Ingrese el texto de los botones a crear:"),
        actions=[
            ft.Column(
                controls=[
                    nombreboton,
                    ft.Row(
                        [
                            ft.TextButton(
                                text="Aceptar",
                                on_click=lambda e: agregarboton(e),
                            ),
                            ft.TextButton(
                                text="Cancelar",
                                on_click=lambda e: cerrar(e),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ]
            ),
        ],
    )
    filabotonera = ft.Row(
        [],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    counter2 = ft.TextField(
        value="0",
        label="Contador de Clicks: ",
        width=120,
        text_align=ft.TextAlign.CENTER,
    )

    """ page.floating_action_button = ft.FloatingActionButton(
        # text="Button Generator",
        icon=ft.icons.SETTINGS_BACKUP_RESTORE,
        on_click=lambda e: reset(e),
    )
    page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_FLOAT
 """

    def reset(e):
        counter2.value = "0"
        page.snack_bar = ft.SnackBar(
            content=ft.Text("Contador Reiniciado"),
            open=True,
            duration=2500,
            behavior=ft.SnackBarBehavior.FIXED,
            action="Dismiss",
            # dismiss_direction=ft.DismissDirection.HORIZONTAL,
        )
        page.update()

    def agregarboton(e):
        filabotonera.controls.append(
            ft.ElevatedButton(
                text=nombreboton.value,
            )
        )
        nombreboton.value = ""
        page.update()

    def cerrar(e):
        page.close_dialog()
        page.update()

    def contador(e):
        counter2.value = str(int(counter2.value) + 1)  # type: ignore
        page.update()

    def anticontador(e):
        counter2.value = str(int(counter2.value) - 1)  # type: ignore
        page.update()

    dlg2 = ft.AlertDialog(
        title=ft.Text("Elegir Interfaz"),
        content=ft.Text("Por favor seleccione la interfaz de su agrado:"),
        actions=[
            ft.Column(
                controls=[
                    ft.Row(
                        [
                            ft.ElevatedButton(
                                text="Interfaz PC",
                                on_click=lambda e: interfaz1(e, page),
                            ),
                            ft.ElevatedButton(
                                text="Interfaz Telefono",
                                on_click=lambda e: interfaz2(e, page),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row(
                        [
                            ft.TextButton(
                                text="Cancelar",
                                on_click=lambda e: cerrar(e),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ]
            ),
        ],
    )

    def interfaz1(e, page: ft.Page):
        # page.bgcolor = ft.colors.RED
        #page.window_frameless = False
        cerrar(e)
        page.controls.clear()  # type: ignore
        page.window_max_width = 1920
        page.window_max_height = 1080
        page.window_min_width = 1280
        page.window_min_height = 720
        page.window_width = 1280
        page.window_height = 720
        page.window_resizable = True
        #page.window_center()

       
        page.add(ft.TextField("Interfaz PC", read_only=True))
        page.add(
            ft.Row(
                [
                    ft.IconButton(
                        icon=ft.icons.REMOVE,
                        on_click=lambda e: anticontador(e),
                    ),
                    ft.ElevatedButton(
                        text="Button Generator",
                        on_click=lambda e: page.show_dialog(dlg),
                    ),
                    ft.IconButton(
                        icon=ft.icons.ADD,
                        on_click=lambda e: contador(e),
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            filabotonera,
            ft.Row(
                [
                    counter2,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        )
        page.update()

    def interfaz2(e, page: ft.Page):
        # page.bgcolor = ft.colors.BLUE
        # page.remove(counter2)
        #page.window_frameless = True
        cerrar(e)
        page.controls.clear()  # type: ignore
        page.window_min_width = 350
        page.window_min_height = 650
        page.window_max_width = 350
        page.window_max_height = 650
        page.window_width = 350
        page.window_height = 650
        page.window_resizable = False
        page.window_center()
        
        for i in range(10):
            page.add(ft.Text(f"Line {i+1}"))
            if i > 4:
                # page.controls.pop(0)  # type: ignore
                page.remove_at(0)
            page.update()
            time.sleep(0.3)
        page.add(ft.TextField("Interfaz Telefono", read_only=True))

        def checkbox_changed(e):
            output_text.value = f"You have learned how to ski :  {todo_check.value}."
            page.update()

        output_text = ft.Text()
        todo_check = ft.Checkbox(
            label="ToDo: Learn how to use ski", value=False, on_change=checkbox_changed
        )
        page.add(todo_check, output_text)
        page.update()

    page.show_dialog(dlg2)


# ft.app(target=main, view=ft.AppView.FLET_APP , port=5500, host="localhost")
ft.app(target=main, web_renderer=ft.WebRenderer.CANVAS_KIT, port=5500, host="localhost")
