import flet as ft

def get_busqueda( search_handle_submit: callable, search_handle_change: callable,list_items: list) -> ft.SearchBar:
  return ft.SearchBar(
        bar_leading=ft.IconButton(
            icon=ft.icons.MENU,
            icon_color=ft.colors.BLACK,
            on_click=lambda e: e.open_view(),
        ),
        bar_trailing=[
            ft.IconButton(
                icon=ft.icons.SEARCH_SHARP,
                icon_color=ft.colors.BLACK,
                on_click=search_handle_submit,
                # on_click=lambda e: add_image(e, images),
            ),
        ],
        controls=list_items,
        value="",
        bar_hint_text="Ingresé su ubicación actual",
        view_hint_text="Ingresé su ubicación actual",
        width=338,
        height=56,
        view_elevation=4,
        bar_bgcolor="#f3edf7",
        bar_overlay_color="#ffffff",
        # capitalization=ft.TextCapitalization.WORDS,
        on_submit=search_handle_submit,
        on_change=search_handle_change,
        on_animation_end=lambda e: e.update(),
        on_tap=lambda e: e.control.open_view(),
    )