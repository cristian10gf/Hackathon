
import flet as ft
import FleetingViews as fleeview


def main(pag: ft.Page):
    view_def = {
        "page1": {
            "bgcolor": ft.colors.RED,
            "vertical_aligment": ft.MainAxisAlignment.CENTER,
            "horizontal_aligment": ft.CrossAxisAlignment.CENTER,
        },
        "page2": {
            "bgcolor": ft.colors.RED,
            "vertical_aligment": ft.MainAxisAlignment.CENTER,
            
        },
        "page3": {
            "bgcolor": ft.colors.BLUE,
            "vertical_aligment": ft.MainAxisAlignment.CENTER,
        },
    }

    fv = fleeview.create_views(view_definitions=view_def,page=pag)
    appbar = ft.AppBar(
        leading=ft.IconButton(icon=ft.icons.ABC),
        title=ft.Text("Multipages"),
        actions=[
            ft.IconButton(icon=ft.icons.ADD, on_click=lambda e: fv.view_go("page1",duration=300)),
            ft.IconButton(icon=ft.icons.EDIT, on_click=lambda e: fv.view_go("page2",duration=300)),
            ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e: fv.view_go("page3",duration=300)),
        ],
    )


    fv.views["page1"].appbar = appbar
    fv.views["page2"].appbar = appbar
    fv.views["page3"].appbar = appbar
    pag.update()


ft.app(target=main)

