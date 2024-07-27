import flet as ft

name = "NavigationBar Example"


def example():
    class Example(ft.Column):
        def __init__(self):
            super().__init__()
            self.navigation_bar = ft.NavigationBar(
                destinations=[
                    ft.NavigationDestination(icon=ft.icons.EXPLORE, label="Explore"),
                    ft.NavigationDestination(icon=ft.icons.COMMUTE, label="Commute"),
                    ft.NavigationDestination(
                        icon=ft.icons.BOOKMARK_BORDER,
                        selected_icon=ft.icons.BOOKMARK,
                        label="Explore",
                    ),
                ],
                shadow_color=ft.colors.with_opacity(0.1, ft.colors.WHITE),
            )

            self.controls = [
                ft.ElevatedButton(
                    "Show NavigationBar", on_click=self.show_navigation_bar
                ),
            ]

        def show_navigation_bar(self, e):
            e.control.page.navigation_bar = self.navigation_bar
            e.control.page.update()

        # happens when example is removed from the page (when user chooses different control group on the navigation rail)
        def will_unmount(self):
            self.page.navigation_bar = None # type: ignore
            self.page.update() # type: ignore

    navigation_bar_example = Example()

    return navigation_bar_example

def main(page: ft.Page):
    

    page.title = "NavigationBar Example"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_height = 800
    page.window_width = 360
    page.window_resizable = False
    page.window_max_height = 800
    page.window_max_width = 360
    page.window_center()
    page.bgcolor = ft.colors.WHITE


    #colu= ft.Column(navigation_bar=ft.NavigationBar(destinations=[)
    page.add(example())
    page.update()

ft.app(target=main)
