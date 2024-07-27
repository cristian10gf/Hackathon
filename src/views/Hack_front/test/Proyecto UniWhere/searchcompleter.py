import flet as ft
from nameplaces import NAMES
import re

def printer(e):
    print("Yellow!")


def main(page: ft.Page):
    page.title = "Autocomplete search names"




    def textbox_changed(e):
        str_lower = e.control.value.lower()
        pattern = re.compile(
            re.escape(str_lower), re.IGNORECASE
        )  # re.escape is used to escape any special characters
        list_view.controls = (
            [list_items.get(n) for n in NAMES if pattern.search(n)] if str_lower else []
        )
        page.update()

    list_items = {
        name: ft.ListTile(
            title=ft.Text(name),
            leading=ft.Icon(ft.icons.ACCESSIBILITY),
            on_click=printer,
        )
        for name in NAMES
    }

    text_field = ft.TextField(label="Search name:", on_change=textbox_changed)
    list_view = ft.ListView(expand=1, spacing=10, padding=20)

    page.add(text_field, list_view)


ft.app(
    port=8080,
    target=main,
)  # view=ft.WEB_BROWSER)
