import flet as ft
from flet import (
    ElevatedButton,
    FilePicker,
    FilePickerResultEvent,
    Page,
    Row,
    Text,
    icons,
)


def main(page: Page):
    # Pick files dialog
    page.bgcolor = ft.colors.WHITE

    # si no hay archivos seleccionados, se muestra "Cancelled!"
    # con la funcion map se obtiene el nombre de los archivos seleccionados separados por coma
    # busca el parametro name en cada archivo de e.files
    def pick_files_result(
        e: FilePickerResultEvent,
    ):  # nombre de los archivos seleccionados separados por coma
        selected_files.value = (
            "|:  :|".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        )
        # imprime el nombre del ultimo archivo seleccionado
        print(e.files[-1].name),  # type: ignore
        selected_files.update()

    pick_files_dialog = FilePicker(on_result=pick_files_result)
    selected_files = Text()

    # Save file dialog
    def save_file_result(e: FilePickerResultEvent):
        save_file_path.value = e.path if e.path else "Cancelled!"
        save_file_path.update()

    save_file_dialog = FilePicker(on_result=save_file_result)
    save_file_path = Text()

    # Open directory dialog
    def get_directory_result(e: FilePickerResultEvent):
        directory_path.value = e.path if e.path else "Cancelled!"
        directory_path.update()

    get_directory_dialog = FilePicker(on_result=get_directory_result)
    directory_path = Text()

    # hide all dialogs in overlay
    page.overlay.extend([pick_files_dialog, save_file_dialog, get_directory_dialog])
    borde = ft.Border(
        top=ft.BorderSide(1, ft.colors.with_opacity(1, "#d9d9d9")),
        bottom=ft.BorderSide(1, ft.colors.with_opacity(1, "#d9d9d9")),
        left=ft.BorderSide(1, ft.colors.with_opacity(1, "#d9d9d9")),
        right=ft.BorderSide(1, ft.colors.with_opacity(1, "#d9d9d9")),
    )
    page.fonts = {
        "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
        "Comfortaa": r"fonts\Comfortaa-Regular.ttf",
        "Roboto": r"fonts\Roboto-Medium.ttf",
    }
    page.add(
        ft.Column(
            [
                Row(
                    [
                        ElevatedButton(
                            "Pick files",
                            icon=icons.UPLOAD_FILE,
                            on_click=lambda _: pick_files_dialog.pick_files(
                                allowed_extensions=["jpg", "png"],
                                allow_multiple=True,
                            ),
                        ),
                        selected_files,
                    ]
                ),
                Row(
                    [
                        ElevatedButton(
                            "Save file",
                            icon=icons.SAVE,
                            on_click=lambda _: save_file_dialog.save_file(),
                            disabled=page.web,
                        ),
                        save_file_path,
                    ]
                ),
                Row(
                    [
                        ElevatedButton(
                            "Open directory",
                            icon=icons.FOLDER_OPEN,
                            on_click=lambda _: get_directory_dialog.get_directory_path(),
                            disabled=page.web,
                        ),
                        directory_path,
                    ]
                ),
                
                ft.Stack(
                    [
                        ft.Card(
                            content=ft.Container(
                                content=ft.TextField(
                                    value="Ingresé una imagen o video de su ubicación actual.",
                                    multiline=True,
                                    read_only=True,
                                    # text_size=33,
                                    text_align=ft.TextAlign.CENTER,
                                    bgcolor=ft.colors.TRANSPARENT,
                                    color=ft.colors.BLACK,
                                    border=ft.InputBorder.NONE,
                                    border_color=ft.colors.TRANSPARENT,
                                    hover_color=ft.colors.TRANSPARENT,
                                    height=74,
                                    width=342,
                                    adaptive=True,
                                    text_style=ft.TextStyle(font_family="Roboto"),
                                    border_radius=10,
                                ),
                                width=342,
                                height=94,
                                padding=10,
                                #alignment=ft.Alignment(0, 0),
                                border=borde,
                                border_radius=10,
                                # bgcolor=ft.colors.GREY,
                            ),
                            elevation=10,
                            color=ft.colors.with_opacity(1, "#F5F5F5"),
                        ),
                        ft.GestureDetector(
                            mouse_cursor=ft.MouseCursor.CLICK,
                            # on_vertical_drag_update=lambda e: on_pan_update(e),
                            on_tap=lambda _: pick_files_dialog.pick_files(
                                allowed_extensions=["jpg", "png", "mp4", "avi", "mov", "wmv", "flv", "mkv", "webm"],
                                allow_multiple=True,
                            ),
                            width=342,
                            height=94,
                            # left=400,
                            # top=100,
                        ),
                    ],
                ),
            ]
        ),
    )


ft.app(target=main, view=ft.AppView.FLET_APP)
