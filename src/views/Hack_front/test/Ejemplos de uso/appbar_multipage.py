import flet as ft

name = "AppBar Example"


def main(page: ft.Page):
    def handle_dismissal(e):
        page.add(ft.Text("Drawer dismissed"))

    def handle_change(e):
        page.add(ft.Text(f"Selected Index changed: {drawer.selected_index}"))
        # page.close(drawer)

    drawer = ft.NavigationDrawer(
        on_dismiss=handle_dismissal,
        on_change=handle_change,
        controls=[
            ft.Container(height=12),
            ft.NavigationDrawerDestination(
                label="Item 1",
                icon=ft.icons.DOOR_BACK_DOOR_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.DOOR_BACK_DOOR),
            ),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.MAIL_OUTLINED),
                label="Item 2",
                selected_icon=ft.icons.MAIL,
            
            ),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.PHONE_OUTLINED),
                label="Item 3",
                selected_icon=ft.icons.PHONE,
            ),
        ],
    )
    page.drawer = drawer
    page.title = name
    def change_page(e):
        page.controls.clear() # type: ignore
        page.add(page2)
    def change_page1(e):
        page.controls.clear() # type: ignore
        page.add(page1)
    page1 = ft.Pagelet(
        appbar=ft.AppBar(
            leading=ft.Row(controls=[ft.IconButton(icon=ft.icons.MENU,on_click=lambda e: page.show_drawer(drawer) )] ),
            leading_width=40,
            title=ft.Text("Pagina 1"),
            center_title=False,
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[
                ft.Row(
                    controls=[
                        ft.IconButton(icon=ft.icons.MAIL),
                        ft.IconButton(icon=ft.icons.SOAP),

                    ]
                ),
                ft.IconButton(icon=ft.icons.ARROW_FORWARD_IOS , on_click=change_page),

            ],
        ),
        content=ft.Container(
            content=ft.Row(controls=[ft.Text("Body")]),
                



        ),
    )
    page2 = ft.Pagelet(
        appbar=ft.AppBar(
            leading=ft.Row(controls=[ft.IconButton(icon=ft.icons.MENU,on_click=lambda e: page.show_drawer(drawer) )] ),
            leading_width=40,
            title=ft.Text("Pagina 2"),
            center_title=False,
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[
                ft.Row(
                    controls=[
                        ft.IconButton(icon=ft.icons.MAIL),
                        ft.IconButton(icon=ft.icons.ARROW_BACK_IOS , on_click=change_page1),
                    ]
                ),
                
            ],
        ),
        content=ft.Container(
            content=ft.Row(controls=[ft.Text("sss")]),
        ),
    )
    

    page.add(page1)


ft.app(target=main)
