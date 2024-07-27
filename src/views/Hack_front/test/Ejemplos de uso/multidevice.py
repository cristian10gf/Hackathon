from calendar import c
import flet as ft


def main(page: ft.Page):
    page.title = "Prueba Conceptual"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.bgcolor = ft.colors.WHITE
    page.insert(100000, ft.Text("Initial route: /"))
    counter2 = ft.TextField(
        value="0",
        label="Contador de Clicks: ",
        width=120,
        text_align=ft.TextAlign.CENTER,
    )

    page.add(
        ft.AppBar(
            title=ft.Text("Prueba Conceptual"),
            bgcolor=ft.colors.BLUE,
            center_title=True,
        ),
        counter2,
    )
    print(page.route)
    page.add(ft.Text(f"Eleccion de interfaz"))

    """ nombreboton = ft.TextField(
        label="Texto del Boton",
        #on_change=print("Texto del Boton"),
    ) """
    dlg = ft.AlertDialog(
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

    def cerrar(e):
        page.close_dialog()
        page.update()

    def interfaz1(e, page):
        page.bgcolor = ft.colors.RED
        page.controls.clear()  # type: ignore
        page.add(ft.TextField("Interfaz PC"))
        page.update()

    def interfaz2(e, page):
        page.bgcolor = ft.colors.BLUE
        page.remove(counter2)
        #page.controls.clear()  # type: ignore
        page.add(ft.TextField("Interfaz Telefono"))
        page.update()

    page.show_dialog(dlg)
    """ page.add(
        ft.Row(
            [
               
                ft.ElevatedButton(
                    text="Elige pibe", on_click=lambda e: page.show_dialog(dlg)
                ),
                
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        
    ) """


# ft.app(target=main, view=ft.AppView.FLET_APP , port=5500, host="localhost")
ft.app(target=main)
