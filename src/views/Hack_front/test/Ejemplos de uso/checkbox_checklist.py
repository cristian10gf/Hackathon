import flet as ft


def main(page):
    def checkbox_changed(e):
        output_text.value = f"You have learned how to ski :  {todo_check.value}."
        page.update()

    output_text = ft.Text()
    todo_check = ft.Checkbox(
        label="ToDo: Learn how to use ski", value=False, on_change=checkbox_changed
    )
    page.add(todo_check, output_text)

    name = "NavigationDrawer example"

    def calculator_drawer():
        """end_drawer = ft.NavigationDrawer(
            controls=[
                ft.NavigationDrawerDestination(
                    icon=ft.icons.ADD_TO_HOME_SCREEN_SHARP, label="Item 1"
                ),
                ft.NavigationDrawerDestination(icon=ft.icons.ADD_COMMENT, label="Item 2"),
            ],
        )"""

        drawer = ft.NavigationDrawer(
            controls=[
                ft.NavigationDrawerDestination(
                    selected_icon_content=ft.ElevatedButton(
                        "Button 1", on_click=lambda e: None
                    ),
                    icon=ft.icons.ADD_TO_HOME_SCREEN_SHARP,
                    label="Item 1",
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.icons.ADD_COMMENT,
                    label="Item 2",
                    selected_icon=ft.icons.CLEAR,
                ),
            ],
        )

        """ def open_end_drawer(e):
            e.control.page.end_drawer = end_drawer
            end_drawer.open = True
            e.control.page.update()
        """

        def open_drawer(e):
            e.control.page.drawer = drawer
            drawer.open = True
            e.control.page.update()

        return ft.Column(
            [
                # ft.ElevatedButton("Open end drawer", on_click=open_end_drawer),
                ft.ElevatedButton("Open drawer", on_click=open_drawer),
            ]
        )
    def all_operations_Symbols():
        return ft.Tabs(
            selected_index=1,
            animation_duration=300,
            tabs=[
                ft.Tab(
                    text="Tab 1",
                    content=ft.Container(
                        content=ft.Text("This is Tab 1"), alignment=ft.alignment.center
                    ),
                ),
                ft.Tab(
                    tab_content=ft.Icon(ft.icons.SEARCH),
                    content=ft.Text("This is Tab 2"),
                ),
                ft.Tab(
                    text="Tab 3",
                    icon=ft.icons.SETTINGS,
                    content=ft.Text("This is Tab 3"),
                ),
            ],
            width=800,
            height=600,
        )
    examplee = calculator_drawer()
    page.add(examplee)
    page.add(all_operations_Symbols())


ft.app(target=main)
